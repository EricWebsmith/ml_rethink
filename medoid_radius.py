import numpy as np

class MedoidRadius(object):
    distance_matrix_ = None
    n_samples=0
    labels_ = []
    medoids_ = []
    
    #select
    def __select_medoid(self, mask_row):
        members=mask_row.argsort()[-mask_row.sum():]
        n_members=len(members)
        distances=np.zeros((n_members))
        index=0
        for member in members:
            
            distance = sum(self.matrix_distances_[member] * mask_row)/sum(mask_row)
            distances[index] = distance
            index+=1

        return members[distances.argmin()]
    
    def fit(self, distance_matrix, radius, mask=None):
        self.matrix_distances_=distance_matrix
        self.n_samples=distance_matrix.shape[0]
        self.labels_=np.array(range(0,self.n_samples))
        
        self.medoids_ = []
        #here we use a mask to cache if the distance is less than radius,
        #thus we don't have to compare them all them time.
        if not mask:
            mask = distance_matrix<radius
            mask = mask * 1
        while True:
            mask_row_sum = mask.sum(axis=0)
            if sum(mask_row_sum)<=1:
                break
            #candidate
            old_medoid = mask_row_sum.argmax()
            old_mask_row=mask[old_medoid]
            if old_mask_row.shape[0]==2:
                return
            new_medoid=self.__select_medoid(old_mask_row)

            new_mask_row=mask[new_medoid]

            while (old_medoid!=new_medoid) \
                and (old_mask_row==new_mask_row).all() \
                and (sum(new_mask_row)>0):
                old_medoid=new_medoid
                old_mask_row=new_mask_row
                new_medoid=self.__select_medoid(new_mask_row)
                new_mask_row=mask[new_medoid]
                if sum(new_mask_row)==0:
                    break

            members=new_mask_row.argsort()[-new_mask_row.sum():]
            if len(members)>1:
                self.medoids_.append(new_medoid)
                self.labels_[members]=new_medoid
            mask[members]=0
            mask[:,members]=0