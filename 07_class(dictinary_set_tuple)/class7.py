from typing import Dict , Union, Optional, Any

import pprint

key = Union [str,int]
value = Union[str,int,list,dict,tuple,set,float]
data : dict[key,value] = {"Dname":"Farah",
                      'Sname': "zarrar",
                        "fname": "nasir",
                        "abc" : [1,2,4,3],
                        "xyz" : {1,2,3},
                        "efg" : (1,2,3),
                        "cde" : {"a" : "nasar","b": "2"},
                        # [1,2,3] : "khurasan", # unhashable type: 'list'
                        # (1,3,4) : "khurasan", error
                        # {1,2,4} : "khurasan", error
                        # 101 : "swat"
                        }  
print(data["cde"]['b'])
