"""
Preston Sergent
"""

aptdict = {"sources.list": True}
etcdict = {"apt": aptdict}
newfs = {"etc": etcdict}
print(newfs["etc"]["apt"]["sources.list"])
newfs["etc"]["apt"]["sources.list"] = "fuck"
print(newfs["etc"]["apt"]["sources.list"])
