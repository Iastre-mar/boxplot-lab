#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import veusz.plugins as plugins
class FloatPlugin(plugins.DatasetPlugin):
    name = 'FloatPlugin'
    def __init__(self):
        self.fields = [
        plugins.FieldDataset('ds_in', 'Input dataset'),
        plugins.FieldFloat('value', 'Value', default=0.),
        plugins.FieldDataset('ds_out', 'Output dataset name'),
        ]
        
        
    def getDatasets(self, fields):
        """Returns single output dataset (self.dsout).
        This method should return a list of Dataset objects, which can include
        Dataset1D, Dataset2D and DatasetText
        """

        # raise DatasetPluginException if there are errors
        if fields['ds_out'] == '':
            raise plugins.DatasetPluginException('Invalid output dataset name')

        # make a new dataset with name in fields['ds_out']
        self.ds_out = plugins.Dataset1D(fields['ds_out'])

        # return list of datasets
        return [self.ds_out]
    
    
    def updateDatasets(self, fields, helper):
        """
        This function should *update* the dataset(s) returned by getDatasets
        """

        # get the input dataset - helper provides methods for getting other
        # datasets from Veusz
        ds_in = helper.getDataset(fields['ds_in'])

        # just to be explicit
        try:
            newdata = pd.Series(map(lambda x: float(x), ds_in.data))
        except:
            newdata = ds_in.data

        # update output dataset with input dataset (plus value) and errorbars
        self.ds_out.update(data=newdata,
                           serr=ds_in.serr, perr=ds_in.perr, nerr=ds_in.nerr)


# In[ ]:




