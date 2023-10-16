from flask import Flask, render_template
import numpy as np
import tensorflow as tf

threads = np.array([
    {
        "mainQuestion": {
            "profile": {
                "username": "j.miller",
                "_id": "st210"
                },
            "references": {
                "year": "2010",
                "session": "N",
                "paper": "P2",
                "syllabus": "Z",
                "topic": "moles and stoichiometry"
            },
            "question": {
                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                "attachments": {
                    "audio": True,
                    "image": True
                }
            },
            "dateThreadWasMade": "12-04-2022"
        },
        "responses": [
            {
                "profile": {
                    "username": "b.baggins",
                        "_id": "st213"
                },
                "answer": {
                    "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                    "attachments": {
                        "audio": True,
                        "video": True
                    }
                },
                "likes": 253,
                "dateResponseWasMade": "12-04-22",
            
            },
            {
                "profile": {
                    "username": "b.baggins",
                        "_id": "st213"
                },
                "answer": {
                    "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                    "attachments": {
                        "audio": True,
                        "video": True
                    }
                },
                "likes": 253,
                "dateResponseWasMade": "12-04-22",
            
                },
                {
                    "profile": {
                        "username": "b.baggins",
                            "_id": "st213"
                    },
                    "answer": {
                        "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                        "attachments": {
                            "audio": True,
                            "video": True
                        }
                    },
                    "likes": 253,
                    "dateResponseWasMade": "12-04-22",
                
                    },
                    {
                        "profile": {
                            "username": "b.baggins",
                                "_id": "st213"
                        },
                        "answer": {
                            "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                            "attachments": {
                                "audio": True,
                                "video": True
                            }
                        },
                        "likes": 253,
                        "dateResponseWasMade": "12-04-22",
                    
                        "responses":[
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "level one nesting using recursion",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                                
                                "responses":[
                                    {
                                        "profile": {
                                            "username": "b.baggins",
                                                "_id": "st213"
                                        },
                                        "answer": {
                                            "description": "level two nesting using recursion",
                                            "attachments": {
                                                "audio": True,
                                                "video": True
                                            }
                                        },
                                        "likes": 253,
                                        "dateResponseWasMade": "12-04-22",
                                        "responses":[
                                            {
                                                "profile": {
                                                    "username": "b.baggins",
                                                        "_id": "st213"
                                                },
                                                "answer": {
                                                    "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                                                    "attachments": {
                                                        "audio": True,
                                                        "video": True
                                                    }
                                                },
                                                "likes": 253,
                                                "dateResponseWasMade": "12-04-22",
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]

                        },
        ]
    },

    {
        "mainQuestion": {
            "profile": {
                "username": "j.miller",
                "_id": "st210"
                },
            "references": {
                "year": "1980",
                "session": "J",
                "paper": "P4",
                "syllabus": "C",
                "topic": "Atoms and Molecules"
            },
            "question": {
                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                "attachments": {
                    "audio": True,
                    "image": True
                }
            },
            "dateThreadWasMade": "12-04-2022"
        },
        "responses": [{
            "profile": {
                "username": "b.baggins",
                    "_id": "st213"
            },
            "answer": {
                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                "attachments": {
                    "audio": True,
                    "video": True
                }
            },
            "likes": 253,
            "dateResponseWasMade": "12-04-22",
           
            "responses":[
                {
                    "profile": {
                        "username": "b.baggins",
                            "_id": "st213"
                    },
                    "answer": {
                        "description": "level one nesting using recursion",
                        "attachments": {
                            "audio": True,
                            "video": True
                        }
                    },
                    "likes": 253,
                    "dateResponseWasMade": "12-04-22",
                    
                    "responses":[
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "level two nesting using recursion",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                            "responses":[
                                {
                                    "profile": {
                                        "username": "b.baggins",
                                            "_id": "st213"
                                    },
                                    "answer": {
                                        "description": "level one nesting using recursion",
                                        "attachments": {
                                            "audio": True,
                                            "video": True
                                        }
                                    },
                                    "likes": 253,
                                    "dateResponseWasMade": "12-04-22",
                                }
                            ]
                        }
                    ]
                }
            ]
        }]
    },

    {
        "mainQuestion": {
            "profile": {
                "username": "j.miller",
                "_id": "st210"
                },
            "references": {
                "year": "2010",
                "session": "N",
                "paper": "P2",
                "syllabus": "Z",
                "topic": "moles and stoichiometry"
            },
            "question": {
                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                "attachments": {
                    "audio": True,
                    "image": True
                }
            },
            "dateThreadWasMade": "12-04-2022"
        },
        "responses": [{
            "profile": {
                "username": "b.baggins",
                    "_id": "st213"
            },
            "answer": {
                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                "attachments": {
                    "audio": True,
                    "video": True
                }
            },
            "likes": 253,
            "dateResponseWasMade": "12-04-22",
           
            "responses":[
                {
                    "profile": {
                        "username": "b.baggins",
                            "_id": "st213"
                    },
                    "answer": {
                        "description": "level one nesting using recursion",
                        "attachments": {
                            "audio": True,
                            "video": True
                        }
                    },
                    "likes": 253,
                    "dateResponseWasMade": "12-04-22",
                    
                    "responses":[
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "level two nesting using recursion",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                            "responses":[
                                {
                                    "profile": {
                                        "username": "b.baggins",
                                            "_id": "st213"
                                    },
                                    "answer": {
                                        "description": "level one nesting using recursion",
                                        "attachments": {
                                            "audio": True,
                                            "video": True
                                        }
                                    },
                                    "likes": 253,
                                    "dateResponseWasMade": "12-04-22",
                                }
                            ]
                        }
                    ]
                }
            ]
        }]
    },

    {
        "mainQuestion": {
            "profile": {
                "username": "j.miller",
                "_id": "st210"
                },
            "references": {
                "year": "2010",
                "session": "N",
                "paper": "P2",
                "syllabus": "Z",
                "topic": "moles and stoichiometry"
            },
            "question": {
                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                "attachments": {
                    "audio": True,
                    "image": True
                }
            },
            "dateThreadWasMade": "12-04-2022"
        },
        "responses": [{
            "profile": {
                "username": "b.baggins",
                    "_id": "st213"
            },
            "answer": {
                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                "attachments": {
                    "audio": True,
                    "video": True
                }
            },
            "likes": 253,
            "dateResponseWasMade": "12-04-22",
           
            "responses":[
                {
                    "profile": {
                        "username": "b.baggins",
                            "_id": "st213"
                    },
                    "answer": {
                        "description": "level one nesting using recursion",
                        "attachments": {
                            "audio": True,
                            "video": True
                        }
                    },
                    "likes": 253,
                    "dateResponseWasMade": "12-04-22",
                    
                    "responses":[
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "level two nesting using recursion",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                            "responses":[
                                {
                                    "profile": {
                                        "username": "b.baggins",
                                            "_id": "st213"
                                    },
                                    "answer": {
                                        "description": "level one nesting using recursion",
                                        "attachments": {
                                            "audio": True,
                                            "video": True
                                        }
                                    },
                                    "likes": 253,
                                    "dateResponseWasMade": "12-04-22",
                                }
                            ]
                        }
                    ]
                }
            ]
        }]
    },

    {
        "mainQuestion": {
            "profile": {
                "username": "j.miller",
                "_id": "st210"
                },
            "references": {
                "year": "2010",
                "session": "N",
                "paper": "P2",
                "syllabus": "Z",
                "topic": "moles and stoichiometry"
            },
            "question": {
                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                "attachments": {
                    "audio": True,
                    "image": True
                }
            },
            "dateThreadWasMade": "12-04-2022"
        },
        "responses": [{
            "profile": {
                "username": "b.baggins",
                    "_id": "st213"
            },
            "answer": {
                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                "attachments": {
                    "audio": True,
                    "video": True
                }
            },
            "likes": 253,
            "dateResponseWasMade": "12-04-22",
           
            "responses":[
                {
                    "profile": {
                        "username": "b.baggins",
                            "_id": "st213"
                    },
                    "answer": {
                        "description": "level one nesting using recursion",
                        "attachments": {
                            "audio": True,
                            "video": True
                        }
                    },
                    "likes": 253,
                    "dateResponseWasMade": "12-04-22",
                    
                    "responses":[
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "level two nesting using recursion",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                            "responses":[
                                {
                                    "profile": {
                                        "username": "b.baggins",
                                            "_id": "st213"
                                    },
                                    "answer": {
                                        "description": "level one nesting using recursion",
                                        "attachments": {
                                            "audio": True,
                                            "video": True
                                        }
                                    },
                                    "likes": 253,
                                    "dateResponseWasMade": "12-04-22",
                                }
                            ]
                        }
                    ]
                }
            ]
        }]
    },

    {
        "mainQuestion": {
            "profile": {
                "username": "j.miller",
                "_id": "st210"
                },
            "references": {
                "year": "2010",
                "session": "N",
                "paper": "P2",
                "syllabus": "Z",
                "topic": "moles and stoichiometry"
            },
            "question": {
                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                "attachments": {
                    "audio": True,
                    "image": True
                }
            },
            "dateThreadWasMade": "12-04-2022"
        },
        "responses": [{
            "profile": {
                "username": "b.baggins",
                    "_id": "st213"
            },
            "answer": {
                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                "attachments": {
                    "audio": True,
                    "video": True
                }
            },
            "likes": 253,
            "dateResponseWasMade": "12-04-22",
           
            "responses":[
                {
                    "profile": {
                        "username": "b.baggins",
                            "_id": "st213"
                    },
                    "answer": {
                        "description": "level one nesting using recursion",
                        "attachments": {
                            "audio": True,
                            "video": True
                        }
                    },
                    "likes": 253,
                    "dateResponseWasMade": "12-04-22",
                    
                    "responses":[
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "level two nesting using recursion",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                            "responses":[
                                {
                                    "profile": {
                                        "username": "b.baggins",
                                            "_id": "st213"
                                    },
                                    "answer": {
                                        "description": "level one nesting using recursion",
                                        "attachments": {
                                            "audio": True,
                                            "video": True
                                        }
                                    },
                                    "likes": 253,
                                    "dateResponseWasMade": "12-04-22",
                                }
                            ]
                        }
                    ]
                }
            ]
        }]
    },

    {
        "mainQuestion": {
            "profile": {
                "username": "j.miller",
                "_id": "st210"
                },
            "references": {
                "year": "2010",
                "session": "N",
                "paper": "P2",
                "syllabus": "Z",
                "topic": "moles and stoichiometry"
            },
            "question": {
                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                "attachments": {
                    "audio": True,
                    "image": True
                }
            },
            "dateThreadWasMade": "12-04-2022"
        },
        "responses": [{
            "profile": {
                "username": "b.baggins",
                    "_id": "st213"
            },
            "answer": {
                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                "attachments": {
                    "audio": True,
                    "video": True
                }
            },
            "likes": 253,
            "dateResponseWasMade": "12-04-22",
           
            "responses":[
                {
                    "profile": {
                        "username": "b.baggins",
                            "_id": "st213"
                    },
                    "answer": {
                        "description": "level one nesting using recursion",
                        "attachments": {
                            "audio": True,
                            "video": True
                        }
                    },
                    "likes": 253,
                    "dateResponseWasMade": "12-04-22",
                    
                    "responses":[
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "level two nesting using recursion",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                            "responses":[
                                {
                                    "profile": {
                                        "username": "b.baggins",
                                            "_id": "st213"
                                    },
                                    "answer": {
                                        "description": "level one nesting using recursion",
                                        "attachments": {
                                            "audio": True,
                                            "video": True
                                        }
                                    },
                                    "likes": 253,
                                    "dateResponseWasMade": "12-04-22",
                                }
                            ]
                        }
                    ]
                }
            ]
        }]
    },

    {
        "mainQuestion": {
            "profile": {
                "username": "j.miller",
                "_id": "st210"
                },
            "references": {
                "year": "2010",
                "session": "N",
                "paper": "P2",
                "syllabus": "Z",
                "topic": "moles and stoichiometry"
            },
            "question": {
                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                "attachments": {
                    "audio": True,
                    "image": True
                }
            },
            "dateThreadWasMade": "12-04-2022"
        },
        "responses": [{
            "profile": {
                "username": "b.baggins",
                    "_id": "st213"
            },
            "answer": {
                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                "attachments": {
                    "audio": True,
                    "video": True
                }
            },
            "likes": 253,
            "dateResponseWasMade": "12-04-22",
           
            "responses":[
                {
                    "profile": {
                        "username": "b.baggins",
                            "_id": "st213"
                    },
                    "answer": {
                        "description": "level one nesting using recursion",
                        "attachments": {
                            "audio": True,
                            "video": True
                        }
                    },
                    "likes": 253,
                    "dateResponseWasMade": "12-04-22",
                    
                    "responses":[
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "level two nesting using recursion",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                            "responses":[
                                {
                                    "profile": {
                                        "username": "b.baggins",
                                            "_id": "st213"
                                    },
                                    "answer": {
                                        "description": "level one nesting using recursion",
                                        "attachments": {
                                            "audio": True,
                                            "video": True
                                        }
                                    },
                                    "likes": 253,
                                    "dateResponseWasMade": "12-04-22",
                                }
                            ]
                        }
                    ]
                }
            ]
        }]
    },


    {
        "mainQuestion": {
            "profile": {
                "username": "j.miller",
                "_id": "st210"
                },
            "references": {
                "year": "2010",
                "session": "N",
                "paper": "P2",
                "syllabus": "Z",
                "topic": "moles and stoichiometry"
            },
            "question": {
                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                "attachments": {
                    "audio": True,
                    "image": True
                }
            },
            "dateThreadWasMade": "12-04-2022"
        },
        "responses": [{
            "profile": {
                "username": "b.baggins",
                    "_id": "st213"
            },
            "answer": {
                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                "attachments": {
                    "audio": True,
                    "video": True
                }
            },
            "likes": 253,
            "dateResponseWasMade": "12-04-22",
           
            "responses":[
                {
                    "profile": {
                        "username": "b.baggins",
                            "_id": "st213"
                    },
                    "answer": {
                        "description": "level one nesting using recursion",
                        "attachments": {
                            "audio": True,
                            "video": True
                        }
                    },
                    "likes": 253,
                    "dateResponseWasMade": "12-04-22",
                    
                    "responses":[
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "level two nesting using recursion",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                            "responses":[
                                {
                                    "profile": {
                                        "username": "b.baggins",
                                            "_id": "st213"
                                    },
                                    "answer": {
                                        "description": "level one nesting using recursion",
                                        "attachments": {
                                            "audio": True,
                                            "video": True
                                        }
                                    },
                                    "likes": 253,
                                    "dateResponseWasMade": "12-04-22",
                                }
                            ]
                        }
                    ]
                }
            ]
        }]
    },

    {
        "mainQuestion": {
            "profile": {
                "username": "j.miller",
                "_id": "st210"
                },
            "references": {
                "year": "2010",
                "session": "N",
                "paper": "P2",
                "syllabus": "Z",
                "topic": "moles and stoichiometry"
            },
            "question": {
                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                "attachments": {
                    "audio": True,
                    "image": True
                }
            },
            "dateThreadWasMade": "12-04-2022"
        },
        "responses": [{
            "profile": {
                "username": "b.baggins",
                    "_id": "st213"
            },
            "answer": {
                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                "attachments": {
                    "audio": True,
                    "video": True
                }
            },
            "likes": 253,
            "dateResponseWasMade": "12-04-22",
           
            "responses":[
                {
                    "profile": {
                        "username": "b.baggins",
                            "_id": "st213"
                    },
                    "answer": {
                        "description": "level one nesting using recursion",
                        "attachments": {
                            "audio": True,
                            "video": True
                        }
                    },
                    "likes": 253,
                    "dateResponseWasMade": "12-04-22",
                    
                    "responses":[
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "level two nesting using recursion",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                            "responses":[
                                {
                                    "profile": {
                                        "username": "b.baggins",
                                            "_id": "st213"
                                    },
                                    "answer": {
                                        "description": "level one nesting using recursion",
                                        "attachments": {
                                            "audio": True,
                                            "video": True
                                        }
                                    },
                                    "likes": 253,
                                    "dateResponseWasMade": "12-04-22",
                                }
                            ]
                        }
                    ]
                }
            ]
        }]
    },
])

app = Flask(__name__, template_folder="template")
@app.route("/", methods=["GET", "POST"])
def index():
    filters = ["default"]
    filtered = np.array([
                {
                    "mainQuestion": {
                        "profile": {
                            "username": "j.miller",
                            "_id": "st210"
                            },
                        "references": {
                            "year": "2010",
                            "session": "N",
                            "paper": "P2",
                            "syllabus": "Z",
                            "topic": "moles and stoichiometry"
                        },
                        "question": {
                            "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                            "attachments": {
                                "audio": True,
                                "image": True
                            }
                        },
                        "dateThreadWasMade": "12-04-2022"
                    },
                    "responses": [
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                        
                        },
                        {
                            "profile": {
                                "username": "b.baggins",
                                    "_id": "st213"
                            },
                            "answer": {
                                "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                                "attachments": {
                                    "audio": True,
                                    "video": True
                                }
                            },
                            "likes": 253,
                            "dateResponseWasMade": "12-04-22",
                        
                            },
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                            
                                },
                                {
                                    "profile": {
                                        "username": "b.baggins",
                                            "_id": "st213"
                                    },
                                    "answer": {
                                        "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                                        "attachments": {
                                            "audio": True,
                                            "video": True
                                        }
                                    },
                                    "likes": 253,
                                    "dateResponseWasMade": "12-04-22",
                                
                                    "responses":[
                                        {
                                            "profile": {
                                                "username": "b.baggins",
                                                    "_id": "st213"
                                            },
                                            "answer": {
                                                "description": "level one nesting using recursion",
                                                "attachments": {
                                                    "audio": True,
                                                    "video": True
                                                }
                                            },
                                            "likes": 253,
                                            "dateResponseWasMade": "12-04-22",
                                            
                                            "responses":[
                                                {
                                                    "profile": {
                                                        "username": "b.baggins",
                                                            "_id": "st213"
                                                    },
                                                    "answer": {
                                                        "description": "level two nesting using recursion",
                                                        "attachments": {
                                                            "audio": True,
                                                            "video": True
                                                        }
                                                    },
                                                    "likes": 253,
                                                    "dateResponseWasMade": "12-04-22",
                                                    "responses":[
                                                        {
                                                            "profile": {
                                                                "username": "b.baggins",
                                                                    "_id": "st213"
                                                            },
                                                            "answer": {
                                                                "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                                                                "attachments": {
                                                                    "audio": True,
                                                                    "video": True
                                                                }
                                                            },
                                                            "likes": 253,
                                                            "dateResponseWasMade": "12-04-22",
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]

                                    },
                    ]
                },

                {
                    "mainQuestion": {
                        "profile": {
                            "username": "j.miller",
                            "_id": "st210"
                            },
                        "references": {
                            "year": "1980",
                            "session": "J",
                            "paper": "P4",
                            "syllabus": "C",
                            "topic": "Atoms and Molecules"
                        },
                        "question": {
                            "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                            "attachments": {
                                "audio": True,
                                "image": True
                            }
                        },
                        "dateThreadWasMade": "12-04-2022"
                    },
                    "responses": [{
                        "profile": {
                            "username": "b.baggins",
                                "_id": "st213"
                        },
                        "answer": {
                            "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                            "attachments": {
                                "audio": True,
                                "video": True
                            }
                        },
                        "likes": 253,
                        "dateResponseWasMade": "12-04-22",
                    
                        "responses":[
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "level one nesting using recursion",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                                
                                "responses":[
                                    {
                                        "profile": {
                                            "username": "b.baggins",
                                                "_id": "st213"
                                        },
                                        "answer": {
                                            "description": "level two nesting using recursion",
                                            "attachments": {
                                                "audio": True,
                                                "video": True
                                            }
                                        },
                                        "likes": 253,
                                        "dateResponseWasMade": "12-04-22",
                                        "responses":[
                                            {
                                                "profile": {
                                                    "username": "b.baggins",
                                                        "_id": "st213"
                                                },
                                                "answer": {
                                                    "description": "level one nesting using recursion",
                                                    "attachments": {
                                                        "audio": True,
                                                        "video": True
                                                    }
                                                },
                                                "likes": 253,
                                                "dateResponseWasMade": "12-04-22",
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }]
                },

                {
                    "mainQuestion": {
                        "profile": {
                            "username": "j.miller",
                            "_id": "st210"
                            },
                        "references": {
                            "year": "2010",
                            "session": "N",
                            "paper": "P2",
                            "syllabus": "Z",
                            "topic": "moles and stoichiometry"
                        },
                        "question": {
                            "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                            "attachments": {
                                "audio": True,
                                "image": True
                            }
                        },
                        "dateThreadWasMade": "12-04-2022"
                    },
                    "responses": [{
                        "profile": {
                            "username": "b.baggins",
                                "_id": "st213"
                        },
                        "answer": {
                            "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                            "attachments": {
                                "audio": True,
                                "video": True
                            }
                        },
                        "likes": 253,
                        "dateResponseWasMade": "12-04-22",
                    
                        "responses":[
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "level one nesting using recursion",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                                
                                "responses":[
                                    {
                                        "profile": {
                                            "username": "b.baggins",
                                                "_id": "st213"
                                        },
                                        "answer": {
                                            "description": "level two nesting using recursion",
                                            "attachments": {
                                                "audio": True,
                                                "video": True
                                            }
                                        },
                                        "likes": 253,
                                        "dateResponseWasMade": "12-04-22",
                                        "responses":[
                                            {
                                                "profile": {
                                                    "username": "b.baggins",
                                                        "_id": "st213"
                                                },
                                                "answer": {
                                                    "description": "level one nesting using recursion",
                                                    "attachments": {
                                                        "audio": True,
                                                        "video": True
                                                    }
                                                },
                                                "likes": 253,
                                                "dateResponseWasMade": "12-04-22",
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }]
                },

                {
                    "mainQuestion": {
                        "profile": {
                            "username": "j.miller",
                            "_id": "st210"
                            },
                        "references": {
                            "year": "2010",
                            "session": "N",
                            "paper": "P2",
                            "syllabus": "Z",
                            "topic": "moles and stoichiometry"
                        },
                        "question": {
                            "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                            "attachments": {
                                "audio": True,
                                "image": True
                            }
                        },
                        "dateThreadWasMade": "12-04-2022"
                    },
                    "responses": [{
                        "profile": {
                            "username": "b.baggins",
                                "_id": "st213"
                        },
                        "answer": {
                            "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                            "attachments": {
                                "audio": True,
                                "video": True
                            }
                        },
                        "likes": 253,
                        "dateResponseWasMade": "12-04-22",
                    
                        "responses":[
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "level one nesting using recursion",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                                
                                "responses":[
                                    {
                                        "profile": {
                                            "username": "b.baggins",
                                                "_id": "st213"
                                        },
                                        "answer": {
                                            "description": "level two nesting using recursion",
                                            "attachments": {
                                                "audio": True,
                                                "video": True
                                            }
                                        },
                                        "likes": 253,
                                        "dateResponseWasMade": "12-04-22",
                                        "responses":[
                                            {
                                                "profile": {
                                                    "username": "b.baggins",
                                                        "_id": "st213"
                                                },
                                                "answer": {
                                                    "description": "level one nesting using recursion",
                                                    "attachments": {
                                                        "audio": True,
                                                        "video": True
                                                    }
                                                },
                                                "likes": 253,
                                                "dateResponseWasMade": "12-04-22",
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }]
                },

                {
                    "mainQuestion": {
                        "profile": {
                            "username": "j.miller",
                            "_id": "st210"
                            },
                        "references": {
                            "year": "2010",
                            "session": "N",
                            "paper": "P2",
                            "syllabus": "Z",
                            "topic": "moles and stoichiometry"
                        },
                        "question": {
                            "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                            "attachments": {
                                "audio": True,
                                "image": True
                            }
                        },
                        "dateThreadWasMade": "12-04-2022"
                    },
                    "responses": [{
                        "profile": {
                            "username": "b.baggins",
                                "_id": "st213"
                        },
                        "answer": {
                            "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                            "attachments": {
                                "audio": True,
                                "video": True
                            }
                        },
                        "likes": 253,
                        "dateResponseWasMade": "12-04-22",
                    
                        "responses":[
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "level one nesting using recursion",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                                
                                "responses":[
                                    {
                                        "profile": {
                                            "username": "b.baggins",
                                                "_id": "st213"
                                        },
                                        "answer": {
                                            "description": "level two nesting using recursion",
                                            "attachments": {
                                                "audio": True,
                                                "video": True
                                            }
                                        },
                                        "likes": 253,
                                        "dateResponseWasMade": "12-04-22",
                                        "responses":[
                                            {
                                                "profile": {
                                                    "username": "b.baggins",
                                                        "_id": "st213"
                                                },
                                                "answer": {
                                                    "description": "level one nesting using recursion",
                                                    "attachments": {
                                                        "audio": True,
                                                        "video": True
                                                    }
                                                },
                                                "likes": 253,
                                                "dateResponseWasMade": "12-04-22",
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }]
                },

                {
                    "mainQuestion": {
                        "profile": {
                            "username": "j.miller",
                            "_id": "st210"
                            },
                        "references": {
                            "year": "2010",
                            "session": "N",
                            "paper": "P2",
                            "syllabus": "Z",
                            "topic": "moles and stoichiometry"
                        },
                        "question": {
                            "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                            "attachments": {
                                "audio": True,
                                "image": True
                            }
                        },
                        "dateThreadWasMade": "12-04-2022"
                    },
                    "responses": [{
                        "profile": {
                            "username": "b.baggins",
                                "_id": "st213"
                        },
                        "answer": {
                            "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                            "attachments": {
                                "audio": True,
                                "video": True
                            }
                        },
                        "likes": 253,
                        "dateResponseWasMade": "12-04-22",
                    
                        "responses":[
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "level one nesting using recursion",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                                
                                "responses":[
                                    {
                                        "profile": {
                                            "username": "b.baggins",
                                                "_id": "st213"
                                        },
                                        "answer": {
                                            "description": "level two nesting using recursion",
                                            "attachments": {
                                                "audio": True,
                                                "video": True
                                            }
                                        },
                                        "likes": 253,
                                        "dateResponseWasMade": "12-04-22",
                                        "responses":[
                                            {
                                                "profile": {
                                                    "username": "b.baggins",
                                                        "_id": "st213"
                                                },
                                                "answer": {
                                                    "description": "level one nesting using recursion",
                                                    "attachments": {
                                                        "audio": True,
                                                        "video": True
                                                    }
                                                },
                                                "likes": 253,
                                                "dateResponseWasMade": "12-04-22",
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }]
                },

                {
                    "mainQuestion": {
                        "profile": {
                            "username": "j.miller",
                            "_id": "st210"
                            },
                        "references": {
                            "year": "2010",
                            "session": "N",
                            "paper": "P2",
                            "syllabus": "Z",
                            "topic": "moles and stoichiometry"
                        },
                        "question": {
                            "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                            "attachments": {
                                "audio": True,
                                "image": True
                            }
                        },
                        "dateThreadWasMade": "12-04-2022"
                    },
                    "responses": [{
                        "profile": {
                            "username": "b.baggins",
                                "_id": "st213"
                        },
                        "answer": {
                            "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                            "attachments": {
                                "audio": True,
                                "video": True
                            }
                        },
                        "likes": 253,
                        "dateResponseWasMade": "12-04-22",
                    
                        "responses":[
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "level one nesting using recursion",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                                
                                "responses":[
                                    {
                                        "profile": {
                                            "username": "b.baggins",
                                                "_id": "st213"
                                        },
                                        "answer": {
                                            "description": "level two nesting using recursion",
                                            "attachments": {
                                                "audio": True,
                                                "video": True
                                            }
                                        },
                                        "likes": 253,
                                        "dateResponseWasMade": "12-04-22",
                                        "responses":[
                                            {
                                                "profile": {
                                                    "username": "b.baggins",
                                                        "_id": "st213"
                                                },
                                                "answer": {
                                                    "description": "level one nesting using recursion",
                                                    "attachments": {
                                                        "audio": True,
                                                        "video": True
                                                    }
                                                },
                                                "likes": 253,
                                                "dateResponseWasMade": "12-04-22",
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }]
                },

                {
                    "mainQuestion": {
                        "profile": {
                            "username": "j.miller",
                            "_id": "st210"
                            },
                        "references": {
                            "year": "2010",
                            "session": "N",
                            "paper": "P2",
                            "syllabus": "Z",
                            "topic": "moles and stoichiometry"
                        },
                        "question": {
                            "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                            "attachments": {
                                "audio": True,
                                "image": True
                            }
                        },
                        "dateThreadWasMade": "12-04-2022"
                    },
                    "responses": [{
                        "profile": {
                            "username": "b.baggins",
                                "_id": "st213"
                        },
                        "answer": {
                            "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                            "attachments": {
                                "audio": True,
                                "video": True
                            }
                        },
                        "likes": 253,
                        "dateResponseWasMade": "12-04-22",
                    
                        "responses":[
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "level one nesting using recursion",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                                
                                "responses":[
                                    {
                                        "profile": {
                                            "username": "b.baggins",
                                                "_id": "st213"
                                        },
                                        "answer": {
                                            "description": "level two nesting using recursion",
                                            "attachments": {
                                                "audio": True,
                                                "video": True
                                            }
                                        },
                                        "likes": 253,
                                        "dateResponseWasMade": "12-04-22",
                                        "responses":[
                                            {
                                                "profile": {
                                                    "username": "b.baggins",
                                                        "_id": "st213"
                                                },
                                                "answer": {
                                                    "description": "level one nesting using recursion",
                                                    "attachments": {
                                                        "audio": True,
                                                        "video": True
                                                    }
                                                },
                                                "likes": 253,
                                                "dateResponseWasMade": "12-04-22",
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }]
                },

                {
                    "mainQuestion": {
                        "profile": {
                            "username": "j.miller",
                            "_id": "st210"
                            },
                        "references": {
                            "year": "2010",
                            "session": "N",
                            "paper": "P2",
                            "syllabus": "Z",
                            "topic": "moles and stoichiometry"
                        },
                        "question": {
                            "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                            "attachments": {
                                "audio": True,
                                "image": True
                            }
                        },
                        "dateThreadWasMade": "12-04-2022"
                    },
                    "responses": [{
                        "profile": {
                            "username": "b.baggins",
                                "_id": "st213"
                        },
                        "answer": {
                            "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                            "attachments": {
                                "audio": True,
                                "video": True
                            }
                        },
                        "likes": 253,
                        "dateResponseWasMade": "12-04-22",
                    
                        "responses":[
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "level one nesting using recursion",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                                
                                "responses":[
                                    {
                                        "profile": {
                                            "username": "b.baggins",
                                                "_id": "st213"
                                        },
                                        "answer": {
                                            "description": "level two nesting using recursion",
                                            "attachments": {
                                                "audio": True,
                                                "video": True
                                            }
                                        },
                                        "likes": 253,
                                        "dateResponseWasMade": "12-04-22",
                                        "responses":[
                                            {
                                                "profile": {
                                                    "username": "b.baggins",
                                                        "_id": "st213"
                                                },
                                                "answer": {
                                                    "description": "level one nesting using recursion",
                                                    "attachments": {
                                                        "audio": True,
                                                        "video": True
                                                    }
                                                },
                                                "likes": 253,
                                                "dateResponseWasMade": "12-04-22",
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }]
                },

                {
                    "mainQuestion": {
                        "profile": {
                            "username": "j.miller",
                            "_id": "st210"
                            },
                        "references": {
                            "year": "2010",
                            "session": "N",
                            "paper": "P2",
                            "syllabus": "Z",
                            "topic": "moles and stoichiometry"
                        },
                        "question": {
                            "description": "Carboxylic acids belong to a class of organic compounds in which a carbon (C) atom is bonded to an oxygen (O) atom by a double bond and to a hydroxyl group (−OH) by a single bond. A : I am trying to add silica to the sides of gold nanobipyramids (AuBP) such that only the tips are exposed. I have been following two papers to perform this reaction scheme - (1).",
                            "attachments": {
                                "audio": True,
                                "image": True
                            }
                        },
                        "dateThreadWasMade": "12-04-2022"
                    },
                    "responses": [{
                        "profile": {
                            "username": "b.baggins",
                                "_id": "st213"
                        },
                        "answer": {
                            "description": "The organosilane is require, silica has -OH group while gold has thiol. You need a linkage agent, MPTMS for example.",
                            "attachments": {
                                "audio": True,
                                "video": True
                            }
                        },
                        "likes": 253,
                        "dateResponseWasMade": "12-04-22",
                    
                        "responses":[
                            {
                                "profile": {
                                    "username": "b.baggins",
                                        "_id": "st213"
                                },
                                "answer": {
                                    "description": "level one nesting using recursion",
                                    "attachments": {
                                        "audio": True,
                                        "video": True
                                    }
                                },
                                "likes": 253,
                                "dateResponseWasMade": "12-04-22",
                                
                                "responses":[
                                    {
                                        "profile": {
                                            "username": "b.baggins",
                                                "_id": "st213"
                                        },
                                        "answer": {
                                            "description": "level two nesting using recursion",
                                            "attachments": {
                                                "audio": True,
                                                "video": True
                                            }
                                        },
                                        "likes": 253,
                                        "dateResponseWasMade": "12-04-22",
                                        "responses":[
                                            {
                                                "profile": {
                                                    "username": "b.baggins",
                                                        "_id": "st213"
                                                },
                                                "answer": {
                                                    "description": "level one nesting using recursion",
                                                    "attachments": {
                                                        "audio": True,
                                                        "video": True
                                                    }
                                                },
                                                "likes": 253,
                                                "dateResponseWasMade": "12-04-22",
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }]
                },
            ])
    new_filtered = []
    if request.method == "POST":
        search_value = request.form.get("search_value")
        if search_value:
            filters.append(search_value)
            for thread in filtered:
                topic = thread.get("mainQuestion").get("references").get("topic")
                if topic.lower() == search_value.lower():
                    new_filtered.append(thread)

    if len(new_filtered) >=1:
        filtered = np.array(new_filtered)

    # filters = np.array(filters)

    return render_template("index.html", threads=filtered, filters=filters)



if __name__ == "__main__":
    app.run()
    
    