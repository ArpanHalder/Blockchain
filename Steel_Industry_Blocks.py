# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 22:30:05 2021

@author: halder

Steel Industry Blocks, to have a class to store all relvant data on steel supply chain

How to Use:
    import Steel_Industry_Blocks as sib
    
    data = sib.Furnes(Attributes)

**Catagories of Block #To be Programmed

Source Block
Transport Blocks
Treaders Block (looks like don't need')
Storage Block
Furnes Block
SMS Block
Manufacturar Block
Distributor Block
"""

#class __DSCertificate(): #TODO:
import bchain2 as bc

class Source:
    def __init__(self,CertificateOfOrigin,ProductionDetails,index):
        self.CertificateOfOrigin = CertificateOfOrigin;
        self.ProductionDetails = ProductionDetails;
        self.index = index
        self.block = bc.Block(self, self.index, "NA", "NA")    
    
class Transport:
    def __init__(self, data, index, source_index, prev_hash ):
        #TODO add time stamp of creatation in the data and use that in the block making
        self.block = bc.Block(data,index,source_index, prev_hash)
        
class Storage:
    def __init__(self, data, index, source_index, prev_hash ):
        #TODO add time stamp of creatation in the data and use that in the block making
        self.block = bc.Block(data,index,source_index, prev_hash)
        
class Furnes:
    def __init__(self, data, index, source_indexs, prev_hashs ):
        #TODO add time stamp of creatation in the data and use that in the block making
        self.block = bc.Block(data,index,source_indexs, prev_hashs)
        
class SMS:
    def __init__(self, data, index, source_indexs, prev_hashs ):
        #TODO add time stamp of creatation in the data and use that in the block making
        self.block = bc.Block(data,index,source_indexs, prev_hashs)
        
class Manufacturar:
    def __init__(self, data, index, source_indexs, prev_hashs ):
        #TODO add time stamp of creatation in the data and use that in the block making
        self.block = bc.Block(data,index,source_indexs, prev_hashs)
        
class Distributor:
    def __init__(self, data, index, source_index, prev_hash ):
        #TODO add time stamp of creatation in the data and use that in the block making
        self.block = bc.Block(data,index,source_index, prev_hash)