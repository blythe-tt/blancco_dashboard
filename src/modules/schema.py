credentials_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
        "security_token": {"type": "string"},
        "domain": {"type": "string"},
    },
    "required": ["username","password","security_token"],
    "additionalProperties": False
}

blancco_schema = {
    "type": "object",
    "properties": {
        "assetid": {
            "type": "string",
            "minLength": 8,
            "maxLength": 8,
            "pattern": "^[0-9]*$"
        },
    },
    "required": ["assetid"],
    "additionalProperties": False
}

salesforce_schema = {
    "type": "object",
    "properties": {
        "Name": {
            "type": "string",
            "minLength": 8,
            "if": {
                "pattern": "^[0-9]*$"
            },
            "then": {
                "maxLength": 8
            },
            "else": {
                "maxLength": 255
            }
        },
        "Asset_Number__c": {
            "type": "string",
            "minLength": 8,
            "maxLength": 127,
            "if": {
                "pattern": "^[0-9]*$"
            },
            "then": {
                "maxLength": 8
            },
            "else": {
                "maxLength": 127
            }
        },
        "Opportunity__c": {
            "type": "string",
            "minLength": 18,
            "maxLength": 18,
            "pattern": "^[A-Za-z0-9]{18}$",
        },
        "Donor_Asset_Number__c": {
            "type": "string",
            "minLength": 3,
            "maxLength": 64
        },
        "Asset_Quantity__c": {
            "type": "integer",
            "exclusiveMinimum": 0,
            "Maximum": 99999
        },
        "AccountId": {
            "type": "string",
            "minLength": 18,
            "maxLength": 18,
            "pattern": "^[A-Za-z0-9]{18}$",
        },
        "Asset_Type__c": {
            "enum": ["null","Desktop", "Laptop", "Monitor", "Box", "Shipping Box", "Server", "Virtual Box", "Storage Pallet", "Printer", "Projector", "Switch", "Hard Drive", "Mobile Phone", "Laptop Charger", "Shipping Container", "Tablet", "Disk Drive", "Raspberry PI"]
        },
        "ContactId": {
            "type": "string",
            "minLength": 18,
            "maxLength": 18,
            "pattern": "^[A-Za-z0-9]{18}$",
        },
        "Make__c": {
            "type": "string",
            "maxLength": 64
        },
        "Status": {
            "enum": ["null","Registered", "Pre-tested", "Purchased", "Installed", "Wiped", "Imaged", "Imaged for Africa including Educational Software", "Imaged for Sale", "Boxed for Shipping", "Shipped", "Scrapped", "Sold", "Retained for Operations"]
        },
        "Model__c": {
            "type": "string",
            "maxLength": 64
        },
        "SerialNumber": {
            "type": "string",
            "maxLength": 80,
        },
        "Recipient_Account__c": {
            "type": "string",
            "minLength": 18,
            "maxLength": 18,
            "pattern": "^[A-Za-z0-9]{18}$",
        },
        "ParentId": {
            "type": "string",
            "if": {
                "pattern": "null"
            },
            "then": {
            },
            "else": {
                "pattern": "^[A-Za-z0-9]{18}$",
                "minLength": 18,
                "maxLength": 18,
            }
        },
        "Processor__c": {
            "type": "string",
            "maxLength": 128
        },
        "Ram__c": {
            "type": "string",
            "maxLength": 64
        },
        "OS_Installed__c": {
            "type": "string",
            "maxLength": 64
        },
        "Disk_Erase_Type__c": {
            "type": "string",
            "maxLength": 128
        },
        "Erase_Time__c": {
            "type": "string",
            "maxLength": 32
        },
        "Disk_Model__c": {
            "type": "string",
            "maxLength": 127
        },
        "Erase_Status__c": {
            "type": "string",
            "maxLength": 255
        },
        "Erase_Rounds__c": {
            "type": "string",
            "maxLength": 255
        },
        "Erase_Exception_Message__c": {
            "type": "string",
            "maxLength": 255
        },
        "Erase_Failure_Message__c": {
            "type": "string",
            "maxLength": 255
        },
        "Erase_Information_Message__c": {
            "type": "string",
            "maxLength": 255
        },
        "Date_Sold__c": {
            "type": "string",
            "minLength": 10,
            "maxLength": 10
        },
    },
    "required": ["Name"],
    "additionalProperties": False
}
salesforce_create_schema = {
    "required": ["Name", "Asset_Number__c", "Opportunity__c"],
    "anyOf": [
        {"required" : ["AccountId"]},
        {"required" : ["ContactId"]}
    ],
}
salesforce_search_schema = {
    "type": "object",
    "properties": {
        "Name": {
            "type": "string",
            "minLength": 8,
            "if": {
                "pattern": "^[0-9]*$"
            },
            "then": {
                "maxLength": 8
            },
            "else": {
                "maxLength": 255
            }
        },
        "Id": {
            "type": "string",
            "minLength": 18,
            "maxLength": 18,
            "pattern": "^[A-Za-z0-9]{18}$",
        }
    },
    "additionalProperties": False
}
salesforce_request_schema = {
    "type": "object",
    "properties": {
            "Name": {
                "type": "string",
                "minLength": 8,
                "if": {
                    "pattern": "^[0-9]*$"
                },
                "then": {
                    "maxLength": 8
                },
                "else": {
                    "maxLength": 255
                }
        }
    },
    "required": ["Name"],
    "additionalProperties": False
}
salesforce_summary_request_schema = {
    "type": "object",
    "properties": {
        "Name": {
            "type": "string",
            "minLength": 8,
            "if": {
                "pattern": "^[0-9]*$"
            },
            "then": {
                "maxLength": 8
            },
            "else": {
                "maxLength": 255
            }
        },
        "Id": {
            "type": "string",
            "minLength": 18,
            "maxLength": 18,
            "pattern": "^[A-Za-z0-9]{18}$",
        }
    },
    "oneOf": [
        {"required" : ["Name"]},
        {"required" : ["Id"]}
    ],
}
salesforce_opportunity_search_schema = {}
salesforce_opportunity_request_schema = {
    "type": "object",
    "properties": {
        "Name": {
            "type": "string",
            "minLength": 3,
            "maxLength": 255
        },
        "Id": {
            "type": "string",
            "minLength": 18,
            "maxLength": 18,
            "pattern": "^[A-Za-z0-9]{18}$",
        },
        "IsDeleted": {
            "type": "string",
            "minLength": 0
        },
        "AccountId": {
            "type": "string",
            "minLength": 0
        },
        "RecordTypeId": {
            "type": "string",
            "minLength": 0
        },
        "IsPrivate": {
            "type": "string",
            "minLength": 0
        },
        "Description": {
            "type": "string",
            "minLength": 0
        },
        "StageName": {
            "type": "string",
            "minLength": 0
        },
        "Amount": {
            "type": "string",
            "minLength": 0
        },
        "ExpectedRevenue": {
            "type": "string",
            "minLength": 0
        },
        "TotalOpportunityQuantity": {
            "type": "string",
            "minLength": 0
        },
        "CloseDate": {
            "type": "string",
            "minLength": 0
        },
        "Type": {
            "type": "string",
            "minLength": 0
        },
        "NextStep": {
            "type": "string",
            "minLength": 0
        },
        "LeadSource": {
            "type": "string",
            "minLength": 0
        },
        "IsClosed": {
            "type": "string",
            "minLength": 0
        },
        "IsWon": {
            "type": "string",
            "minLength": 0
        },
        "ForecastCategory": {
            "type": "string",
            "minLength": 0
        },
        "ForecastCategoryName": {
            "type": "string",
            "minLength": 0
        },
        "CampaignId": {
            "type": "string",
            "minLength": 0
        },
        "HasOpportunityLineItem": {
            "type": "string",
            "minLength": 0
        },
        "Pricebook2Id": {
            "type": "string",
            "minLength": 0
        },
        "OwnerId": {
            "type": "string",
            "minLength": 0
        },
        "CreatedDate": {
            "type": "string",
            "minLength": 0
        },
        "CreatedById": {
            "type": "string",
            "minLength": 0
        },
        "LastModifiedDate": {
            "type": "string",
            "minLength": 0
        },
        "LastModifiedById": {
            "type": "string",
            "minLength": 0
        },
        "SystemModstamp": {
            "type": "string",
            "minLength": 0
        },
        "LastActivityDate": {
            "type": "string",
            "minLength": 0
        },
        "LastStageChangeDate": {
            "type": "string",
            "minLength": 0
        },
        "FiscalQuarter": {
            "type": "string",
            "minLength": 0
        },
        "FiscalYear": {
            "type": "string",
            "minLength": 0
        },
        "Fiscal": {
            "type": "string",
            "minLength": 0
        },
        "ContactId": {
            "type": "string",
            "minLength": 0
        },
        "LastViewedDate": {
            "type": "string",
            "minLength": 0
        },
        "LastReferencedDate": {
            "type": "string",
            "minLength": 0
        },
        "ContractId": {
            "type": "string",
            "minLength": 0
        },
        "HasOpenActivity": {
            "type": "string",
            "minLength": 0
        },
        "HasOverdueTask": {
            "type": "string",
            "minLength": 0
        },
        "LastAmountChangedHistoryId": {
            "type": "string",
            "minLength": 0
        },
        "LastCloseDateChangedHistoryId": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Amount_Outstanding__c": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Contact_Id_for_Role__c": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Do_Not_Automatically_Create_Payment__c": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Is_Opp_From_Individual__c": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Member_Level__c": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Membership_End_Date__c": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Membership_Origin__c": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Membership_Start_Date__c": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Amount_Written_Off__c": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Number_of_Payments__c": {
            "type": "string",
            "minLength": 0
        },
        "npe01__Payments_Made__c": {
            "type": "string",
            "minLength": 0
        },
        "npo02__CombinedRollupFieldset__c": {
            "type": "string",
            "minLength": 0
        },
        "npo02__systemHouseholdContactRoleProcessor__c": {
            "type": "string",
            "minLength": 0
        },
        "npe03__Recurring_Donation__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Batch__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Acknowledgment_Date__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Acknowledgment_Status__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Recurring_Donation_Installment_Name__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Recurring_Donation_Installment_Number__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Primary_Contact__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Grant_Contract_Date__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Grant_Contract_Number__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Grant_Period_End_Date__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Grant_Period_Start_Date__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Grant_Program_Area_s__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Grant_Requirements_Website__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Is_Grant_Renewal__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Previous_Grant_Opportunity__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Requested_Amount__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Next_Grant_Deadline_Due_Date__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Primary_Contact_Campaign_Member_Status__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Honoree_Contact__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Honoree_Name__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Notification_Message__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Notification_Preference__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Notification_Recipient_Contact__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Notification_Recipient_Information__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Notification_Recipient_Name__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Tribute_Type__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Matching_Gift_Account__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Matching_Gift_Employer__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Matching_Gift_Status__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Matching_Gift__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Fair_Market_Value__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__In_Kind_Description__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__In_Kind_Donor_Declared_Value__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__In_Kind_Type__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Ask_Date__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Closed_Lost_Reason__c": {
            "type": "string",
            "minLength": 0
        },
        "npsp__Gift_Strategy__c": {
            "type": "string",
            "minLength": 0
        },
        "DVI_Cables__c": {
            "type": "string",
            "minLength": 0
        },
        "Other_Equipment__c": {
            "type": "string",
            "minLength": 0
        },
        "Desktops__c": {
            "type": "string",
            "minLength": 0
        },
        "Laptops__c": {
            "type": "string",
            "minLength": 0
        },
        "Monitors__c": {
            "type": "string",
            "minLength": 0
        },
        "Keyboards__c": {
            "type": "string",
            "minLength": 0
        },
        "Mice__c": {
            "type": "string",
            "minLength": 0
        },
        "VGA_Cables__c": {
            "type": "string",
            "minLength": 0
        },
        "Power_Leads_Kettle__c": {
            "type": "string",
            "minLength": 0
        },
        "Power_Leads_Clover__c": {
            "type": "string",
            "minLength": 0
        },
        "Power_Adaptors__c": {
            "type": "string",
            "minLength": 0
        },
        "Mice_PS2__c": {
            "type": "string",
            "minLength": 0
        },
        "Keyboards_PS2__c": {
            "type": "string",
            "minLength": 0
        },
        "Order_Product__c": {
            "type": "string",
            "minLength": 0
        },
        "Product__c": {
            "type": "string",
            "minLength": 0
        },
        "HDDs__c": {
            "type": "string",
            "minLength": 0
        },
        "Laser_Printers__c": {
            "type": "string",
            "minLength": 0
        },
        "Projectors__c": {
            "type": "string",
            "minLength": 0
        },
        "Switches__c": {
            "type": "string",
            "minLength": 0
        },
        "Age_of_PCs_laptops__c": {
            "type": "string",
            "minLength": 0
        },
        "Any_other_equipment_or_comments__c": {
            "type": "string",
            "minLength": 0
        },
        "Computer_accessories__c": {
            "type": "string",
            "minLength": 0
        },
        "Expected_Number_of_Desktops__c": {
            "type": "string",
            "minLength": 0
        },
        "Expected_Number_of_Laptops__c": {
            "type": "string",
            "minLength": 0
        },
        "Expected_Number_of_Monitors__c": {
            "type": "string",
            "minLength": 0
        },
        "Location__c": {
            "type": "string",
            "minLength": 0
        },
        "Mobile_phones_or_smartphones__c": {
            "type": "string",
            "minLength": 0
        },
        "Operating_system__c": {
            "type": "string",
            "minLength": 0
        },
        "PCs_or_laptops__c": {
            "type": "string",
            "minLength": 0
        },
        "RAM__c": {
            "type": "string",
            "minLength": 0
        },
        "Tablets_or_iPads__c": {
            "type": "string",
            "minLength": 0
        },
        "Desktops_Laptops__c": {
            "type": "string",
            "minLength": 0
        },
        "Tablets_Delivered__c": {
            "type": "string",
            "minLength": 0
        },
        "Smartphones_Delivered__c": {
            "type": "string",
            "minLength": 0
        },
        "DDC_Requested__c": {
            "type": "string",
            "minLength": 0
        },
        "Days_since_Last_Activity__c": {
            "type": "string",
            "minLength": 0
        },
        "DDC_Sent__c": {
            "type": "string",
            "minLength": 0
        },
        "DDC_Days_T__c": {
            "type": "string",
            "minLength": 0
        },
        "DDC_Days_Outstanding__c": {
            "type": "string",
            "minLength": 0
        },
        "Wipe_Method_Requested__c": {
            "type": "string",
            "minLength": 0
        },
        "FGD_Collection__c": {
            "type": "string",
            "minLength": 0
        },
        "FGD_Comment__c": {
            "type": "string",
            "minLength": 0
        }
    },
    "required": ["Name"],
    "additionalProperties": False
}

salesforce_opportunity_summary_schema = {
    "type": "object",
    "properties": {
        "Name": {
            "type": "string",
            "minLength": 3,
            "maxLength": 255
        },
        "Id": {
            "type": "string",
            "minLength": 18,
            "maxLength": 18,
            "pattern": "^[A-Za-z0-9]{18}$",
        }
    },
    "oneOf": [
        {"required" : ["Name"]},
        {"required" : ["Id"]}
    ],
}