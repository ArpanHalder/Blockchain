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
Treaders Block
Storage Block
Furnes Block
SMS Block
Manufacturar Block
Distributor Block
"""

#class __DSCertificate(): #TODO:
import bchain as bc

class Source():
    def __init__(self,CertificateOfOrigin,BatchDetails,Production):
        self.CertificateOfOrigin = CertificateOfOrigin;
        self.BatchDetails = BatchDetails;
        self.Production = Production;