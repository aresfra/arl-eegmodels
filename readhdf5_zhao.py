def traverse_datasets(hdf_file):
    import h5py  
    import numpy as np
    
    # def h5py_dataset_iterator(g, prefix=''):
        # for key in g.keys():
            # item = g[key]
            # path = '{}/{}'.format(prefix, key)
            # if isinstance(item, h5py.DataSet):
                # yield(path, item)
            # elif isinstance(item, h5py.Group):
                # yield from h5py_dataset_iterator(item, path)
        
    
    with h5py.File(hdf_file, 'r') as f:
        # for (path, dset) in h5py_dataset_iterator(f):
            # print(path, dset)
            
        #datasample = f["RawData"]["Samples"]
        #intervals = f["AsynchronData"]["Time"]
        data1 = np.array(f["RawData"]["Samples"][:])  ##datasample原始数据
        #print(data1.shape)
        
        t1 = np.array(f["AsynchronData"]["Time"][:]).flatten()  ##时间间隔
        trigger = t1.tolist()
        #print("length of trigger", len(trigger))
       
       
        samples = np.zeros((150,32,180)) ##150个数据
        
        for i in range(0, len(trigger), 2):
            samples_start = int(trigger[i])
            samples_end = int(samples_start+1.5*4800)
            #print(type(samples_end), samples_start)
            trial_data = data1[samples_start:samples_end][:].T
            print(type(trial_data), trial_data.shape)
            trial_data_norm = trial_data - np.mean(trial_data)
            resam_trial_data = trial_data_norm[::1, ::40]  ###resampling to 120Hz
            
            print("after resampling", type(resam_trial_data), resam_trial_data.shape)
            j = int(i/2)
            samples[j] = resam_trial_data
            
        
        print("type of samples ", samples.shape)
    return samples