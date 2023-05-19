# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)]
# From type library 'SIDRASolutions.SI.API.tlb'
# On Wed Sep 21 10:28:19 2022
'SIDRA INTERSECTION 9.1 API'
makepy_version = '0.5.01'
python_version = 0x30907f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{F1DF19D9-2999-4A13-9436-4CE374012F6A}')
MajorVersion = 9
MinorVersion = 1
LibraryFlags = 8
LCID = 0x0

class constants:
	enumSILicenseType_NETWORK     =1          # from enum enumSILicenseType
	enumSILicenseType_PLUS        =0          # from enum enumSILicenseType
	enumSSFloatingConsumptionMethod_Offline=1          # from enum enumSSFloatingConsumptionMethod
	enumSSFloatingConsumptionMethod_Online=0          # from enum enumSSFloatingConsumptionMethod
	enumSSLicenseCategory_Educational=2          # from enum enumSSLicenseCategory
	enumSSLicenseCategory_Internal=5          # from enum enumSSLicenseCategory
	enumSSLicenseCategory_Preview =3          # from enum enumSSLicenseCategory
	enumSSLicenseCategory_Professional=1          # from enum enumSSLicenseCategory
	enumSSLicenseCategory_Trial   =0          # from enum enumSSLicenseCategory
	enumSSLicenseCategory_Workshop=4          # from enum enumSSLicenseCategory
	enumSSLicenseExpiryType_NotTimeLimited=1          # from enum enumSSLicenseExpiryType
	enumSSLicenseExpiryType_TimeLimited=0          # from enum enumSSLicenseExpiryType
	enumSSLicenseLevel_Enterprise =3          # from enum enumSSLicenseLevel
	enumSSLicenseLevel_Floating   =2          # from enum enumSSLicenseLevel
	enumSSLicenseLevel_OnePC      =1          # from enum enumSSLicenseLevel
	enumSSLicenseLevel_OnePC_NoBinding=4          # from enum enumSSLicenseLevel
	enumSSLicenseLevel_Unlicensed =0          # from enum enumSSLicenseLevel
	enumSSLicenseStatus_CheckValidate=6          # from enum enumSSLicenseStatus
	enumSSLicenseStatus_Delete    =8          # from enum enumSSLicenseStatus
	enumSSLicenseStatus_Duplicate =1          # from enum enumSSLicenseStatus
	enumSSLicenseStatus_Expired   =5          # from enum enumSSLicenseStatus
	enumSSLicenseStatus_Fraud     =3          # from enum enumSSLicenseStatus
	enumSSLicenseStatus_Ok        =0          # from enum enumSSLicenseStatus
	enumSSLicenseStatus_Returned  =4          # from enum enumSSLicenseStatus
	enumSSLicenseStatus_Upgrade   =7          # from enum enumSSLicenseStatus
	enumSSLicenseStatus_Void      =2          # from enum enumSSLicenseStatus
	enumSSLicenseWatermarkOption_NotShowing=1          # from enum enumSSLicenseWatermarkOption
	enumSSLicenseWatermarkOption_Showing=0          # from enum enumSSLicenseWatermarkOption
	enumSSLicensingMethod_Custom  =2          # from enum enumSSLicensingMethod
	enumSSLicensingMethod_Fixed   =0          # from enum enumSSLicensingMethod
	enumSSLicensingMethod_Floating=1          # from enum enumSSLicensingMethod

from win32com.client import DispatchBaseClass
class IDisposable(DispatchBaseClass):
	CLSID = IID('{805D7A98-D4AF-3F0F-967F-E5CF45312D2C}')
	coclass_clsid = IID('{D92122F2-74F7-4A2B-953E-B75CF1B2738D}')

	def Dispose(self):
		return self._oleobj_.InvokeTypes(1610743808, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IEnumerable(DispatchBaseClass):
	CLSID = IID('{496B0ABE-CDEE-11D3-88E8-00902754C43A}')
	coclass_clsid = IID('{A5050181-1C6A-4BF4-A8C5-4A712A954A90}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,1,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00020404-0000-0000-C000-000000000046}')

class ISIAPI(DispatchBaseClass):
	CLSID = IID('{7FB3D82F-C33F-4919-AF8B-5AE805445CA5}')
	coclass_clsid = IID('{D92122F2-74F7-4A2B-953E-B75CF1B2738D}')

	def Close(self):
		return self._oleobj_.InvokeTypes(1610743818, LCID, 1, (11, 0), (),)

	def CloseDbConnection(self):
		return self._oleobj_.InvokeTypes(1610743817, LCID, 1, (11, 0), (),)

	def CloseProject(self):
		return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (11, 0), (),)

	def CreateAndOpenProject(self, filename=defaultNamedNotOptArg, newProjectName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743819, LCID, 1, (11, 0), ((8, 1), (8, 1)),filename
			, newProjectName)

	def OpenDbConnection(self):
		return self._oleobj_.InvokeTypes(1610743816, LCID, 1, (11, 0), (),)

	def OpenProject(self, filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (11, 0), ((8, 1),),filename
			)

	def SubmitDataChanges(self):
		return self._oleobj_.InvokeTypes(1610743815, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"IntPtrSize": (1610743811, 2, (3, 0), (), "IntPtrSize", None),
		"IsLicensed": (1610743809, 2, (11, 0), (), "IsLicensed", None),
		"LastErrorMessage": (1610743810, 2, (8, 0), (), "LastErrorMessage", None),
		# Method 'Project' returns object of type 'ISIAPIProject'
		"Project": (1610743808, 2, (9, 0), (), "Project", '{5817180B-2283-40FB-8068-C2F2D656EF04}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIAnalysis(DispatchBaseClass):
	CLSID = IID('{C3D8FE89-6620-45E7-898A-F4108FA95E6F}')
	coclass_clsid = IID('{3988FB26-C8F8-4AA9-8FCB-B803193F4D50}')

	_prop_map_get_ = {
		"Analysis_option": (1610743809, 2, (3, 0), (), "Analysis_option", None),
		"Design_Life_Constant_num_years": (1610743821, 2, (3, 0), (), "Design_Life_Constant_num_years", None),
		"Design_Life_Growth_Model": (1610743815, 2, (3, 0), (), "Design_Life_Growth_Model", None),
		"Design_Life_Is_constant_num_years_applied": (1610743819, 2, (11, 0), (), "Design_Life_Is_constant_num_years_applied", None),
		"Design_Life_Objective": (1610743813, 2, (3, 0), (), "Design_Life_Objective", None),
		"Design_Life_Years": (1610743817, 2, (3, 0), (), "Design_Life_Years", None),
		"Flow_Scale_Constant_factor": (1610743831, 2, (4, 0), (), "Flow_Scale_Constant_factor", None),
		"Flow_Scale_Is_constant_factor_applied": (1610743829, 2, (11, 0), (), "Flow_Scale_Is_constant_factor_applied", None),
		"Flow_Scale_Lower": (1610743825, 2, (4, 0), (), "Flow_Scale_Lower", None),
		"Flow_Scale_Objective": (1610743823, 2, (3, 0), (), "Flow_Scale_Objective", None),
		"Flow_Scale_Upper": (1610743827, 2, (4, 0), (), "Flow_Scale_Upper", None),
		"Result_lane_origin": (1610743839, 2, (3, 0), (), "Result_lane_origin", None),
		"Result_laneno": (1610743841, 2, (3, 0), (), "Result_laneno", None),
		"Result_leg_origin": (1610743837, 2, (3, 0), (), "Result_leg_origin", None),
		"Result_mc_class": (1610743847, 2, (3, 0), (), "Result_mc_class", None),
		"Result_option": (1610743835, 2, (3, 0), (), "Result_option", None),
		"Result_pedmov_option": (1610743849, 2, (3, 0), (), "Result_pedmov_option", None),
		"Result_pedmov_origin": (1610743851, 2, (3, 0), (), "Result_pedmov_origin", None),
		"Result_pedmov_stage_no": (1610743855, 2, (3, 0), (), "Result_pedmov_stage_no", None),
		"Result_pedmov_type": (1610743853, 2, (3, 0), (), "Result_pedmov_type", None),
		"Result_vehmov_dest": (1610743845, 2, (3, 0), (), "Result_vehmov_dest", None),
		"Result_vehmov_origin": (1610743843, 2, (3, 0), (), "Result_vehmov_origin", None),
		"Selected_sensitivity_groupno": (1610743811, 2, (3, 0), (), "Selected_sensitivity_groupno", None),
		# Method 'SensitivityGeneralParameterGroup' returns object of type 'ISIAPISensitivity'
		"SensitivityGeneralParameterGroup": (1610743833, 2, (9, 0), (), "SensitivityGeneralParameterGroup", '{D025138A-4F4C-4613-8FA7-D1FD5550A50C}'),
		# Method 'SensitivityRoundaboutParameterGroup' returns object of type 'ISIAPISensitivity'
		"SensitivityRoundaboutParameterGroup": (1610743834, 2, (9, 0), (), "SensitivityRoundaboutParameterGroup", '{D025138A-4F4C-4613-8FA7-D1FD5550A50C}'),
		# Method 'Site' returns object of type 'ISIAPISite'
		"Site": (1610743808, 2, (9, 0), (), "Site", '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}'),
	}
	_prop_map_put_ = {
		"Analysis_option": ((1610743809, LCID, 4, 0),()),
		"Design_Life_Constant_num_years": ((1610743821, LCID, 4, 0),()),
		"Design_Life_Growth_Model": ((1610743815, LCID, 4, 0),()),
		"Design_Life_Is_constant_num_years_applied": ((1610743819, LCID, 4, 0),()),
		"Design_Life_Objective": ((1610743813, LCID, 4, 0),()),
		"Design_Life_Years": ((1610743817, LCID, 4, 0),()),
		"Flow_Scale_Constant_factor": ((1610743831, LCID, 4, 0),()),
		"Flow_Scale_Is_constant_factor_applied": ((1610743829, LCID, 4, 0),()),
		"Flow_Scale_Lower": ((1610743825, LCID, 4, 0),()),
		"Flow_Scale_Objective": ((1610743823, LCID, 4, 0),()),
		"Flow_Scale_Upper": ((1610743827, LCID, 4, 0),()),
		"Result_lane_origin": ((1610743839, LCID, 4, 0),()),
		"Result_laneno": ((1610743841, LCID, 4, 0),()),
		"Result_leg_origin": ((1610743837, LCID, 4, 0),()),
		"Result_mc_class": ((1610743847, LCID, 4, 0),()),
		"Result_option": ((1610743835, LCID, 4, 0),()),
		"Result_pedmov_option": ((1610743849, LCID, 4, 0),()),
		"Result_pedmov_origin": ((1610743851, LCID, 4, 0),()),
		"Result_pedmov_stage_no": ((1610743855, LCID, 4, 0),()),
		"Result_pedmov_type": ((1610743853, LCID, 4, 0),()),
		"Result_vehmov_dest": ((1610743845, LCID, 4, 0),()),
		"Result_vehmov_origin": ((1610743843, LCID, 4, 0),()),
		"Selected_sensitivity_groupno": ((1610743811, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIDiagnosticMsg(DispatchBaseClass):
	CLSID = IID('{CC6E10F5-9A73-41A2-BCA8-235D7FB0091A}')
	coclass_clsid = IID('{6BD716CD-F4A3-4CAF-A052-24F92F02130D}')

	_prop_map_get_ = {
		"Log_time": (1610743810, 2, (7, 0), (), "Log_time", None),
		"Message": (1610743808, 2, (8, 0), (), "Message", None),
		"Message_type": (1610743809, 2, (3, 0), (), "Message_type", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIDiagnosticMsgs(DispatchBaseClass):
	CLSID = IID('{CBFD7927-0588-4CF2-BEB4-052B1F31A027}')
	coclass_clsid = IID('{98563BD9-ED3E-4ECA-ABAD-FCC3D86B1021}')

	# Result is of type ISIAPIDiagnosticMsg
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CC6E10F5-9A73-41A2-BCA8-235D7FB0091A}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CC6E10F5-9A73-41A2-BCA8-235D7FB0091A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CC6E10F5-9A73-41A2-BCA8-235D7FB0091A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIGapAcceptanceSpecificApp(DispatchBaseClass):
	CLSID = IID('{8860D705-1B2F-4F1E-B59A-6C4992A3FE9A}')
	coclass_clsid = IID('{8FAEAC43-040F-48C1-9FF0-D8883FFFFE11}')

	_prop_map_get_ = {
		"Critical_gap": (1610743808, 2, (4, 0), (), "Critical_gap", None),
		"End_departures": (1610743812, 2, (4, 0), (), "End_departures", None),
		"Exit_flow_effect": (1610743814, 2, (4, 0), (), "Exit_flow_effect", None),
		"Followup_headway": (1610743810, 2, (4, 0), (), "Followup_headway", None),
		"Percent_opposed_by_nearest": (1610743816, 2, (4, 0), (), "Percent_opposed_by_nearest", None),
	}
	_prop_map_put_ = {
		"Critical_gap": ((1610743808, LCID, 4, 0),()),
		"End_departures": ((1610743812, LCID, 4, 0),()),
		"Exit_flow_effect": ((1610743814, LCID, 4, 0),()),
		"Followup_headway": ((1610743810, LCID, 4, 0),()),
		"Percent_opposed_by_nearest": ((1610743816, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIIsland(DispatchBaseClass):
	CLSID = IID('{E741707B-9A4C-414A-A4F0-482E5F098534}')
	coclass_clsid = IID('{EA335953-2755-4056-860C-5355FA753978}')

	_prop_map_get_ = {
		# Method 'ConnectedIsland' returns object of type 'ISIAPIIsland'
		"ConnectedIsland": (1610743824, 2, (9, 0), (), "ConnectedIsland", '{E741707B-9A4C-414A-A4F0-482E5F098534}'),
		"Fill_style": (1610743817, 2, (3, 0), (), "Fill_style", None),
		"Is_for_freeway": (1610743822, 2, (11, 0), (), "Is_for_freeway", None),
		"Is_pedstage_separator": (1610743810, 2, (11, 0), (), "Is_pedstage_separator", None),
		"Is_rou_splitter": (1610743812, 2, (11, 0), (), "Is_rou_splitter", None),
		"Is_short": (1610743820, 2, (11, 0), (), "Is_short", None),
		"Island_no": (1610743808, 2, (3, 0), (), "Island_no", None),
		# Method 'Leg' returns object of type 'ISIAPILeg'
		"Leg": (1610743819, 2, (9, 0), (), "Leg", '{24A8E5D9-0016-45F2-9941-12E58EE54A05}'),
		"Position": (1610743809, 2, (3, 0), (), "Position", None),
		"Width": (1610743813, 2, (4, 0), (), "Width", None),
		"Width_back": (1610743815, 2, (4, 0), (), "Width_back", None),
	}
	_prop_map_put_ = {
		"ConnectedIsland": ((1610743824, LCID, 8, 0),()),
		"Fill_style": ((1610743817, LCID, 4, 0),()),
		"Is_for_freeway": ((1610743822, LCID, 4, 0),()),
		"Is_pedstage_separator": ((1610743810, LCID, 4, 0),()),
		"Is_short": ((1610743820, LCID, 4, 0),()),
		"Width": ((1610743813, LCID, 4, 0),()),
		"Width_back": ((1610743815, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIIslands(DispatchBaseClass):
	CLSID = IID('{6B55FEF0-D591-4E75-B2BA-81E22B796325}')
	coclass_clsid = IID('{F797F2BF-20A2-4353-9E76-14B778448B3B}')

	def IslandExists(self, Island_no=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Island_no
			)

	# Result is of type ISIAPIIsland
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Island_no=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Island_no
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E741707B-9A4C-414A-A4F0-482E5F098534}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Island_no=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Island_no
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E741707B-9A4C-414A-A4F0-482E5F098534}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E741707B-9A4C-414A-A4F0-482E5F098534}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPILaneApproach(DispatchBaseClass):
	CLSID = IID('{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')
	coclass_clsid = IID('{C64B58F7-7E6C-4D01-B73F-74EE785691D5}')

	def RemoveDisciplines(self):
		return self._oleobj_.InvokeTypes(1610743862, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"Basic_saturation_flow": (1610743824, 2, (3, 0), (), "Basic_saturation_flow", None),
		"Buses_stopping": (1610743844, 2, (3, 0), (), "Buses_stopping", None),
		"Buses_stopping_user": (1610743842, 2, (11, 0), (), "Buses_stopping_user", None),
		"Capacity_adjustment": (1610743834, 2, (4, 0), (), "Capacity_adjustment", None),
		"Configuration": (1610743810, 2, (3, 0), (), "Configuration", None),
		"Control_type": (1610743814, 2, (3, 0), (), "Control_type", None),
		"Delay_model_param": (1610743871, 2, (4, 0), (), "Delay_model_param", None),
		"Delay_model_param_user": (1610743869, 2, (11, 0), (), "Delay_model_param_user", None),
		"Departure_headway_awsc": (1610743859, 2, (4, 0), (), "Departure_headway_awsc", None),
		"Grade": (1610743820, 2, (4, 0), (), "Grade", None),
		"Initial_demand_vol": (1610743873, 2, (4, 0), (), "Initial_demand_vol", None),
		"Is_capacity_adj_for_network": (1610743836, 2, (11, 0), (), "Is_capacity_adj_for_network", None),
		"Is_departure_headway_awsc_applied": (1610743857, 2, (11, 0), (), "Is_departure_headway_awsc_applied", None),
		"Is_dominant_lane": (1610743838, 2, (11, 0), (), "Is_dominant_lane", None),
		"Is_satn_flow_estimation_applied": (1610743863, 2, (11, 0), (), "Is_satn_flow_estimation_applied", None),
		"Is_sliplane_excluded_from_signal_analysis": (1610743850, 2, (11, 0), (), "Is_sliplane_excluded_from_signal_analysis", None),
		"Is_sliplane_included_in_entry_lane_count": (1610743840, 2, (11, 0), (), "Is_sliplane_included_in_entry_lane_count", None),
		# Method 'LaneApproachMovements' returns object of type 'ISIAPILaneApproachMovements'
		"LaneApproachMovements": (1610743852, 2, (9, 0), (), "LaneApproachMovements", '{881029ED-4A7E-4469-A782-F48BF5E0F373}'),
		# Method 'LaneMovements' returns object of type 'ISIAPILaneMovements'
		"LaneMovements": (1610743853, 2, (9, 0), (), "LaneMovements", '{C1711C63-BCCC-41F6-94CC-80BFBF951D74}'),
		"Laneno": (1610743808, 2, (3, 0), (), "Laneno", None),
		"LastErrorMessage": (1610743861, 2, (8, 0), (), "LastErrorMessage", None),
		# Method 'Leg' returns object of type 'ISIAPILeg'
		"Leg": (1610743856, 2, (9, 0), (), "Leg", '{24A8E5D9-0016-45F2-9941-12E58EE54A05}'),
		"Length": (1610743816, 2, (4, 0), (), "Length", None),
		"Parking_manoeuvres": (1610743848, 2, (3, 0), (), "Parking_manoeuvres", None),
		"Parking_manoeuvres_user": (1610743846, 2, (11, 0), (), "Parking_manoeuvres_user", None),
		"Position": (1610743809, 2, (3, 0), (), "Position", None),
		"Saturation_speed": (1610743832, 2, (4, 0), (), "Saturation_speed", None),
		"Saturation_speed_user": (1610743830, 2, (11, 0), (), "Saturation_speed_user", None),
		# Method 'Segment1' returns object of type 'ISIAPILaneSegment'
		"Segment1": (1610743854, 2, (9, 0), (), "Segment1", '{6BE9B7D6-A12E-4CB5-A938-08260963BE84}'),
		# Method 'Segment2' returns object of type 'ISIAPILaneSegment'
		"Segment2": (1610743855, 2, (9, 0), (), "Segment2", '{6BE9B7D6-A12E-4CB5-A938-08260963BE84}'),
		"Shortlane_capacity_factor": (1610743867, 2, (4, 0), (), "Shortlane_capacity_factor", None),
		"Shortlane_capacity_option": (1610743865, 2, (3, 0), (), "Shortlane_capacity_option", None),
		"Slip_control_type": (1610743822, 2, (3, 0), (), "Slip_control_type", None),
		"Type": (1610743812, 2, (3, 0), (), "Type", None),
		"Utilisation": (1610743828, 2, (4, 0), (), "Utilisation", None),
		"Utilisation_user": (1610743826, 2, (11, 0), (), "Utilisation_user", None),
		"Width": (1610743818, 2, (4, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Basic_saturation_flow": ((1610743824, LCID, 4, 0),()),
		"Buses_stopping": ((1610743844, LCID, 4, 0),()),
		"Buses_stopping_user": ((1610743842, LCID, 4, 0),()),
		"Capacity_adjustment": ((1610743834, LCID, 4, 0),()),
		"Configuration": ((1610743810, LCID, 4, 0),()),
		"Control_type": ((1610743814, LCID, 4, 0),()),
		"Delay_model_param": ((1610743871, LCID, 4, 0),()),
		"Delay_model_param_user": ((1610743869, LCID, 4, 0),()),
		"Departure_headway_awsc": ((1610743859, LCID, 4, 0),()),
		"Grade": ((1610743820, LCID, 4, 0),()),
		"Initial_demand_vol": ((1610743873, LCID, 4, 0),()),
		"Is_capacity_adj_for_network": ((1610743836, LCID, 4, 0),()),
		"Is_departure_headway_awsc_applied": ((1610743857, LCID, 4, 0),()),
		"Is_dominant_lane": ((1610743838, LCID, 4, 0),()),
		"Is_satn_flow_estimation_applied": ((1610743863, LCID, 4, 0),()),
		"Is_sliplane_excluded_from_signal_analysis": ((1610743850, LCID, 4, 0),()),
		"Is_sliplane_included_in_entry_lane_count": ((1610743840, LCID, 4, 0),()),
		"Length": ((1610743816, LCID, 4, 0),()),
		"Parking_manoeuvres": ((1610743848, LCID, 4, 0),()),
		"Parking_manoeuvres_user": ((1610743846, LCID, 4, 0),()),
		"Saturation_speed": ((1610743832, LCID, 4, 0),()),
		"Saturation_speed_user": ((1610743830, LCID, 4, 0),()),
		"Shortlane_capacity_factor": ((1610743867, LCID, 4, 0),()),
		"Shortlane_capacity_option": ((1610743865, LCID, 4, 0),()),
		"Slip_control_type": ((1610743822, LCID, 4, 0),()),
		"Type": ((1610743812, LCID, 4, 0),()),
		"Utilisation": ((1610743828, LCID, 4, 0),()),
		"Utilisation_user": ((1610743826, LCID, 4, 0),()),
		"Width": ((1610743818, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILaneApproachMovement(DispatchBaseClass):
	CLSID = IID('{5C8E5D1E-E796-4190-8965-8BBD365D0D7F}')
	coclass_clsid = IID('{A5CA350D-1764-431A-B3DE-4E66AEC098CE}')

	_prop_map_get_ = {
		"Destination": (1610743808, 2, (3, 0), (), "Destination", None),
		"Free_queue": (1610743809, 2, (4, 0), (), "Free_queue", None),
		# Method 'LaneApproach' returns object of type 'ISIAPILaneApproach'
		"LaneApproach": (1610743812, 2, (9, 0), (), "LaneApproach", '{5F156412-3EAE-40A0-99B2-06D8E48D87D1}'),
		# Method 'LaneApproachMovementMCs' returns object of type 'ISIAPILaneApproachMovementMCs'
		"LaneApproachMovementMCs": (1610743811, 2, (9, 0), (), "LaneApproachMovementMCs", '{E94C2A89-6DE0-4AE6-82E9-48DD3B752E1A}'),
	}
	_prop_map_put_ = {
		"Free_queue": ((1610743809, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILaneApproachMovementMC(DispatchBaseClass):
	CLSID = IID('{92115A53-7558-433A-AC10-E109B19E83ED}')
	coclass_clsid = IID('{A8FE0EAC-41F7-4B6D-A03E-BD4296549E04}')

	_prop_map_get_ = {
		"Exists": (1610743809, 2, (11, 0), (), "Exists", None),
		# Method 'LaneApproachMovement' returns object of type 'ISIAPILaneApproachMovement'
		"LaneApproachMovement": (1610743811, 2, (9, 0), (), "LaneApproachMovement", '{5C8E5D1E-E796-4190-8965-8BBD365D0D7F}'),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
	}
	_prop_map_put_ = {
		"Exists": ((1610743809, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILaneApproachMovementMCs(DispatchBaseClass):
	CLSID = IID('{E94C2A89-6DE0-4AE6-82E9-48DD3B752E1A}')
	coclass_clsid = IID('{D0F9DE87-E61E-43C9-AB12-A81DCCF2BE76}')

	# Result is of type ISIAPILaneApproachMovementMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{92115A53-7558-433A-AC10-E109B19E83ED}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{92115A53-7558-433A-AC10-E109B19E83ED}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{92115A53-7558-433A-AC10-E109B19E83ED}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPILaneApproachMovements(DispatchBaseClass):
	CLSID = IID('{881029ED-4A7E-4469-A782-F48BF5E0F373}')
	coclass_clsid = IID('{3C6FB29C-52F6-426B-AE37-987D1910CF22}')

	# Result is of type ISIAPILaneApproachMovement
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Destination
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5C8E5D1E-E796-4190-8965-8BBD365D0D7F}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Destination
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5C8E5D1E-E796-4190-8965-8BBD365D0D7F}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{5C8E5D1E-E796-4190-8965-8BBD365D0D7F}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPILaneApproachs(DispatchBaseClass):
	CLSID = IID('{148779D1-5A0D-48B1-9CBB-7002DAB05D95}')
	coclass_clsid = IID('{78A0E9B9-165B-4790-8B63-0003CEE1381F}')

	# Result is of type ISIAPILaneApproach
	def AddLane(self):
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddLane', '{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')
		return ret

	# Result is of type ISIAPILaneApproach
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Laneno
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')
		return ret

	def LaneApproachExists(self, Laneno=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Laneno
			)

	def RemoveLane(self):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (1610743812, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Laneno
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743812, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPILaneExit(DispatchBaseClass):
	CLSID = IID('{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')
	coclass_clsid = IID('{F142FCA8-DBFF-4477-BA9B-4B6F416B3642}')

	_prop_map_get_ = {
		"Configuration": (1610743810, 2, (3, 0), (), "Configuration", None),
		"Grade": (1610743816, 2, (4, 0), (), "Grade", None),
		"Is_merge_applied": (1610743822, 2, (11, 0), (), "Is_merge_applied", None),
		# Method 'LaneMovements' returns object of type 'ISIAPILaneMovements'
		"LaneMovements": (1610743818, 2, (9, 0), (), "LaneMovements", '{C1711C63-BCCC-41F6-94CC-80BFBF951D74}'),
		"Laneno": (1610743808, 2, (3, 0), (), "Laneno", None),
		# Method 'Leg' returns object of type 'ISIAPILeg'
		"Leg": (1610743821, 2, (9, 0), (), "Leg", '{24A8E5D9-0016-45F2-9941-12E58EE54A05}'),
		"Length": (1610743812, 2, (4, 0), (), "Length", None),
		"Merge_type": (1610743824, 2, (3, 0), (), "Merge_type", None),
		"Position": (1610743809, 2, (3, 0), (), "Position", None),
		# Method 'PriorityMergeParam' returns object of type 'ISIAPILaneExitMergeParam'
		"PriorityMergeParam": (1610743826, 2, (9, 0), (), "PriorityMergeParam", '{9702C419-60FE-48C2-8412-23B83BF5C78C}'),
		# Method 'Segment1' returns object of type 'ISIAPILaneSegment'
		"Segment1": (1610743819, 2, (9, 0), (), "Segment1", '{6BE9B7D6-A12E-4CB5-A938-08260963BE84}'),
		# Method 'Segment2' returns object of type 'ISIAPILaneSegment'
		"Segment2": (1610743820, 2, (9, 0), (), "Segment2", '{6BE9B7D6-A12E-4CB5-A938-08260963BE84}'),
		"Width": (1610743814, 2, (4, 0), (), "Width", None),
		# Method 'ZipperMergeParam' returns object of type 'ISIAPILaneExitMergeParam'
		"ZipperMergeParam": (1610743827, 2, (9, 0), (), "ZipperMergeParam", '{9702C419-60FE-48C2-8412-23B83BF5C78C}'),
	}
	_prop_map_put_ = {
		"Configuration": ((1610743810, LCID, 4, 0),()),
		"Grade": ((1610743816, LCID, 4, 0),()),
		"Is_merge_applied": ((1610743822, LCID, 4, 0),()),
		"Length": ((1610743812, LCID, 4, 0),()),
		"Merge_type": ((1610743824, LCID, 4, 0),()),
		"Width": ((1610743814, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILaneExitMergeParam(DispatchBaseClass):
	CLSID = IID('{9702C419-60FE-48C2-8412-23B83BF5C78C}')
	coclass_clsid = IID('{4E294323-0877-4866-8E42-50BDE4F0FC69}')

	_prop_map_get_ = {
		"Critical_gap": (1610743812, 2, (4, 0), (), "Critical_gap", None),
		"Followup_headway": (1610743814, 2, (4, 0), (), "Followup_headway", None),
		# Method 'LaneExit' returns object of type 'ISIAPILaneExit'
		"LaneExit": (1610743818, 2, (9, 0), (), "LaneExit", '{FE1B8A3D-ECC2-4B36-876E-FDB052503918}'),
		"Minimum_departures": (1610743816, 2, (4, 0), (), "Minimum_departures", None),
		"Percent_opposing_mergelane": (1610743810, 2, (4, 0), (), "Percent_opposing_mergelane", None),
		"Percent_opposing_shortlane": (1610743808, 2, (4, 0), (), "Percent_opposing_shortlane", None),
	}
	_prop_map_put_ = {
		"Critical_gap": ((1610743812, LCID, 4, 0),()),
		"Followup_headway": ((1610743814, LCID, 4, 0),()),
		"Minimum_departures": ((1610743816, LCID, 4, 0),()),
		"Percent_opposing_mergelane": ((1610743810, LCID, 4, 0),()),
		"Percent_opposing_shortlane": ((1610743808, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILaneExits(DispatchBaseClass):
	CLSID = IID('{99F74111-A47C-45B1-94DE-16E6F4194A60}')
	coclass_clsid = IID('{6B84632B-C622-4C79-BCDB-16DBC5FE472E}')

	# Result is of type ISIAPILaneExit
	def AddLane(self):
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddLane', '{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')
		return ret

	# Result is of type ISIAPILaneExit
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Laneno
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')
		return ret

	def LaneExitExists(self, Laneno=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Laneno
			)

	def RemoveLane(self):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (1610743812, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Laneno
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743812, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPILaneMovement(DispatchBaseClass):
	CLSID = IID('{6DC82697-7A67-4BB3-8DA8-3F51C1D71135}')
	coclass_clsid = IID('{62BB3A21-AE88-44DE-83A4-68663A3C1A09}')

	_prop_map_get_ = {
		"Destination": (1610743810, 2, (3, 0), (), "Destination", None),
		"DestinationLaneno": (1610743811, 2, (3, 0), (), "DestinationLaneno", None),
		# Method 'LaneMovementMCs' returns object of type 'ISIAPILaneMovementMCs'
		"LaneMovementMCs": (1610743814, 2, (9, 0), (), "LaneMovementMCs", '{D8D650BB-D92A-4A21-9F34-F76F1C225497}'),
		"Lane_blockage_calib_factor": (1610743812, 2, (4, 0), (), "Lane_blockage_calib_factor", None),
		"Origin": (1610743808, 2, (3, 0), (), "Origin", None),
		"OriginLaneno": (1610743809, 2, (3, 0), (), "OriginLaneno", None),
	}
	_prop_map_put_ = {
		"Lane_blockage_calib_factor": ((1610743812, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILaneMovementMC(DispatchBaseClass):
	CLSID = IID('{D1EA4B6C-DC27-44B5-B0BE-233F53D81B6C}')
	coclass_clsid = IID('{61E72EEE-F3BA-4B3D-8733-017C4F399459}')

	_prop_map_get_ = {
		"Flow_proportion": (1610743809, 2, (4, 0), (), "Flow_proportion", None),
		# Method 'LaneMovement' returns object of type 'ISIAPILaneMovement'
		"LaneMovement": (1610743811, 2, (9, 0), (), "LaneMovement", '{6DC82697-7A67-4BB3-8DA8-3F51C1D71135}'),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
	}
	_prop_map_put_ = {
		"Flow_proportion": ((1610743809, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILaneMovementMCs(DispatchBaseClass):
	CLSID = IID('{D8D650BB-D92A-4A21-9F34-F76F1C225497}')
	coclass_clsid = IID('{1C1577BA-CBAC-4781-9A9F-40C6A2AD215D}')

	# Result is of type ISIAPILaneMovementMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D1EA4B6C-DC27-44B5-B0BE-233F53D81B6C}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D1EA4B6C-DC27-44B5-B0BE-233F53D81B6C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D1EA4B6C-DC27-44B5-B0BE-233F53D81B6C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPILaneMovements(DispatchBaseClass):
	CLSID = IID('{C1711C63-BCCC-41F6-94CC-80BFBF951D74}')
	coclass_clsid = IID('{6C29D3CD-B050-411A-9B2B-F7A008C9342E}')

	# Result is of type ISIAPILaneMovement
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Leg=defaultNamedNotOptArg, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),Leg
			, Laneno)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6DC82697-7A67-4BB3-8DA8-3F51C1D71135}')
		return ret

	def LaneMovementExists(self, Leg=defaultNamedNotOptArg, Laneno=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1), (3, 1)),Leg
			, Laneno)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Leg=defaultNamedNotOptArg, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),Leg
			, Laneno)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{6DC82697-7A67-4BB3-8DA8-3F51C1D71135}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{6DC82697-7A67-4BB3-8DA8-3F51C1D71135}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPILaneSegment(DispatchBaseClass):
	CLSID = IID('{6BE9B7D6-A12E-4CB5-A938-08260963BE84}')
	coclass_clsid = IID('{8A1FCFC4-08FB-4CB6-A9BC-E58D495ACAB6}')

	_prop_map_get_ = {
		"Colour": (1610743812, 2, (3, 0), (), "Colour", None),
		"Display_id": (1610743814, 2, (8, 0), (), "Display_id", None),
		# Method 'LaneApproach' returns object of type 'ISIAPILaneApproach'
		"LaneApproach": (1610743819, 2, (9, 0), (), "LaneApproach", '{5F156412-3EAE-40A0-99B2-06D8E48D87D1}'),
		# Method 'LaneExit' returns object of type 'ISIAPILaneExit'
		"LaneExit": (1610743820, 2, (9, 0), (), "LaneExit", '{FE1B8A3D-ECC2-4B36-876E-FDB052503918}'),
		# Method 'LaneSegmentMCs' returns object of type 'ISIAPILaneSegmentMCs'
		"LaneSegmentMCs": (1610743818, 2, (9, 0), (), "LaneSegmentMCs", '{4962E57C-6B9E-4331-94DB-F141DA807485}'),
		"Length": (1610743810, 2, (4, 0), (), "Length", None),
		"Overflow_merge_lane_num_1": (1610743816, 2, (3, 0), (), "Overflow_merge_lane_num_1", None),
		"Segment_no": (1610743808, 2, (3, 0), (), "Segment_no", None),
		"Type": (1610743809, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Colour": ((1610743812, LCID, 4, 0),()),
		"Display_id": ((1610743814, LCID, 4, 0),()),
		"Length": ((1610743810, LCID, 4, 0),()),
		"Overflow_merge_lane_num_1": ((1610743816, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILaneSegmentMC(DispatchBaseClass):
	CLSID = IID('{52442B71-F816-4AA6-9A01-9F66957C3925}')
	coclass_clsid = IID('{34AA399B-6B65-46DE-8F64-9A59ACECCF8E}')

	_prop_map_get_ = {
		"Exists": (1610743809, 2, (11, 0), (), "Exists", None),
		# Method 'LaneSegment' returns object of type 'ISIAPILaneSegment'
		"LaneSegment": (1610743815, 2, (9, 0), (), "LaneSegment", '{6BE9B7D6-A12E-4CB5-A938-08260963BE84}'),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
		"Percent_change_to_left": (1610743811, 2, (4, 0), (), "Percent_change_to_left", None),
		"Percent_change_to_right": (1610743813, 2, (4, 0), (), "Percent_change_to_right", None),
	}
	_prop_map_put_ = {
		"Exists": ((1610743809, LCID, 4, 0),()),
		"Percent_change_to_left": ((1610743811, LCID, 4, 0),()),
		"Percent_change_to_right": ((1610743813, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILaneSegmentMCs(DispatchBaseClass):
	CLSID = IID('{4962E57C-6B9E-4331-94DB-F141DA807485}')
	coclass_clsid = IID('{CDB7B33D-887D-4EAE-9596-1207BFC72BB5}')

	# Result is of type ISIAPILaneSegmentMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{52442B71-F816-4AA6-9A01-9F66957C3925}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{52442B71-F816-4AA6-9A01-9F66957C3925}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{52442B71-F816-4AA6-9A01-9F66957C3925}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPILeg(DispatchBaseClass):
	CLSID = IID('{24A8E5D9-0016-45F2-9941-12E58EE54A05}')
	coclass_clsid = IID('{D8B9A97D-F4E1-4E42-81D2-C370A157DC13}')

	# Result is of type ISIAPILaneApproach
	def InsertApproachLane(self, positionOnLeg=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743835, LCID, 1, (9, 0), ((3, 1),),positionOnLeg
			)
		if ret is not None:
			ret = Dispatch(ret, 'InsertApproachLane', '{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')
		return ret

	# Result is of type ISIAPILaneExit
	def InsertExitLane(self, positionOnLeg=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743836, LCID, 1, (9, 0), ((3, 1),),positionOnLeg
			)
		if ret is not None:
			ret = Dispatch(ret, 'InsertExitLane', '{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')
		return ret

	# Result is of type ISIAPIIsland
	def InsertIsland(self, positionOnLeg=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743837, LCID, 1, (9, 0), ((3, 1),),positionOnLeg
			)
		if ret is not None:
			ret = Dispatch(ret, 'InsertIsland', '{E741707B-9A4C-414A-A4F0-482E5F098534}')
		return ret

	# Result is of type ISIAPIIsland
	def InsertIsland_RoundaboutSplitter(self, positionOnLeg=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743838, LCID, 1, (9, 0), ((3, 1),),positionOnLeg
			)
		if ret is not None:
			ret = Dispatch(ret, 'InsertIsland_RoundaboutSplitter', '{E741707B-9A4C-414A-A4F0-482E5F098534}')
		return ret

	def RemoveItem(self, positionOnLeg=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743839, LCID, 1, (11, 0), ((3, 1),),positionOnLeg
			)

	_prop_map_get_ = {
		"Approach_control": (1610743823, 2, (3, 0), (), "Approach_control", None),
		"Approach_distance": (1610743811, 2, (4, 0), (), "Approach_distance", None),
		"Area_type_factor": (1610743821, 2, (4, 0), (), "Area_type_factor", None),
		"Exit_distance": (1610743815, 2, (4, 0), (), "Exit_distance", None),
		"Exit_distance_user": (1610743813, 2, (11, 0), (), "Exit_distance_user", None),
		"Extra_bunching": (1610743819, 2, (4, 0), (), "Extra_bunching", None),
		"Extra_bunching_nw": (1610743847, 2, (4, 0), (), "Extra_bunching_nw", None),
		"Extra_bunching_nw_user": (1610743845, 2, (11, 0), (), "Extra_bunching_nw_user", None),
		"Extra_bunching_user": (1610743817, 2, (11, 0), (), "Extra_bunching_user", None),
		"Is_departure_headway_awsc_applied": (1610743825, 2, (11, 0), (), "Is_departure_headway_awsc_applied", None),
		"Is_uturn_before_intersection": (1610743841, 2, (11, 0), (), "Is_uturn_before_intersection", None),
		"Is_uturn_before_intersection_excluded_from_signal_analysis": (1610743843, 2, (11, 0), (), "Is_uturn_before_intersection_excluded_from_signal_analysis", None),
		# Method 'Islands' returns object of type 'ISIAPIIslands'
		"Islands": (1610743834, 2, (9, 0), (), "Islands", '{6B55FEF0-D591-4E75-B2BA-81E22B796325}'),
		# Method 'LaneApproachs' returns object of type 'ISIAPILaneApproachs'
		"LaneApproachs": (1610743832, 2, (9, 0), (), "LaneApproachs", '{148779D1-5A0D-48B1-9CBB-7002DAB05D95}'),
		# Method 'LaneExits' returns object of type 'ISIAPILaneExits'
		"LaneExits": (1610743833, 2, (9, 0), (), "LaneExits", '{99F74111-A47C-45B1-94DE-16E6F4194A60}'),
		"LastErrorMessage": (1610743829, 2, (8, 0), (), "LastErrorMessage", None),
		"LegGeometry": (1610743827, 2, (3, 0), (), "LegGeometry", None),
		# Method 'Leg_roundabout' returns object of type 'ISIAPILeg_roundabout'
		"Leg_roundabout": (1610743831, 2, (9, 0), (), "Leg_roundabout", '{25BFA806-8BFC-4ADF-9A0B-9DA47FE86246}'),
		# Method 'MovementPedSlipLane_Existing' returns object of type 'ISIAPIMovement_ped'
		"MovementPedSlipLane_Existing": (1610743840, 2, (9, 0), (), "MovementPedSlipLane_Existing", '{0099AEAC-F9B6-4DCE-9C0E-1434E9D603D7}'),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		"Orientation": (1610743808, 2, (3, 0), (), "Orientation", None),
		# Method 'Site' returns object of type 'ISIAPISite'
		"Site": (1610743830, 2, (9, 0), (), "Site", '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}'),
	}
	_prop_map_put_ = {
		"Approach_control": ((1610743823, LCID, 4, 0),()),
		"Approach_distance": ((1610743811, LCID, 4, 0),()),
		"Area_type_factor": ((1610743821, LCID, 4, 0),()),
		"Exit_distance": ((1610743815, LCID, 4, 0),()),
		"Exit_distance_user": ((1610743813, LCID, 4, 0),()),
		"Extra_bunching": ((1610743819, LCID, 4, 0),()),
		"Extra_bunching_nw": ((1610743847, LCID, 4, 0),()),
		"Extra_bunching_nw_user": ((1610743845, LCID, 4, 0),()),
		"Extra_bunching_user": ((1610743817, LCID, 4, 0),()),
		"Is_departure_headway_awsc_applied": ((1610743825, LCID, 4, 0),()),
		"Is_uturn_before_intersection": ((1610743841, LCID, 4, 0),()),
		"Is_uturn_before_intersection_excluded_from_signal_analysis": ((1610743843, LCID, 4, 0),()),
		"LegGeometry": ((1610743827, LCID, 4, 0),()),
		"Name": ((1610743809, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILeg_rou_hcm(DispatchBaseClass):
	CLSID = IID('{13F6A490-E35F-4AF3-9FCE-843062E81CCD}')
	coclass_clsid = IID('{3824A747-9BC3-4304-B6C1-0969796A33EA}')

	_prop_map_get_ = {
		"Entry_circ_adj": (1610743811, 2, (3, 0), (), "Entry_circ_adj", None),
		"Hcm_model": (1610743808, 2, (3, 0), (), "Hcm_model", None),
		# Method 'Leg_roundabout' returns object of type 'ISIAPILeg_roundabout'
		"Leg_roundabout": (1610743833, 2, (9, 0), (), "Leg_roundabout", '{25BFA806-8BFC-4ADF-9A0B-9DA47FE86246}'),
		"Model_calib_factor": (1610743809, 2, (4, 0), (), "Model_calib_factor", None),
		"Multi_circ_multi_entry_dominant_param_a": (1610743825, 2, (4, 0), (), "Multi_circ_multi_entry_dominant_param_a", None),
		"Multi_circ_multi_entry_dominant_param_b": (1610743827, 2, (4, 0), (), "Multi_circ_multi_entry_dominant_param_b", None),
		"Multi_circ_multi_entry_subdominant_param_a": (1610743829, 2, (4, 0), (), "Multi_circ_multi_entry_subdominant_param_a", None),
		"Multi_circ_multi_entry_subdominant_param_b": (1610743831, 2, (4, 0), (), "Multi_circ_multi_entry_subdominant_param_b", None),
		"Multi_circ_single_entry_param_a": (1610743821, 2, (4, 0), (), "Multi_circ_single_entry_param_a", None),
		"Multi_circ_single_entry_param_b": (1610743823, 2, (4, 0), (), "Multi_circ_single_entry_param_b", None),
		"Single_circ_multi_entry_param_a": (1610743817, 2, (4, 0), (), "Single_circ_multi_entry_param_a", None),
		"Single_circ_multi_entry_param_b": (1610743819, 2, (4, 0), (), "Single_circ_multi_entry_param_b", None),
		"Single_circ_single_entry_param_a": (1610743813, 2, (4, 0), (), "Single_circ_single_entry_param_a", None),
		"Single_circ_single_entry_param_b": (1610743815, 2, (4, 0), (), "Single_circ_single_entry_param_b", None),
	}
	_prop_map_put_ = {
		"Entry_circ_adj": ((1610743811, LCID, 4, 0),()),
		"Model_calib_factor": ((1610743809, LCID, 4, 0),()),
		"Multi_circ_multi_entry_dominant_param_a": ((1610743825, LCID, 4, 0),()),
		"Multi_circ_multi_entry_dominant_param_b": ((1610743827, LCID, 4, 0),()),
		"Multi_circ_multi_entry_subdominant_param_a": ((1610743829, LCID, 4, 0),()),
		"Multi_circ_multi_entry_subdominant_param_b": ((1610743831, LCID, 4, 0),()),
		"Multi_circ_single_entry_param_a": ((1610743821, LCID, 4, 0),()),
		"Multi_circ_single_entry_param_b": ((1610743823, LCID, 4, 0),()),
		"Single_circ_multi_entry_param_a": ((1610743817, LCID, 4, 0),()),
		"Single_circ_multi_entry_param_b": ((1610743819, LCID, 4, 0),()),
		"Single_circ_single_entry_param_a": ((1610743813, LCID, 4, 0),()),
		"Single_circ_single_entry_param_b": ((1610743815, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILeg_rou_hcm6_extended(DispatchBaseClass):
	CLSID = IID('{BD507F2C-6D0F-4256-8E40-79299F021130}')
	coclass_clsid = IID('{FDA1F3A6-FA03-4937-99CB-AA207DD504F9}')

	_prop_map_get_ = {
		"Entry_circ_adj": (1610743810, 2, (3, 0), (), "Entry_circ_adj", None),
		# Method 'Leg_roundabout' returns object of type 'ISIAPILeg_roundabout'
		"Leg_roundabout": (1610743852, 2, (9, 0), (), "Leg_roundabout", '{25BFA806-8BFC-4ADF-9A0B-9DA47FE86246}'),
		"Model_calib_factor": (1610743808, 2, (4, 0), (), "Model_calib_factor", None),
		"Multi_circ_single_entry_param_a": (1610743828, 2, (4, 0), (), "Multi_circ_single_entry_param_a", None),
		"Multi_circ_single_entry_param_b": (1610743830, 2, (4, 0), (), "Multi_circ_single_entry_param_b", None),
		"Multi_circ_slip_entry_param_a": (1610743848, 2, (4, 0), (), "Multi_circ_slip_entry_param_a", None),
		"Multi_circ_slip_entry_param_b": (1610743850, 2, (4, 0), (), "Multi_circ_slip_entry_param_b", None),
		"Multi_circ_three_entry_dominant_param_a": (1610743840, 2, (4, 0), (), "Multi_circ_three_entry_dominant_param_a", None),
		"Multi_circ_three_entry_dominant_param_b": (1610743842, 2, (4, 0), (), "Multi_circ_three_entry_dominant_param_b", None),
		"Multi_circ_three_entry_subdominant_param_a": (1610743844, 2, (4, 0), (), "Multi_circ_three_entry_subdominant_param_a", None),
		"Multi_circ_three_entry_subdominant_param_b": (1610743846, 2, (4, 0), (), "Multi_circ_three_entry_subdominant_param_b", None),
		"Multi_circ_two_entry_dominant_param_a": (1610743832, 2, (4, 0), (), "Multi_circ_two_entry_dominant_param_a", None),
		"Multi_circ_two_entry_dominant_param_b": (1610743834, 2, (4, 0), (), "Multi_circ_two_entry_dominant_param_b", None),
		"Multi_circ_two_entry_subdominant_param_a": (1610743836, 2, (4, 0), (), "Multi_circ_two_entry_subdominant_param_a", None),
		"Multi_circ_two_entry_subdominant_param_b": (1610743838, 2, (4, 0), (), "Multi_circ_two_entry_subdominant_param_b", None),
		"Single_circ_single_entry_param_a": (1610743812, 2, (4, 0), (), "Single_circ_single_entry_param_a", None),
		"Single_circ_single_entry_param_b": (1610743814, 2, (4, 0), (), "Single_circ_single_entry_param_b", None),
		"Single_circ_slip_entry_param_a": (1610743824, 2, (4, 0), (), "Single_circ_slip_entry_param_a", None),
		"Single_circ_slip_entry_param_b": (1610743826, 2, (4, 0), (), "Single_circ_slip_entry_param_b", None),
		"Single_circ_two_entry_dominant_param_a": (1610743816, 2, (4, 0), (), "Single_circ_two_entry_dominant_param_a", None),
		"Single_circ_two_entry_dominant_param_b": (1610743818, 2, (4, 0), (), "Single_circ_two_entry_dominant_param_b", None),
		"Single_circ_two_entry_subdominant_param_a": (1610743820, 2, (4, 0), (), "Single_circ_two_entry_subdominant_param_a", None),
		"Single_circ_two_entry_subdominant_param_b": (1610743822, 2, (4, 0), (), "Single_circ_two_entry_subdominant_param_b", None),
	}
	_prop_map_put_ = {
		"Entry_circ_adj": ((1610743810, LCID, 4, 0),()),
		"Model_calib_factor": ((1610743808, LCID, 4, 0),()),
		"Multi_circ_single_entry_param_a": ((1610743828, LCID, 4, 0),()),
		"Multi_circ_single_entry_param_b": ((1610743830, LCID, 4, 0),()),
		"Multi_circ_slip_entry_param_a": ((1610743848, LCID, 4, 0),()),
		"Multi_circ_slip_entry_param_b": ((1610743850, LCID, 4, 0),()),
		"Multi_circ_three_entry_dominant_param_a": ((1610743840, LCID, 4, 0),()),
		"Multi_circ_three_entry_dominant_param_b": ((1610743842, LCID, 4, 0),()),
		"Multi_circ_three_entry_subdominant_param_a": ((1610743844, LCID, 4, 0),()),
		"Multi_circ_three_entry_subdominant_param_b": ((1610743846, LCID, 4, 0),()),
		"Multi_circ_two_entry_dominant_param_a": ((1610743832, LCID, 4, 0),()),
		"Multi_circ_two_entry_dominant_param_b": ((1610743834, LCID, 4, 0),()),
		"Multi_circ_two_entry_subdominant_param_a": ((1610743836, LCID, 4, 0),()),
		"Multi_circ_two_entry_subdominant_param_b": ((1610743838, LCID, 4, 0),()),
		"Single_circ_single_entry_param_a": ((1610743812, LCID, 4, 0),()),
		"Single_circ_single_entry_param_b": ((1610743814, LCID, 4, 0),()),
		"Single_circ_slip_entry_param_a": ((1610743824, LCID, 4, 0),()),
		"Single_circ_slip_entry_param_b": ((1610743826, LCID, 4, 0),()),
		"Single_circ_two_entry_dominant_param_a": ((1610743816, LCID, 4, 0),()),
		"Single_circ_two_entry_dominant_param_b": ((1610743818, LCID, 4, 0),()),
		"Single_circ_two_entry_subdominant_param_a": ((1610743820, LCID, 4, 0),()),
		"Single_circ_two_entry_subdominant_param_b": ((1610743822, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILeg_roundabout(DispatchBaseClass):
	CLSID = IID('{25BFA806-8BFC-4ADF-9A0B-9DA47FE86246}')
	coclass_clsid = IID('{B9DD66CB-2900-4C0D-A7F9-A0BDF06656E9}')

	_prop_map_get_ = {
		"App_half_width": (1610743838, 2, (4, 0), (), "App_half_width", None),
		"Capacity_at_zero_flow": (1610743844, 2, (4, 0), (), "Capacity_at_zero_flow", None),
		"Capacity_at_zero_flow_user": (1610743842, 2, (11, 0), (), "Capacity_at_zero_flow_user", None),
		"Circulating_transition_line": (1610743828, 2, (11, 0), (), "Circulating_transition_line", None),
		"Circulating_width": (1610743814, 2, (4, 0), (), "Circulating_width", None),
		"Entry_angle": (1610743824, 2, (4, 0), (), "Entry_angle", None),
		"Entry_circ_adj": (1610743836, 2, (3, 0), (), "Entry_circ_adj", None),
		"Entry_circ_adj_user": (1610743834, 2, (11, 0), (), "Entry_circ_adj_user", None),
		"Entry_radius": (1610743822, 2, (4, 0), (), "Entry_radius", None),
		"Environment_factor": (1610743832, 2, (4, 0), (), "Environment_factor", None),
		"Environment_factor_user": (1610743830, 2, (11, 0), (), "Environment_factor_user", None),
		"Flare_length": (1610743840, 2, (4, 0), (), "Flare_length", None),
		"Grade_separated": (1610743846, 2, (11, 0), (), "Grade_separated", None),
		"Inscribed_diameter": (1610743820, 2, (4, 0), (), "Inscribed_diameter", None),
		"Inscribed_diameter_user": (1610743818, 2, (11, 0), (), "Inscribed_diameter_user", None),
		"Is_raindrop_design": (1610743826, 2, (11, 0), (), "Is_raindrop_design", None),
		"Island_diameter": (1610743816, 2, (4, 0), (), "Island_diameter", None),
		# Method 'Leg' returns object of type 'ISIAPILeg'
		"Leg": (1610743848, 2, (9, 0), (), "Leg", '{24A8E5D9-0016-45F2-9941-12E58EE54A05}'),
		# Method 'LegRouHCM2010' returns object of type 'ISIAPILeg_rou_hcm'
		"LegRouHCM2010": (1610743849, 2, (9, 0), (), "LegRouHCM2010", '{13F6A490-E35F-4AF3-9FCE-843062E81CCD}'),
		# Method 'LegRouHCM6' returns object of type 'ISIAPILeg_rou_hcm'
		"LegRouHCM6": (1610743850, 2, (9, 0), (), "LegRouHCM6", '{13F6A490-E35F-4AF3-9FCE-843062E81CCD}'),
		# Method 'LegRouHCM6Extended' returns object of type 'ISIAPILeg_rou_hcm6_extended'
		"LegRouHCM6Extended": (1610743851, 2, (9, 0), (), "LegRouHCM6Extended", '{BD507F2C-6D0F-4256-8E40-79299F021130}'),
		"Num_circulating_lanes": (1610743808, 2, (3, 0), (), "Num_circulating_lanes", None),
		"Num_downstream_circulating_lanes": (1610743812, 2, (3, 0), (), "Num_downstream_circulating_lanes", None),
		"Num_downstream_circulating_lanes_user": (1610743810, 2, (11, 0), (), "Num_downstream_circulating_lanes_user", None),
	}
	_prop_map_put_ = {
		"App_half_width": ((1610743838, LCID, 4, 0),()),
		"Capacity_at_zero_flow": ((1610743844, LCID, 4, 0),()),
		"Capacity_at_zero_flow_user": ((1610743842, LCID, 4, 0),()),
		"Circulating_transition_line": ((1610743828, LCID, 4, 0),()),
		"Circulating_width": ((1610743814, LCID, 4, 0),()),
		"Entry_angle": ((1610743824, LCID, 4, 0),()),
		"Entry_circ_adj": ((1610743836, LCID, 4, 0),()),
		"Entry_circ_adj_user": ((1610743834, LCID, 4, 0),()),
		"Entry_radius": ((1610743822, LCID, 4, 0),()),
		"Environment_factor": ((1610743832, LCID, 4, 0),()),
		"Environment_factor_user": ((1610743830, LCID, 4, 0),()),
		"Flare_length": ((1610743840, LCID, 4, 0),()),
		"Grade_separated": ((1610743846, LCID, 4, 0),()),
		"Inscribed_diameter": ((1610743820, LCID, 4, 0),()),
		"Inscribed_diameter_user": ((1610743818, LCID, 4, 0),()),
		"Is_raindrop_design": ((1610743826, LCID, 4, 0),()),
		"Island_diameter": ((1610743816, LCID, 4, 0),()),
		"Num_circulating_lanes": ((1610743808, LCID, 4, 0),()),
		"Num_downstream_circulating_lanes": ((1610743812, LCID, 4, 0),()),
		"Num_downstream_circulating_lanes_user": ((1610743810, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPILegs(DispatchBaseClass):
	CLSID = IID('{D7F45026-862A-432F-BC67-E0557FED8203}')
	coclass_clsid = IID('{CB79F519-887E-4349-B499-5FFF86EB475D}')

	# Result is of type ISIAPILeg
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Orientation=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Orientation
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{24A8E5D9-0016-45F2-9941-12E58EE54A05}')
		return ret

	def LegExists(self, Orientation=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Orientation
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Orientation=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Orientation
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{24A8E5D9-0016-45F2-9941-12E58EE54A05}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{24A8E5D9-0016-45F2-9941-12E58EE54A05}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIModelSetting(DispatchBaseClass):
	CLSID = IID('{DB0EFBA0-673A-4E4B-B359-ED0CAFA0643F}')
	coclass_clsid = IID('{4F6A34D7-8E26-4D62-819E-6A100FB00AC9}')

	_prop_map_get_ = {
		"Calibration_note": (1610743882, 2, (8, 0), (), "Calibration_note", None),
		"Downstream_SL_CalibrationParameter": (1610743858, 2, (4, 0), (), "Downstream_SL_CalibrationParameter", None),
		"Downstream_SL_Distance_FullLaneUtil": (1610743856, 2, (4, 0), (), "Downstream_SL_Distance_FullLaneUtil", None),
		"Downstream_SL_Distance_Min": (1610743854, 2, (4, 0), (), "Downstream_SL_Distance_Min", None),
		"Downstream_SL_Util_Ratio_Min": (1610743852, 2, (4, 0), (), "Downstream_SL_Util_Ratio_Min", None),
		"Gap_Acceptance_Capacity": (1610743822, 2, (3, 0), (), "Gap_Acceptance_Capacity", None),
		"Hours_per_Year": (1610743816, 2, (3, 0), (), "Hours_per_Year", None),
		"Is_geometric_delay_excluded": (1610743848, 2, (11, 0), (), "Is_geometric_delay_excluded", None),
		"Is_hcm6_extended_applied": (1610743886, 2, (11, 0), (), "Is_hcm6_extended_applied", None),
		"Is_hcm_delay_formula_applied": (1610743850, 2, (11, 0), (), "Is_hcm_delay_formula_applied", None),
		"Is_hcm_queue_formula_applied": (1610743866, 2, (11, 0), (), "Is_hcm_queue_formula_applied", None),
		"Is_ped_cost_included": (1610743838, 2, (11, 0), (), "Is_ped_cost_included", None),
		"LOS_Method": (1610743808, 2, (3, 0), (), "LOS_Method", None),
		"LOS_Target": (1610743810, 2, (3, 0), (), "LOS_Target", None),
		"Major_road_turn_flow_factor": (1610743820, 2, (4, 0), (), "Major_road_turn_flow_factor", None),
		"Midblock_eff_det_zone_len": (1610743884, 2, (4, 0), (), "Midblock_eff_det_zone_len", None),
		"Min_prob_blockage": (1610743846, 2, (4, 0), (), "Min_prob_blockage", None),
		"Ped_LOS_Method": (1610743880, 2, (3, 0), (), "Ped_LOS_Method", None),
		"Ped_average_income": (1610743840, 2, (4, 0), (), "Ped_average_income", None),
		"Ped_los_target": (1610743860, 2, (3, 0), (), "Ped_los_target", None),
		"Ped_time_value_factor": (1610743842, 2, (4, 0), (), "Ped_time_value_factor", None),
		"Percentile_Queue": (1610743814, 2, (3, 0), (), "Percentile_Queue", None),
		"Percentile_queue_option": (1610743862, 2, (3, 0), (), "Percentile_queue_option", None),
		"Performance_Measure": (1610743812, 2, (3, 0), (), "Performance_Measure", None),
		"Platoon_disp_distance_max": (1610743876, 2, (4, 0), (), "Platoon_disp_distance_max", None),
		"Platoon_disp_distance_min": (1610743874, 2, (4, 0), (), "Platoon_disp_distance_min", None),
		"Platoon_disp_factor_max": (1610743872, 2, (4, 0), (), "Platoon_disp_factor_max", None),
		"Platoon_disp_factor_min": (1610743870, 2, (4, 0), (), "Platoon_disp_factor_min", None),
		"Platoon_disp_n": (1610743878, 2, (4, 0), (), "Platoon_disp_n", None),
		"Platoon_front_factor": (1610743868, 2, (4, 0), (), "Platoon_front_factor", None),
		"Reduct_opposing_flow_rate_level": (1610743818, 2, (3, 0), (), "Reduct_opposing_flow_rate_level", None),
		"Rou_Capacity_Model": (1610743824, 2, (3, 0), (), "Rou_Capacity_Model", None),
		"Rou_FHWA_2000_Urban_compact_applied": (1610743832, 2, (11, 0), (), "Rou_FHWA_2000_Urban_compact_applied", None),
		"Rou_FHWA_2000_model_applied": (1610743830, 2, (11, 0), (), "Rou_FHWA_2000_model_applied", None),
		"Rou_HCM_2000_model_applied": (1610743834, 2, (11, 0), (), "Rou_HCM_2000_model_applied", None),
		"Rou_HCM_2010_OD_pattern_effects_included": (1610743828, 2, (11, 0), (), "Rou_HCM_2010_OD_pattern_effects_included", None),
		"Rou_HCM_6_OD_pattern_effects_included": (1610743864, 2, (11, 0), (), "Rou_HCM_6_OD_pattern_effects_included", None),
		"Rou_LOS_Method": (1610743826, 2, (3, 0), (), "Rou_LOS_Method", None),
		"Rou_NAASRA_1986_model_applied": (1610743836, 2, (11, 0), (), "Rou_NAASRA_1986_model_applied", None),
		"Shortlane_queue_storage_ratio_incl": (1610743844, 2, (11, 0), (), "Shortlane_queue_storage_ratio_incl", None),
		"Shortlane_upstream_delay_stops_included": (1610743888, 2, (11, 0), (), "Shortlane_upstream_delay_stops_included", None),
	}
	_prop_map_put_ = {
		"Calibration_note": ((1610743882, LCID, 4, 0),()),
		"Downstream_SL_CalibrationParameter": ((1610743858, LCID, 4, 0),()),
		"Downstream_SL_Distance_FullLaneUtil": ((1610743856, LCID, 4, 0),()),
		"Downstream_SL_Distance_Min": ((1610743854, LCID, 4, 0),()),
		"Downstream_SL_Util_Ratio_Min": ((1610743852, LCID, 4, 0),()),
		"Gap_Acceptance_Capacity": ((1610743822, LCID, 4, 0),()),
		"Hours_per_Year": ((1610743816, LCID, 4, 0),()),
		"Is_geometric_delay_excluded": ((1610743848, LCID, 4, 0),()),
		"Is_hcm6_extended_applied": ((1610743886, LCID, 4, 0),()),
		"Is_hcm_delay_formula_applied": ((1610743850, LCID, 4, 0),()),
		"Is_hcm_queue_formula_applied": ((1610743866, LCID, 4, 0),()),
		"Is_ped_cost_included": ((1610743838, LCID, 4, 0),()),
		"LOS_Method": ((1610743808, LCID, 4, 0),()),
		"LOS_Target": ((1610743810, LCID, 4, 0),()),
		"Major_road_turn_flow_factor": ((1610743820, LCID, 4, 0),()),
		"Midblock_eff_det_zone_len": ((1610743884, LCID, 4, 0),()),
		"Min_prob_blockage": ((1610743846, LCID, 4, 0),()),
		"Ped_LOS_Method": ((1610743880, LCID, 4, 0),()),
		"Ped_average_income": ((1610743840, LCID, 4, 0),()),
		"Ped_los_target": ((1610743860, LCID, 4, 0),()),
		"Ped_time_value_factor": ((1610743842, LCID, 4, 0),()),
		"Percentile_Queue": ((1610743814, LCID, 4, 0),()),
		"Percentile_queue_option": ((1610743862, LCID, 4, 0),()),
		"Performance_Measure": ((1610743812, LCID, 4, 0),()),
		"Platoon_disp_distance_max": ((1610743876, LCID, 4, 0),()),
		"Platoon_disp_distance_min": ((1610743874, LCID, 4, 0),()),
		"Platoon_disp_factor_max": ((1610743872, LCID, 4, 0),()),
		"Platoon_disp_factor_min": ((1610743870, LCID, 4, 0),()),
		"Platoon_disp_n": ((1610743878, LCID, 4, 0),()),
		"Platoon_front_factor": ((1610743868, LCID, 4, 0),()),
		"Reduct_opposing_flow_rate_level": ((1610743818, LCID, 4, 0),()),
		"Rou_Capacity_Model": ((1610743824, LCID, 4, 0),()),
		"Rou_FHWA_2000_Urban_compact_applied": ((1610743832, LCID, 4, 0),()),
		"Rou_FHWA_2000_model_applied": ((1610743830, LCID, 4, 0),()),
		"Rou_HCM_2000_model_applied": ((1610743834, LCID, 4, 0),()),
		"Rou_HCM_2010_OD_pattern_effects_included": ((1610743828, LCID, 4, 0),()),
		"Rou_HCM_6_OD_pattern_effects_included": ((1610743864, LCID, 4, 0),()),
		"Rou_LOS_Method": ((1610743826, LCID, 4, 0),()),
		"Rou_NAASRA_1986_model_applied": ((1610743836, LCID, 4, 0),()),
		"Shortlane_queue_storage_ratio_incl": ((1610743844, LCID, 4, 0),()),
		"Shortlane_upstream_delay_stops_included": ((1610743888, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIMovementClass(DispatchBaseClass):
	CLSID = IID('{69AB3019-BCEB-413C-90C3-09A8DA0144DD}')
	coclass_clsid = IID('{22DCD1A6-1C92-478E-ABAB-FA0AFBE2F235}')

	_prop_map_get_ = {
		"Average_income": (1610743832, 2, (4, 0), (), "Average_income", None),
		"Base_class": (1610743816, 2, (3, 0), (), "Base_class", None),
		"Co2_to_fuel_ratio": (1610743840, 2, (4, 0), (), "Co2_to_fuel_ratio", None),
		"Cost_method": (1610743824, 2, (3, 0), (), "Cost_method", None),
		"DesiredSpeed": (1610743844, 2, (4, 0), (), "DesiredSpeed", None),
		"DesiredSpeedMethod": (1610743842, 2, (3, 0), (), "DesiredSpeedMethod", None),
		"Display_id": (1610743814, 2, (8, 0), (), "Display_id", None),
		"Fuel_pump_price": (1610743826, 2, (4, 0), (), "Fuel_pump_price", None),
		"Gap_acceptance_factor_midblock_zebra": (1610743850, 2, (4, 0), (), "Gap_acceptance_factor_midblock_zebra", None),
		"Gap_acceptance_factor_sliplane_zebra": (1610743848, 2, (4, 0), (), "Gap_acceptance_factor_sliplane_zebra", None),
		"Is_cost_included": (1610743823, 2, (11, 0), (), "Is_cost_included", None),
		"Is_included": (1610743809, 2, (11, 0), (), "Is_included", None),
		"Is_userclass": (1610743811, 2, (11, 0), (), "Is_userclass", None),
		"LowerLimitOfSpeedEfficiency": (1610743846, 2, (4, 0), (), "LowerLimitOfSpeedEfficiency", None),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
		"Mass": (1610743836, 2, (4, 0), (), "Mass", None),
		"Max_power": (1610743838, 2, (4, 0), (), "Max_power", None),
		# Method 'MergeParam' returns object of type 'ISIAPIMovementClassMergeParam'
		"MergeParam": (1610743852, 2, (9, 0), (), "MergeParam", '{86D55C22-E6CE-4FF9-89A9-F53001A61501}'),
		"Model_designation": (1610743818, 2, (3, 0), (), "Model_designation", None),
		# Method 'MovementClassFuelEmissions' returns object of type 'ISIAPIMovementClassFuelEmissions'
		"MovementClassFuelEmissions": (1610743819, 2, (9, 0), (), "MovementClassFuelEmissions", '{BF9EA147-CE73-49C5-A6DB-7FAA6DFC663E}'),
		"Name": (1610743812, 2, (8, 0), (), "Name", None),
		"Pc_equivalent": (1610743821, 2, (4, 0), (), "Pc_equivalent", None),
		"Resource_cost_factor": (1610743828, 2, (4, 0), (), "Resource_cost_factor", None),
		"Run_cost_fuel_ratio": (1610743830, 2, (4, 0), (), "Run_cost_fuel_ratio", None),
		# Method 'Site' returns object of type 'ISIAPISite'
		"Site": (1610743820, 2, (9, 0), (), "Site", '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}'),
		"Time_value_factor": (1610743834, 2, (4, 0), (), "Time_value_factor", None),
	}
	_prop_map_put_ = {
		"Average_income": ((1610743832, LCID, 4, 0),()),
		"Base_class": ((1610743816, LCID, 4, 0),()),
		"Co2_to_fuel_ratio": ((1610743840, LCID, 4, 0),()),
		"Cost_method": ((1610743824, LCID, 4, 0),()),
		"DesiredSpeed": ((1610743844, LCID, 4, 0),()),
		"DesiredSpeedMethod": ((1610743842, LCID, 4, 0),()),
		"Display_id": ((1610743814, LCID, 4, 0),()),
		"Fuel_pump_price": ((1610743826, LCID, 4, 0),()),
		"Gap_acceptance_factor_midblock_zebra": ((1610743850, LCID, 4, 0),()),
		"Gap_acceptance_factor_sliplane_zebra": ((1610743848, LCID, 4, 0),()),
		"Is_included": ((1610743809, LCID, 4, 0),()),
		"LowerLimitOfSpeedEfficiency": ((1610743846, LCID, 4, 0),()),
		"Mass": ((1610743836, LCID, 4, 0),()),
		"Max_power": ((1610743838, LCID, 4, 0),()),
		"Name": ((1610743812, LCID, 4, 0),()),
		"Pc_equivalent": ((1610743821, LCID, 4, 0),()),
		"Resource_cost_factor": ((1610743828, LCID, 4, 0),()),
		"Run_cost_fuel_ratio": ((1610743830, LCID, 4, 0),()),
		"Time_value_factor": ((1610743834, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIMovementClassFuelEmission(DispatchBaseClass):
	CLSID = IID('{94958D62-C2A0-40CD-A631-894BD1A1BC00}')
	coclass_clsid = IID('{7C2A53C7-B12F-4C83-A409-1BDD05DADB5C}')

	_prop_map_get_ = {
		"A": (1610743811, 2, (4, 0), (), "A", None),
		"B": (1610743813, 2, (4, 0), (), "B", None),
		"Beta1": (1610743815, 2, (4, 0), (), "Beta1", None),
		"Emission_class": (1610743808, 2, (3, 0), (), "Emission_class", None),
		"Idle": (1610743809, 2, (4, 0), (), "Idle", None),
		# Method 'MovementClass' returns object of type 'ISIAPIMovementClass'
		"MovementClass": (1610743817, 2, (9, 0), (), "MovementClass", '{69AB3019-BCEB-413C-90C3-09A8DA0144DD}'),
	}
	_prop_map_put_ = {
		"A": ((1610743811, LCID, 4, 0),()),
		"B": ((1610743813, LCID, 4, 0),()),
		"Beta1": ((1610743815, LCID, 4, 0),()),
		"Idle": ((1610743809, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIMovementClassFuelEmissions(DispatchBaseClass):
	CLSID = IID('{BF9EA147-CE73-49C5-A6DB-7FAA6DFC663E}')
	coclass_clsid = IID('{7D7AAA7B-6F56-44C2-A439-22A50FA85997}')

	def Exists(self, emissionClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),emissionClass
			)

	# Result is of type ISIAPIMovementClassFuelEmission
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, emissionClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),emissionClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{94958D62-C2A0-40CD-A631-894BD1A1BC00}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, emissionClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),emissionClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{94958D62-C2A0-40CD-A631-894BD1A1BC00}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{94958D62-C2A0-40CD-A631-894BD1A1BC00}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIMovementClassMergeParam(DispatchBaseClass):
	CLSID = IID('{86D55C22-E6CE-4FF9-89A9-F53001A61501}')
	coclass_clsid = IID('{E567F5BB-9F02-452E-8633-568913739EBC}')

	_prop_map_get_ = {
		"Contlane_cap_mergelane": (1610743818, 2, (4, 0), (), "Contlane_cap_mergelane", None),
		"Contlane_cap_shortlane": (1610743812, 2, (4, 0), (), "Contlane_cap_shortlane", None),
		"Gap_acceptance_factor_mergelane": (1610743814, 2, (4, 0), (), "Gap_acceptance_factor_mergelane", None),
		"Gap_acceptance_factor_shortlane": (1610743808, 2, (4, 0), (), "Gap_acceptance_factor_shortlane", None),
		# Method 'MovementClass' returns object of type 'ISIAPIMovementClass'
		"MovementClass": (1610743820, 2, (9, 0), (), "MovementClass", '{69AB3019-BCEB-413C-90C3-09A8DA0144DD}'),
		"Opposing_veh_factor_mergelane": (1610743816, 2, (4, 0), (), "Opposing_veh_factor_mergelane", None),
		"Opposing_veh_factor_shortlane": (1610743810, 2, (4, 0), (), "Opposing_veh_factor_shortlane", None),
	}
	_prop_map_put_ = {
		"Contlane_cap_mergelane": ((1610743818, LCID, 4, 0),()),
		"Contlane_cap_shortlane": ((1610743812, LCID, 4, 0),()),
		"Gap_acceptance_factor_mergelane": ((1610743814, LCID, 4, 0),()),
		"Gap_acceptance_factor_shortlane": ((1610743808, LCID, 4, 0),()),
		"Opposing_veh_factor_mergelane": ((1610743816, LCID, 4, 0),()),
		"Opposing_veh_factor_shortlane": ((1610743810, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIMovementClasses(DispatchBaseClass):
	CLSID = IID('{39B087B7-EB2C-4B47-8923-F8DD4238C771}')
	coclass_clsid = IID('{ECE0790E-AA84-41A3-A0E2-74E3E2E4E2C5}')

	# Result is of type ISIAPIMovementClass
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{69AB3019-BCEB-413C-90C3-09A8DA0144DD}')
		return ret

	def MovementClassExists(self, mcClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),mcClass
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{69AB3019-BCEB-413C-90C3-09A8DA0144DD}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{69AB3019-BCEB-413C-90C3-09A8DA0144DD}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIMovement_ped(DispatchBaseClass):
	CLSID = IID('{0099AEAC-F9B6-4DCE-9C0E-1434E9D603D7}')
	coclass_clsid = IID('{695474FC-BF40-4A63-B1D3-0E9D5974BB68}')

	_prop_map_get_ = {
		"Actuation_option": (1610743872, 2, (3, 0), (), "Actuation_option", None),
		"Actuation_percent": (1610743874, 2, (4, 0), (), "Actuation_percent", None),
		"Approach_distance": (1610743830, 2, (4, 0), (), "Approach_distance", None),
		"Clearance1_time": (1610743862, 2, (3, 0), (), "Clearance1_time", None),
		"Clearance1_time_user": (1610743860, 2, (11, 0), (), "Clearance1_time_user", None),
		"Clearance2_time": (1610743866, 2, (3, 0), (), "Clearance2_time", None),
		"Clearance2_time_option": (1610743864, 2, (3, 0), (), "Clearance2_time_option", None),
		"Conflict_zone_length": (1610743882, 2, (4, 0), (), "Conflict_zone_length", None),
		"Conflict_zone_length_user": (1610743880, 2, (11, 0), (), "Conflict_zone_length_user", None),
		"Control_type": (1610743884, 2, (3, 0), (), "Control_type", None),
		"Crossing_distance": (1610743842, 2, (4, 0), (), "Crossing_distance", None),
		"Crossing_distance_user": (1610743840, 2, (11, 0), (), "Crossing_distance_user", None),
		"Crossing_speed": (1610743854, 2, (4, 0), (), "Crossing_speed", None),
		"Crosswalk_space": (1610743878, 2, (4, 0), (), "Crosswalk_space", None),
		"Display_id": (1610743814, 2, (8, 0), (), "Display_id", None),
		"End_gain": (1610743870, 2, (3, 0), (), "End_gain", None),
		"Exists": (1610743812, 2, (11, 0), (), "Exists", None),
		"Exit_distance": (1610743836, 2, (4, 0), (), "Exit_distance", None),
		"Flow_scale": (1610743820, 2, (4, 0), (), "Flow_scale", None),
		"Growth_rate": (1610743822, 2, (4, 0), (), "Growth_rate", None),
		"Is_high_priority": (1610743876, 2, (11, 0), (), "Is_high_priority", None),
		"Is_walk_time_extended": (1610743852, 2, (11, 0), (), "Is_walk_time_extended", None),
		"Maximum_green_time": (1610743850, 2, (3, 0), (), "Maximum_green_time", None),
		"Maximum_green_time_user": (1610743848, 2, (11, 0), (), "Maximum_green_time_user", None),
		"Minimum_clearance_time": (1610743858, 2, (3, 0), (), "Minimum_clearance_time", None),
		"Minimum_green_time": (1610743846, 2, (3, 0), (), "Minimum_green_time", None),
		"Minimum_green_time_user": (1610743844, 2, (11, 0), (), "Minimum_green_time_user", None),
		"Minimum_walk_time": (1610743856, 2, (3, 0), (), "Minimum_walk_time", None),
		"Opposing_ped_factor": (1610743824, 2, (4, 0), (), "Opposing_ped_factor", None),
		"Origin": (1610743809, 2, (3, 0), (), "Origin", None),
		"Peak_flow_factor": (1610743818, 2, (4, 0), (), "Peak_flow_factor", None),
		"Practical_degree_of_saturation": (1610743828, 2, (4, 0), (), "Practical_degree_of_saturation", None),
		"Practical_degree_of_saturation_user": (1610743826, 2, (11, 0), (), "Practical_degree_of_saturation_user", None),
		"Queue_space": (1610743832, 2, (4, 0), (), "Queue_space", None),
		"Saturation_flow_rate": (1610743838, 2, (3, 0), (), "Saturation_flow_rate", None),
		# Method 'Site' returns object of type 'ISIAPISite'
		"Site": (1610743811, 2, (9, 0), (), "Site", '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}'),
		"Stage": (1610743810, 2, (3, 0), (), "Stage", None),
		"Start_loss": (1610743868, 2, (3, 0), (), "Start_loss", None),
		"Type": (1610743808, 2, (3, 0), (), "Type", None),
		"Volume": (1610743816, 2, (4, 0), (), "Volume", None),
		"Walking_speed": (1610743834, 2, (4, 0), (), "Walking_speed", None),
	}
	_prop_map_put_ = {
		"Actuation_option": ((1610743872, LCID, 4, 0),()),
		"Actuation_percent": ((1610743874, LCID, 4, 0),()),
		"Approach_distance": ((1610743830, LCID, 4, 0),()),
		"Clearance1_time": ((1610743862, LCID, 4, 0),()),
		"Clearance1_time_user": ((1610743860, LCID, 4, 0),()),
		"Clearance2_time": ((1610743866, LCID, 4, 0),()),
		"Clearance2_time_option": ((1610743864, LCID, 4, 0),()),
		"Conflict_zone_length": ((1610743882, LCID, 4, 0),()),
		"Conflict_zone_length_user": ((1610743880, LCID, 4, 0),()),
		"Control_type": ((1610743884, LCID, 4, 0),()),
		"Crossing_distance": ((1610743842, LCID, 4, 0),()),
		"Crossing_distance_user": ((1610743840, LCID, 4, 0),()),
		"Crossing_speed": ((1610743854, LCID, 4, 0),()),
		"Crosswalk_space": ((1610743878, LCID, 4, 0),()),
		"Display_id": ((1610743814, LCID, 4, 0),()),
		"End_gain": ((1610743870, LCID, 4, 0),()),
		"Exists": ((1610743812, LCID, 4, 0),()),
		"Exit_distance": ((1610743836, LCID, 4, 0),()),
		"Flow_scale": ((1610743820, LCID, 4, 0),()),
		"Growth_rate": ((1610743822, LCID, 4, 0),()),
		"Is_high_priority": ((1610743876, LCID, 4, 0),()),
		"Is_walk_time_extended": ((1610743852, LCID, 4, 0),()),
		"Maximum_green_time": ((1610743850, LCID, 4, 0),()),
		"Maximum_green_time_user": ((1610743848, LCID, 4, 0),()),
		"Minimum_clearance_time": ((1610743858, LCID, 4, 0),()),
		"Minimum_green_time": ((1610743846, LCID, 4, 0),()),
		"Minimum_green_time_user": ((1610743844, LCID, 4, 0),()),
		"Minimum_walk_time": ((1610743856, LCID, 4, 0),()),
		"Opposing_ped_factor": ((1610743824, LCID, 4, 0),()),
		"Peak_flow_factor": ((1610743818, LCID, 4, 0),()),
		"Practical_degree_of_saturation": ((1610743828, LCID, 4, 0),()),
		"Practical_degree_of_saturation_user": ((1610743826, LCID, 4, 0),()),
		"Queue_space": ((1610743832, LCID, 4, 0),()),
		"Saturation_flow_rate": ((1610743838, LCID, 4, 0),()),
		"Start_loss": ((1610743868, LCID, 4, 0),()),
		"Volume": ((1610743816, LCID, 4, 0),()),
		"Walking_speed": ((1610743834, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIMovement_peds(DispatchBaseClass):
	CLSID = IID('{DE5491F4-C24E-4505-A74A-DC4E93712375}')
	coclass_clsid = IID('{2680FEE3-C577-402C-BEC4-ED25E864B1C4}')

	# Result is of type ISIAPIMovement_ped
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Type=defaultNamedNotOptArg, Origin=defaultNamedNotOptArg, Stage=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1), (3, 1)),Type
			, Origin, Stage)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0099AEAC-F9B6-4DCE-9C0E-1434E9D603D7}')
		return ret

	def MovementExists(self, Type=defaultNamedNotOptArg, Origin=defaultNamedNotOptArg, Stage=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),Type
			, Origin, Stage)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Type=defaultNamedNotOptArg, Origin=defaultNamedNotOptArg, Stage=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1), (3, 1)),Type
			, Origin, Stage)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0099AEAC-F9B6-4DCE-9C0E-1434E9D603D7}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{0099AEAC-F9B6-4DCE-9C0E-1434E9D603D7}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIMovement_vehicle_od(DispatchBaseClass):
	CLSID = IID('{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}')
	coclass_clsid = IID('{BDA8A10E-42F8-4CDB-961D-7B85BB245C66}')

	_prop_map_get_ = {
		"Critical_gap": (1610743828, 2, (4, 0), (), "Critical_gap", None),
		"Destination": (1610743809, 2, (3, 0), (), "Destination", None),
		"Display_ltr_id": (1610743822, 2, (8, 0), (), "Display_ltr_id", None),
		"Display_od_id": (1610743820, 2, (8, 0), (), "Display_od_id", None),
		"End_departures": (1610743832, 2, (4, 0), (), "End_departures", None),
		"Exists": (1610743816, 2, (11, 0), (), "Exists", None),
		"Exit_flow_effect": (1610743836, 2, (4, 0), (), "Exit_flow_effect", None),
		"Followup_headway": (1610743830, 2, (4, 0), (), "Followup_headway", None),
		"IsPossible": (1610743811, 2, (11, 0), (), "IsPossible", None),
		"Is_TWSC_adj_applied": (1610743824, 2, (11, 0), (), "Is_TWSC_adj_applied", None),
		"Is_gap_acceptance_usergiven": (1610743826, 2, (11, 0), (), "Is_gap_acceptance_usergiven", None),
		"Minimum_departures": (1610743834, 2, (4, 0), (), "Minimum_departures", None),
		# Method 'MovementVehicleODMCs' returns object of type 'ISIAPIMovement_vehicle_od_mcs'
		"MovementVehicleODMCs": (1610743812, 2, (9, 0), (), "MovementVehicleODMCs", '{69A455C4-0A3C-4A69-8A20-DFC672995EDC}'),
		"ODMovDesignation": (1610743810, 2, (3, 0), (), "ODMovDesignation", None),
		"Opposing_ped_effect_option": (1610743842, 2, (3, 0), (), "Opposing_ped_effect_option", None),
		"Opposing_ped_effect_option_signals": (1610743840, 2, (3, 0), (), "Opposing_ped_effect_option_signals", None),
		"Opposing_ped_effect_start_loss": (1610743844, 2, (3, 0), (), "Opposing_ped_effect_start_loss", None),
		# Method 'Opposingmovement_peds' returns object of type 'ISIAPIOpposingmovement_peds'
		"Opposingmovement_peds": (1610743815, 2, (9, 0), (), "Opposingmovement_peds", '{580C5233-F043-4662-8C1D-2E0C31C568B9}'),
		# Method 'Opposingmovement_vehicles' returns object of type 'ISIAPIOpposingmovement_vehicles'
		"Opposingmovement_vehicles": (1610743814, 2, (9, 0), (), "Opposingmovement_vehicles", '{677C1F98-D3D5-40B3-A5E5-5AEBD3A33CCC}'),
		"Origin": (1610743808, 2, (3, 0), (), "Origin", None),
		"Percent_opposed_by_nearest": (1610743838, 2, (4, 0), (), "Percent_opposed_by_nearest", None),
		# Method 'Site' returns object of type 'ISIAPISite'
		"Site": (1610743813, 2, (9, 0), (), "Site", '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}'),
		"Total_volume": (1610743846, 2, (4, 0), (), "Total_volume", None),
		"Turndesignation": (1610743818, 2, (3, 0), (), "Turndesignation", None),
		"Zebra_ped_critical_gap": (1610743849, 2, (4, 0), (), "Zebra_ped_critical_gap", None),
		"Zebra_ped_followup_headway": (1610743851, 2, (4, 0), (), "Zebra_ped_followup_headway", None),
		"Zebra_ped_gap_acceptance_option": (1610743847, 2, (3, 0), (), "Zebra_ped_gap_acceptance_option", None),
		"Zebra_ped_minimum_departures": (1610743853, 2, (4, 0), (), "Zebra_ped_minimum_departures", None),
	}
	_prop_map_put_ = {
		"Critical_gap": ((1610743828, LCID, 4, 0),()),
		"Display_ltr_id": ((1610743822, LCID, 4, 0),()),
		"Display_od_id": ((1610743820, LCID, 4, 0),()),
		"End_departures": ((1610743832, LCID, 4, 0),()),
		"Exists": ((1610743816, LCID, 4, 0),()),
		"Exit_flow_effect": ((1610743836, LCID, 4, 0),()),
		"Followup_headway": ((1610743830, LCID, 4, 0),()),
		"Is_TWSC_adj_applied": ((1610743824, LCID, 4, 0),()),
		"Is_gap_acceptance_usergiven": ((1610743826, LCID, 4, 0),()),
		"Minimum_departures": ((1610743834, LCID, 4, 0),()),
		"Opposing_ped_effect_option": ((1610743842, LCID, 4, 0),()),
		"Opposing_ped_effect_option_signals": ((1610743840, LCID, 4, 0),()),
		"Opposing_ped_effect_start_loss": ((1610743844, LCID, 4, 0),()),
		"Percent_opposed_by_nearest": ((1610743838, LCID, 4, 0),()),
		"Turndesignation": ((1610743818, LCID, 4, 0),()),
		"Zebra_ped_critical_gap": ((1610743849, LCID, 4, 0),()),
		"Zebra_ped_followup_headway": ((1610743851, LCID, 4, 0),()),
		"Zebra_ped_gap_acceptance_option": ((1610743847, LCID, 4, 0),()),
		"Zebra_ped_minimum_departures": ((1610743853, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIMovement_vehicle_od_mc(DispatchBaseClass):
	CLSID = IID('{55D25294-3468-41D8-96A1-B5B6E06AFF99}')
	coclass_clsid = IID('{23B2A7F0-0A7C-4DD8-BB86-8613CA079749}')

	_prop_map_get_ = {
		"Approach_speed": (1610743821, 2, (4, 0), (), "Approach_speed", None),
		"Arrival_percentage": (1610743863, 2, (4, 0), (), "Arrival_percentage", None),
		"Arrival_type": (1610743861, 2, (3, 0), (), "Arrival_type", None),
		"Coordination_type": (1610743859, 2, (3, 0), (), "Coordination_type", None),
		"Early_cutoff": (1610743887, 2, (4, 0), (), "Early_cutoff", None),
		"End_gain": (1610743871, 2, (3, 0), (), "End_gain", None),
		"Exists": (1610743809, 2, (11, 0), (), "Exists", None),
		"Exit_distance": (1610743827, 2, (4, 0), (), "Exit_distance", None),
		"Exit_distance_user": (1610743825, 2, (11, 0), (), "Exit_distance_user", None),
		"Exit_speed": (1610743823, 2, (4, 0), (), "Exit_speed", None),
		"Extra_midblock_delay": (1610743901, 2, (4, 0), (), "Extra_midblock_delay", None),
		"Flow_scale": (1610743817, 2, (4, 0), (), "Flow_scale", None),
		"Gap_acceptance_factor": (1610743851, 2, (4, 0), (), "Gap_acceptance_factor", None),
		"Growth_rate": (1610743815, 2, (4, 0), (), "Growth_rate", None),
		"Has_extra_midblock_delay": (1610743899, 2, (11, 0), (), "Has_extra_midblock_delay", None),
		"Is_early_cutoff": (1610743885, 2, (11, 0), (), "Is_early_cutoff", None),
		"Is_high_priority": (1610743897, 2, (11, 0), (), "Is_high_priority", None),
		"Is_late_release": (1610743889, 2, (11, 0), (), "Is_late_release", None),
		"Late_release": (1610743891, 2, (4, 0), (), "Late_release", None),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
		"Maximum_green_time": (1610743879, 2, (3, 0), (), "Maximum_green_time", None),
		"Maximum_green_time_user": (1610743877, 2, (11, 0), (), "Maximum_green_time_user", None),
		"Minimum_green_time": (1610743875, 2, (3, 0), (), "Minimum_green_time", None),
		"Minimum_green_time_user": (1610743873, 2, (11, 0), (), "Minimum_green_time_user", None),
		# Method 'Movement_vehicle_od' returns object of type 'ISIAPIMovement_vehicle_od'
		"Movement_vehicle_od": (1610743810, 2, (9, 0), (), "Movement_vehicle_od", '{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}'),
		"Negotiation_distance": (1610743831, 2, (4, 0), (), "Negotiation_distance", None),
		"Negotiation_distance_user": (1610743829, 2, (11, 0), (), "Negotiation_distance_user", None),
		"Negotiation_radius": (1610743835, 2, (4, 0), (), "Negotiation_radius", None),
		"Negotiation_radius_option": (1610743833, 2, (3, 0), (), "Negotiation_radius_option", None),
		"Negotiation_speed": (1610743839, 2, (4, 0), (), "Negotiation_speed", None),
		"Negotiation_speed_user": (1610743837, 2, (11, 0), (), "Negotiation_speed_user", None),
		"Non_actuated": (1610743865, 2, (11, 0), (), "Non_actuated", None),
		"Occupancy": (1610743813, 2, (4, 0), (), "Occupancy", None),
		"Opposing_veh_factor": (1610743853, 2, (4, 0), (), "Opposing_veh_factor", None),
		"Peak_flow_factor": (1610743819, 2, (4, 0), (), "Peak_flow_factor", None),
		"Phase_actuation_option": (1610743893, 2, (3, 0), (), "Phase_actuation_option", None),
		"Phase_actuation_percent": (1610743895, 2, (4, 0), (), "Phase_actuation_percent", None),
		"Practical_degree_of_saturation": (1610743857, 2, (4, 0), (), "Practical_degree_of_saturation", None),
		"Practical_degree_of_saturation_user": (1610743855, 2, (11, 0), (), "Practical_degree_of_saturation_user", None),
		"Queue_space": (1610743841, 2, (4, 0), (), "Queue_space", None),
		"Start_loss": (1610743869, 2, (3, 0), (), "Start_loss", None),
		"Stopline_travel_time": (1610743883, 2, (3, 0), (), "Stopline_travel_time", None),
		"Stopline_travel_time_user": (1610743881, 2, (11, 0), (), "Stopline_travel_time_user", None),
		"Turn_on_red": (1610743867, 2, (11, 0), (), "Turn_on_red", None),
		"Turn_radius": (1610743849, 2, (4, 0), (), "Turn_radius", None),
		"Turn_veh_effect_option": (1610743845, 2, (3, 0), (), "Turn_veh_effect_option", None),
		"Turning_veh_factor": (1610743847, 2, (4, 0), (), "Turning_veh_factor", None),
		"Vehicle_length": (1610743843, 2, (4, 0), (), "Vehicle_length", None),
		"Volume": (1610743811, 2, (4, 0), (), "Volume", None),
	}
	_prop_map_put_ = {
		"Approach_speed": ((1610743821, LCID, 4, 0),()),
		"Arrival_percentage": ((1610743863, LCID, 4, 0),()),
		"Arrival_type": ((1610743861, LCID, 4, 0),()),
		"Coordination_type": ((1610743859, LCID, 4, 0),()),
		"Early_cutoff": ((1610743887, LCID, 4, 0),()),
		"End_gain": ((1610743871, LCID, 4, 0),()),
		"Exit_distance": ((1610743827, LCID, 4, 0),()),
		"Exit_distance_user": ((1610743825, LCID, 4, 0),()),
		"Exit_speed": ((1610743823, LCID, 4, 0),()),
		"Extra_midblock_delay": ((1610743901, LCID, 4, 0),()),
		"Flow_scale": ((1610743817, LCID, 4, 0),()),
		"Gap_acceptance_factor": ((1610743851, LCID, 4, 0),()),
		"Growth_rate": ((1610743815, LCID, 4, 0),()),
		"Has_extra_midblock_delay": ((1610743899, LCID, 4, 0),()),
		"Is_early_cutoff": ((1610743885, LCID, 4, 0),()),
		"Is_high_priority": ((1610743897, LCID, 4, 0),()),
		"Is_late_release": ((1610743889, LCID, 4, 0),()),
		"Late_release": ((1610743891, LCID, 4, 0),()),
		"Maximum_green_time": ((1610743879, LCID, 4, 0),()),
		"Maximum_green_time_user": ((1610743877, LCID, 4, 0),()),
		"Minimum_green_time": ((1610743875, LCID, 4, 0),()),
		"Minimum_green_time_user": ((1610743873, LCID, 4, 0),()),
		"Negotiation_distance": ((1610743831, LCID, 4, 0),()),
		"Negotiation_distance_user": ((1610743829, LCID, 4, 0),()),
		"Negotiation_radius": ((1610743835, LCID, 4, 0),()),
		"Negotiation_radius_option": ((1610743833, LCID, 4, 0),()),
		"Negotiation_speed": ((1610743839, LCID, 4, 0),()),
		"Negotiation_speed_user": ((1610743837, LCID, 4, 0),()),
		"Non_actuated": ((1610743865, LCID, 4, 0),()),
		"Occupancy": ((1610743813, LCID, 4, 0),()),
		"Opposing_veh_factor": ((1610743853, LCID, 4, 0),()),
		"Peak_flow_factor": ((1610743819, LCID, 4, 0),()),
		"Phase_actuation_option": ((1610743893, LCID, 4, 0),()),
		"Phase_actuation_percent": ((1610743895, LCID, 4, 0),()),
		"Practical_degree_of_saturation": ((1610743857, LCID, 4, 0),()),
		"Practical_degree_of_saturation_user": ((1610743855, LCID, 4, 0),()),
		"Queue_space": ((1610743841, LCID, 4, 0),()),
		"Start_loss": ((1610743869, LCID, 4, 0),()),
		"Stopline_travel_time": ((1610743883, LCID, 4, 0),()),
		"Stopline_travel_time_user": ((1610743881, LCID, 4, 0),()),
		"Turn_on_red": ((1610743867, LCID, 4, 0),()),
		"Turn_radius": ((1610743849, LCID, 4, 0),()),
		"Turn_veh_effect_option": ((1610743845, LCID, 4, 0),()),
		"Turning_veh_factor": ((1610743847, LCID, 4, 0),()),
		"Vehicle_length": ((1610743843, LCID, 4, 0),()),
		"Volume": ((1610743811, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIMovement_vehicle_od_mcs(DispatchBaseClass):
	CLSID = IID('{69A455C4-0A3C-4A69-8A20-DFC672995EDC}')
	coclass_clsid = IID('{8447273B-5B6D-438B-A672-27CE30624350}')

	# Result is of type ISIAPIMovement_vehicle_od_mc
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{55D25294-3468-41D8-96A1-B5B6E06AFF99}')
		return ret

	def MovementClassExists(self, mcClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),mcClass
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{55D25294-3468-41D8-96A1-B5B6E06AFF99}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{55D25294-3468-41D8-96A1-B5B6E06AFF99}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIMovement_vehicle_ods(DispatchBaseClass):
	CLSID = IID('{87B16289-A709-4781-ADA1-92C6D1F3EB3D}')
	coclass_clsid = IID('{954FF861-147D-46C1-BBBD-3B1FC1EEE70C}')

	# Result is of type ISIAPIMovement_vehicle_od
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),Origin
			, Destination)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}')
		return ret

	def MovementExists(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1), (3, 1)),Origin
			, Destination)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),Origin
			, Destination)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPINetwork(DispatchBaseClass):
	CLSID = IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')
	coclass_clsid = IID('{2756D52B-FF46-4C94-8B37-0443810347CB}')

	# Result is of type ISIAPINetworkCCG
	def AddNetworkCCG(self):
		ret = self._oleobj_.InvokeTypes(1610743887, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddNetworkCCG', '{6635581E-7C13-461E-9917-85B7CA3F7B07}')
		return ret

	# Result is of type ISIAPINetworkLegConnection
	def AddNetworkLegConnection(self, nwSite1=defaultNamedNotOptArg, legOrientation1=defaultNamedNotOptArg, nwSite2=defaultNamedNotOptArg, legOrientation2=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743885, LCID, 1, (9, 0), ((9, 1), (3, 1), (9, 1), (3, 1)),nwSite1
			, legOrientation1, nwSite2, legOrientation2)
		if ret is not None:
			ret = Dispatch(ret, 'AddNetworkLegConnection', '{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}')
		return ret

	# Result is of type ISIAPINetworkSite
	def AddNetworkSite(self, Site=defaultNamedNotOptArg, layoutX=defaultNamedNotOptArg, layoutY=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743883, LCID, 1, (9, 0), ((9, 1), (4, 1), (4, 1)),Site
			, layoutX, layoutY)
		if ret is not None:
			ret = Dispatch(ret, 'AddNetworkSite', '{4888B50C-984E-4865-B2CE-4FA9B66C2622}')
		return ret

	# Result is of type ISIAPIRoute
	def AddRoute(self):
		ret = self._oleobj_.InvokeTypes(1610743889, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddRoute', '{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')
		return ret

	# Result is of type ISIAPIRoute
	def CloneRoute(self, route=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743894, LCID, 1, (9, 0), ((9, 1),),route
			)
		if ret is not None:
			ret = Dispatch(ret, 'CloneRoute', '{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')
		return ret

	def CreateLayoutPngData(self):
		return self._ApplyTypes_(1610743896, 1, (8209, 0), (), 'CreateLayoutPngData', None,)

	def CreateLayoutPngFile(self, filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743897, LCID, 1, (11, 0), ((8, 1),),filename
			)

	def MoveNetworkCCGTo(self, ccg=defaultNamedNotOptArg, newPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743892, LCID, 1, (11, 0), ((9, 1), (3, 1)),ccg
			, newPosition)

	def MoveRouteTo(self, route=defaultNamedNotOptArg, newPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743895, LCID, 1, (11, 0), ((9, 1), (3, 1)),route
			, newPosition)

	def Process(self):
		return self._oleobj_.InvokeTypes(1610743881, LCID, 1, (11, 0), (),)

	def ProcessByRoutes(self):
		return self._oleobj_.InvokeTypes(1610743891, LCID, 1, (11, 0), (),)

	def RemoveNetworkCCG(self, ccg=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743888, LCID, 1, (11, 0), ((9, 1),),ccg
			)

	def RemoveNetworkLegConnection(self, nwLegConn=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743886, LCID, 1, (11, 0), ((9, 1),),nwLegConn
			)

	def RemoveNetworkSite(self, networkSite=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743884, LCID, 1, (11, 0), ((9, 1),),networkSite
			)

	def RemoveOutputData(self):
		return self._oleobj_.InvokeTypes(1610743955, LCID, 1, (11, 0), (),)

	def RemoveRoute(self, route=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743890, LCID, 1, (11, 0), ((9, 1),),route
			)

	def ResetRouteSignalOffsetPriority(self):
		return self._oleobj_.InvokeTypes(1610743893, LCID, 1, (11, 0), (),)

	def UpdateModifiedInfo(self):
		return self._oleobj_.InvokeTypes(1610743882, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"Category": (1610743898, 2, (8, 0), (), "Category", None),
		"CostUnit": (1610743822, 2, (8, 0), (), "CostUnit", None),
		"Created_by": (1610743855, 2, (8, 0), (), "Created_by", None),
		"Created_by_company": (1610743856, 2, (8, 0), (), "Created_by_company", None),
		"Created_date": (1610743854, 2, (7, 0), (), "Created_date", None),
		"Created_version": (1610743857, 2, (8, 0), (), "Created_version", None),
		"Cycle_time_option": (1610743842, 2, (3, 0), (), "Cycle_time_option", None),
		# Method 'DemandSensitivity' returns object of type 'ISIAPINetworkDemandSensitivity'
		"DemandSensitivity": (1610743934, 2, (9, 0), (), "DemandSensitivity", '{B8795F7C-B342-4E4D-9F88-398D704B4453}'),
		"Description": (1610743820, 2, (8, 0), (), "Description", None),
		# Method 'DiagnosticMsgs' returns object of type 'ISIAPIDiagnosticMsgs'
		"DiagnosticMsgs": (1610743877, 2, (9, 0), (), "DiagnosticMsgs", '{CBFD7927-0588-4CF2-BEB4-052B1F31A027}'),
		"DiagnosticStatus": (1610743876, 2, (3, 0), (), "DiagnosticStatus", None),
		"DriveOnLeft": (1610743818, 2, (11, 0), (), "DriveOnLeft", None),
		"Green_split_priority_option": (1610743928, 2, (3, 0), (), "Green_split_priority_option", None),
		"HoursPerYear": (1610743830, 2, (3, 0), (), "HoursPerYear", None),
		"IsIncludedInProjectSummary": (1610743932, 2, (11, 0), (), "IsIncludedInProjectSummary", None),
		"IsLaneBlockageModelApplied": (1610743952, 2, (11, 0), (), "IsLaneBlockageModelApplied", None),
		"IsPlatoonDispersionApplied": (1610743840, 2, (11, 0), (), "IsPlatoonDispersionApplied", None),
		"IsShortlaneQueueStorageRatioIncl": (1610743824, 2, (11, 0), (), "IsShortlaneQueueStorageRatioIncl", None),
		"Is_geometric_delay_excluded": (1610743946, 2, (11, 0), (), "Is_geometric_delay_excluded", None),
		"Is_hcm_delay_formula_applied": (1610743948, 2, (11, 0), (), "Is_hcm_delay_formula_applied", None),
		"Is_hcm_queue_formula_applied": (1610743950, 2, (11, 0), (), "Is_hcm_queue_formula_applied", None),
		"Is_timing_optimised_for_selected_result": (1610743930, 2, (11, 0), (), "Is_timing_optimised_for_selected_result", None),
		"LOSMethod": (1610743826, 2, (3, 0), (), "LOSMethod", None),
		"LOSTarget": (1610743828, 2, (3, 0), (), "LOSTarget", None),
		"Lane_blockage_effect_option": (1610743902, 2, (3, 0), (), "Lane_blockage_effect_option", None),
		"LastErrorMessage": (1610743875, 2, (8, 0), (), "LastErrorMessage", None),
		"MaxIterations": (1610743832, 2, (3, 0), (), "MaxIterations", None),
		"ModelName": (1610743817, 2, (8, 0), (), "ModelName", None),
		"ModelSignature": (1610743816, 2, (8, 0), (), "ModelSignature", None),
		"Modified_by": (1610743859, 2, (8, 0), (), "Modified_by", None),
		"Modified_by_company": (1610743860, 2, (8, 0), (), "Modified_by_company", None),
		"Modified_date": (1610743858, 2, (7, 0), (), "Modified_date", None),
		"Modified_version": (1610743861, 2, (8, 0), (), "Modified_version", None),
		"MultiRoutesSummaryOption": (1610743852, 2, (3, 0), (), "MultiRoutesSummaryOption", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		# Method 'NetworkCCGs' returns object of type 'ISIAPINetworkCCGs'
		"NetworkCCGs": (1610743879, 2, (9, 0), (), "NetworkCCGs", '{AFE37B56-E6C5-4F98-8853-6FFF575C25BC}'),
		"NetworkCycleTime": (1610743844, 2, (3, 0), (), "NetworkCycleTime", None),
		# Method 'NetworkFolder' returns object of type 'ISIAPINetworkFolder'
		"NetworkFolder": (1610743935, 2, (9, 0), (), "NetworkFolder", '{18533800-8D94-4C98-8BF7-59DC4E51C2DF}'),
		"NetworkID": (1610743811, 2, (8, 0), (), "NetworkID", None),
		# Method 'NetworkLegConnections' returns object of type 'ISIAPINetworkLegConnections'
		"NetworkLegConnections": (1610743864, 2, (9, 0), (), "NetworkLegConnections", '{F29A35EA-9B6B-46B7-839B-EC921C94A479}'),
		# Method 'NetworkMCs' returns object of type 'ISIAPINetworkMCs'
		"NetworkMCs": (1610743954, 2, (9, 0), (), "NetworkMCs", '{EA51880D-3150-4EF5-B203-17CC4EAC2214}'),
		# Method 'NetworkSites' returns object of type 'ISIAPINetworkSites'
		"NetworkSites": (1610743863, 2, (9, 0), (), "NetworkSites", '{8B19120E-37DE-43E9-AB2F-9F1743650053}'),
		"Network_id": (1610743808, 2, (3, 0), (), "Network_id", None),
		"OffsetDefinition": (1610743838, 2, (3, 0), (), "OffsetDefinition", None),
		"Optimum_cycle_time_increment": (1610743910, 2, (3, 0), (), "Optimum_cycle_time_increment", None),
		"Optimum_cycle_time_lower": (1610743906, 2, (3, 0), (), "Optimum_cycle_time_lower", None),
		"Optimum_cycle_time_lower_user": (1610743904, 2, (11, 0), (), "Optimum_cycle_time_lower_user", None),
		"Optimum_cycle_time_optim_method": (1610743914, 2, (3, 0), (), "Optimum_cycle_time_optim_method", None),
		"Optimum_cycle_time_perf_measure": (1610743912, 2, (3, 0), (), "Optimum_cycle_time_perf_measure", None),
		"Optimum_cycle_time_upper": (1610743908, 2, (3, 0), (), "Optimum_cycle_time_upper", None),
		"Optimum_max_green_optim_method": (1610743924, 2, (3, 0), (), "Optimum_max_green_optim_method", None),
		"Optimum_max_green_percent_increment": (1610743920, 2, (3, 0), (), "Optimum_max_green_percent_increment", None),
		"Optimum_max_green_percent_lower": (1610743916, 2, (3, 0), (), "Optimum_max_green_percent_lower", None),
		"Optimum_max_green_percent_upper": (1610743918, 2, (3, 0), (), "Optimum_max_green_percent_upper", None),
		"Optimum_max_green_perf_measure": (1610743922, 2, (3, 0), (), "Optimum_max_green_perf_measure", None),
		# Method 'OutputNetwork' returns object of type 'ISIAPIOutputNetwork'
		"OutputNetwork": (1610743865, 2, (9, 0), (), "OutputNetwork", '{5E551751-0DA8-4E10-931A-D474F6FFBB27}'),
		# Method 'OutputNetworkByRoutes' returns object of type 'ISIAPIOutputNetwork'
		"OutputNetworkByRoutes": (1610743866, 2, (9, 0), (), "OutputNetworkByRoutes", '{5E551751-0DA8-4E10-931A-D474F6FFBB27}'),
		"Peakflowperiod": (1610743900, 2, (3, 0), (), "Peakflowperiod", None),
		"Percentile_Queue": (1610743873, 2, (3, 0), (), "Percentile_Queue", None),
		"Percentile_queue_option": (1610743871, 2, (3, 0), (), "Percentile_queue_option", None),
		"Performance_Measure": (1610743869, 2, (3, 0), (), "Performance_Measure", None),
		"Position": (1610743813, 2, (3, 0), (), "Position", None),
		"Practical_cycle_rounding": (1610743848, 2, (3, 0), (), "Practical_cycle_rounding", None),
		"Practical_max_cycle_time": (1610743846, 2, (3, 0), (), "Practical_max_cycle_time", None),
		"ProcessingError": (1610743862, 2, (8, 0), (), "ProcessingError", None),
		# Method 'Project' returns object of type 'ISIAPIProject'
		"Project": (1610743878, 2, (9, 0), (), "Project", '{5817180B-2283-40FB-8068-C2F2D656EF04}'),
		# Method 'Routes' returns object of type 'ISIAPIRoutes'
		"Routes": (1610743880, 2, (9, 0), (), "Routes", '{DE44AC02-4804-4587-87BB-AC8E0ED05EEB}'),
		"SignalOffsetOption": (1610743836, 2, (3, 0), (), "SignalOffsetOption", None),
		"SitePhaseTimesOption": (1610743850, 2, (3, 0), (), "SitePhaseTimesOption", None),
		"Site_los_method": (1610743867, 2, (3, 0), (), "Site_los_method", None),
		"SpeedEfficiencyLOSUpperLimit_B": (1610743936, 2, (4, 0), (), "SpeedEfficiencyLOSUpperLimit_B", None),
		"SpeedEfficiencyLOSUpperLimit_C": (1610743938, 2, (4, 0), (), "SpeedEfficiencyLOSUpperLimit_C", None),
		"SpeedEfficiencyLOSUpperLimit_D": (1610743940, 2, (4, 0), (), "SpeedEfficiencyLOSUpperLimit_D", None),
		"SpeedEfficiencyLOSUpperLimit_E": (1610743942, 2, (4, 0), (), "SpeedEfficiencyLOSUpperLimit_E", None),
		"SpeedEfficiencyLOSUpperLimit_F": (1610743944, 2, (4, 0), (), "SpeedEfficiencyLOSUpperLimit_F", None),
		"StoppingDxPercent": (1610743834, 2, (4, 0), (), "StoppingDxPercent", None),
		"Title": (1610743814, 2, (8, 0), (), "Title", None),
		"Units": (1610743819, 2, (3, 0), (), "Units", None),
		"Variable_phasing_perf_measure": (1610743926, 2, (3, 0), (), "Variable_phasing_perf_measure", None),
	}
	_prop_map_put_ = {
		"Category": ((1610743898, LCID, 4, 0),()),
		"CostUnit": ((1610743822, LCID, 4, 0),()),
		"Cycle_time_option": ((1610743842, LCID, 4, 0),()),
		"Description": ((1610743820, LCID, 4, 0),()),
		"Green_split_priority_option": ((1610743928, LCID, 4, 0),()),
		"HoursPerYear": ((1610743830, LCID, 4, 0),()),
		"IsIncludedInProjectSummary": ((1610743932, LCID, 4, 0),()),
		"IsLaneBlockageModelApplied": ((1610743952, LCID, 4, 0),()),
		"IsPlatoonDispersionApplied": ((1610743840, LCID, 4, 0),()),
		"IsShortlaneQueueStorageRatioIncl": ((1610743824, LCID, 4, 0),()),
		"Is_geometric_delay_excluded": ((1610743946, LCID, 4, 0),()),
		"Is_hcm_delay_formula_applied": ((1610743948, LCID, 4, 0),()),
		"Is_hcm_queue_formula_applied": ((1610743950, LCID, 4, 0),()),
		"Is_timing_optimised_for_selected_result": ((1610743930, LCID, 4, 0),()),
		"LOSMethod": ((1610743826, LCID, 4, 0),()),
		"LOSTarget": ((1610743828, LCID, 4, 0),()),
		"Lane_blockage_effect_option": ((1610743902, LCID, 4, 0),()),
		"MaxIterations": ((1610743832, LCID, 4, 0),()),
		"MultiRoutesSummaryOption": ((1610743852, LCID, 4, 0),()),
		"Name": ((1610743809, LCID, 4, 0),()),
		"NetworkCycleTime": ((1610743844, LCID, 4, 0),()),
		"NetworkID": ((1610743811, LCID, 4, 0),()),
		"OffsetDefinition": ((1610743838, LCID, 4, 0),()),
		"Optimum_cycle_time_increment": ((1610743910, LCID, 4, 0),()),
		"Optimum_cycle_time_lower": ((1610743906, LCID, 4, 0),()),
		"Optimum_cycle_time_lower_user": ((1610743904, LCID, 4, 0),()),
		"Optimum_cycle_time_optim_method": ((1610743914, LCID, 4, 0),()),
		"Optimum_cycle_time_perf_measure": ((1610743912, LCID, 4, 0),()),
		"Optimum_cycle_time_upper": ((1610743908, LCID, 4, 0),()),
		"Optimum_max_green_optim_method": ((1610743924, LCID, 4, 0),()),
		"Optimum_max_green_percent_increment": ((1610743920, LCID, 4, 0),()),
		"Optimum_max_green_percent_lower": ((1610743916, LCID, 4, 0),()),
		"Optimum_max_green_percent_upper": ((1610743918, LCID, 4, 0),()),
		"Optimum_max_green_perf_measure": ((1610743922, LCID, 4, 0),()),
		"Peakflowperiod": ((1610743900, LCID, 4, 0),()),
		"Percentile_Queue": ((1610743873, LCID, 4, 0),()),
		"Percentile_queue_option": ((1610743871, LCID, 4, 0),()),
		"Performance_Measure": ((1610743869, LCID, 4, 0),()),
		"Practical_cycle_rounding": ((1610743848, LCID, 4, 0),()),
		"Practical_max_cycle_time": ((1610743846, LCID, 4, 0),()),
		"SignalOffsetOption": ((1610743836, LCID, 4, 0),()),
		"SitePhaseTimesOption": ((1610743850, LCID, 4, 0),()),
		"Site_los_method": ((1610743867, LCID, 4, 0),()),
		"SpeedEfficiencyLOSUpperLimit_B": ((1610743936, LCID, 4, 0),()),
		"SpeedEfficiencyLOSUpperLimit_C": ((1610743938, LCID, 4, 0),()),
		"SpeedEfficiencyLOSUpperLimit_D": ((1610743940, LCID, 4, 0),()),
		"SpeedEfficiencyLOSUpperLimit_E": ((1610743942, LCID, 4, 0),()),
		"SpeedEfficiencyLOSUpperLimit_F": ((1610743944, LCID, 4, 0),()),
		"StoppingDxPercent": ((1610743834, LCID, 4, 0),()),
		"Title": ((1610743814, LCID, 4, 0),()),
		"Variable_phasing_perf_measure": ((1610743926, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPINetworkCCG(DispatchBaseClass):
	CLSID = IID('{6635581E-7C13-461E-9917-85B7CA3F7B07}')
	coclass_clsid = IID('{6D2F736E-A370-4F0A-ADBB-415015499B40}')

	# Result is of type ISIAPINetworkCCGSequence
	def AddCCGSequence(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743827, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddCCGSequence', '{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')
		return ret

	def AddNetworkSite(self, networkSite=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743825, LCID, 1, (11, 0), ((9, 1),),networkSite
			)

	# Result is of type ISIAPINetworkCCGSequence
	def CloneCCGSequence(self, ccgSequence=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743829, LCID, 1, (9, 0), ((9, 1),),ccgSequence
			)
		if ret is not None:
			ret = Dispatch(ret, 'CloneCCGSequence', '{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')
		return ret

	def MoveCCGSequenceTo(self, ccgSequence=defaultNamedNotOptArg, newPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743830, LCID, 1, (11, 0), ((9, 1), (3, 1)),ccgSequence
			, newPosition)

	def RemoveCCGSequence(self, ccgSequence=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743828, LCID, 1, (11, 0), ((9, 1),),ccgSequence
			)

	def RemoveNetworkSite(self, networkSite=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743826, LCID, 1, (11, 0), ((9, 1),),networkSite
			)

	_prop_map_get_ = {
		# Method 'CCGSequences' returns object of type 'ISIAPINetworkCCGSequences'
		"CCGSequences": (1610743823, 2, (9, 0), (), "CCGSequences", '{833D5364-D498-47D7-BE84-44624D8D16B5}'),
		"CoordinatedOption": (1610743817, 2, (3, 0), (), "CoordinatedOption", None),
		"IsReference": (1610743813, 2, (11, 0), (), "IsReference", None),
		"Is_multi_sequence_enabled": (1610743831, 2, (11, 0), (), "Is_multi_sequence_enabled", None),
		"LastErrorMessage": (1610743824, 2, (8, 0), (), "LastErrorMessage", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		# Method 'Network' returns object of type 'ISIAPINetwork'
		"Network": (1610743821, 2, (9, 0), (), "Network", '{C5A62A3D-7D9C-4544-8547-499D4C770332}'),
		"NetworkCCGID": (1610743810, 2, (8, 0), (), "NetworkCCGID", None),
		# Method 'NetworkSites' returns object of type 'ISIAPINetworkSites'
		"NetworkSites": (1610743822, 2, (9, 0), (), "NetworkSites", '{8B19120E-37DE-43E9-AB2F-9F1743650053}'),
		"Offset": (1610743815, 2, (3, 0), (), "Offset", None),
		"Position": (1610743812, 2, (3, 0), (), "Position", None),
		"Signal_analysis_method": (1610743819, 2, (3, 0), (), "Signal_analysis_method", None),
	}
	_prop_map_put_ = {
		"CoordinatedOption": ((1610743817, LCID, 4, 0),()),
		"IsReference": ((1610743813, LCID, 4, 0),()),
		"Is_multi_sequence_enabled": ((1610743831, LCID, 4, 0),()),
		"Name": ((1610743808, LCID, 4, 0),()),
		"NetworkCCGID": ((1610743810, LCID, 4, 0),()),
		"Offset": ((1610743815, LCID, 4, 0),()),
		"Signal_analysis_method": ((1610743819, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPINetworkCCGPhase(DispatchBaseClass):
	CLSID = IID('{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')
	coclass_clsid = IID('{1D63D43D-AE3E-4580-A807-1D8F60277E86}')

	# Result is of type ISIAPIPhasemovement_peds
	def GetPhasemovementPedsByNetworkSite(self, networkSite=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743839, LCID, 1, (9, 0), ((9, 1),),networkSite
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPhasemovementPedsByNetworkSite', '{8F802394-B3B4-4D06-8EA2-A0247C600A86}')
		return ret

	# Result is of type ISIAPIPhasemovement_vehicles
	def GetPhasemovementVehiclesByNetworkSite(self, networkSite=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743838, LCID, 1, (9, 0), ((9, 1),),networkSite
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPhasemovementVehiclesByNetworkSite', '{843F1163-A090-4AA1-9AB4-8CF90C0A8BFF}')
		return ret

	_prop_map_get_ = {
		"All_red_time": (1610743819, 2, (3, 0), (), "All_red_time", None),
		"Dummy_maximum_green_time": (1610743829, 2, (3, 0), (), "Dummy_maximum_green_time", None),
		"Dummy_maximum_green_time_user": (1610743827, 2, (11, 0), (), "Dummy_maximum_green_time_user", None),
		"Dummy_minimum_green_time": (1610743825, 2, (3, 0), (), "Dummy_minimum_green_time", None),
		"Dummy_minimum_green_time_user": (1610743823, 2, (11, 0), (), "Dummy_minimum_green_time_user", None),
		"Has_dummy": (1610743821, 2, (11, 0), (), "Has_dummy", None),
		"IsReferencePhase": (1610743813, 2, (11, 0), (), "IsReferencePhase", None),
		"Is_variable": (1610743811, 2, (11, 0), (), "Is_variable", None),
		"Minimum_time": (1610743831, 2, (3, 0), (), "Minimum_time", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		"Phase_frequency": (1610743835, 2, (4, 0), (), "Phase_frequency", None),
		"Phase_frequency_user": (1610743833, 2, (11, 0), (), "Phase_frequency_user", None),
		"Phase_time": (1610743815, 2, (3, 0), (), "Phase_time", None),
		"Position": (1610743810, 2, (3, 0), (), "Position", None),
		"Yellow_time": (1610743817, 2, (3, 0), (), "Yellow_time", None),
		# Method 'ccgSequence' returns object of type 'ISIAPINetworkCCGSequence'
		"ccgSequence": (1610743837, 2, (9, 0), (), "ccgSequence", '{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}'),
	}
	_prop_map_put_ = {
		"All_red_time": ((1610743819, LCID, 4, 0),()),
		"Dummy_maximum_green_time": ((1610743829, LCID, 4, 0),()),
		"Dummy_maximum_green_time_user": ((1610743827, LCID, 4, 0),()),
		"Dummy_minimum_green_time": ((1610743825, LCID, 4, 0),()),
		"Dummy_minimum_green_time_user": ((1610743823, LCID, 4, 0),()),
		"Has_dummy": ((1610743821, LCID, 4, 0),()),
		"IsReferencePhase": ((1610743813, LCID, 4, 0),()),
		"Is_variable": ((1610743811, LCID, 4, 0),()),
		"Minimum_time": ((1610743831, LCID, 4, 0),()),
		"Name": ((1610743808, LCID, 4, 0),()),
		"Phase_frequency": ((1610743835, LCID, 4, 0),()),
		"Phase_frequency_user": ((1610743833, LCID, 4, 0),()),
		"Phase_time": ((1610743815, LCID, 4, 0),()),
		"Yellow_time": ((1610743817, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPINetworkCCGPhases(DispatchBaseClass):
	CLSID = IID('{A2B9F260-C553-40A5-99CB-16F98407645F}')
	coclass_clsid = IID('{7A5CF9F9-A024-451D-8C83-60F453170DC4}')

	# Result is of type ISIAPINetworkCCGPhase
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, phasename=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),phasename
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')
		return ret

	# Result is of type ISIAPINetworkCCGPhase
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')
		return ret

	def PhaseExists(self, phasename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), ((8, 1),),phasename
			)

	_prop_map_get_ = {
		"Count": (1610743811, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, phasename=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),phasename
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743811, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPINetworkCCGSequence(DispatchBaseClass):
	CLSID = IID('{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')
	coclass_clsid = IID('{0C3B93A9-7DEE-4339-9CF8-1E5F7F64653C}')

	# Result is of type ISIAPINetworkCCGPhase
	def AddCCGPhase(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743862, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddCCGPhase', '{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')
		return ret

	# Result is of type ISIAPINetworkCCGPhase
	def CloneCCGPhase(self, ccgPhase=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743865, LCID, 1, (9, 0), ((9, 1),),ccgPhase
			)
		if ret is not None:
			ret = Dispatch(ret, 'CloneCCGPhase', '{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')
		return ret

	# Result is of type ISIAPINetworkCCGPhase
	def InsertCCGPhase(self, Position=defaultNamedNotOptArg, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743863, LCID, 1, (9, 0), ((3, 1), (8, 1)),Position
			, Name)
		if ret is not None:
			ret = Dispatch(ret, 'InsertCCGPhase', '{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')
		return ret

	def MoveCCGPhaseTo(self, ccgPhase=defaultNamedNotOptArg, newPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743866, LCID, 1, (11, 0), ((9, 1), (3, 1)),ccgPhase
			, newPosition)

	def RemoveCCGPhase(self, ccgPhase=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743864, LCID, 1, (11, 0), ((9, 1),),ccgPhase
			)

	_prop_map_get_ = {
		"Actuated_gap_major_mov": (1610743851, 2, (4, 0), (), "Actuated_gap_major_mov", None),
		"Actuated_gap_minor_mov": (1610743853, 2, (4, 0), (), "Actuated_gap_minor_mov", None),
		"Actuated_max_green_major_mov": (1610743847, 2, (4, 0), (), "Actuated_max_green_major_mov", None),
		"Actuated_max_green_minor_mov": (1610743849, 2, (4, 0), (), "Actuated_max_green_minor_mov", None),
		# Method 'CCGPhases' returns object of type 'ISIAPINetworkCCGPhases'
		"CCGPhases": (1610743860, 2, (9, 0), (), "CCGPhases", '{A2B9F260-C553-40A5-99CB-16F98407645F}'),
		"Cycle_time_option": (1610743813, 2, (3, 0), (), "Cycle_time_option", None),
		"Eff_det_zone_len_major_mov": (1610743855, 2, (4, 0), (), "Eff_det_zone_len_major_mov", None),
		"Eff_det_zone_len_minor_mov": (1610743857, 2, (4, 0), (), "Eff_det_zone_len_minor_mov", None),
		"Green_split_priority_option": (1610743845, 2, (3, 0), (), "Green_split_priority_option", None),
		"Is_selected": (1610743811, 2, (11, 0), (), "Is_selected", None),
		"LastErrorMessage": (1610743861, 2, (8, 0), (), "LastErrorMessage", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		# Method 'NetworkCCG' returns object of type 'ISIAPINetworkCCG'
		"NetworkCCG": (1610743859, 2, (9, 0), (), "NetworkCCG", '{6635581E-7C13-461E-9917-85B7CA3F7B07}'),
		"Optimum_cycle_time_increment": (1610743825, 2, (3, 0), (), "Optimum_cycle_time_increment", None),
		"Optimum_cycle_time_lower": (1610743821, 2, (3, 0), (), "Optimum_cycle_time_lower", None),
		"Optimum_cycle_time_lower_user": (1610743819, 2, (11, 0), (), "Optimum_cycle_time_lower_user", None),
		"Optimum_cycle_time_optim_method": (1610743829, 2, (3, 0), (), "Optimum_cycle_time_optim_method", None),
		"Optimum_cycle_time_perf_measure": (1610743827, 2, (3, 0), (), "Optimum_cycle_time_perf_measure", None),
		"Optimum_cycle_time_upper": (1610743823, 2, (3, 0), (), "Optimum_cycle_time_upper", None),
		"Optimum_max_green_optim_method": (1610743839, 2, (3, 0), (), "Optimum_max_green_optim_method", None),
		"Optimum_max_green_percent_increment": (1610743835, 2, (3, 0), (), "Optimum_max_green_percent_increment", None),
		"Optimum_max_green_percent_lower": (1610743831, 2, (3, 0), (), "Optimum_max_green_percent_lower", None),
		"Optimum_max_green_percent_upper": (1610743833, 2, (3, 0), (), "Optimum_max_green_percent_upper", None),
		"Optimum_max_green_perf_measure": (1610743837, 2, (3, 0), (), "Optimum_max_green_perf_measure", None),
		"Position": (1610743810, 2, (3, 0), (), "Position", None),
		"Practical_cycle_rounding": (1610743817, 2, (3, 0), (), "Practical_cycle_rounding", None),
		"Practical_max_cycle_time": (1610743815, 2, (3, 0), (), "Practical_max_cycle_time", None),
		"Usergiven_cycle_time": (1610743843, 2, (3, 0), (), "Usergiven_cycle_time", None),
		"Variable_phasing_perf_measure": (1610743841, 2, (3, 0), (), "Variable_phasing_perf_measure", None),
	}
	_prop_map_put_ = {
		"Actuated_gap_major_mov": ((1610743851, LCID, 4, 0),()),
		"Actuated_gap_minor_mov": ((1610743853, LCID, 4, 0),()),
		"Actuated_max_green_major_mov": ((1610743847, LCID, 4, 0),()),
		"Actuated_max_green_minor_mov": ((1610743849, LCID, 4, 0),()),
		"Cycle_time_option": ((1610743813, LCID, 4, 0),()),
		"Eff_det_zone_len_major_mov": ((1610743855, LCID, 4, 0),()),
		"Eff_det_zone_len_minor_mov": ((1610743857, LCID, 4, 0),()),
		"Green_split_priority_option": ((1610743845, LCID, 4, 0),()),
		"Is_selected": ((1610743811, LCID, 4, 0),()),
		"Name": ((1610743808, LCID, 4, 0),()),
		"Optimum_cycle_time_increment": ((1610743825, LCID, 4, 0),()),
		"Optimum_cycle_time_lower": ((1610743821, LCID, 4, 0),()),
		"Optimum_cycle_time_lower_user": ((1610743819, LCID, 4, 0),()),
		"Optimum_cycle_time_optim_method": ((1610743829, LCID, 4, 0),()),
		"Optimum_cycle_time_perf_measure": ((1610743827, LCID, 4, 0),()),
		"Optimum_cycle_time_upper": ((1610743823, LCID, 4, 0),()),
		"Optimum_max_green_optim_method": ((1610743839, LCID, 4, 0),()),
		"Optimum_max_green_percent_increment": ((1610743835, LCID, 4, 0),()),
		"Optimum_max_green_percent_lower": ((1610743831, LCID, 4, 0),()),
		"Optimum_max_green_percent_upper": ((1610743833, LCID, 4, 0),()),
		"Optimum_max_green_perf_measure": ((1610743837, LCID, 4, 0),()),
		"Practical_cycle_rounding": ((1610743817, LCID, 4, 0),()),
		"Practical_max_cycle_time": ((1610743815, LCID, 4, 0),()),
		"Usergiven_cycle_time": ((1610743843, LCID, 4, 0),()),
		"Variable_phasing_perf_measure": ((1610743841, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPINetworkCCGSequences(DispatchBaseClass):
	CLSID = IID('{833D5364-D498-47D7-BE84-44624D8D16B5}')
	coclass_clsid = IID('{10A357EA-76F6-4197-B4DC-BA4E0B877F70}')

	# Result is of type ISIAPINetworkCCGSequence
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')
		return ret

	# Result is of type ISIAPINetworkCCGSequence
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')
		return ret

	def SequenceExists(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), ((8, 1),),Name
			)

	_prop_map_get_ = {
		"Count": (1610743811, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743811, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPINetworkCCGs(DispatchBaseClass):
	CLSID = IID('{AFE37B56-E6C5-4F98-8853-6FFF575C25BC}')
	coclass_clsid = IID('{F42C1BFD-FE64-49F5-9EA9-97A29C94E9A8}')

	# Result is of type ISIAPINetworkCCG
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ccgName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),ccgName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6635581E-7C13-461E-9917-85B7CA3F7B07}')
		return ret

	# Result is of type ISIAPINetworkCCG
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{6635581E-7C13-461E-9917-85B7CA3F7B07}')
		return ret

	def NetworkCCGExists(self, ccgName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), ((8, 1),),ccgName
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ccgName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),ccgName
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{6635581E-7C13-461E-9917-85B7CA3F7B07}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{6635581E-7C13-461E-9917-85B7CA3F7B07}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPINetworkDemandSensitivity(DispatchBaseClass):
	CLSID = IID('{B8795F7C-B342-4E4D-9F88-398D704B4453}')
	coclass_clsid = IID('{75BDF116-4417-40F7-9D85-0E70C279A0E0}')

	_prop_map_get_ = {
		"Analysis_option": (1610743809, 2, (3, 0), (), "Analysis_option", None),
		"Design_Life_Constant_num_years": (1610743819, 2, (3, 0), (), "Design_Life_Constant_num_years", None),
		"Design_Life_Growth_Model": (1610743813, 2, (3, 0), (), "Design_Life_Growth_Model", None),
		"Design_Life_Is_constant_num_years_applied": (1610743817, 2, (11, 0), (), "Design_Life_Is_constant_num_years_applied", None),
		"Design_Life_Objective": (1610743811, 2, (3, 0), (), "Design_Life_Objective", None),
		"Design_Life_Years": (1610743815, 2, (3, 0), (), "Design_Life_Years", None),
		"Flow_Scale_Constant_factor": (1610743829, 2, (4, 0), (), "Flow_Scale_Constant_factor", None),
		"Flow_Scale_Is_constant_factor_applied": (1610743827, 2, (11, 0), (), "Flow_Scale_Is_constant_factor_applied", None),
		"Flow_Scale_Lower": (1610743823, 2, (4, 0), (), "Flow_Scale_Lower", None),
		"Flow_Scale_Objective": (1610743821, 2, (3, 0), (), "Flow_Scale_Objective", None),
		"Flow_Scale_Upper": (1610743825, 2, (4, 0), (), "Flow_Scale_Upper", None),
		# Method 'Network' returns object of type 'ISIAPINetwork'
		"Network": (1610743808, 2, (9, 0), (), "Network", '{C5A62A3D-7D9C-4544-8547-499D4C770332}'),
		"Result_option": (1610743832, 2, (3, 0), (), "Result_option", None),
		# Method 'SensitivityGeneralParameterGroup' returns object of type 'ISIAPISensitivity'
		"SensitivityGeneralParameterGroup": (1610743831, 2, (9, 0), (), "SensitivityGeneralParameterGroup", '{D025138A-4F4C-4613-8FA7-D1FD5550A50C}'),
	}
	_prop_map_put_ = {
		"Analysis_option": ((1610743809, LCID, 4, 0),()),
		"Design_Life_Constant_num_years": ((1610743819, LCID, 4, 0),()),
		"Design_Life_Growth_Model": ((1610743813, LCID, 4, 0),()),
		"Design_Life_Is_constant_num_years_applied": ((1610743817, LCID, 4, 0),()),
		"Design_Life_Objective": ((1610743811, LCID, 4, 0),()),
		"Design_Life_Years": ((1610743815, LCID, 4, 0),()),
		"Flow_Scale_Constant_factor": ((1610743829, LCID, 4, 0),()),
		"Flow_Scale_Is_constant_factor_applied": ((1610743827, LCID, 4, 0),()),
		"Flow_Scale_Lower": ((1610743823, LCID, 4, 0),()),
		"Flow_Scale_Objective": ((1610743821, LCID, 4, 0),()),
		"Flow_Scale_Upper": ((1610743825, LCID, 4, 0),()),
		"Result_option": ((1610743832, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPINetworkFolder(DispatchBaseClass):
	CLSID = IID('{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')
	coclass_clsid = IID('{EABC402D-EA39-45D4-B70C-57ABA79EE4AE}')

	# Result is of type ISIAPINetwork
	def AddNetwork(self, softwareSetup=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743813, LCID, 1, (9, 0), ((3, 1),),softwareSetup
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddNetwork', '{C5A62A3D-7D9C-4544-8547-499D4C770332}')
		return ret

	# Result is of type ISIAPINetwork
	def AddNetwork_2(self, softwareSetupSignature=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743814, LCID, 1, (9, 0), ((8, 1),),softwareSetupSignature
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddNetwork_2', '{C5A62A3D-7D9C-4544-8547-499D4C770332}')
		return ret

	# Result is of type ISIAPINetwork
	def CloneNetwork(self, Network=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743816, LCID, 1, (9, 0), ((9, 1),),Network
			)
		if ret is not None:
			ret = Dispatch(ret, 'CloneNetwork', '{C5A62A3D-7D9C-4544-8547-499D4C770332}')
		return ret

	# Result is of type ISIAPINetwork
	def CloneNetworkWithSites(self, Network=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743817, LCID, 1, (9, 0), ((9, 1),),Network
			)
		if ret is not None:
			ret = Dispatch(ret, 'CloneNetworkWithSites', '{C5A62A3D-7D9C-4544-8547-499D4C770332}')
		return ret

	def MoveNetworkTo(self, Network=defaultNamedNotOptArg, newPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743818, LCID, 1, (11, 0), ((9, 1), (3, 1)),Network
			, newPosition)

	def MoveNetworksToFolder(self, networkNames=defaultNamedNotOptArg, destFolder=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743819, LCID, 1, (3, 0), ((8, 1), (9, 1)),networkNames
			, destFolder)

	def RemoveNetwork(self, Network=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743815, LCID, 1, (11, 0), ((9, 1),),Network
			)

	_prop_map_get_ = {
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		# Method 'Networks' returns object of type 'ISIAPINetworks'
		"Networks": (1610743811, 2, (9, 0), (), "Networks", '{98CE5F37-494C-484F-B8F5-50993C839B3B}'),
		"Position": (1610743810, 2, (3, 0), (), "Position", None),
		# Method 'Project' returns object of type 'ISIAPIProject'
		"Project": (1610743812, 2, (9, 0), (), "Project", '{5817180B-2283-40FB-8068-C2F2D656EF04}'),
	}
	_prop_map_put_ = {
		"Name": ((1610743808, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPINetworkFolders(DispatchBaseClass):
	CLSID = IID('{12AD1FBE-8A7B-4CB9-9DD5-F233FC8FC13C}')
	coclass_clsid = IID('{14AB4741-60D5-4E2C-A7D9-391036F4ADA2}')

	# Result is of type ISIAPINetworkFolder
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')
		return ret

	# Result is of type ISIAPINetworkFolder
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')
		return ret

	def NetworkFolderExists(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), ((8, 1),),Name
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPINetworkLegConnection(DispatchBaseClass):
	CLSID = IID('{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}')
	coclass_clsid = IID('{16F09299-E4AE-446A-961B-8EE1ABB10071}')

	_prop_map_get_ = {
		"ConnectionType": (1610743815, 2, (3, 0), (), "ConnectionType", None),
		"Leg1_Orientation": (1610743809, 2, (3, 0), (), "Leg1_Orientation", None),
		"Leg2_Orientation": (1610743811, 2, (3, 0), (), "Leg2_Orientation", None),
		# Method 'Network' returns object of type 'ISIAPINetwork'
		"Network": (1610743812, 2, (9, 0), (), "Network", '{C5A62A3D-7D9C-4544-8547-499D4C770332}'),
		# Method 'NetworkSite1' returns object of type 'ISIAPINetworkSite'
		"NetworkSite1": (1610743813, 2, (9, 0), (), "NetworkSite1", '{4888B50C-984E-4865-B2CE-4FA9B66C2622}'),
		# Method 'NetworkSite2' returns object of type 'ISIAPINetworkSite'
		"NetworkSite2": (1610743814, 2, (9, 0), (), "NetworkSite2", '{4888B50C-984E-4865-B2CE-4FA9B66C2622}'),
		"Site1_Name": (1610743808, 2, (8, 0), (), "Site1_Name", None),
		"Site2_Name": (1610743810, 2, (8, 0), (), "Site2_Name", None),
		"ZIndex": (1610743817, 2, (3, 0), (), "ZIndex", None),
	}
	_prop_map_put_ = {
		"ConnectionType": ((1610743815, LCID, 4, 0),()),
		"ZIndex": ((1610743817, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPINetworkLegConnections(DispatchBaseClass):
	CLSID = IID('{F29A35EA-9B6B-46B7-839B-EC921C94A479}')
	coclass_clsid = IID('{01B7EA08-A88F-45BE-903F-FB14E5182042}')

	# Result is of type ISIAPINetworkLegConnection
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPINetworkMC(DispatchBaseClass):
	CLSID = IID('{213E3AC6-7026-49A5-A65E-B5E2CE167E8D}')
	coclass_clsid = IID('{2574B151-F7F0-4022-9BA1-A341BC5D729C}')

	_prop_map_get_ = {
		"DesiredSpeed": (1610743811, 2, (4, 0), (), "DesiredSpeed", None),
		"DesiredSpeedMethod": (1610743809, 2, (3, 0), (), "DesiredSpeedMethod", None),
		"LowerLimitOfSpeedEfficiency": (1610743813, 2, (4, 0), (), "LowerLimitOfSpeedEfficiency", None),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
		# Method 'Network' returns object of type 'ISIAPINetwork'
		"Network": (1610743815, 2, (9, 0), (), "Network", '{C5A62A3D-7D9C-4544-8547-499D4C770332}'),
	}
	_prop_map_put_ = {
		"DesiredSpeed": ((1610743811, LCID, 4, 0),()),
		"DesiredSpeedMethod": ((1610743809, LCID, 4, 0),()),
		"LowerLimitOfSpeedEfficiency": ((1610743813, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPINetworkMCs(DispatchBaseClass):
	CLSID = IID('{EA51880D-3150-4EF5-B203-17CC4EAC2214}')
	coclass_clsid = IID('{CEE4DFD4-600F-4DAC-BA31-BE8B7F1DF783}')

	# Result is of type ISIAPINetworkMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{213E3AC6-7026-49A5-A65E-B5E2CE167E8D}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{213E3AC6-7026-49A5-A65E-B5E2CE167E8D}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{213E3AC6-7026-49A5-A65E-B5E2CE167E8D}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPINetworkSite(DispatchBaseClass):
	CLSID = IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')
	coclass_clsid = IID('{37361C6E-E0EE-4D90-AA13-88732732B094}')

	_prop_map_get_ = {
		"CoordinatedOption": (1610743820, 2, (3, 0), (), "CoordinatedOption", None),
		# Method 'DiagnosticMsgs' returns object of type 'ISIAPIDiagnosticMsgs'
		"DiagnosticMsgs": (1610743826, 2, (9, 0), (), "DiagnosticMsgs", '{CBFD7927-0588-4CF2-BEB4-052B1F31A027}'),
		"DiagnosticStatus": (1610743825, 2, (3, 0), (), "DiagnosticStatus", None),
		"IsIncludedInProjectSummary": (1610743827, 2, (11, 0), (), "IsIncludedInProjectSummary", None),
		"IsReference": (1610743812, 2, (11, 0), (), "IsReference", None),
		# Method 'Network' returns object of type 'ISIAPINetwork'
		"Network": (1610743809, 2, (9, 0), (), "Network", '{C5A62A3D-7D9C-4544-8547-499D4C770332}'),
		# Method 'NetworkCCG' returns object of type 'ISIAPINetworkCCG'
		"NetworkCCG": (1610743823, 2, (9, 0), (), "NetworkCCG", '{6635581E-7C13-461E-9917-85B7CA3F7B07}'),
		# Method 'NetworkLegConnections' returns object of type 'ISIAPINetworkLegConnections'
		"NetworkLegConnections": (1610743822, 2, (9, 0), (), "NetworkLegConnections", '{F29A35EA-9B6B-46B7-839B-EC921C94A479}'),
		"NetworkSite_id": (1610743808, 2, (3, 0), (), "NetworkSite_id", None),
		"Offset": (1610743814, 2, (3, 0), (), "Offset", None),
		# Method 'Site' returns object of type 'ISIAPISite'
		"Site": (1610743824, 2, (9, 0), (), "Site", '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}'),
		"SiteName": (1610743810, 2, (8, 0), (), "SiteName", None),
		# Method 'SiteOutputset' returns object of type 'ISIAPIOutputset'
		"SiteOutputset": (1610743811, 2, (9, 0), (), "SiteOutputset", '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}'),
		"layoutX": (1610743816, 2, (4, 0), (), "layoutX", None),
		"layoutY": (1610743818, 2, (4, 0), (), "layoutY", None),
	}
	_prop_map_put_ = {
		"CoordinatedOption": ((1610743820, LCID, 4, 0),()),
		"IsIncludedInProjectSummary": ((1610743827, LCID, 4, 0),()),
		"IsReference": ((1610743812, LCID, 4, 0),()),
		"Offset": ((1610743814, LCID, 4, 0),()),
		"layoutX": ((1610743816, LCID, 4, 0),()),
		"layoutY": ((1610743818, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPINetworkSites(DispatchBaseClass):
	CLSID = IID('{8B19120E-37DE-43E9-AB2F-9F1743650053}')
	coclass_clsid = IID('{380DA3D4-9F8D-4C74-935B-707EA324270C}')

	# Result is of type ISIAPINetworkSite
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, SiteName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),SiteName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4888B50C-984E-4865-B2CE-4FA9B66C2622}')
		return ret

	# Result is of type ISIAPINetworkSite
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{4888B50C-984E-4865-B2CE-4FA9B66C2622}')
		return ret

	def NetworkSiteExists(self, SiteName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), ((8, 1),),SiteName
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, SiteName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),SiteName
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4888B50C-984E-4865-B2CE-4FA9B66C2622}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4888B50C-984E-4865-B2CE-4FA9B66C2622}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPINetworks(DispatchBaseClass):
	CLSID = IID('{98CE5F37-494C-484F-B8F5-50993C839B3B}')
	coclass_clsid = IID('{19F0570A-094B-4C3E-A770-FFCA0601ADDA}')

	# Result is of type ISIAPINetwork
	def GetNetworkByID(self, Network_id=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743812, LCID, 1, (9, 0), ((3, 1),),Network_id
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNetworkByID', '{C5A62A3D-7D9C-4544-8547-499D4C770332}')
		return ret

	# Result is of type ISIAPINetwork
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, networkname=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),networkname
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C5A62A3D-7D9C-4544-8547-499D4C770332}')
		return ret

	# Result is of type ISIAPINetwork
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{C5A62A3D-7D9C-4544-8547-499D4C770332}')
		return ret

	def NetworkExists(self, networkname=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), ((8, 1),),networkname
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, networkname=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),networkname
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C5A62A3D-7D9C-4544-8547-499D4C770332}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C5A62A3D-7D9C-4544-8547-499D4C770332}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOpposingmovement_ped(DispatchBaseClass):
	CLSID = IID('{1602B72A-4010-4F67-B45D-5C8A493BC687}')
	coclass_clsid = IID('{5AC30B47-D990-41E3-A4E7-A6EB907B1552}')

	_prop_map_get_ = {
		# Method 'Movement_vehicle_od' returns object of type 'ISIAPIMovement_vehicle_od'
		"Movement_vehicle_od": (1610743813, 2, (9, 0), (), "Movement_vehicle_od", '{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}'),
		"Opposing": (1610743811, 2, (11, 0), (), "Opposing", None),
		"Opposingmovement_ped_origin": (1610743809, 2, (3, 0), (), "Opposingmovement_ped_origin", None),
		"Opposingmovement_ped_stage": (1610743810, 2, (3, 0), (), "Opposingmovement_ped_stage", None),
		"Opposingmovement_ped_type": (1610743808, 2, (3, 0), (), "Opposingmovement_ped_type", None),
	}
	_prop_map_put_ = {
		"Opposing": ((1610743811, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOpposingmovement_peds(DispatchBaseClass):
	CLSID = IID('{580C5233-F043-4662-8C1D-2E0C31C568B9}')
	coclass_clsid = IID('{D9E4FBC3-03B6-41E7-A725-5D0300B1D687}')

	# Result is of type ISIAPIOpposingmovement_ped
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, opposing_ped_type=defaultNamedNotOptArg, opposing_ped_origin=defaultNamedNotOptArg, opposin_ped_stage=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1), (3, 1)),opposing_ped_type
			, opposing_ped_origin, opposin_ped_stage)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{1602B72A-4010-4F67-B45D-5C8A493BC687}')
		return ret

	# Result is of type ISIAPIOpposingmovement_ped
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{1602B72A-4010-4F67-B45D-5C8A493BC687}')
		return ret

	def OpposingmovementPedExists(self, opposing_ped_type=defaultNamedNotOptArg, opposing_ped_origin=defaultNamedNotOptArg, opposin_ped_stage=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),opposing_ped_type
			, opposing_ped_origin, opposin_ped_stage)

	_prop_map_get_ = {
		"Count": (1610743811, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, opposing_ped_type=defaultNamedNotOptArg, opposing_ped_origin=defaultNamedNotOptArg, opposin_ped_stage=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1), (3, 1)),opposing_ped_type
			, opposing_ped_origin, opposin_ped_stage)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1602B72A-4010-4F67-B45D-5C8A493BC687}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{1602B72A-4010-4F67-B45D-5C8A493BC687}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743811, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOpposingmovement_vehicle(DispatchBaseClass):
	CLSID = IID('{CDC74ADC-2CF3-49D5-8DC5-3821AC96AA91}')
	coclass_clsid = IID('{99EEB0D9-CD36-4CC6-B8D7-924CE09C963D}')

	_prop_map_get_ = {
		# Method 'Movement_vehicle_od' returns object of type 'ISIAPIMovement_vehicle_od'
		"Movement_vehicle_od": (1610743812, 2, (9, 0), (), "Movement_vehicle_od", '{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}'),
		"Opposing": (1610743810, 2, (11, 0), (), "Opposing", None),
		"Opposingmovement_vehicle_destination": (1610743809, 2, (3, 0), (), "Opposingmovement_vehicle_destination", None),
		"Opposingmovement_vehicle_origin": (1610743808, 2, (3, 0), (), "Opposingmovement_vehicle_origin", None),
	}
	_prop_map_put_ = {
		"Opposing": ((1610743810, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOpposingmovement_vehicles(DispatchBaseClass):
	CLSID = IID('{677C1F98-D3D5-40B3-A5E5-5AEBD3A33CCC}')
	coclass_clsid = IID('{EAEECED7-036B-4734-BCA8-8EF70D134D28}')

	# Result is of type ISIAPIOpposingmovement_vehicle
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, opposing_veh_origin=defaultNamedNotOptArg, opposing_veh_destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),opposing_veh_origin
			, opposing_veh_destination)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CDC74ADC-2CF3-49D5-8DC5-3821AC96AA91}')
		return ret

	# Result is of type ISIAPIOpposingmovement_vehicle
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{CDC74ADC-2CF3-49D5-8DC5-3821AC96AA91}')
		return ret

	def OpposingmovementVehicleExists(self, opposing_veh_origin=defaultNamedNotOptArg, opposing_veh_destination=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), ((3, 1), (3, 1)),opposing_veh_origin
			, opposing_veh_destination)

	_prop_map_get_ = {
		"Count": (1610743811, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, opposing_veh_origin=defaultNamedNotOptArg, opposing_veh_destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),opposing_veh_origin
			, opposing_veh_destination)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CDC74ADC-2CF3-49D5-8DC5-3821AC96AA91}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CDC74ADC-2CF3-49D5-8DC5-3821AC96AA91}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743811, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputAnalysis(DispatchBaseClass):
	CLSID = IID('{91779742-CF41-42AD-963E-22F788CA96F4}')
	coclass_clsid = IID('{2B3CCFD8-4A9C-4A0E-B589-3D1F3A6FFEA1}')

	_prop_map_get_ = {
		"Design_Life_Analysis_status": (1610743809, 2, (3, 0), (), "Design_Life_Analysis_status", None),
		"Design_Life_Selected_future_year": (1610743808, 2, (3, 0), (), "Design_Life_Selected_future_year", None),
		"Flow_Scale_Analysis_status": (1610743811, 2, (3, 0), (), "Flow_Scale_Analysis_status", None),
		"Flow_Scale_Largest_movement_flow_scale": (1610743810, 2, (4, 0), (), "Flow_Scale_Largest_movement_flow_scale", None),
		"Sensitivity_Analysis_status": (1610743813, 2, (3, 0), (), "Sensitivity_Analysis_status", None),
		"Sensitivity_Selected_parameter_scale": (1610743812, 2, (4, 0), (), "Sensitivity_Selected_parameter_scale", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputCirculatingLane(DispatchBaseClass):
	CLSID = IID('{7F03E897-A19D-41C6-A6EA-FECCF36A3358}')
	coclass_clsid = IID('{207A9ACF-CDFD-415C-8D9F-07019F6CF7AB}')

	_prop_map_get_ = {
		"Laneno": (1610743809, 2, (3, 0), (), "Laneno", None),
		"Orientation": (1610743808, 2, (3, 0), (), "Orientation", None),
		# Method 'OutputCirculatingLaneMCs' returns object of type 'ISIAPIOutputCirculatingLaneMCs'
		"OutputCirculatingLaneMCs": (1610743814, 2, (9, 0), (), "OutputCirculatingLaneMCs", '{E3D1A42E-AA21-4472-B566-8EAE73EAB615}'),
		# Method 'OutputLeg' returns object of type 'ISIAPIOutputLeg'
		"OutputLeg": (1610743813, 2, (9, 0), (), "OutputLeg", '{4D03B4B2-FBC7-4EC5-B7D8-984398036302}'),
		"Roucircf_pcu": (1610743811, 2, (4, 0), (), "Roucircf_pcu", None),
		"Roucircf_percent": (1610743812, 2, (4, 0), (), "Roucircf_percent", None),
		"Roucircf_veh": (1610743810, 2, (4, 0), (), "Roucircf_veh", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputCirculatingLaneMC(DispatchBaseClass):
	CLSID = IID('{FA80BAB6-860C-4FA9-841D-3ECB6EA78605}')
	coclass_clsid = IID('{AC1E9E02-F9EB-4AE2-91B7-8E0656BB3918}')

	_prop_map_get_ = {
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
		# Method 'OutputCirculatingLane' returns object of type 'ISIAPIOutputCirculatingLane'
		"OutputCirculatingLane": (1610743812, 2, (9, 0), (), "OutputCirculatingLane", '{7F03E897-A19D-41C6-A6EA-FECCF36A3358}'),
		"Roucircf_pcu": (1610743810, 2, (4, 0), (), "Roucircf_pcu", None),
		"Roucircf_percent": (1610743811, 2, (4, 0), (), "Roucircf_percent", None),
		"Roucircf_veh": (1610743809, 2, (4, 0), (), "Roucircf_veh", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputCirculatingLaneMCs(DispatchBaseClass):
	CLSID = IID('{E3D1A42E-AA21-4472-B566-8EAE73EAB615}')
	coclass_clsid = IID('{FF4EC6A5-5840-4E3D-84E1-86F02CC3F788}')

	# Result is of type ISIAPIOutputCirculatingLaneMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FA80BAB6-860C-4FA9-841D-3ECB6EA78605}')
		return ret

	def MovementClassExists(self, mcClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),mcClass
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FA80BAB6-860C-4FA9-841D-3ECB6EA78605}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{FA80BAB6-860C-4FA9-841D-3ECB6EA78605}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputCirculatingLanes(DispatchBaseClass):
	CLSID = IID('{0FC1F22D-8C53-40A4-B9AB-B8B9D664B8EE}')
	coclass_clsid = IID('{B191000C-58A2-414D-AE1C-4EFC68B3827A}')

	# Result is of type ISIAPIOutputCirculatingLane
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Laneno
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7F03E897-A19D-41C6-A6EA-FECCF36A3358}')
		return ret

	def LaneExists(self, Laneno=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Laneno
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Laneno
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7F03E897-A19D-41C6-A6EA-FECCF36A3358}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{7F03E897-A19D-41C6-A6EA-FECCF36A3358}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputGraphTuple(DispatchBaseClass):
	CLSID = IID('{E69891AB-798F-4534-9C25-8BCD74AF811A}')
	coclass_clsid = IID('{F7AAE6AF-D859-4522-A447-CD18941AE963}')

	_prop_map_get_ = {
		"Arrival_flow_total": (1610743870, 2, (4, 0), (), "Arrival_flow_total", None),
		"Arrival_flow_total_person": (1610743871, 2, (4, 0), (), "Arrival_flow_total_person", None),
		"Capacity_effective": (1610743810, 2, (4, 0), (), "Capacity_effective", None),
		"Carbon_dioxide_total": (1610743825, 2, (4, 0), (), "Carbon_dioxide_total", None),
		"Carbon_monoxide_total": (1610743824, 2, (4, 0), (), "Carbon_monoxide_total", None),
		"Cycle_time": (1610743820, 2, (4, 0), (), "Cycle_time", None),
		"Deg_satn": (1610743811, 2, (4, 0), (), "Deg_satn", None),
		"Deg_satn_ped": (1610743831, 2, (4, 0), (), "Deg_satn_ped", None),
		"Delay_control_average": (1610743813, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_average_ped": (1610743836, 2, (4, 0), (), "Delay_control_average_ped", None),
		"Delay_control_average_veh": (1610743835, 2, (4, 0), (), "Delay_control_average_veh", None),
		"Delay_control_average_worstlane": (1610743837, 2, (4, 0), (), "Delay_control_average_worstlane", None),
		"Delay_control_average_worstmov": (1610743814, 2, (4, 0), (), "Delay_control_average_worstmov", None),
		"Delay_control_average_worstmov_ped": (1610743838, 2, (4, 0), (), "Delay_control_average_worstmov_ped", None),
		"Delay_control_average_worstmov_person": (1610743839, 2, (4, 0), (), "Delay_control_average_worstmov_person", None),
		"Delay_control_total_ped": (1610743833, 2, (4, 0), (), "Delay_control_total_ped", None),
		"Delay_control_total_person": (1610743834, 2, (4, 0), (), "Delay_control_total_person", None),
		"Delay_control_total_veh": (1610743832, 2, (4, 0), (), "Delay_control_total_veh", None),
		"Delay_geometric_average": (1610743840, 2, (4, 0), (), "Delay_geometric_average", None),
		"Delay_stopline_average": (1610743841, 2, (4, 0), (), "Delay_stopline_average", None),
		"Demand_flow_total": (1610743809, 2, (4, 0), (), "Demand_flow_total", None),
		"Demand_flow_total_ped": (1610743828, 2, (4, 0), (), "Demand_flow_total_ped", None),
		"Demand_flow_total_person": (1610743829, 2, (4, 0), (), "Demand_flow_total_person", None),
		"Fuel_consumption_total": (1610743821, 2, (4, 0), (), "Fuel_consumption_total", None),
		"Hydrocarbons_total": (1610743822, 2, (4, 0), (), "Hydrocarbons_total", None),
		"Level_of_service": (1610743873, 2, (3, 0), (), "Level_of_service", None),
		"Level_of_service_ped": (1610743843, 2, (3, 0), (), "Level_of_service_ped", None),
		"Level_of_service_veh": (1610743842, 2, (3, 0), (), "Level_of_service_veh", None),
		"Nox_total": (1610743823, 2, (4, 0), (), "Nox_total", None),
		"Operating_cost_total": (1610743826, 2, (4, 0), (), "Operating_cost_total", None),
		"Operating_cost_total_ped": (1610743869, 2, (4, 0), (), "Operating_cost_total_ped", None),
		"Operating_cost_total_veh": (1610743868, 2, (4, 0), (), "Operating_cost_total_veh", None),
		"Perc_heavy_veh": (1610743830, 2, (4, 0), (), "Perc_heavy_veh", None),
		"Performance_index": (1610743818, 2, (4, 0), (), "Performance_index", None),
		"Performance_index_ped": (1610743853, 2, (4, 0), (), "Performance_index_ped", None),
		"Performance_index_veh": (1610743852, 2, (4, 0), (), "Performance_index_veh", None),
		"Practical_spare_capacity": (1610743812, 2, (4, 0), (), "Practical_spare_capacity", None),
		"Prop_queued_ped": (1610743850, 2, (4, 0), (), "Prop_queued_ped", None),
		"Prop_queued_person": (1610743851, 2, (4, 0), (), "Prop_queued_person", None),
		"Prop_queued_veh": (1610743849, 2, (4, 0), (), "Prop_queued_veh", None),
		"Queue_dist_maxback_percentile": (1610743817, 2, (4, 0), (), "Queue_dist_maxback_percentile", None),
		"Queue_maxback_percentile": (1610743816, 2, (4, 0), (), "Queue_maxback_percentile", None),
		"SpeedEfficiency": (1610743872, 2, (4, 0), (), "SpeedEfficiency", None),
		"Stop_rate": (1610743815, 2, (4, 0), (), "Stop_rate", None),
		"Stop_rate_ped": (1610743848, 2, (4, 0), (), "Stop_rate_ped", None),
		"Stop_rate_veh": (1610743847, 2, (4, 0), (), "Stop_rate_veh", None),
		"Total_stops_ped": (1610743845, 2, (4, 0), (), "Total_stops_ped", None),
		"Total_stops_person": (1610743846, 2, (4, 0), (), "Total_stops_person", None),
		"Total_stops_veh": (1610743844, 2, (4, 0), (), "Total_stops_veh", None),
		"Travel_dist_av_ped": (1610743858, 2, (4, 0), (), "Travel_dist_av_ped", None),
		"Travel_dist_av_person": (1610743859, 2, (4, 0), (), "Travel_dist_av_person", None),
		"Travel_dist_av_veh": (1610743857, 2, (4, 0), (), "Travel_dist_av_veh", None),
		"Travel_dist_total_ped": (1610743855, 2, (4, 0), (), "Travel_dist_total_ped", None),
		"Travel_dist_total_person": (1610743856, 2, (4, 0), (), "Travel_dist_total_person", None),
		"Travel_dist_total_veh": (1610743854, 2, (4, 0), (), "Travel_dist_total_veh", None),
		"Travel_speed": (1610743819, 2, (4, 0), (), "Travel_speed", None),
		"Travel_speed_ped": (1610743866, 2, (4, 0), (), "Travel_speed_ped", None),
		"Travel_speed_person": (1610743867, 2, (4, 0), (), "Travel_speed_person", None),
		"Travel_time_av_ped": (1610743864, 2, (4, 0), (), "Travel_time_av_ped", None),
		"Travel_time_av_person": (1610743865, 2, (4, 0), (), "Travel_time_av_person", None),
		"Travel_time_av_veh": (1610743863, 2, (4, 0), (), "Travel_time_av_veh", None),
		"Travel_time_total_ped": (1610743861, 2, (4, 0), (), "Travel_time_total_ped", None),
		"Travel_time_total_person": (1610743862, 2, (4, 0), (), "Travel_time_total_person", None),
		"Travel_time_total_veh": (1610743860, 2, (4, 0), (), "Travel_time_total_veh", None),
		"Unsettled": (1610743827, 2, (11, 0), (), "Unsettled", None),
		"X_value": (1610743808, 2, (4, 0), (), "X_value", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputGraphTuples(DispatchBaseClass):
	CLSID = IID('{3E26EBE1-0955-49EB-8E9F-8CC3B645361B}')
	coclass_clsid = IID('{8177D1E3-5454-4BB5-AE18-D7147D4C8A35}')

	# Result is of type ISIAPIOutputGraphTuple
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E69891AB-798F-4534-9C25-8BCD74AF811A}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E69891AB-798F-4534-9C25-8BCD74AF811A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E69891AB-798F-4534-9C25-8BCD74AF811A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputLane(DispatchBaseClass):
	CLSID = IID('{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}')
	coclass_clsid = IID('{F51F3BC3-A54E-4748-9886-5D4F3C30D4F0}')

	_prop_map_get_ = {
		"Adjfactor_buses": (1610743915, 2, (4, 0), (), "Adjfactor_buses", None),
		"Adjfactor_flowscale": (1610743916, 2, (4, 0), (), "Adjfactor_flowscale", None),
		"Adjfactor_grade": (1610743913, 2, (4, 0), (), "Adjfactor_grade", None),
		"Adjfactor_lanewidth": (1610743912, 2, (4, 0), (), "Adjfactor_lanewidth", None),
		"Adjfactor_parking": (1610743914, 2, (4, 0), (), "Adjfactor_parking", None),
		"Adjfactor_trafficflow": (1610743917, 2, (4, 0), (), "Adjfactor_trafficflow", None),
		"Arrival_flow_flag": (1610743901, 2, (3, 0), (), "Arrival_flow_flag", None),
		"Average_queue_space": (1610743868, 2, (4, 0), (), "Average_queue_space", None),
		"Avg_num_of_cycles_to_depart": (1610743909, 2, (4, 0), (), "Avg_num_of_cycles_to_depart", None),
		"Avg_veh_length": (1610743940, 2, (4, 0), (), "Avg_veh_length", None),
		"Calc_mf_flag": (1610743890, 2, (3, 0), (), "Calc_mf_flag", None),
		"Capacity": (1610743810, 2, (4, 0), (), "Capacity", None),
		"Capacity_adj": (1610743871, 2, (4, 0), (), "Capacity_adj", None),
		"Capacity_adj_flag": (1610743872, 2, (3, 0), (), "Capacity_adj_flag", None),
		"Capacity_end_deps": (1610743811, 2, (4, 0), (), "Capacity_end_deps", None),
		"Capacity_min": (1610743812, 2, (4, 0), (), "Capacity_min", None),
		"Capacity_shortlane_affected": (1610743855, 2, (11, 0), (), "Capacity_shortlane_affected", None),
		"CongestionCoefficient": (1610743932, 2, (4, 0), (), "CongestionCoefficient", None),
		"Contlane_affect_by_adjshortlane": (1610743920, 2, (3, 0), (), "Contlane_affect_by_adjshortlane", None),
		"Control_type": (1610743919, 2, (3, 0), (), "Control_type", None),
		"Cum_storage_space": (1610743945, 2, (4, 0), (), "Cum_storage_space", None),
		"Deg_satn": (1610743857, 2, (4, 0), (), "Deg_satn", None),
		"Delay_acc_dec_dn": (1610743858, 2, (4, 0), (), "Delay_acc_dec_dn", None),
		"Delay_ctrl": (1610743813, 2, (4, 0), (), "Delay_ctrl", None),
		"Delay_geo": (1610743814, 2, (4, 0), (), "Delay_geo", None),
		"Delay_idle": (1610743815, 2, (4, 0), (), "Delay_idle", None),
		"Delay_model_1": (1610743816, 2, (4, 0), (), "Delay_model_1", None),
		"Delay_model_2": (1610743817, 2, (4, 0), (), "Delay_model_2", None),
		"Delay_n": (1610743818, 2, (4, 0), (), "Delay_n", None),
		"Delay_q": (1610743819, 2, (4, 0), (), "Delay_q", None),
		"Delay_queue_moveup": (1610743859, 2, (4, 0), (), "Delay_queue_moveup", None),
		"Density": (1610743935, 2, (4, 0), (), "Density", None),
		"Density_pcu": (1610743949, 2, (4, 0), (), "Density_pcu", None),
		"Driver_response_time": (1610743869, 2, (4, 0), (), "Driver_response_time", None),
		"Equivalent_AT": (1610743918, 2, (3, 0), (), "Equivalent_AT", None),
		"Flag_na": (1610743863, 2, (3, 0), (), "Flag_na", None),
		"Flow_HV": (1610743822, 2, (4, 0), (), "Flow_HV", None),
		"Flow_HV_capconstr": (1610743826, 2, (4, 0), (), "Flow_HV_capconstr", None),
		"Flow_HV_pct": (1610743823, 2, (4, 0), (), "Flow_HV_pct", None),
		"Flow_HV_pct_capconstr": (1610743827, 2, (4, 0), (), "Flow_HV_pct_capconstr", None),
		"Flow_LV": (1610743821, 2, (4, 0), (), "Flow_LV", None),
		"Flow_LV_capconstr": (1610743825, 2, (4, 0), (), "Flow_LV_capconstr", None),
		"Flow_total": (1610743820, 2, (4, 0), (), "Flow_total", None),
		"Flow_total_capconstr": (1610743824, 2, (4, 0), (), "Flow_total_capconstr", None),
		"Gap_accept_blocked_time": (1610743924, 2, (4, 0), (), "Gap_accept_blocked_time", None),
		"Gap_accept_cycle_time": (1610743923, 2, (4, 0), (), "Gap_accept_cycle_time", None),
		"Gap_accept_unblocked_time": (1610743925, 2, (4, 0), (), "Gap_accept_unblocked_time", None),
		"Green_periods": (1610743892, 2, (3, 0), (), "Green_periods", None),
		"Headway": (1610743937, 2, (4, 0), (), "Headway", None),
		"Headway_scats_mf": (1610743887, 2, (4, 0), (), "Headway_scats_mf", None),
		"Initial_demand_vol": (1610743908, 2, (4, 0), (), "Initial_demand_vol", None),
		"Initial_demand_vol_clear_time": (1610743879, 2, (4, 0), (), "Initial_demand_vol_clear_time", None),
		"Is_dominant": (1610743870, 2, (11, 0), (), "Is_dominant", None),
		"Is_nw_connected": (1610743898, 2, (11, 0), (), "Is_nw_connected", None),
		"LOS_density": (1610743948, 2, (3, 0), (), "LOS_density", None),
		"Lane_block_adj": (1610743877, 2, (4, 0), (), "Lane_block_adj", None),
		"Lane_change_from_left": (1610743894, 2, (4, 0), (), "Lane_change_from_left", None),
		"Lane_change_from_right": (1610743896, 2, (4, 0), (), "Lane_change_from_right", None),
		"Lane_change_to_left": (1610743895, 2, (4, 0), (), "Lane_change_to_left", None),
		"Lane_change_to_right": (1610743897, 2, (4, 0), (), "Lane_change_to_right", None),
		"Laneno": (1610743809, 2, (3, 0), (), "Laneno", None),
		"Level_of_service": (1610743854, 2, (8, 0), (), "Level_of_service", None),
		"Minimum_delay": (1610743926, 2, (4, 0), (), "Minimum_delay", None),
		"Net_inflow": (1610743899, 2, (4, 0), (), "Net_inflow", None),
		"Net_inflow_capconstr": (1610743900, 2, (4, 0), (), "Net_inflow_capconstr", None),
		"Net_outflow": (1610743927, 2, (4, 0), (), "Net_outflow", None),
		"Net_outflow_capconstr": (1610743928, 2, (4, 0), (), "Net_outflow_capconstr", None),
		"Occupancy_scats_mf": (1610743888, 2, (4, 0), (), "Occupancy_scats_mf", None),
		"Occupancy_time": (1610743938, 2, (4, 0), (), "Occupancy_time", None),
		"Opposing_ped_factor": (1610743921, 2, (4, 0), (), "Opposing_ped_factor", None),
		"Orientation": (1610743808, 2, (3, 0), (), "Orientation", None),
		# Method 'OutputLaneGreenPeriods' returns object of type 'ISIAPIOutputLaneGreenPeriods'
		"OutputLaneGreenPeriods": (1610743874, 2, (9, 0), (), "OutputLaneGreenPeriods", '{472D3454-925A-442D-8498-E4A01EF86C20}'),
		# Method 'OutputLaneMCs' returns object of type 'ISIAPIOutputLaneMCs'
		"OutputLaneMCs": (1610743876, 2, (9, 0), (), "OutputLaneMCs", '{A04D1E92-C344-4E0E-850A-1B97D38BD7B8}'),
		# Method 'OutputLaneODs' returns object of type 'ISIAPIOutputLaneODs'
		"OutputLaneODs": (1610743873, 2, (9, 0), (), "OutputLaneODs", '{83C46DBA-91A4-4A1F-9EC4-7ECEB223C6DA}'),
		# Method 'OutputLeg' returns object of type 'ISIAPIOutputLeg'
		"OutputLeg": (1610743875, 2, (9, 0), (), "OutputLeg", '{4D03B4B2-FBC7-4EC5-B7D8-984398036302}'),
		"Oversatn_duration": (1610743881, 2, (4, 0), (), "Oversatn_duration", None),
		"Perc_arriving_during_green": (1610743883, 2, (4, 0), (), "Perc_arriving_during_green", None),
		"Platoon_ratio": (1610743884, 2, (4, 0), (), "Platoon_ratio", None),
		"Prob_blockage": (1610743829, 2, (4, 0), (), "Prob_blockage", None),
		"Prob_shortlane_overflow": (1610743910, 2, (4, 0), (), "Prob_shortlane_overflow", None),
		"Progression_factor_delay": (1610743885, 2, (4, 0), (), "Progression_factor_delay", None),
		"Progression_factor_queue": (1610743886, 2, (4, 0), (), "Progression_factor_queue", None),
		"Prop_queued": (1610743828, 2, (4, 0), (), "Prop_queued", None),
		"Queue_constraint_flag": (1610743891, 2, (3, 0), (), "Queue_constraint_flag", None),
		"Queue_cycav_1": (1610743831, 2, (4, 0), (), "Queue_cycav_1", None),
		"Queue_cycav_2": (1610743832, 2, (4, 0), (), "Queue_cycav_2", None),
		"Queue_cycav_mean": (1610743833, 2, (4, 0), (), "Queue_cycav_mean", None),
		"Queue_cycav_percentile": (1610743834, 2, (4, 0), (), "Queue_cycav_percentile", None),
		"Queue_dist_cycav_mean": (1610743904, 2, (4, 0), (), "Queue_dist_cycav_mean", None),
		"Queue_dist_cycav_percentile": (1610743905, 2, (4, 0), (), "Queue_dist_cycav_percentile", None),
		"Queue_dist_greenstart_mean": (1610743906, 2, (4, 0), (), "Queue_dist_greenstart_mean", None),
		"Queue_dist_greenstart_percentile": (1610743907, 2, (4, 0), (), "Queue_dist_greenstart_percentile", None),
		"Queue_dist_maxback_mean": (1610743839, 2, (4, 0), (), "Queue_dist_maxback_mean", None),
		"Queue_dist_maxback_percentile": (1610743840, 2, (4, 0), (), "Queue_dist_maxback_percentile", None),
		"Queue_dist_overflow": (1610743929, 2, (4, 0), (), "Queue_dist_overflow", None),
		"Queue_greenstart_mean": (1610743902, 2, (4, 0), (), "Queue_greenstart_mean", None),
		"Queue_greenstart_percentile": (1610743903, 2, (4, 0), (), "Queue_greenstart_percentile", None),
		"Queue_maxback_1": (1610743835, 2, (4, 0), (), "Queue_maxback_1", None),
		"Queue_maxback_2": (1610743836, 2, (4, 0), (), "Queue_maxback_2", None),
		"Queue_maxback_mean": (1610743837, 2, (4, 0), (), "Queue_maxback_mean", None),
		"Queue_maxback_mean_flag": (1610743946, 2, (3, 0), (), "Queue_maxback_mean_flag", None),
		"Queue_maxback_percentile": (1610743838, 2, (4, 0), (), "Queue_maxback_percentile", None),
		"Queue_maxback_percentile_flag": (1610743947, 2, (3, 0), (), "Queue_maxback_percentile_flag", None),
		"Queue_overflow": (1610743841, 2, (4, 0), (), "Queue_overflow", None),
		"Queue_space": (1610743830, 2, (4, 0), (), "Queue_space", None),
		"Queue_storage_ratio_avg": (1610743861, 2, (4, 0), (), "Queue_storage_ratio_avg", None),
		"Queue_storage_ratio_percentile": (1610743860, 2, (4, 0), (), "Queue_storage_ratio_percentile", None),
		"Queue_unrestr_mean": (1610743944, 2, (4, 0), (), "Queue_unrestr_mean", None),
		"Residual_demand_vol": (1610743878, 2, (4, 0), (), "Residual_demand_vol", None),
		"Residual_demand_vol_clear_time": (1610743880, 2, (4, 0), (), "Residual_demand_vol_clear_time", None),
		"Satflow_basic": (1610743842, 2, (4, 0), (), "Satflow_basic", None),
		"Satflow_basic_adj": (1610743911, 2, (4, 0), (), "Satflow_basic_adj", None),
		"Satflow_scats": (1610743843, 2, (4, 0), (), "Satflow_scats", None),
		"Satflow_scats_mf": (1610743844, 2, (4, 0), (), "Satflow_scats_mf", None),
		"Satn_flow": (1610743865, 2, (4, 0), (), "Satn_flow", None),
		"Satn_headway": (1610743866, 2, (4, 0), (), "Satn_headway", None),
		"Satn_spacing": (1610743867, 2, (4, 0), (), "Satn_spacing", None),
		"Satn_speed": (1610743864, 2, (4, 0), (), "Satn_speed", None),
		"Shortlane_flow_moved": (1610743845, 2, (11, 0), (), "Shortlane_flow_moved", None),
		"Space_occupancy_ratio": (1610743941, 2, (4, 0), (), "Space_occupancy_ratio", None),
		"Space_scats_mf": (1610743889, 2, (4, 0), (), "Space_scats_mf", None),
		"Space_time": (1610743939, 2, (4, 0), (), "Space_time", None),
		"Spacing": (1610743936, 2, (4, 0), (), "Spacing", None),
		"SpeedEfficiency": (1610743930, 2, (4, 0), (), "SpeedEfficiency", None),
		"SpeedEfficiencyFlag": (1610743931, 2, (3, 0), (), "SpeedEfficiencyFlag", None),
		"Stop_rate": (1610743882, 2, (4, 0), (), "Stop_rate", None),
		"Stoprate_1": (1610743846, 2, (4, 0), (), "Stoprate_1", None),
		"Stoprate_2": (1610743847, 2, (4, 0), (), "Stoprate_2", None),
		"Stoprate_geo": (1610743848, 2, (4, 0), (), "Stoprate_geo", None),
		"Stoprate_overall": (1610743849, 2, (4, 0), (), "Stoprate_overall", None),
		"Stoprate_qmovup": (1610743850, 2, (4, 0), (), "Stoprate_qmovup", None),
		"T2_reduced": (1610743851, 2, (11, 0), (), "T2_reduced", None),
		"Time_occupancy_ratio": (1610743942, 2, (4, 0), (), "Time_occupancy_ratio", None),
		"Total_stops": (1610743862, 2, (4, 0), (), "Total_stops", None),
		"TravelTimeIndex": (1610743933, 2, (4, 0), (), "TravelTimeIndex", None),
		"Unblocked_time_ratio": (1610743922, 2, (4, 0), (), "Unblocked_time_ratio", None),
		"Underutil_flag": (1610743852, 2, (3, 0), (), "Underutil_flag", None),
		"Uninterrupted_speed": (1610743934, 2, (4, 0), (), "Uninterrupted_speed", None),
		"Uninterrupted_travel_delay": (1610743943, 2, (4, 0), (), "Uninterrupted_travel_delay", None),
		"Upstr_flow_after_exit_sl": (1610743893, 2, (4, 0), (), "Upstr_flow_after_exit_sl", None),
		"Util_factor": (1610743853, 2, (4, 0), (), "Util_factor", None),
		"X1_flag": (1610743856, 2, (3, 0), (), "X1_flag", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputLaneExit(DispatchBaseClass):
	CLSID = IID('{00351D05-37F3-4949-BC7C-186B4F6231E7}')
	coclass_clsid = IID('{BF2C2275-C235-40CF-A2AB-54A9C372C1D9}')

	_prop_map_get_ = {
		"Capacity_ml": (1610743827, 2, (4, 0), (), "Capacity_ml", None),
		"Capacity_sl": (1610743818, 2, (4, 0), (), "Capacity_sl", None),
		"Critical_gap_ml": (1610743824, 2, (4, 0), (), "Critical_gap_ml", None),
		"Critical_gap_sl": (1610743815, 2, (4, 0), (), "Critical_gap_sl", None),
		"Deg_satn_ml": (1610743828, 2, (4, 0), (), "Deg_satn_ml", None),
		"Deg_satn_sl": (1610743819, 2, (4, 0), (), "Deg_satn_sl", None),
		"Flow": (1610743810, 2, (4, 0), (), "Flow", None),
		"Flow_capconstr": (1610743811, 2, (4, 0), (), "Flow_capconstr", None),
		"Followup_headway_ml": (1610743825, 2, (4, 0), (), "Followup_headway_ml", None),
		"Followup_headway_sl": (1610743816, 2, (4, 0), (), "Followup_headway_sl", None),
		"Lane_flow_rate_ml": (1610743826, 2, (4, 0), (), "Lane_flow_rate_ml", None),
		"Lane_flow_rate_sl": (1610743817, 2, (4, 0), (), "Lane_flow_rate_sl", None),
		"Laneno": (1610743809, 2, (3, 0), (), "Laneno", None),
		"Merge_analysis_applied": (1610743812, 2, (11, 0), (), "Merge_analysis_applied", None),
		"Merge_delay_ml": (1610743830, 2, (4, 0), (), "Merge_delay_ml", None),
		"Merge_delay_sl": (1610743821, 2, (4, 0), (), "Merge_delay_sl", None),
		"Min_delay_ml": (1610743829, 2, (4, 0), (), "Min_delay_ml", None),
		"Min_delay_sl": (1610743820, 2, (4, 0), (), "Min_delay_sl", None),
		"Opposing_flow_rate_pcu_ml": (1610743823, 2, (4, 0), (), "Opposing_flow_rate_pcu_ml", None),
		"Opposing_flow_rate_pcu_sl": (1610743814, 2, (4, 0), (), "Opposing_flow_rate_pcu_sl", None),
		"Opposing_flow_rate_veh_ml": (1610743822, 2, (4, 0), (), "Opposing_flow_rate_veh_ml", None),
		"Opposing_flow_rate_veh_sl": (1610743813, 2, (4, 0), (), "Opposing_flow_rate_veh_sl", None),
		"Orientation": (1610743808, 2, (3, 0), (), "Orientation", None),
		# Method 'OutputLeg' returns object of type 'ISIAPIOutputLeg'
		"OutputLeg": (1610743831, 2, (9, 0), (), "OutputLeg", '{4D03B4B2-FBC7-4EC5-B7D8-984398036302}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputLaneExits(DispatchBaseClass):
	CLSID = IID('{91DFAD2B-DD5C-40FE-B5DB-B4C40175952C}')
	coclass_clsid = IID('{DEBB105B-76D0-4FD5-A113-447035DC51FC}')

	# Result is of type ISIAPIOutputLaneExit
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Laneno
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{00351D05-37F3-4949-BC7C-186B4F6231E7}')
		return ret

	def LaneExists(self, Laneno=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Laneno
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Laneno
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{00351D05-37F3-4949-BC7C-186B4F6231E7}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{00351D05-37F3-4949-BC7C-186B4F6231E7}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputLaneGreenPeriod(DispatchBaseClass):
	CLSID = IID('{2A8E738C-3173-41EB-A45C-AEDD77B5D649}')
	coclass_clsid = IID('{1E733D74-F977-426E-93F7-2A8BF1454878}')

	_prop_map_get_ = {
		"Capacity": (1610743809, 2, (4, 0), (), "Capacity", None),
		"Depflow_gt_adjsatn": (1610743827, 2, (3, 0), (), "Depflow_gt_adjsatn", None),
		"Eff_green_end": (1610743819, 2, (3, 0), (), "Eff_green_end", None),
		"Eff_green_start": (1610743817, 2, (3, 0), (), "Eff_green_start", None),
		"End_sat_green": (1610743818, 2, (3, 0), (), "End_sat_green", None),
		"Flow_ratio": (1610743823, 2, (4, 0), (), "Flow_ratio", None),
		"Green_end_time": (1610743811, 2, (3, 0), (), "Green_end_time", None),
		"Green_ratio": (1610743824, 2, (4, 0), (), "Green_ratio", None),
		"Green_satn_time": (1610743820, 2, (4, 0), (), "Green_satn_time", None),
		"Green_start_time": (1610743810, 2, (3, 0), (), "Green_start_time", None),
		"Greenperiod": (1610743808, 2, (3, 0), (), "Greenperiod", None),
		# Method 'OutputLane' returns object of type 'ISIAPIOutputLane'
		"OutputLane": (1610743828, 2, (9, 0), (), "OutputLane", '{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}'),
		"Queclearance_time": (1610743821, 2, (4, 0), (), "Queclearance_time", None),
		"Queue_discharge_rate": (1610743826, 2, (4, 0), (), "Queue_discharge_rate", None),
		"Residual_queue": (1610743822, 2, (4, 0), (), "Residual_queue", None),
		"Satflow_full": (1610743812, 2, (4, 0), (), "Satflow_full", None),
		"Satflow_laneblock_adj": (1610743814, 2, (4, 0), (), "Satflow_laneblock_adj", None),
		"Satflow_queuecleartime_adj": (1610743815, 2, (4, 0), (), "Satflow_queuecleartime_adj", None),
		"Satflow_reduced": (1610743813, 2, (4, 0), (), "Satflow_reduced", None),
		"Shortlane_effect": (1610743816, 2, (11, 0), (), "Shortlane_effect", None),
		"Subcycle": (1610743825, 2, (3, 0), (), "Subcycle", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputLaneGreenPeriods(DispatchBaseClass):
	CLSID = IID('{472D3454-925A-442D-8498-E4A01EF86C20}')
	coclass_clsid = IID('{2FF0DB72-0FE3-4A4D-B5CF-904BB39595AA}')

	def GreenPeriodExists(self, Greenperiod=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Greenperiod
			)

	# Result is of type ISIAPIOutputLaneGreenPeriod
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Greenperiod=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Greenperiod
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{2A8E738C-3173-41EB-A45C-AEDD77B5D649}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Greenperiod=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Greenperiod
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{2A8E738C-3173-41EB-A45C-AEDD77B5D649}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{2A8E738C-3173-41EB-A45C-AEDD77B5D649}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputLaneMC(DispatchBaseClass):
	CLSID = IID('{96DB0ABD-FA20-4F9D-B2C8-4441009B4B88}')
	coclass_clsid = IID('{AD35D08C-C0AF-4D8F-9B88-751892BB25E3}')

	_prop_map_get_ = {
		"Arrival_flow_flag": (1610743821, 2, (3, 0), (), "Arrival_flow_flag", None),
		"Calc_exists": (1610743809, 2, (11, 0), (), "Calc_exists", None),
		"Exist_in_nw_upstream_only": (1610743817, 2, (11, 0), (), "Exist_in_nw_upstream_only", None),
		"Flow_total": (1610743810, 2, (4, 0), (), "Flow_total", None),
		"Flow_total_capconstr": (1610743811, 2, (4, 0), (), "Flow_total_capconstr", None),
		"Lane_change_from_left": (1610743813, 2, (4, 0), (), "Lane_change_from_left", None),
		"Lane_change_from_right": (1610743815, 2, (4, 0), (), "Lane_change_from_right", None),
		"Lane_change_to_left": (1610743814, 2, (4, 0), (), "Lane_change_to_left", None),
		"Lane_change_to_right": (1610743816, 2, (4, 0), (), "Lane_change_to_right", None),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
		"Net_inflow": (1610743818, 2, (4, 0), (), "Net_inflow", None),
		"Net_inflow_capconstr": (1610743819, 2, (4, 0), (), "Net_inflow_capconstr", None),
		# Method 'OutputLane' returns object of type 'ISIAPIOutputLane'
		"OutputLane": (1610743820, 2, (9, 0), (), "OutputLane", '{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}'),
		"Upstr_flow_after_exit_sl": (1610743812, 2, (4, 0), (), "Upstr_flow_after_exit_sl", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputLaneMCs(DispatchBaseClass):
	CLSID = IID('{A04D1E92-C344-4E0E-850A-1B97D38BD7B8}')
	coclass_clsid = IID('{1FBBD5AB-E682-4C06-BEFC-6EDB64D3666A}')

	# Result is of type ISIAPIOutputLaneMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{96DB0ABD-FA20-4F9D-B2C8-4441009B4B88}')
		return ret

	def MovementClassExists(self, mcClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),mcClass
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{96DB0ABD-FA20-4F9D-B2C8-4441009B4B88}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{96DB0ABD-FA20-4F9D-B2C8-4441009B4B88}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputLaneOD(DispatchBaseClass):
	CLSID = IID('{BD4E1996-A933-4CEA-A1FD-9B0C7B81E9F3}')
	coclass_clsid = IID('{B378D9C3-4E9D-4819-8762-BD68819E5CB2}')

	_prop_map_get_ = {
		"Arrival_flow_flag": (1610743840, 2, (3, 0), (), "Arrival_flow_flag", None),
		"Average_speed": (1610743827, 2, (4, 0), (), "Average_speed", None),
		"Average_speed_flag": (1610743834, 2, (3, 0), (), "Average_speed_flag", None),
		"Calc_exists": (1610743816, 2, (11, 0), (), "Calc_exists", None),
		"Cap_constraint_effect": (1610743825, 2, (3, 0), (), "Cap_constraint_effect", None),
		"Crit_gap": (1610743809, 2, (4, 0), (), "Crit_gap", None),
		"Crit_gap_flag": (1610743836, 2, (3, 0), (), "Crit_gap_flag", None),
		"Critical_spacing": (1610743817, 2, (4, 0), (), "Critical_spacing", None),
		"Destination": (1610743808, 2, (3, 0), (), "Destination", None),
		"Flow": (1610743811, 2, (4, 0), (), "Flow", None),
		"Flow_capconstr": (1610743812, 2, (4, 0), (), "Flow_capconstr", None),
		"Foll_up_hdwy": (1610743810, 2, (4, 0), (), "Foll_up_hdwy", None),
		"Foll_up_hdwy_flag": (1610743837, 2, (3, 0), (), "Foll_up_hdwy_flag", None),
		"Gap_accept_blocked_time": (1610743843, 2, (4, 0), (), "Gap_accept_blocked_time", None),
		"Gap_accept_cycle_time": (1610743842, 2, (4, 0), (), "Gap_accept_cycle_time", None),
		"Gap_accept_unblocked_time": (1610743844, 2, (4, 0), (), "Gap_accept_unblocked_time", None),
		"HVE_for_entry": (1610743832, 2, (4, 0), (), "HVE_for_entry", None),
		"HVE_pcu": (1610743820, 2, (4, 0), (), "HVE_pcu", None),
		"Intrabunch_headway": (1610743830, 2, (4, 0), (), "Intrabunch_headway", None),
		"Intrabunch_headway_flag": (1610743835, 2, (3, 0), (), "Intrabunch_headway_flag", None),
		"Lane_output_type": (1610743818, 2, (3, 0), (), "Lane_output_type", None),
		"Minimum_delay": (1610743845, 2, (4, 0), (), "Minimum_delay", None),
		"OD_factor": (1610743826, 2, (4, 0), (), "OD_factor", None),
		"OD_factor_flag": (1610743833, 2, (3, 0), (), "OD_factor_flag", None),
		"Opposing_flow": (1610743819, 2, (4, 0), (), "Opposing_flow", None),
		"Opposing_flow_flag": (1610743838, 2, (3, 0), (), "Opposing_flow_flag", None),
		"Opposing_flow_pcu": (1610743821, 2, (4, 0), (), "Opposing_flow_pcu", None),
		"Opposing_flow_ped": (1610743822, 2, (4, 0), (), "Opposing_flow_ped", None),
		"Opposing_flow_ped_flag": (1610743839, 2, (3, 0), (), "Opposing_flow_ped_flag", None),
		# Method 'OutputLane' returns object of type 'ISIAPIOutputLane'
		"OutputLane": (1610743814, 2, (9, 0), (), "OutputLane", '{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}'),
		# Method 'OutputLaneODMCs' returns object of type 'ISIAPIOutputLaneODMCs'
		"OutputLaneODMCs": (1610743815, 2, (9, 0), (), "OutputLaneODMCs", '{8B1F140D-9817-413B-9AE1-7BF9777B4EB8}'),
		"Percent_exit_flow_incl": (1610743824, 2, (4, 0), (), "Percent_exit_flow_incl", None),
		"Percent_nearest_lane_only": (1610743823, 2, (4, 0), (), "Percent_nearest_lane_only", None),
		"Priority_sharing_flag": (1610743831, 2, (3, 0), (), "Priority_sharing_flag", None),
		"Proportion_bunched": (1610743829, 2, (4, 0), (), "Proportion_bunched", None),
		"Proportion_bunched_flag": (1610743828, 2, (3, 0), (), "Proportion_bunched_flag", None),
		"Subdom_eq_dom": (1610743813, 2, (11, 0), (), "Subdom_eq_dom", None),
		"Unblocked_time_ratio": (1610743841, 2, (4, 0), (), "Unblocked_time_ratio", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputLaneODMC(DispatchBaseClass):
	CLSID = IID('{BD6E29F3-4E14-4A9C-AA40-65954AB6BE78}')
	coclass_clsid = IID('{4F4B3FF2-23D4-4461-AACB-6E2F84E31DC0}')

	_prop_map_get_ = {
		"Arrival_flow_flag": (1610743819, 2, (3, 0), (), "Arrival_flow_flag", None),
		"Calc_exists": (1610743809, 2, (11, 0), (), "Calc_exists", None),
		"Flow": (1610743810, 2, (4, 0), (), "Flow", None),
		"Flow_capconstr": (1610743811, 2, (4, 0), (), "Flow_capconstr", None),
		"Gap_accept_blocked_time": (1610743817, 2, (4, 0), (), "Gap_accept_blocked_time", None),
		"Gap_accept_cycle_time": (1610743816, 2, (4, 0), (), "Gap_accept_cycle_time", None),
		"Gap_accept_unblocked_time": (1610743818, 2, (4, 0), (), "Gap_accept_unblocked_time", None),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
		"Minimum_delay": (1610743820, 2, (4, 0), (), "Minimum_delay", None),
		# Method 'OutputLaneOD' returns object of type 'ISIAPIOutputLaneOD'
		"OutputLaneOD": (1610743814, 2, (9, 0), (), "OutputLaneOD", '{BD4E1996-A933-4CEA-A1FD-9B0C7B81E9F3}'),
		"Shortlane_overflow": (1610743812, 2, (11, 0), (), "Shortlane_overflow", None),
		"Sl_overflow": (1610743813, 2, (4, 0), (), "Sl_overflow", None),
		"Unblocked_time_ratio": (1610743815, 2, (4, 0), (), "Unblocked_time_ratio", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputLaneODMCs(DispatchBaseClass):
	CLSID = IID('{8B1F140D-9817-413B-9AE1-7BF9777B4EB8}')
	coclass_clsid = IID('{BA8AE905-D5B8-4CAB-B5F4-FCA3F78E9E63}')

	# Result is of type ISIAPIOutputLaneODMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{BD6E29F3-4E14-4A9C-AA40-65954AB6BE78}')
		return ret

	def MovementClassExists(self, mcClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),mcClass
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{BD6E29F3-4E14-4A9C-AA40-65954AB6BE78}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{BD6E29F3-4E14-4A9C-AA40-65954AB6BE78}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputLaneODs(DispatchBaseClass):
	CLSID = IID('{83C46DBA-91A4-4A1F-9EC4-7ECEB223C6DA}')
	coclass_clsid = IID('{AF3C822E-8BAC-4DA0-819B-9312B69AD052}')

	# Result is of type ISIAPIOutputLaneOD
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Destination
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{BD4E1996-A933-4CEA-A1FD-9B0C7B81E9F3}')
		return ret

	def LaneODExists(self, Destination=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Destination
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Destination
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{BD4E1996-A933-4CEA-A1FD-9B0C7B81E9F3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{BD4E1996-A933-4CEA-A1FD-9B0C7B81E9F3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputLanes(DispatchBaseClass):
	CLSID = IID('{376D0161-59D0-4F0E-911E-A7DD6774983E}')
	coclass_clsid = IID('{0D940366-6119-4660-8B95-80796E0695DB}')

	# Result is of type ISIAPIOutputLane
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Laneno
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}')
		return ret

	def LaneExists(self, Laneno=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Laneno
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Laneno=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Laneno
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputLeg(DispatchBaseClass):
	CLSID = IID('{4D03B4B2-FBC7-4EC5-B7D8-984398036302}')
	coclass_clsid = IID('{E9A07B34-F024-4B0D-8F6E-54F6E743AC2C}')

	_prop_map_get_ = {
		"Arrival_flow_flag": (1610743882, 2, (3, 0), (), "Arrival_flow_flag", None),
		"Average_entry_lane_width": (1610743872, 2, (4, 0), (), "Average_entry_lane_width", None),
		"Avg_num_of_cycles_to_depart": (1610743889, 2, (4, 0), (), "Avg_num_of_cycles_to_depart", None),
		"Avg_veh_length": (1610743907, 2, (4, 0), (), "Avg_veh_length", None),
		"Capacity_adj_flag_worstlane": (1610743888, 2, (3, 0), (), "Capacity_adj_flag_worstlane", None),
		"Capacity_adj_worstlane": (1610743887, 2, (4, 0), (), "Capacity_adj_worstlane", None),
		"Capacity_effective": (1610743817, 2, (4, 0), (), "Capacity_effective", None),
		"Capacity_lane_total": (1610743818, 2, (4, 0), (), "Capacity_lane_total", None),
		"Capacity_mov_total": (1610743819, 2, (4, 0), (), "Capacity_mov_total", None),
		"Carbon_dioxide_rate": (1610743853, 2, (4, 0), (), "Carbon_dioxide_rate", None),
		"Carbon_dioxide_total": (1610743847, 2, (4, 0), (), "Carbon_dioxide_total", None),
		"Carbon_monoxide_rate": (1610743855, 2, (4, 0), (), "Carbon_monoxide_rate", None),
		"Carbon_monoxide_total": (1610743849, 2, (4, 0), (), "Carbon_monoxide_total", None),
		"Circulating_flow": (1610743858, 2, (4, 0), (), "Circulating_flow", None),
		"Circulating_flow_pcu": (1610743868, 2, (4, 0), (), "Circulating_flow_pcu", None),
		"CongestionCoefficient": (1610743894, 2, (4, 0), (), "CongestionCoefficient", None),
		"Deg_satn": (1610743820, 2, (4, 0), (), "Deg_satn", None),
		"Delay_control_average": (1610743821, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_average_worstlane": (1610743863, 2, (4, 0), (), "Delay_control_average_worstlane", None),
		"Delay_control_average_worstmov": (1610743864, 2, (4, 0), (), "Delay_control_average_worstmov", None),
		"Delay_control_total": (1610743822, 2, (4, 0), (), "Delay_control_total", None),
		"Delay_geometric": (1610743865, 2, (4, 0), (), "Delay_geometric", None),
		"Delay_stopline_average": (1610743866, 2, (4, 0), (), "Delay_stopline_average", None),
		"Density": (1610743901, 2, (4, 0), (), "Density", None),
		"Density_pcu": (1610743902, 2, (4, 0), (), "Density_pcu", None),
		"DesiredSpeed": (1610743898, 2, (4, 0), (), "DesiredSpeed", None),
		"DesiredSpeedMethod": (1610743897, 2, (3, 0), (), "DesiredSpeedMethod", None),
		"DesiredSpeedProgram": (1610743899, 2, (4, 0), (), "DesiredSpeedProgram", None),
		"Exiting_flow": (1610743857, 2, (4, 0), (), "Exiting_flow", None),
		"Exiting_flow_capconstr": (1610743867, 2, (4, 0), (), "Exiting_flow_capconstr", None),
		"Extra_bunching": (1610743875, 2, (4, 0), (), "Extra_bunching", None),
		"Extra_bunching_flag": (1610743876, 2, (3, 0), (), "Extra_bunching_flag", None),
		"FHWA_capacity_zero_circ_flow": (1610743869, 2, (4, 0), (), "FHWA_capacity_zero_circ_flow", None),
		"Flow_HV": (1610743811, 2, (4, 0), (), "Flow_HV", None),
		"Flow_HV_capconstr": (1610743815, 2, (4, 0), (), "Flow_HV_capconstr", None),
		"Flow_HV_pct": (1610743812, 2, (4, 0), (), "Flow_HV_pct", None),
		"Flow_HV_pct_capconstr": (1610743816, 2, (4, 0), (), "Flow_HV_pct_capconstr", None),
		"Flow_LV": (1610743810, 2, (4, 0), (), "Flow_LV", None),
		"Flow_LV_capconstr": (1610743814, 2, (4, 0), (), "Flow_LV_capconstr", None),
		"Flow_total": (1610743809, 2, (4, 0), (), "Flow_total", None),
		"Flow_total_capconstr": (1610743813, 2, (4, 0), (), "Flow_total_capconstr", None),
		"Fuel_consumption_rate": (1610743852, 2, (4, 0), (), "Fuel_consumption_rate", None),
		"Fuel_consumption_total": (1610743846, 2, (4, 0), (), "Fuel_consumption_total", None),
		"Headway": (1610743904, 2, (4, 0), (), "Headway", None),
		"Hydrocarbons_rate": (1610743854, 2, (4, 0), (), "Hydrocarbons_rate", None),
		"Hydrocarbons_total": (1610743848, 2, (4, 0), (), "Hydrocarbons_total", None),
		"Idling_time_average": (1610743877, 2, (4, 0), (), "Idling_time_average", None),
		"Inscribed_diameter": (1610743870, 2, (4, 0), (), "Inscribed_diameter", None),
		"LOS_density": (1610743911, 2, (8, 0), (), "LOS_density", None),
		"Level_of_service": (1610743823, 2, (8, 0), (), "Level_of_service", None),
		"Level_of_service_worstlane": (1610743825, 2, (8, 0), (), "Level_of_service_worstlane", None),
		"Level_of_service_worstmov": (1610743824, 2, (8, 0), (), "Level_of_service_worstmov", None),
		"Net_inflow": (1610743879, 2, (4, 0), (), "Net_inflow", None),
		"Net_inflow_capconstr": (1610743880, 2, (4, 0), (), "Net_inflow_capconstr", None),
		"Net_outflow": (1610743881, 2, (4, 0), (), "Net_outflow", None),
		"Net_outflow_capconstr": (1610743891, 2, (4, 0), (), "Net_outflow_capconstr", None),
		"Nox_rate": (1610743856, 2, (4, 0), (), "Nox_rate", None),
		"Nox_total": (1610743850, 2, (4, 0), (), "Nox_total", None),
		"Num_entry_lanes": (1610743871, 2, (3, 0), (), "Num_entry_lanes", None),
		"Occupancy_time": (1610743905, 2, (4, 0), (), "Occupancy_time", None),
		"Operating_cost_rate": (1610743851, 2, (4, 0), (), "Operating_cost_rate", None),
		"Operating_cost_total": (1610743845, 2, (4, 0), (), "Operating_cost_total", None),
		"Orientation": (1610743808, 2, (3, 0), (), "Orientation", None),
		# Method 'OutputCirculatingLanes' returns object of type 'ISIAPIOutputCirculatingLanes'
		"OutputCirculatingLanes": (1610743862, 2, (9, 0), (), "OutputCirculatingLanes", '{0FC1F22D-8C53-40A4-B9AB-B8B9D664B8EE}'),
		# Method 'OutputLaneExits' returns object of type 'ISIAPIOutputLaneExits'
		"OutputLaneExits": (1610743912, 2, (9, 0), (), "OutputLaneExits", '{91DFAD2B-DD5C-40FE-B5DB-B4C40175952C}'),
		# Method 'OutputLanes' returns object of type 'ISIAPIOutputLanes'
		"OutputLanes": (1610743861, 2, (9, 0), (), "OutputLanes", '{376D0161-59D0-4F0E-911E-A7DD6774983E}'),
		# Method 'OutputLegMCs' returns object of type 'ISIAPIOutputLegMCs'
		"OutputLegMCs": (1610743860, 2, (9, 0), (), "OutputLegMCs", '{C2BFE7C1-8AED-441A-AA66-B016245FC854}'),
		# Method 'Outputset' returns object of type 'ISIAPIOutputset'
		"Outputset": (1610743913, 2, (9, 0), (), "Outputset", '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}'),
		"Performance_index": (1610743839, 2, (4, 0), (), "Performance_index", None),
		"Platoonmode_type": (1610743892, 2, (3, 0), (), "Platoonmode_type", None),
		"Prob_blockage": (1610743896, 2, (4, 0), (), "Prob_blockage", None),
		"Prop_queued_upstr_signal": (1610743873, 2, (4, 0), (), "Prop_queued_upstr_signal", None),
		"Prop_queued_upstr_signal_flag": (1610743874, 2, (3, 0), (), "Prop_queued_upstr_signal_flag", None),
		"Proportion_queued": (1610743838, 2, (4, 0), (), "Proportion_queued", None),
		"Queue_cycav_mean": (1610743826, 2, (4, 0), (), "Queue_cycav_mean", None),
		"Queue_cycav_percentile": (1610743827, 2, (4, 0), (), "Queue_cycav_percentile", None),
		"Queue_dist_cycav_mean": (1610743830, 2, (4, 0), (), "Queue_dist_cycav_mean", None),
		"Queue_dist_cycav_percentile": (1610743831, 2, (4, 0), (), "Queue_dist_cycav_percentile", None),
		"Queue_dist_greenstart_mean": (1610743885, 2, (4, 0), (), "Queue_dist_greenstart_mean", None),
		"Queue_dist_greenstart_percentile": (1610743886, 2, (4, 0), (), "Queue_dist_greenstart_percentile", None),
		"Queue_dist_maxback_mean": (1610743832, 2, (4, 0), (), "Queue_dist_maxback_mean", None),
		"Queue_dist_maxback_percentile": (1610743833, 2, (4, 0), (), "Queue_dist_maxback_percentile", None),
		"Queue_greenstart_mean": (1610743883, 2, (4, 0), (), "Queue_greenstart_mean", None),
		"Queue_greenstart_percentile": (1610743884, 2, (4, 0), (), "Queue_greenstart_percentile", None),
		"Queue_maxback_mean": (1610743828, 2, (4, 0), (), "Queue_maxback_mean", None),
		"Queue_maxback_percentile": (1610743829, 2, (4, 0), (), "Queue_maxback_percentile", None),
		"Queue_storage_ratio_avg": (1610743834, 2, (4, 0), (), "Queue_storage_ratio_avg", None),
		"Queue_storage_ratio_percentile": (1610743835, 2, (4, 0), (), "Queue_storage_ratio_percentile", None),
		"Space_occupancy_ratio": (1610743908, 2, (4, 0), (), "Space_occupancy_ratio", None),
		"Space_time": (1610743906, 2, (4, 0), (), "Space_time", None),
		"Spacing": (1610743903, 2, (4, 0), (), "Spacing", None),
		"SpeedEfficiency": (1610743878, 2, (4, 0), (), "SpeedEfficiency", None),
		"SpeedEfficiencyFlag": (1610743893, 2, (3, 0), (), "SpeedEfficiencyFlag", None),
		"Stop_rate": (1610743836, 2, (4, 0), (), "Stop_rate", None),
		"Stops_total": (1610743837, 2, (4, 0), (), "Stops_total", None),
		"Time_occupancy_ratio": (1610743909, 2, (4, 0), (), "Time_occupancy_ratio", None),
		"Total_lane_changes": (1610743890, 2, (4, 0), (), "Total_lane_changes", None),
		"TravelTimeIndex": (1610743895, 2, (4, 0), (), "TravelTimeIndex", None),
		"Travel_distance_average": (1610743841, 2, (4, 0), (), "Travel_distance_average", None),
		"Travel_distance_total": (1610743840, 2, (4, 0), (), "Travel_distance_total", None),
		"Travel_speed": (1610743844, 2, (4, 0), (), "Travel_speed", None),
		"Travel_time_average": (1610743843, 2, (4, 0), (), "Travel_time_average", None),
		"Travel_time_total": (1610743842, 2, (4, 0), (), "Travel_time_total", None),
		"Uninterrupted_speed": (1610743900, 2, (4, 0), (), "Uninterrupted_speed", None),
		"Uninterrupted_travel_delay": (1610743910, 2, (4, 0), (), "Uninterrupted_travel_delay", None),
		"X1_flag": (1610743859, 2, (3, 0), (), "X1_flag", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputLegMC(DispatchBaseClass):
	CLSID = IID('{2E9D2343-958B-4C06-9CD9-C004A4B481ED}')
	coclass_clsid = IID('{F3741C26-DB83-4B1A-B27C-3A77398B820D}')

	_prop_map_get_ = {
		"Arrival_flow_flag": (1610743819, 2, (3, 0), (), "Arrival_flow_flag", None),
		"Avg_num_of_cycles_to_depart": (1610743833, 2, (4, 0), (), "Avg_num_of_cycles_to_depart", None),
		"Calc_exists": (1610743823, 2, (11, 0), (), "Calc_exists", None),
		"Capacity_adj_flag_worstlane": (1610743843, 2, (3, 0), (), "Capacity_adj_flag_worstlane", None),
		"Capacity_adj_worstlane": (1610743842, 2, (4, 0), (), "Capacity_adj_worstlane", None),
		"Circulating_flow": (1610743814, 2, (4, 0), (), "Circulating_flow", None),
		"Circulating_flow_pcu": (1610743815, 2, (4, 0), (), "Circulating_flow_pcu", None),
		"CongestionCoefficient": (1610743837, 2, (4, 0), (), "CongestionCoefficient", None),
		"Deg_satn": (1610743824, 2, (4, 0), (), "Deg_satn", None),
		"Delay_control_average": (1610743825, 2, (4, 0), (), "Delay_control_average", None),
		"DesiredSpeed": (1610743845, 2, (4, 0), (), "DesiredSpeed", None),
		"DesiredSpeedMethod": (1610743844, 2, (3, 0), (), "DesiredSpeedMethod", None),
		"DesiredSpeedProgram": (1610743846, 2, (4, 0), (), "DesiredSpeedProgram", None),
		"Exist_in_nw_upstream_only": (1610743816, 2, (11, 0), (), "Exist_in_nw_upstream_only", None),
		"Exiting_flow": (1610743812, 2, (4, 0), (), "Exiting_flow", None),
		"Exiting_flow_capconstr": (1610743813, 2, (4, 0), (), "Exiting_flow_capconstr", None),
		"Flow": (1610743809, 2, (4, 0), (), "Flow", None),
		"Flow_capconstr": (1610743810, 2, (4, 0), (), "Flow_capconstr", None),
		"Level_of_service": (1610743826, 2, (8, 0), (), "Level_of_service", None),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
		"Net_inflow": (1610743817, 2, (4, 0), (), "Net_inflow", None),
		"Net_inflow_capconstr": (1610743818, 2, (4, 0), (), "Net_inflow_capconstr", None),
		"Net_outflow": (1610743821, 2, (4, 0), (), "Net_outflow", None),
		"Net_outflow_capconstr": (1610743822, 2, (4, 0), (), "Net_outflow_capconstr", None),
		# Method 'OutputLeg' returns object of type 'ISIAPIOutputLeg'
		"OutputLeg": (1610743811, 2, (9, 0), (), "OutputLeg", '{4D03B4B2-FBC7-4EC5-B7D8-984398036302}'),
		"Prob_blockage": (1610743839, 2, (4, 0), (), "Prob_blockage", None),
		"Proportion_queued": (1610743831, 2, (4, 0), (), "Proportion_queued", None),
		"Queue_dist_maxback_mean": (1610743829, 2, (4, 0), (), "Queue_dist_maxback_mean", None),
		"Queue_dist_maxback_percentile": (1610743830, 2, (4, 0), (), "Queue_dist_maxback_percentile", None),
		"Queue_maxback_mean": (1610743827, 2, (4, 0), (), "Queue_maxback_mean", None),
		"Queue_maxback_percentile": (1610743828, 2, (4, 0), (), "Queue_maxback_percentile", None),
		"Queue_storage_ratio_avg": (1610743840, 2, (4, 0), (), "Queue_storage_ratio_avg", None),
		"Queue_storage_ratio_percentile": (1610743841, 2, (4, 0), (), "Queue_storage_ratio_percentile", None),
		"SpeedEfficiency": (1610743835, 2, (4, 0), (), "SpeedEfficiency", None),
		"SpeedEfficiencyFlag": (1610743836, 2, (3, 0), (), "SpeedEfficiencyFlag", None),
		"Stop_rate": (1610743832, 2, (4, 0), (), "Stop_rate", None),
		"Total_lane_changes": (1610743820, 2, (4, 0), (), "Total_lane_changes", None),
		"TravelTimeIndex": (1610743838, 2, (4, 0), (), "TravelTimeIndex", None),
		"Travel_speed": (1610743834, 2, (4, 0), (), "Travel_speed", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputLegMCs(DispatchBaseClass):
	CLSID = IID('{C2BFE7C1-8AED-441A-AA66-B016245FC854}')
	coclass_clsid = IID('{A8384538-2E01-41E9-B927-A1B92997CBAE}')

	# Result is of type ISIAPIOutputLegMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{2E9D2343-958B-4C06-9CD9-C004A4B481ED}')
		return ret

	def MovementClassExists(self, mcClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),mcClass
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{2E9D2343-958B-4C06-9CD9-C004A4B481ED}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{2E9D2343-958B-4C06-9CD9-C004A4B481ED}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputLegPerson(DispatchBaseClass):
	CLSID = IID('{F402DAA3-8B5C-47C7-BAB5-F124A4A16AC7}')
	coclass_clsid = IID('{437CCE51-F160-474A-9E8C-2F4563AB7972}')

	_prop_map_get_ = {
		"Arrival_flow_total": (1610743810, 2, (4, 0), (), "Arrival_flow_total", None),
		"Delay_control_average": (1610743811, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_average_worstmov": (1610743812, 2, (4, 0), (), "Delay_control_average_worstmov", None),
		"Delay_control_total": (1610743813, 2, (4, 0), (), "Delay_control_total", None),
		"Demand_flow_total": (1610743809, 2, (4, 0), (), "Demand_flow_total", None),
		"Operating_cost_total": (1610743822, 2, (4, 0), (), "Operating_cost_total", None),
		"Orientation": (1610743808, 2, (3, 0), (), "Orientation", None),
		# Method 'Outputset' returns object of type 'ISIAPIOutputset'
		"Outputset": (1610743824, 2, (9, 0), (), "Outputset", '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}'),
		"Performance_index": (1610743823, 2, (4, 0), (), "Performance_index", None),
		"Proportion_queued": (1610743816, 2, (4, 0), (), "Proportion_queued", None),
		"Stop_rate": (1610743814, 2, (4, 0), (), "Stop_rate", None),
		"Stops_total": (1610743815, 2, (4, 0), (), "Stops_total", None),
		"Travel_distance_average": (1610743818, 2, (4, 0), (), "Travel_distance_average", None),
		"Travel_distance_total": (1610743817, 2, (4, 0), (), "Travel_distance_total", None),
		"Travel_speed": (1610743821, 2, (4, 0), (), "Travel_speed", None),
		"Travel_time_average": (1610743820, 2, (4, 0), (), "Travel_time_average", None),
		"Travel_time_total": (1610743819, 2, (4, 0), (), "Travel_time_total", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputLegPersons(DispatchBaseClass):
	CLSID = IID('{D31B97D0-0C54-45B5-9529-1DFF92F8B457}')
	coclass_clsid = IID('{6894003C-85BB-4C7D-AF06-4DA6296A53CD}')

	# Result is of type ISIAPIOutputLegPerson
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Orientation=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Orientation
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F402DAA3-8B5C-47C7-BAB5-F124A4A16AC7}')
		return ret

	def LegPersonExists(self, Orientation=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Orientation
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Orientation=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Orientation
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F402DAA3-8B5C-47C7-BAB5-F124A4A16AC7}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{F402DAA3-8B5C-47C7-BAB5-F124A4A16AC7}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputLegs(DispatchBaseClass):
	CLSID = IID('{7A84E80F-58FD-4C53-94B3-29713CCED51C}')
	coclass_clsid = IID('{CC917735-7108-44B2-AB13-4CA33F9BF15E}')

	# Result is of type ISIAPIOutputLeg
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Orientation=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Orientation
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4D03B4B2-FBC7-4EC5-B7D8-984398036302}')
		return ret

	def LegExists(self, Orientation=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Orientation
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Orientation=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Orientation
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4D03B4B2-FBC7-4EC5-B7D8-984398036302}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4D03B4B2-FBC7-4EC5-B7D8-984398036302}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputMeteredRoundabout(DispatchBaseClass):
	CLSID = IID('{B11203CA-CABF-43DF-9156-6898CA85836F}')
	coclass_clsid = IID('{8E03F3A5-D77C-4D28-834D-5CEC97CB8B93}')

	_prop_map_get_ = {
		"Blank_time_ratio": (1610743812, 2, (4, 0), (), "Blank_time_ratio", None),
		"Controlling_queue_detection_probability": (1610743813, 2, (4, 0), (), "Controlling_queue_detection_probability", None),
		"Metered_displayed_blank": (1610743809, 2, (3, 0), (), "Metered_displayed_blank", None),
		"Metered_displayed_red": (1610743808, 2, (3, 0), (), "Metered_displayed_red", None),
		"Metered_effective_blank": (1610743811, 2, (3, 0), (), "Metered_effective_blank", None),
		"Metered_effective_red": (1610743810, 2, (3, 0), (), "Metered_effective_red", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputMovementPed(DispatchBaseClass):
	CLSID = IID('{C0173099-4351-4B91-8AD7-82B5C047FAC2}')
	coclass_clsid = IID('{B3EBCA38-6BD7-47EE-860F-3CBAA18B0A8E}')

	_prop_map_get_ = {
		"Capacity_mov": (1610743812, 2, (4, 0), (), "Capacity_mov", None),
		"Crossing_dist": (1610743834, 2, (4, 0), (), "Crossing_dist", None),
		"Crossing_dist_user_spec": (1610743835, 2, (11, 0), (), "Crossing_dist_user_spec", None),
		"Deg_satn": (1610743813, 2, (4, 0), (), "Deg_satn", None),
		"Delay_control_average": (1610743814, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_total": (1610743815, 2, (4, 0), (), "Delay_control_total", None),
		"Demand_flow_total": (1610743811, 2, (4, 0), (), "Demand_flow_total", None),
		"Green_periods": (1610743829, 2, (3, 0), (), "Green_periods", None),
		"Level_of_service": (1610743816, 2, (8, 0), (), "Level_of_service", None),
		"Operating_cost_rate": (1610743832, 2, (4, 0), (), "Operating_cost_rate", None),
		"Operating_cost_total": (1610743828, 2, (4, 0), (), "Operating_cost_total", None),
		"Origin": (1610743809, 2, (3, 0), (), "Origin", None),
		# Method 'OutputMovementPed_GreenPeriods' returns object of type 'ISIAPIOutputMovementPed_GreenPeriods'
		"OutputMovementPed_GreenPeriods": (1610743830, 2, (9, 0), (), "OutputMovementPed_GreenPeriods", '{48C726FD-2FE1-44AA-8265-A5CE3B84B7D5}'),
		# Method 'Outputset' returns object of type 'ISIAPIOutputset'
		"Outputset": (1610743836, 2, (9, 0), (), "Outputset", '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}'),
		"Performance_index": (1610743822, 2, (4, 0), (), "Performance_index", None),
		"Practical_degree_of_saturation": (1610743831, 2, (4, 0), (), "Practical_degree_of_saturation", None),
		"Practical_degree_of_saturation_user_spec": (1610743833, 2, (11, 0), (), "Practical_degree_of_saturation_user_spec", None),
		"Proportion_queued": (1610743821, 2, (4, 0), (), "Proportion_queued", None),
		"Queue_dist_maxback_mean": (1610743818, 2, (4, 0), (), "Queue_dist_maxback_mean", None),
		"Queue_maxback_mean": (1610743817, 2, (4, 0), (), "Queue_maxback_mean", None),
		"Stage": (1610743810, 2, (3, 0), (), "Stage", None),
		"Stop_rate": (1610743819, 2, (4, 0), (), "Stop_rate", None),
		"Stops_total": (1610743820, 2, (4, 0), (), "Stops_total", None),
		"Travel_distance_average": (1610743824, 2, (4, 0), (), "Travel_distance_average", None),
		"Travel_distance_total": (1610743823, 2, (4, 0), (), "Travel_distance_total", None),
		"Travel_speed": (1610743827, 2, (4, 0), (), "Travel_speed", None),
		"Travel_time_average": (1610743826, 2, (4, 0), (), "Travel_time_average", None),
		"Travel_time_total": (1610743825, 2, (4, 0), (), "Travel_time_total", None),
		"Type": (1610743808, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputMovementPed_GreenPeriod(DispatchBaseClass):
	CLSID = IID('{D572C46E-740A-4488-BD94-1D2C1111C61F}')
	coclass_clsid = IID('{84D7F6CD-F5FA-4A63-AAD3-A0836A53E19D}')

	_prop_map_get_ = {
		"Adjusted_flow_ratio": (1610743820, 2, (4, 0), (), "Adjusted_flow_ratio", None),
		"Adjusted_lost_time": (1610743819, 2, (3, 0), (), "Adjusted_lost_time", None),
		"Adjusted_lost_time_noact": (1610743834, 2, (3, 0), (), "Adjusted_lost_time_noact", None),
		"Clearance1_time": (1610743832, 2, (3, 0), (), "Clearance1_time", None),
		"Clearance1_time_option": (1610743836, 2, (3, 0), (), "Clearance1_time_option", None),
		"Clearance2_time": (1610743833, 2, (3, 0), (), "Clearance2_time", None),
		"Clearance2_time_option": (1610743837, 2, (3, 0), (), "Clearance2_time_option", None),
		"Clearance_time_total": (1610743838, 2, (3, 0), (), "Clearance_time_total", None),
		"Critical_mov": (1610743824, 2, (11, 0), (), "Critical_mov", None),
		"Displayed_end_time": (1610743828, 2, (3, 0), (), "Displayed_end_time", None),
		"Displayed_start_time": (1610743827, 2, (3, 0), (), "Displayed_start_time", None),
		"Eff_end_time": (1610743815, 2, (3, 0), (), "Eff_end_time", None),
		"Eff_green": (1610743818, 2, (3, 0), (), "Eff_green", None),
		"Eff_min_walk_time": (1610743846, 2, (3, 0), (), "Eff_min_walk_time", None),
		"Eff_min_walk_time_noact": (1610743845, 2, (3, 0), (), "Eff_min_walk_time_noact", None),
		"Eff_start_time": (1610743814, 2, (3, 0), (), "Eff_start_time", None),
		"End_gain": (1610743813, 2, (3, 0), (), "End_gain", None),
		"End_phase": (1610743809, 2, (3, 0), (), "End_phase", None),
		"Flow_ratio": (1610743823, 2, (4, 0), (), "Flow_ratio", None),
		"Greenperiod": (1610743811, 2, (3, 0), (), "Greenperiod", None),
		"Lost_time": (1610743816, 2, (3, 0), (), "Lost_time", None),
		"Min_max_flag": (1610743829, 2, (3, 0), (), "Min_max_flag", None),
		"Min_walk_time": (1610743831, 2, (3, 0), (), "Min_walk_time", None),
		"No_arrival": (1610743830, 2, (11, 0), (), "No_arrival", None),
		"Ped_maximum_time": (1610743841, 2, (3, 0), (), "Ped_maximum_time", None),
		"Ped_maximum_time_option": (1610743851, 2, (3, 0), (), "Ped_maximum_time_option", None),
		"Ped_minimum_time": (1610743839, 2, (3, 0), (), "Ped_minimum_time", None),
		"Ped_minimum_time_user_spec": (1610743840, 2, (11, 0), (), "Ped_minimum_time_user_spec", None),
		"Ped_negative_end_gain": (1610743842, 2, (3, 0), (), "Ped_negative_end_gain", None),
		"Priority": (1610743810, 2, (11, 0), (), "Priority", None),
		"Prob_ped_arrival": (1610743849, 2, (4, 0), (), "Prob_ped_arrival", None),
		"Prob_ped_arrival_option": (1610743850, 2, (3, 0), (), "Prob_ped_arrival_option", None),
		"Reqd_green_time_ratio": (1610743821, 2, (4, 0), (), "Reqd_green_time_ratio", None),
		"Reqd_time": (1610743817, 2, (4, 0), (), "Reqd_time", None),
		"Satn_flow": (1610743822, 2, (4, 0), (), "Satn_flow", None),
		"Start_intergrn": (1610743844, 2, (3, 0), (), "Start_intergrn", None),
		"Start_intergrn_noact": (1610743843, 2, (3, 0), (), "Start_intergrn_noact", None),
		"Start_loss": (1610743812, 2, (3, 0), (), "Start_loss", None),
		"Start_phase": (1610743808, 2, (3, 0), (), "Start_phase", None),
		"Tmax": (1610743826, 2, (4, 0), (), "Tmax", None),
		"Tmin": (1610743825, 2, (4, 0), (), "Tmin", None),
		"Tmin_noact": (1610743835, 2, (4, 0), (), "Tmin_noact", None),
		"Total_walk_time": (1610743848, 2, (3, 0), (), "Total_walk_time", None),
		"Unadj_reqd_time": (1610743852, 2, (4, 0), (), "Unadj_reqd_time", None),
		"Walk_extension_time": (1610743847, 2, (3, 0), (), "Walk_extension_time", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputMovementPed_GreenPeriods(DispatchBaseClass):
	CLSID = IID('{48C726FD-2FE1-44AA-8265-A5CE3B84B7D5}')
	coclass_clsid = IID('{9A430652-1CDD-473B-B7B7-30803DDFA31B}')

	def GreenPeriodExists(self, Greenperiod=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Greenperiod
			)

	# Result is of type ISIAPIOutputMovementPed_GreenPeriod
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Greenperiod=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Greenperiod
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D572C46E-740A-4488-BD94-1D2C1111C61F}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Greenperiod=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Greenperiod
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D572C46E-740A-4488-BD94-1D2C1111C61F}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D572C46E-740A-4488-BD94-1D2C1111C61F}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputMovementPeds(DispatchBaseClass):
	CLSID = IID('{3C02979B-5CC8-41CC-86DC-1884428878F1}')
	coclass_clsid = IID('{1365E5D6-A5D4-4F25-9103-C306C6367EDB}')

	# Result is of type ISIAPIOutputMovementPed
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Type=defaultNamedNotOptArg, Origin=defaultNamedNotOptArg, Stage=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1), (3, 1)),Type
			, Origin, Stage)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C0173099-4351-4B91-8AD7-82B5C047FAC2}')
		return ret

	def MovementExists(self, Type=defaultNamedNotOptArg, Origin=defaultNamedNotOptArg, Stage=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),Type
			, Origin, Stage)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Type=defaultNamedNotOptArg, Origin=defaultNamedNotOptArg, Stage=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1), (3, 1)),Type
			, Origin, Stage)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C0173099-4351-4B91-8AD7-82B5C047FAC2}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C0173099-4351-4B91-8AD7-82B5C047FAC2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputMovementPersonOD(DispatchBaseClass):
	CLSID = IID('{D26606A5-98D6-468D-9B07-D9B3FD9B0321}')
	coclass_clsid = IID('{A72FF5DE-CE06-4986-AE4E-6A0264AC85FE}')

	_prop_map_get_ = {
		"Arrival_flow_total": (1610743811, 2, (4, 0), (), "Arrival_flow_total", None),
		"Delay_control_average": (1610743812, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_average_worstmov": (1610743813, 2, (4, 0), (), "Delay_control_average_worstmov", None),
		"Delay_control_total": (1610743814, 2, (4, 0), (), "Delay_control_total", None),
		"Demand_flow_total": (1610743810, 2, (4, 0), (), "Demand_flow_total", None),
		"Destination": (1610743809, 2, (3, 0), (), "Destination", None),
		"Operating_cost_total": (1610743823, 2, (4, 0), (), "Operating_cost_total", None),
		"Origin": (1610743808, 2, (3, 0), (), "Origin", None),
		# Method 'OutputMovementPersonODMCs' returns object of type 'ISIAPIOutputMovementPersonODMCs'
		"OutputMovementPersonODMCs": (1610743825, 2, (9, 0), (), "OutputMovementPersonODMCs", '{607669B1-C03B-4159-B296-B084B2451BD2}'),
		# Method 'Outputset' returns object of type 'ISIAPIOutputset'
		"Outputset": (1610743826, 2, (9, 0), (), "Outputset", '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}'),
		"Performance_index": (1610743824, 2, (4, 0), (), "Performance_index", None),
		"Proportion_queued": (1610743817, 2, (4, 0), (), "Proportion_queued", None),
		"Stop_rate": (1610743815, 2, (4, 0), (), "Stop_rate", None),
		"Stops_total": (1610743816, 2, (4, 0), (), "Stops_total", None),
		"Travel_distance_average": (1610743819, 2, (4, 0), (), "Travel_distance_average", None),
		"Travel_distance_total": (1610743818, 2, (4, 0), (), "Travel_distance_total", None),
		"Travel_speed": (1610743822, 2, (4, 0), (), "Travel_speed", None),
		"Travel_time_average": (1610743821, 2, (4, 0), (), "Travel_time_average", None),
		"Travel_time_total": (1610743820, 2, (4, 0), (), "Travel_time_total", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputMovementPersonODMC(DispatchBaseClass):
	CLSID = IID('{3B5F488E-D133-4697-85E3-05ACAA1915E9}')
	coclass_clsid = IID('{32E2E2DA-8053-4562-9511-995FAED66C61}')

	_prop_map_get_ = {
		"Arrival_flow_total": (1610743811, 2, (4, 0), (), "Arrival_flow_total", None),
		"Calc_exists": (1610743809, 2, (11, 0), (), "Calc_exists", None),
		"Delay_control_average": (1610743812, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_average_worstmov": (1610743813, 2, (4, 0), (), "Delay_control_average_worstmov", None),
		"Delay_control_total": (1610743814, 2, (4, 0), (), "Delay_control_total", None),
		"Demand_flow_total": (1610743810, 2, (4, 0), (), "Demand_flow_total", None),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
		"Operating_cost_total": (1610743823, 2, (4, 0), (), "Operating_cost_total", None),
		# Method 'OutputMovementPersonOD' returns object of type 'ISIAPIOutputMovementPersonOD'
		"OutputMovementPersonOD": (1610743825, 2, (9, 0), (), "OutputMovementPersonOD", '{D26606A5-98D6-468D-9B07-D9B3FD9B0321}'),
		"Performance_index": (1610743824, 2, (4, 0), (), "Performance_index", None),
		"Proportion_queued": (1610743817, 2, (4, 0), (), "Proportion_queued", None),
		"Stop_rate": (1610743815, 2, (4, 0), (), "Stop_rate", None),
		"Stops_total": (1610743816, 2, (4, 0), (), "Stops_total", None),
		"Travel_distance_average": (1610743819, 2, (4, 0), (), "Travel_distance_average", None),
		"Travel_distance_total": (1610743818, 2, (4, 0), (), "Travel_distance_total", None),
		"Travel_speed": (1610743822, 2, (4, 0), (), "Travel_speed", None),
		"Travel_time_average": (1610743821, 2, (4, 0), (), "Travel_time_average", None),
		"Travel_time_total": (1610743820, 2, (4, 0), (), "Travel_time_total", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputMovementPersonODMCs(DispatchBaseClass):
	CLSID = IID('{607669B1-C03B-4159-B296-B084B2451BD2}')
	coclass_clsid = IID('{701F5599-2068-4533-BBE9-1BEAE64344EB}')

	# Result is of type ISIAPIOutputMovementPersonODMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{3B5F488E-D133-4697-85E3-05ACAA1915E9}')
		return ret

	def MovementClassExists(self, mcClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),mcClass
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{3B5F488E-D133-4697-85E3-05ACAA1915E9}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{3B5F488E-D133-4697-85E3-05ACAA1915E9}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputMovementPersonODs(DispatchBaseClass):
	CLSID = IID('{C1ADE01E-D8D6-44AD-8FB2-18158BD070F1}')
	coclass_clsid = IID('{7448B67E-5F38-4E37-BF4C-A475561C7EFF}')

	# Result is of type ISIAPIOutputMovementPersonOD
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),Origin
			, Destination)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D26606A5-98D6-468D-9B07-D9B3FD9B0321}')
		return ret

	def MovementExists(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1), (3, 1)),Origin
			, Destination)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),Origin
			, Destination)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D26606A5-98D6-468D-9B07-D9B3FD9B0321}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D26606A5-98D6-468D-9B07-D9B3FD9B0321}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputMovementVehicleOD(DispatchBaseClass):
	CLSID = IID('{28749A62-EAF4-4575-BAB2-196A61EA612C}')
	coclass_clsid = IID('{62FF9ABF-31EF-46B7-A288-2B9074A70F87}')

	_prop_map_get_ = {
		"Approach_negotiation_speed": (1610743862, 2, (4, 0), (), "Approach_negotiation_speed", None),
		"Arrival_flow_flag": (1610743881, 2, (3, 0), (), "Arrival_flow_flag", None),
		"Avg_num_of_cycles_to_depart": (1610743892, 2, (4, 0), (), "Avg_num_of_cycles_to_depart", None),
		"Capacity_adj_flag_worstlane": (1610743888, 2, (3, 0), (), "Capacity_adj_flag_worstlane", None),
		"Capacity_adj_worstlane": (1610743887, 2, (4, 0), (), "Capacity_adj_worstlane", None),
		"Capacity_data_type": (1610743882, 2, (3, 0), (), "Capacity_data_type", None),
		"Capacity_mov": (1610743818, 2, (4, 0), (), "Capacity_mov", None),
		"Carbon_dioxide_rate": (1610743857, 2, (4, 0), (), "Carbon_dioxide_rate", None),
		"Carbon_dioxide_total": (1610743851, 2, (4, 0), (), "Carbon_dioxide_total", None),
		"Carbon_monoxide_rate": (1610743859, 2, (4, 0), (), "Carbon_monoxide_rate", None),
		"Carbon_monoxide_total": (1610743853, 2, (4, 0), (), "Carbon_monoxide_total", None),
		"CongestionCoefficient": (1610743899, 2, (4, 0), (), "CongestionCoefficient", None),
		"Cruise_speed": (1610743848, 2, (4, 0), (), "Cruise_speed", None),
		"Deg_satn": (1610743819, 2, (4, 0), (), "Deg_satn", None),
		"Delay_control_average": (1610743822, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_average_worstlane": (1610743873, 2, (4, 0), (), "Delay_control_average_worstlane", None),
		"Delay_control_average_worstmov": (1610743874, 2, (4, 0), (), "Delay_control_average_worstmov", None),
		"Delay_control_total_persons": (1610743824, 2, (4, 0), (), "Delay_control_total_persons", None),
		"Delay_control_total_veh": (1610743823, 2, (4, 0), (), "Delay_control_total_veh", None),
		"Delay_geometric": (1610743826, 2, (4, 0), (), "Delay_geometric", None),
		"Delay_stopline_average": (1610743825, 2, (4, 0), (), "Delay_stopline_average", None),
		"DesiredSpeed": (1610743902, 2, (4, 0), (), "DesiredSpeed", None),
		"DesiredSpeedMethod": (1610743901, 2, (3, 0), (), "DesiredSpeedMethod", None),
		"DesiredSpeedProgram": (1610743903, 2, (4, 0), (), "DesiredSpeedProgram", None),
		"Destination": (1610743809, 2, (3, 0), (), "Destination", None),
		"Effective_control": (1610743871, 2, (3, 0), (), "Effective_control", None),
		"Equivalent_AT": (1610743891, 2, (3, 0), (), "Equivalent_AT", None),
		"Exit_cruise_speed": (1610743864, 2, (4, 0), (), "Exit_cruise_speed", None),
		"Exit_negotiation_speed": (1610743863, 2, (4, 0), (), "Exit_negotiation_speed", None),
		"Flow_HV": (1610743812, 2, (4, 0), (), "Flow_HV", None),
		"Flow_HV_capconstr": (1610743816, 2, (4, 0), (), "Flow_HV_capconstr", None),
		"Flow_HV_pct": (1610743813, 2, (4, 0), (), "Flow_HV_pct", None),
		"Flow_HV_pct_capconstr": (1610743817, 2, (4, 0), (), "Flow_HV_pct_capconstr", None),
		"Flow_LV": (1610743811, 2, (4, 0), (), "Flow_LV", None),
		"Flow_LV_capconstr": (1610743815, 2, (4, 0), (), "Flow_LV_capconstr", None),
		"Flow_total": (1610743810, 2, (4, 0), (), "Flow_total", None),
		"Flow_total_capconstr": (1610743814, 2, (4, 0), (), "Flow_total_capconstr", None),
		"Fuel_consumption_rate": (1610743856, 2, (4, 0), (), "Fuel_consumption_rate", None),
		"Fuel_consumption_total": (1610743850, 2, (4, 0), (), "Fuel_consumption_total", None),
		"Gap_accept_blocked_time": (1610743895, 2, (4, 0), (), "Gap_accept_blocked_time", None),
		"Gap_accept_cycle_time": (1610743894, 2, (4, 0), (), "Gap_accept_cycle_time", None),
		"Gap_accept_unblocked_time": (1610743896, 2, (4, 0), (), "Gap_accept_unblocked_time", None),
		"Green_periods": (1610743861, 2, (3, 0), (), "Green_periods", None),
		"Has_continuous_control": (1610743870, 2, (11, 0), (), "Has_continuous_control", None),
		"Has_giveway_control": (1610743869, 2, (11, 0), (), "Has_giveway_control", None),
		"Has_highangle_slip": (1610743865, 2, (11, 0), (), "Has_highangle_slip", None),
		"Has_lowangle_slip": (1610743866, 2, (11, 0), (), "Has_lowangle_slip", None),
		"Has_signals_control": (1610743867, 2, (11, 0), (), "Has_signals_control", None),
		"Has_stop_control": (1610743868, 2, (11, 0), (), "Has_stop_control", None),
		"Hydrocarbons_rate": (1610743858, 2, (4, 0), (), "Hydrocarbons_rate", None),
		"Hydrocarbons_total": (1610743852, 2, (4, 0), (), "Hydrocarbons_total", None),
		"Idling_time_average": (1610743879, 2, (4, 0), (), "Idling_time_average", None),
		"Level_of_service": (1610743827, 2, (8, 0), (), "Level_of_service", None),
		"Minimum_delay": (1610743897, 2, (4, 0), (), "Minimum_delay", None),
		"Nox_rate": (1610743860, 2, (4, 0), (), "Nox_rate", None),
		"Nox_total": (1610743854, 2, (4, 0), (), "Nox_total", None),
		"Operating_cost_rate": (1610743855, 2, (4, 0), (), "Operating_cost_rate", None),
		"Operating_cost_total": (1610743849, 2, (4, 0), (), "Operating_cost_total", None),
		"Origin": (1610743808, 2, (3, 0), (), "Origin", None),
		# Method 'OutputMovementVehicleODMCs' returns object of type 'ISIAPIOutputMovementVehicleODMCs'
		"OutputMovementVehicleODMCs": (1610743872, 2, (9, 0), (), "OutputMovementVehicleODMCs", '{0059BCEB-1475-43CB-A08D-E392F389F5DB}'),
		# Method 'Outputset' returns object of type 'ISIAPIOutputset'
		"Outputset": (1610743904, 2, (9, 0), (), "Outputset", '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}'),
		"Perc_arriving_during_green": (1610743889, 2, (4, 0), (), "Perc_arriving_during_green", None),
		"Performance_index": (1610743841, 2, (4, 0), (), "Performance_index", None),
		"Platoon_ratio": (1610743890, 2, (4, 0), (), "Platoon_ratio", None),
		"Practical_spare_capacity": (1610743821, 2, (4, 0), (), "Practical_spare_capacity", None),
		"Proportion_queued": (1610743840, 2, (4, 0), (), "Proportion_queued", None),
		"Queue_cycav_mean": (1610743828, 2, (4, 0), (), "Queue_cycav_mean", None),
		"Queue_cycav_percentile": (1610743829, 2, (4, 0), (), "Queue_cycav_percentile", None),
		"Queue_dist_cycav_mean": (1610743832, 2, (4, 0), (), "Queue_dist_cycav_mean", None),
		"Queue_dist_cycav_percentile": (1610743833, 2, (4, 0), (), "Queue_dist_cycav_percentile", None),
		"Queue_dist_greenstart_mean": (1610743885, 2, (4, 0), (), "Queue_dist_greenstart_mean", None),
		"Queue_dist_greenstart_percentile": (1610743886, 2, (4, 0), (), "Queue_dist_greenstart_percentile", None),
		"Queue_dist_maxback_mean": (1610743834, 2, (4, 0), (), "Queue_dist_maxback_mean", None),
		"Queue_dist_maxback_percentile": (1610743835, 2, (4, 0), (), "Queue_dist_maxback_percentile", None),
		"Queue_greenstart_mean": (1610743883, 2, (4, 0), (), "Queue_greenstart_mean", None),
		"Queue_greenstart_percentile": (1610743884, 2, (4, 0), (), "Queue_greenstart_percentile", None),
		"Queue_maxback_mean": (1610743830, 2, (4, 0), (), "Queue_maxback_mean", None),
		"Queue_maxback_percentile": (1610743831, 2, (4, 0), (), "Queue_maxback_percentile", None),
		"Queue_storage_ratio_avg": (1610743836, 2, (4, 0), (), "Queue_storage_ratio_avg", None),
		"Queue_storage_ratio_percentile": (1610743837, 2, (4, 0), (), "Queue_storage_ratio_percentile", None),
		"Running_speed": (1610743847, 2, (4, 0), (), "Running_speed", None),
		"SpeedEfficiency": (1610743880, 2, (4, 0), (), "SpeedEfficiency", None),
		"SpeedEfficiencyFlag": (1610743898, 2, (3, 0), (), "SpeedEfficiencyFlag", None),
		"Stop_rate": (1610743838, 2, (4, 0), (), "Stop_rate", None),
		"Stops_total": (1610743839, 2, (4, 0), (), "Stops_total", None),
		"TravelTimeIndex": (1610743900, 2, (4, 0), (), "TravelTimeIndex", None),
		"Travel_distance_average": (1610743843, 2, (4, 0), (), "Travel_distance_average", None),
		"Travel_distance_stopline_average": (1610743876, 2, (4, 0), (), "Travel_distance_stopline_average", None),
		"Travel_distance_stopline_total": (1610743875, 2, (4, 0), (), "Travel_distance_stopline_total", None),
		"Travel_distance_total": (1610743842, 2, (4, 0), (), "Travel_distance_total", None),
		"Travel_speed": (1610743846, 2, (4, 0), (), "Travel_speed", None),
		"Travel_time_average": (1610743845, 2, (4, 0), (), "Travel_time_average", None),
		"Travel_time_stopline_average": (1610743878, 2, (4, 0), (), "Travel_time_stopline_average", None),
		"Travel_time_stopline_total": (1610743877, 2, (4, 0), (), "Travel_time_stopline_total", None),
		"Travel_time_total": (1610743844, 2, (4, 0), (), "Travel_time_total", None),
		"Unblocked_time_ratio": (1610743893, 2, (4, 0), (), "Unblocked_time_ratio", None),
		"X1_flag": (1610743820, 2, (3, 0), (), "X1_flag", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputMovementVehicleODMC(DispatchBaseClass):
	CLSID = IID('{986170AC-21B5-40BE-B9FF-F0A3C2CDB6D1}')
	coclass_clsid = IID('{DE724601-782C-4198-A2CD-745C397898D4}')

	_prop_map_get_ = {
		"Approach_negotiation_speed": (1610743857, 2, (4, 0), (), "Approach_negotiation_speed", None),
		"Arrival_flow_flag": (1610743882, 2, (3, 0), (), "Arrival_flow_flag", None),
		"Avg_num_of_cycles_to_depart": (1610743888, 2, (4, 0), (), "Avg_num_of_cycles_to_depart", None),
		"Calc_exists": (1610743869, 2, (11, 0), (), "Calc_exists", None),
		"Capacity_mov": (1610743813, 2, (4, 0), (), "Capacity_mov", None),
		"Carbon_dioxide_rate": (1610743852, 2, (4, 0), (), "Carbon_dioxide_rate", None),
		"Carbon_dioxide_total": (1610743846, 2, (4, 0), (), "Carbon_dioxide_total", None),
		"Carbon_monoxide_rate": (1610743854, 2, (4, 0), (), "Carbon_monoxide_rate", None),
		"Carbon_monoxide_total": (1610743848, 2, (4, 0), (), "Carbon_monoxide_total", None),
		"CongestionCoefficient": (1610743899, 2, (4, 0), (), "CongestionCoefficient", None),
		"Cruise_speed": (1610743843, 2, (4, 0), (), "Cruise_speed", None),
		"Deg_satn": (1610743814, 2, (4, 0), (), "Deg_satn", None),
		"Delay_control_average": (1610743817, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_total_persons": (1610743819, 2, (4, 0), (), "Delay_control_total_persons", None),
		"Delay_control_total_veh": (1610743818, 2, (4, 0), (), "Delay_control_total_veh", None),
		"Delay_geometric": (1610743821, 2, (4, 0), (), "Delay_geometric", None),
		"Delay_stopline_average": (1610743820, 2, (4, 0), (), "Delay_stopline_average", None),
		"DesiredSpeed": (1610743902, 2, (4, 0), (), "DesiredSpeed", None),
		"DesiredSpeedMethod": (1610743901, 2, (3, 0), (), "DesiredSpeedMethod", None),
		"DesiredSpeedProgram": (1610743903, 2, (4, 0), (), "DesiredSpeedProgram", None),
		"Destination": (1610743809, 2, (3, 0), (), "Destination", None),
		"Effective_control": (1610743866, 2, (3, 0), (), "Effective_control", None),
		"Equivalent_AT": (1610743878, 2, (3, 0), (), "Equivalent_AT", None),
		"Exit_cruise_speed": (1610743859, 2, (4, 0), (), "Exit_cruise_speed", None),
		"Exit_negotiation_speed": (1610743858, 2, (4, 0), (), "Exit_negotiation_speed", None),
		"Flow": (1610743811, 2, (4, 0), (), "Flow", None),
		"Flow_capconstr": (1610743812, 2, (4, 0), (), "Flow_capconstr", None),
		"Flow_capconstr_no_initial": (1610743904, 2, (4, 0), (), "Flow_capconstr_no_initial", None),
		"Fuel_consumption_rate": (1610743851, 2, (4, 0), (), "Fuel_consumption_rate", None),
		"Fuel_consumption_total": (1610743845, 2, (4, 0), (), "Fuel_consumption_total", None),
		"Gap_accept_blocked_time": (1610743895, 2, (4, 0), (), "Gap_accept_blocked_time", None),
		"Gap_accept_cycle_time": (1610743894, 2, (4, 0), (), "Gap_accept_cycle_time", None),
		"Gap_accept_unblocked_time": (1610743896, 2, (4, 0), (), "Gap_accept_unblocked_time", None),
		"Green_periods": (1610743856, 2, (3, 0), (), "Green_periods", None),
		"Green_time_ratio": (1610743876, 2, (4, 0), (), "Green_time_ratio", None),
		"Has_continuous_control": (1610743865, 2, (11, 0), (), "Has_continuous_control", None),
		"Has_giveway_control": (1610743864, 2, (11, 0), (), "Has_giveway_control", None),
		"Has_highangle_slip": (1610743860, 2, (11, 0), (), "Has_highangle_slip", None),
		"Has_lowangle_slip": (1610743861, 2, (11, 0), (), "Has_lowangle_slip", None),
		"Has_signals_control": (1610743862, 2, (11, 0), (), "Has_signals_control", None),
		"Has_stop_control": (1610743863, 2, (11, 0), (), "Has_stop_control", None),
		"Hydrocarbons_rate": (1610743853, 2, (4, 0), (), "Hydrocarbons_rate", None),
		"Hydrocarbons_total": (1610743847, 2, (4, 0), (), "Hydrocarbons_total", None),
		"Initial_demand_vol": (1610743889, 2, (4, 0), (), "Initial_demand_vol", None),
		"Level_of_service": (1610743822, 2, (8, 0), (), "Level_of_service", None),
		"MC_class": (1610743810, 2, (3, 0), (), "MC_class", None),
		"Minimum_delay": (1610743897, 2, (4, 0), (), "Minimum_delay", None),
		"Negotiation_distance": (1610743874, 2, (4, 0), (), "Negotiation_distance", None),
		"Non_actuated": (1610743880, 2, (11, 0), (), "Non_actuated", None),
		"Nox_rate": (1610743855, 2, (4, 0), (), "Nox_rate", None),
		"Nox_total": (1610743849, 2, (4, 0), (), "Nox_total", None),
		"Operating_cost_rate": (1610743850, 2, (4, 0), (), "Operating_cost_rate", None),
		"Operating_cost_total": (1610743844, 2, (4, 0), (), "Operating_cost_total", None),
		"Origin": (1610743808, 2, (3, 0), (), "Origin", None),
		# Method 'OutputMovementVehicleOD' returns object of type 'ISIAPIOutputMovementVehicleOD'
		"OutputMovementVehicleOD": (1610743868, 2, (9, 0), (), "OutputMovementVehicleOD", '{28749A62-EAF4-4575-BAB2-196A61EA612C}'),
		# Method 'OutputMovementVehicleODMC_GreenPeriods' returns object of type 'ISIAPIOutputMovementVehicleODMC_GreenPeriods'
		"OutputMovementVehicleODMC_GreenPeriods": (1610743867, 2, (9, 0), (), "OutputMovementVehicleODMC_GreenPeriods", '{09DD6321-DDCF-4DA8-9DC6-099B915C5177}'),
		"Oversatn_duration": (1610743892, 2, (4, 0), (), "Oversatn_duration", None),
		"Perc_arriving_during_green": (1610743875, 2, (4, 0), (), "Perc_arriving_during_green", None),
		"Performance_index": (1610743836, 2, (4, 0), (), "Performance_index", None),
		"Platoon_ratio": (1610743877, 2, (4, 0), (), "Platoon_ratio", None),
		"Practical_degree_of_saturation": (1610743883, 2, (4, 0), (), "Practical_degree_of_saturation", None),
		"Practical_spare_capacity": (1610743816, 2, (4, 0), (), "Practical_spare_capacity", None),
		"Proportion_queued": (1610743835, 2, (4, 0), (), "Proportion_queued", None),
		"Queue_cycav_mean": (1610743823, 2, (4, 0), (), "Queue_cycav_mean", None),
		"Queue_cycav_percentile": (1610743824, 2, (4, 0), (), "Queue_cycav_percentile", None),
		"Queue_dist_cycav_mean": (1610743827, 2, (4, 0), (), "Queue_dist_cycav_mean", None),
		"Queue_dist_cycav_percentile": (1610743828, 2, (4, 0), (), "Queue_dist_cycav_percentile", None),
		"Queue_dist_greenstart_mean": (1610743886, 2, (4, 0), (), "Queue_dist_greenstart_mean", None),
		"Queue_dist_greenstart_percentile": (1610743887, 2, (4, 0), (), "Queue_dist_greenstart_percentile", None),
		"Queue_dist_maxback_mean": (1610743829, 2, (4, 0), (), "Queue_dist_maxback_mean", None),
		"Queue_dist_maxback_percentile": (1610743830, 2, (4, 0), (), "Queue_dist_maxback_percentile", None),
		"Queue_greenstart_mean": (1610743884, 2, (4, 0), (), "Queue_greenstart_mean", None),
		"Queue_greenstart_percentile": (1610743885, 2, (4, 0), (), "Queue_greenstart_percentile", None),
		"Queue_maxback_mean": (1610743825, 2, (4, 0), (), "Queue_maxback_mean", None),
		"Queue_maxback_percentile": (1610743826, 2, (4, 0), (), "Queue_maxback_percentile", None),
		"Queue_storage_ratio_avg": (1610743831, 2, (4, 0), (), "Queue_storage_ratio_avg", None),
		"Queue_storage_ratio_percentile": (1610743832, 2, (4, 0), (), "Queue_storage_ratio_percentile", None),
		"Residual_demand_vol": (1610743890, 2, (4, 0), (), "Residual_demand_vol", None),
		"Residual_demand_vol_clear_time": (1610743891, 2, (4, 0), (), "Residual_demand_vol_clear_time", None),
		"Running_speed": (1610743842, 2, (4, 0), (), "Running_speed", None),
		"Signal_coordination": (1610743879, 2, (3, 0), (), "Signal_coordination", None),
		"SpeedEfficiency": (1610743881, 2, (4, 0), (), "SpeedEfficiency", None),
		"SpeedEfficiencyFlag": (1610743898, 2, (3, 0), (), "SpeedEfficiencyFlag", None),
		"Stop_rate": (1610743833, 2, (4, 0), (), "Stop_rate", None),
		"Stops_total": (1610743834, 2, (4, 0), (), "Stops_total", None),
		"TravelTimeIndex": (1610743900, 2, (4, 0), (), "TravelTimeIndex", None),
		"Travel_distance_average": (1610743838, 2, (4, 0), (), "Travel_distance_average", None),
		"Travel_distance_stopline_average": (1610743871, 2, (4, 0), (), "Travel_distance_stopline_average", None),
		"Travel_distance_stopline_total": (1610743870, 2, (4, 0), (), "Travel_distance_stopline_total", None),
		"Travel_distance_total": (1610743837, 2, (4, 0), (), "Travel_distance_total", None),
		"Travel_speed": (1610743841, 2, (4, 0), (), "Travel_speed", None),
		"Travel_time_average": (1610743840, 2, (4, 0), (), "Travel_time_average", None),
		"Travel_time_stopline_average": (1610743873, 2, (4, 0), (), "Travel_time_stopline_average", None),
		"Travel_time_stopline_total": (1610743872, 2, (4, 0), (), "Travel_time_stopline_total", None),
		"Travel_time_total": (1610743839, 2, (4, 0), (), "Travel_time_total", None),
		"Unblocked_time_ratio": (1610743893, 2, (4, 0), (), "Unblocked_time_ratio", None),
		"X1_flag": (1610743815, 2, (3, 0), (), "X1_flag", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputMovementVehicleODMC_GreenPeriod(DispatchBaseClass):
	CLSID = IID('{D1B3E73C-50AF-4E33-83C7-DD0500022669}')
	coclass_clsid = IID('{A3C07D6F-05EB-4636-96F4-2F2E21B76559}')

	_prop_map_get_ = {
		"Adjusted_flow_ratio": (1610743822, 2, (4, 0), (), "Adjusted_flow_ratio", None),
		"Adjusted_lost_time": (1610743821, 2, (3, 0), (), "Adjusted_lost_time", None),
		"Adjusted_lost_time_noact": (1610743839, 2, (3, 0), (), "Adjusted_lost_time_noact", None),
		"Coord_mov_runs": (1610743835, 2, (11, 0), (), "Coord_mov_runs", None),
		"Critical_mov": (1610743826, 2, (11, 0), (), "Critical_mov", None),
		"Displayed_end_time": (1610743832, 2, (3, 0), (), "Displayed_end_time", None),
		"Displayed_green_time": (1610743836, 2, (3, 0), (), "Displayed_green_time", None),
		"Displayed_start_time": (1610743831, 2, (3, 0), (), "Displayed_start_time", None),
		"Eff_end_time": (1610743817, 2, (3, 0), (), "Eff_end_time", None),
		"Eff_green": (1610743820, 2, (3, 0), (), "Eff_green", None),
		"Eff_start_time": (1610743816, 2, (3, 0), (), "Eff_start_time", None),
		"End_gain": (1610743815, 2, (3, 0), (), "End_gain", None),
		"End_phase": (1610743810, 2, (3, 0), (), "End_phase", None),
		"Flow_ratio": (1610743825, 2, (4, 0), (), "Flow_ratio", None),
		"Greenperiod": (1610743808, 2, (3, 0), (), "Greenperiod", None),
		"Lost_time": (1610743818, 2, (3, 0), (), "Lost_time", None),
		"Min_green_noact": (1610743840, 2, (3, 0), (), "Min_green_noact", None),
		"Min_max_flag": (1610743833, 2, (3, 0), (), "Min_max_flag", None),
		"No_arrival": (1610743834, 2, (11, 0), (), "No_arrival", None),
		"Opposed": (1610743811, 2, (11, 0), (), "Opposed", None),
		"Priority": (1610743812, 2, (11, 0), (), "Priority", None),
		"Prob_veh_arrival": (1610743843, 2, (4, 0), (), "Prob_veh_arrival", None),
		"Prob_veh_arrival_flag": (1610743844, 2, (3, 0), (), "Prob_veh_arrival_flag", None),
		"Queue_move_up_speed": (1610743827, 2, (4, 0), (), "Queue_move_up_speed", None),
		"Red_arrow_drop_off_applied": (1610743846, 2, (11, 0), (), "Red_arrow_drop_off_applied", None),
		"Reqd_green_time_ratio": (1610743823, 2, (4, 0), (), "Reqd_green_time_ratio", None),
		"Reqd_time": (1610743819, 2, (4, 0), (), "Reqd_time", None),
		"Satn_flow": (1610743824, 2, (4, 0), (), "Satn_flow", None),
		"Satn_flow_flag": (1610743837, 2, (3, 0), (), "Satn_flow_flag", None),
		"Start_intergrn": (1610743842, 2, (3, 0), (), "Start_intergrn", None),
		"Start_intergrn_noact": (1610743841, 2, (3, 0), (), "Start_intergrn_noact", None),
		"Start_loss": (1610743814, 2, (3, 0), (), "Start_loss", None),
		"Start_phase": (1610743809, 2, (3, 0), (), "Start_phase", None),
		"Timing_data_type": (1610743828, 2, (3, 0), (), "Timing_data_type", None),
		"Tmax": (1610743830, 2, (4, 0), (), "Tmax", None),
		"Tmin": (1610743829, 2, (4, 0), (), "Tmin", None),
		"Tmin_noact": (1610743845, 2, (4, 0), (), "Tmin_noact", None),
		"Unadj_reqd_time": (1610743838, 2, (4, 0), (), "Unadj_reqd_time", None),
		"Undetected": (1610743813, 2, (11, 0), (), "Undetected", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputMovementVehicleODMC_GreenPeriods(DispatchBaseClass):
	CLSID = IID('{09DD6321-DDCF-4DA8-9DC6-099B915C5177}')
	coclass_clsid = IID('{3B2A414F-F47E-46DA-A129-8FA0E569A68E}')

	def GreenPeriodExists(self, Greenperiod=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),Greenperiod
			)

	# Result is of type ISIAPIOutputMovementVehicleODMC_GreenPeriod
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Greenperiod=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Greenperiod
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D1B3E73C-50AF-4E33-83C7-DD0500022669}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Greenperiod=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),Greenperiod
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D1B3E73C-50AF-4E33-83C7-DD0500022669}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D1B3E73C-50AF-4E33-83C7-DD0500022669}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputMovementVehicleODMCs(DispatchBaseClass):
	CLSID = IID('{0059BCEB-1475-43CB-A08D-E392F389F5DB}')
	coclass_clsid = IID('{D8D3C9FE-9684-4EA9-AC7D-3E1533984744}')

	# Result is of type ISIAPIOutputMovementVehicleODMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{986170AC-21B5-40BE-B9FF-F0A3C2CDB6D1}')
		return ret

	def MovementClassExists(self, mcClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),mcClass
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{986170AC-21B5-40BE-B9FF-F0A3C2CDB6D1}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{986170AC-21B5-40BE-B9FF-F0A3C2CDB6D1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputMovementVehicleODs(DispatchBaseClass):
	CLSID = IID('{F7CF3309-E6B6-4637-93F1-DC805C88F46A}')
	coclass_clsid = IID('{1D7046CE-4C37-4EE0-957D-F78BD3FE40E0}')

	# Result is of type ISIAPIOutputMovementVehicleOD
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),Origin
			, Destination)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{28749A62-EAF4-4575-BAB2-196A61EA612C}')
		return ret

	def MovementExists(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1), (3, 1)),Origin
			, Destination)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),Origin
			, Destination)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{28749A62-EAF4-4575-BAB2-196A61EA612C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{28749A62-EAF4-4575-BAB2-196A61EA612C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputMultiSequenceAnalyses(DispatchBaseClass):
	CLSID = IID('{CD988BB1-BF23-45C3-B098-74FABCE0BDF2}')
	coclass_clsid = IID('{41E3DF9C-C236-47ED-A1C3-30A9F5C14C9A}')

	# Result is of type ISIAPIOutputMultiSequenceAnalysis
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6637A5AE-862D-4DB2-A89C-6368E9239E45}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{6637A5AE-862D-4DB2-A89C-6368E9239E45}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{6637A5AE-862D-4DB2-A89C-6368E9239E45}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputMultiSequenceAnalysis(DispatchBaseClass):
	CLSID = IID('{6637A5AE-862D-4DB2-A89C-6368E9239E45}')
	coclass_clsid = IID('{BD186FED-F0F8-49DA-B585-FBE8ED785FE5}')

	_prop_map_get_ = {
		"Capacity_effective": (1610743811, 2, (4, 0), (), "Capacity_effective", None),
		"Carbon_dioxide_total": (1610743820, 2, (4, 0), (), "Carbon_dioxide_total", None),
		"Carbon_monoxide_total": (1610743821, 2, (4, 0), (), "Carbon_monoxide_total", None),
		"Cycle_time": (1610743809, 2, (4, 0), (), "Cycle_time", None),
		"Deg_satn": (1610743810, 2, (4, 0), (), "Deg_satn", None),
		"Delay_control_average": (1610743813, 2, (4, 0), (), "Delay_control_average", None),
		"Fuel_consumption_total": (1610743819, 2, (4, 0), (), "Fuel_consumption_total", None),
		"Hydrocarbons_total": (1610743822, 2, (4, 0), (), "Hydrocarbons_total", None),
		"Nox_total": (1610743823, 2, (4, 0), (), "Nox_total", None),
		"Operating_cost_total": (1610743818, 2, (4, 0), (), "Operating_cost_total", None),
		# Method 'Outputset' returns object of type 'ISIAPIOutputset'
		"Outputset": (1610743826, 2, (9, 0), (), "Outputset", '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}'),
		"Performance_index": (1610743817, 2, (4, 0), (), "Performance_index", None),
		"Practical_spare_capacity": (1610743812, 2, (4, 0), (), "Practical_spare_capacity", None),
		"Queue_dist_maxback_percentile": (1610743816, 2, (4, 0), (), "Queue_dist_maxback_percentile", None),
		"Queue_maxback_percentile": (1610743815, 2, (4, 0), (), "Queue_maxback_percentile", None),
		"Seq_position": (1610743808, 2, (3, 0), (), "Seq_position", None),
		"SpeedEfficiency": (1610743824, 2, (4, 0), (), "SpeedEfficiency", None),
		"Stop_rate": (1610743814, 2, (4, 0), (), "Stop_rate", None),
		"Travel_speed": (1610743825, 2, (4, 0), (), "Travel_speed", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputNetwork(DispatchBaseClass):
	CLSID = IID('{5E551751-0DA8-4E10-931A-D474F6FFBB27}')
	coclass_clsid = IID('{2AACA59E-CEC2-4BF8-B07B-C12BD329A7E9}')

	_prop_map_get_ = {
		"Analysis_method": (1610743819, 2, (3, 0), (), "Analysis_method", None),
		"Analysis_method_flag": (1610743818, 2, (3, 0), (), "Analysis_method_flag", None),
		"Analysis_status": (1610743820, 2, (3, 0), (), "Analysis_status", None),
		"Cycle_time_option": (1610743825, 2, (3, 0), (), "Cycle_time_option", None),
		"GeneratedByVersion": (1610743814, 2, (8, 0), (), "GeneratedByVersion", None),
		"GeneratedTime": (1610743809, 2, (7, 0), (), "GeneratedTime", None),
		"IterationsCount": (1610743810, 2, (3, 0), (), "IterationsCount", None),
		"Largest_movement_flow_scale": (1610743822, 2, (4, 0), (), "Largest_movement_flow_scale", None),
		# Method 'Network' returns object of type 'ISIAPINetwork'
		"Network": (1610743808, 2, (9, 0), (), "Network", '{C5A62A3D-7D9C-4544-8547-499D4C770332}'),
		"NetworkCycleTime": (1610743815, 2, (3, 0), (), "NetworkCycleTime", None),
		"NetworkSummaryType": (1610743816, 2, (3, 0), (), "NetworkSummaryType", None),
		# Method 'OutputNetworkGraphTuples' returns object of type 'ISIAPIOutputNetworkGraphTuples'
		"OutputNetworkGraphTuples": (1610743826, 2, (9, 0), (), "OutputNetworkGraphTuples", '{CCE4D1AD-5F36-4DDD-94AB-6EF78A022E9B}'),
		# Method 'OutputNetworkPedestrian' returns object of type 'ISIAPIOutputNetworkPedestrian'
		"OutputNetworkPedestrian": (1610743812, 2, (9, 0), (), "OutputNetworkPedestrian", '{A690DFE7-BEC8-47B7-A8A0-1176FE2EB02B}'),
		# Method 'OutputNetworkPerson' returns object of type 'ISIAPIOutputNetworkPerson'
		"OutputNetworkPerson": (1610743813, 2, (9, 0), (), "OutputNetworkPerson", '{DD7EC03C-ADB7-402E-973A-CC61673F18E3}'),
		# Method 'OutputNetworkVehicle' returns object of type 'ISIAPIOutputNetworkVehicle'
		"OutputNetworkVehicle": (1610743811, 2, (9, 0), (), "OutputNetworkVehicle", '{F5FAAD8A-BEAF-4C23-8ED9-4B22D4A45051}'),
		# Method 'OutputRouteMovementBasedPerson' returns object of type 'ISIAPIOutputRouteMovementBasedPerson'
		"OutputRouteMovementBasedPerson": (1610743828, 2, (9, 0), (), "OutputRouteMovementBasedPerson", '{3C6C4EF3-04CC-4AD7-A16B-6643D85352C8}'),
		# Method 'OutputRouteMovementBasedVehicle' returns object of type 'ISIAPIOutputRouteMovementBasedVehicle'
		"OutputRouteMovementBasedVehicle": (1610743827, 2, (9, 0), (), "OutputRouteMovementBasedVehicle", '{7FE4BECE-3C4E-4607-8CCA-C099AEE0F8B9}'),
		"Selected_future_year": (1610743821, 2, (3, 0), (), "Selected_future_year", None),
		"Selected_parameter_scale": (1610743823, 2, (4, 0), (), "Selected_parameter_scale", None),
		"Single_ccg": (1610743824, 2, (3, 0), (), "Single_ccg", None),
		# Method 'route' returns object of type 'ISIAPIRoute'
		"route": (1610743817, 2, (9, 0), (), "route", '{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputNetworkGraphTuple(DispatchBaseClass):
	CLSID = IID('{7B8EEE90-6CE2-465A-9022-FF17F8CC2BB4}')
	coclass_clsid = IID('{761871EA-EF42-4D9E-AD88-1363E5E9CCD9}')

	_prop_map_get_ = {
		"Arrival_flow_total": (1610743809, 2, (4, 0), (), "Arrival_flow_total", None),
		"Arrival_flow_total_person": (1610743810, 2, (4, 0), (), "Arrival_flow_total_person", None),
		"Capacity_effective": (1610743813, 2, (4, 0), (), "Capacity_effective", None),
		"Carbon_dioxide_total": (1610743829, 2, (4, 0), (), "Carbon_dioxide_total", None),
		"Carbon_monoxide_total": (1610743828, 2, (4, 0), (), "Carbon_monoxide_total", None),
		"Cycle_time": (1610743824, 2, (4, 0), (), "Cycle_time", None),
		"Deg_satn": (1610743814, 2, (4, 0), (), "Deg_satn", None),
		"Deg_satn_ped": (1610743835, 2, (4, 0), (), "Deg_satn_ped", None),
		"Delay_control_average": (1610743816, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_average_ped": (1610743840, 2, (4, 0), (), "Delay_control_average_ped", None),
		"Delay_control_average_veh": (1610743839, 2, (4, 0), (), "Delay_control_average_veh", None),
		"Delay_control_average_worstlane": (1610743841, 2, (4, 0), (), "Delay_control_average_worstlane", None),
		"Delay_control_average_worstmov": (1610743817, 2, (4, 0), (), "Delay_control_average_worstmov", None),
		"Delay_control_average_worstmov_ped": (1610743842, 2, (4, 0), (), "Delay_control_average_worstmov_ped", None),
		"Delay_control_average_worstmov_person": (1610743843, 2, (4, 0), (), "Delay_control_average_worstmov_person", None),
		"Delay_control_total_ped": (1610743837, 2, (4, 0), (), "Delay_control_total_ped", None),
		"Delay_control_total_person": (1610743838, 2, (4, 0), (), "Delay_control_total_person", None),
		"Delay_control_total_veh": (1610743836, 2, (4, 0), (), "Delay_control_total_veh", None),
		"Delay_geometric_average": (1610743844, 2, (4, 0), (), "Delay_geometric_average", None),
		"Delay_stopline_average": (1610743845, 2, (4, 0), (), "Delay_stopline_average", None),
		"Demand_flow_total": (1610743812, 2, (4, 0), (), "Demand_flow_total", None),
		"Demand_flow_total_ped": (1610743832, 2, (4, 0), (), "Demand_flow_total_ped", None),
		"Demand_flow_total_person": (1610743833, 2, (4, 0), (), "Demand_flow_total_person", None),
		"Fuel_consumption_total": (1610743825, 2, (4, 0), (), "Fuel_consumption_total", None),
		"Hydrocarbons_total": (1610743826, 2, (4, 0), (), "Hydrocarbons_total", None),
		"Level_of_service": (1610743818, 2, (3, 0), (), "Level_of_service", None),
		"Level_of_service_ped": (1610743847, 2, (3, 0), (), "Level_of_service_ped", None),
		"Level_of_service_veh": (1610743846, 2, (3, 0), (), "Level_of_service_veh", None),
		"Nox_total": (1610743827, 2, (4, 0), (), "Nox_total", None),
		"Operating_cost_total": (1610743830, 2, (4, 0), (), "Operating_cost_total", None),
		"Operating_cost_total_ped": (1610743873, 2, (4, 0), (), "Operating_cost_total_ped", None),
		"Operating_cost_total_veh": (1610743872, 2, (4, 0), (), "Operating_cost_total_veh", None),
		"Perc_heavy_veh": (1610743834, 2, (4, 0), (), "Perc_heavy_veh", None),
		"Performance_index": (1610743822, 2, (4, 0), (), "Performance_index", None),
		"Performance_index_ped": (1610743857, 2, (4, 0), (), "Performance_index_ped", None),
		"Performance_index_veh": (1610743856, 2, (4, 0), (), "Performance_index_veh", None),
		"Practical_spare_capacity": (1610743815, 2, (4, 0), (), "Practical_spare_capacity", None),
		"Prop_queued_ped": (1610743854, 2, (4, 0), (), "Prop_queued_ped", None),
		"Prop_queued_person": (1610743855, 2, (4, 0), (), "Prop_queued_person", None),
		"Prop_queued_veh": (1610743853, 2, (4, 0), (), "Prop_queued_veh", None),
		"Queue_dist_maxback_percentile": (1610743821, 2, (4, 0), (), "Queue_dist_maxback_percentile", None),
		"Queue_maxback_percentile": (1610743820, 2, (4, 0), (), "Queue_maxback_percentile", None),
		"SpeedEfficiency": (1610743811, 2, (4, 0), (), "SpeedEfficiency", None),
		"Stop_rate": (1610743819, 2, (4, 0), (), "Stop_rate", None),
		"Stop_rate_ped": (1610743852, 2, (4, 0), (), "Stop_rate_ped", None),
		"Stop_rate_veh": (1610743851, 2, (4, 0), (), "Stop_rate_veh", None),
		"Total_stops_ped": (1610743849, 2, (4, 0), (), "Total_stops_ped", None),
		"Total_stops_person": (1610743850, 2, (4, 0), (), "Total_stops_person", None),
		"Total_stops_veh": (1610743848, 2, (4, 0), (), "Total_stops_veh", None),
		"Travel_dist_av_ped": (1610743862, 2, (4, 0), (), "Travel_dist_av_ped", None),
		"Travel_dist_av_person": (1610743863, 2, (4, 0), (), "Travel_dist_av_person", None),
		"Travel_dist_av_veh": (1610743861, 2, (4, 0), (), "Travel_dist_av_veh", None),
		"Travel_dist_total_ped": (1610743859, 2, (4, 0), (), "Travel_dist_total_ped", None),
		"Travel_dist_total_person": (1610743860, 2, (4, 0), (), "Travel_dist_total_person", None),
		"Travel_dist_total_veh": (1610743858, 2, (4, 0), (), "Travel_dist_total_veh", None),
		"Travel_speed": (1610743823, 2, (4, 0), (), "Travel_speed", None),
		"Travel_speed_ped": (1610743870, 2, (4, 0), (), "Travel_speed_ped", None),
		"Travel_speed_person": (1610743871, 2, (4, 0), (), "Travel_speed_person", None),
		"Travel_time_av_ped": (1610743868, 2, (4, 0), (), "Travel_time_av_ped", None),
		"Travel_time_av_person": (1610743869, 2, (4, 0), (), "Travel_time_av_person", None),
		"Travel_time_av_veh": (1610743867, 2, (4, 0), (), "Travel_time_av_veh", None),
		"Travel_time_total_ped": (1610743865, 2, (4, 0), (), "Travel_time_total_ped", None),
		"Travel_time_total_person": (1610743866, 2, (4, 0), (), "Travel_time_total_person", None),
		"Travel_time_total_veh": (1610743864, 2, (4, 0), (), "Travel_time_total_veh", None),
		"Unsettled": (1610743831, 2, (11, 0), (), "Unsettled", None),
		"X_value": (1610743808, 2, (4, 0), (), "X_value", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputNetworkGraphTuples(DispatchBaseClass):
	CLSID = IID('{CCE4D1AD-5F36-4DDD-94AB-6EF78A022E9B}')
	coclass_clsid = IID('{C4474735-1E00-4BA4-A903-A89A9D95381D}')

	# Result is of type ISIAPIOutputNetworkGraphTuple
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7B8EEE90-6CE2-465A-9022-FF17F8CC2BB4}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7B8EEE90-6CE2-465A-9022-FF17F8CC2BB4}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{7B8EEE90-6CE2-465A-9022-FF17F8CC2BB4}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputNetworkPedestrian(DispatchBaseClass):
	CLSID = IID('{A690DFE7-BEC8-47B7-A8A0-1176FE2EB02B}')
	coclass_clsid = IID('{BBEAE5FC-9424-4977-9EE8-1177608D1825}')

	_prop_map_get_ = {
		"ArrivalFlowTotal": (1610743808, 2, (4, 0), (), "ArrivalFlowTotal", None),
		"DelayControlAverage": (1610743811, 2, (4, 0), (), "DelayControlAverage", None),
		"DelayControlAverageWorstMovement": (1610743812, 2, (4, 0), (), "DelayControlAverageWorstMovement", None),
		"DelayControlTotal": (1610743810, 2, (4, 0), (), "DelayControlTotal", None),
		"DemandFlowTotal": (1610743809, 2, (4, 0), (), "DemandFlowTotal", None),
		"OperatingCostTotal": (1610743822, 2, (4, 0), (), "OperatingCostTotal", None),
		"PerformanceIndex": (1610743816, 2, (4, 0), (), "PerformanceIndex", None),
		"ProportionQueued": (1610743815, 2, (4, 0), (), "ProportionQueued", None),
		"StopRate": (1610743814, 2, (4, 0), (), "StopRate", None),
		"StopsTotal": (1610743813, 2, (4, 0), (), "StopsTotal", None),
		"TravelDistanceAverage": (1610743818, 2, (4, 0), (), "TravelDistanceAverage", None),
		"TravelDistanceTotal": (1610743817, 2, (4, 0), (), "TravelDistanceTotal", None),
		"TravelSpeed": (1610743821, 2, (4, 0), (), "TravelSpeed", None),
		"TravelTimeAverage": (1610743820, 2, (4, 0), (), "TravelTimeAverage", None),
		"TravelTimeTotal": (1610743819, 2, (4, 0), (), "TravelTimeTotal", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputNetworkPerson(DispatchBaseClass):
	CLSID = IID('{DD7EC03C-ADB7-402E-973A-CC61673F18E3}')
	coclass_clsid = IID('{6183EA81-DA0E-44B6-B40D-F1DAF0933E78}')

	_prop_map_get_ = {
		"ArrivalFlowTotal": (1610743808, 2, (4, 0), (), "ArrivalFlowTotal", None),
		"DelayControlAverage": (1610743811, 2, (4, 0), (), "DelayControlAverage", None),
		"DelayControlAverageWorstMovement": (1610743812, 2, (4, 0), (), "DelayControlAverageWorstMovement", None),
		"DelayControlTotal": (1610743810, 2, (4, 0), (), "DelayControlTotal", None),
		"DemandFlowTotal": (1610743809, 2, (4, 0), (), "DemandFlowTotal", None),
		"OperatingCostTotal": (1610743822, 2, (4, 0), (), "OperatingCostTotal", None),
		"PerformanceIndex": (1610743816, 2, (4, 0), (), "PerformanceIndex", None),
		"ProportionQueued": (1610743815, 2, (4, 0), (), "ProportionQueued", None),
		"StopRate": (1610743814, 2, (4, 0), (), "StopRate", None),
		"StopsTotal": (1610743813, 2, (4, 0), (), "StopsTotal", None),
		"TravelDelay": (1610743823, 2, (4, 0), (), "TravelDelay", None),
		"TravelDelayAverage": (1610743824, 2, (4, 0), (), "TravelDelayAverage", None),
		"TravelDistanceAverage": (1610743818, 2, (4, 0), (), "TravelDistanceAverage", None),
		"TravelDistanceTotal": (1610743817, 2, (4, 0), (), "TravelDistanceTotal", None),
		"TravelSpeed": (1610743821, 2, (4, 0), (), "TravelSpeed", None),
		"TravelTimeAverage": (1610743820, 2, (4, 0), (), "TravelTimeAverage", None),
		"TravelTimeTotal": (1610743819, 2, (4, 0), (), "TravelTimeTotal", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputNetworkVehicle(DispatchBaseClass):
	CLSID = IID('{F5FAAD8A-BEAF-4C23-8ED9-4B22D4A45051}')
	coclass_clsid = IID('{82306492-4410-44E4-BBEE-D4223CB0DA23}')

	_prop_map_get_ = {
		"ArrivalFlowTotal": (1610743808, 2, (4, 0), (), "ArrivalFlowTotal", None),
		"ArrivalFlow_HV_pct": (1610743809, 2, (4, 0), (), "ArrivalFlow_HV_pct", None),
		"Capacity_effective": (1610743868, 2, (4, 0), (), "Capacity_effective", None),
		"CarbonDioxideTotal": (1610743827, 2, (4, 0), (), "CarbonDioxideTotal", None),
		"CarbonDioxide_rate": (1610743855, 2, (4, 0), (), "CarbonDioxide_rate", None),
		"CarbonMonoxideTotal": (1610743829, 2, (4, 0), (), "CarbonMonoxideTotal", None),
		"CarbonMonoxide_rate": (1610743857, 2, (4, 0), (), "CarbonMonoxide_rate", None),
		"CongestionCoefficient": (1610743832, 2, (4, 0), (), "CongestionCoefficient", None),
		"DegreeSaturation": (1610743812, 2, (4, 0), (), "DegreeSaturation", None),
		"DelayControlAverage": (1610743814, 2, (4, 0), (), "DelayControlAverage", None),
		"DelayControlAverageWorstLane": (1610743815, 2, (4, 0), (), "DelayControlAverageWorstLane", None),
		"DelayControlAverageWorstMovement": (1610743816, 2, (4, 0), (), "DelayControlAverageWorstMovement", None),
		"DelayControlTotal": (1610743813, 2, (4, 0), (), "DelayControlTotal", None),
		"DelayGeometricAverage": (1610743817, 2, (4, 0), (), "DelayGeometricAverage", None),
		"DelayStoplineAverage": (1610743818, 2, (4, 0), (), "DelayStoplineAverage", None),
		"DemandFlowTotal": (1610743810, 2, (4, 0), (), "DemandFlowTotal", None),
		"DemandFlow_HV_pct": (1610743811, 2, (4, 0), (), "DemandFlow_HV_pct", None),
		"DesiredSpeed": (1610743863, 2, (4, 0), (), "DesiredSpeed", None),
		"DesiredSpeedMethod": (1610743862, 2, (3, 0), (), "DesiredSpeedMethod", None),
		"DesiredTripTime": (1610743836, 2, (4, 0), (), "DesiredTripTime", None),
		"DesiredTripTime_rate": (1610743850, 2, (4, 0), (), "DesiredTripTime_rate", None),
		"FuelConsumptionTotal": (1610743826, 2, (4, 0), (), "FuelConsumptionTotal", None),
		"FuelConsumption_rate": (1610743854, 2, (4, 0), (), "FuelConsumption_rate", None),
		"FuelEconomy": (1610743859, 2, (4, 0), (), "FuelEconomy", None),
		"HydrocarbonsTotal": (1610743828, 2, (4, 0), (), "HydrocarbonsTotal", None),
		"Hydrocarbons_rate": (1610743856, 2, (4, 0), (), "Hydrocarbons_rate", None),
		"IdlingTimeAvg": (1610743838, 2, (4, 0), (), "IdlingTimeAvg", None),
		"IdlingTimeAvgerage_pct": (1610743847, 2, (4, 0), (), "IdlingTimeAvgerage_pct", None),
		"IdlingTimeAvgerage_rate": (1610743846, 2, (4, 0), (), "IdlingTimeAvgerage_rate", None),
		"LevelOfService": (1610743843, 2, (8, 0), (), "LevelOfService", None),
		"Max_dx_percent": (1610743861, 2, (4, 0), (), "Max_dx_percent", None),
		"Max_dx_percent_prev": (1610743866, 2, (4, 0), (), "Max_dx_percent_prev", None),
		"Max_dx_percent_prev2": (1610743867, 2, (4, 0), (), "Max_dx_percent_prev2", None),
		"Min_dx_percent": (1610743860, 2, (4, 0), (), "Min_dx_percent", None),
		"NoxTotal": (1610743830, 2, (4, 0), (), "NoxTotal", None),
		"Nox_rate": (1610743858, 2, (4, 0), (), "Nox_rate", None),
		"NwModel_vari_index": (1610743870, 2, (4, 0), (), "NwModel_vari_index", None),
		"OperatingCostTotal": (1610743825, 2, (4, 0), (), "OperatingCostTotal", None),
		"OperatingCost_rate": (1610743844, 2, (4, 0), (), "OperatingCost_rate", None),
		"PerformanceIndex": (1610743822, 2, (4, 0), (), "PerformanceIndex", None),
		"Practical_spare_capacity": (1610743869, 2, (4, 0), (), "Practical_spare_capacity", None),
		"ProportionQueued": (1610743821, 2, (4, 0), (), "ProportionQueued", None),
		"QueueStorageRatioAverage": (1610743842, 2, (4, 0), (), "QueueStorageRatioAverage", None),
		"QueueStorageRatioMaximum": (1610743841, 2, (4, 0), (), "QueueStorageRatioMaximum", None),
		"RunningTimeAvg": (1610743839, 2, (4, 0), (), "RunningTimeAvg", None),
		"RunningTimeAvgerage_pct": (1610743849, 2, (4, 0), (), "RunningTimeAvgerage_pct", None),
		"RunningTimeAvgerage_rate": (1610743848, 2, (4, 0), (), "RunningTimeAvgerage_rate", None),
		"SpeedEfficiency": (1610743831, 2, (4, 0), (), "SpeedEfficiency", None),
		"SpeedEfficiencyFlag": (1610743871, 2, (3, 0), (), "SpeedEfficiencyFlag", None),
		"StopRate": (1610743820, 2, (4, 0), (), "StopRate", None),
		"StopRate_rate": (1610743853, 2, (4, 0), (), "StopRate_rate", None),
		"StopsTotal": (1610743819, 2, (4, 0), (), "StopsTotal", None),
		"TravelDelay": (1610743837, 2, (4, 0), (), "TravelDelay", None),
		"TravelDelayAverage": (1610743864, 2, (4, 0), (), "TravelDelayAverage", None),
		"TravelDelayAverage_rate": (1610743865, 2, (4, 0), (), "TravelDelayAverage_rate", None),
		"TravelDelay_pct": (1610743852, 2, (4, 0), (), "TravelDelay_pct", None),
		"TravelDelay_rate": (1610743851, 2, (4, 0), (), "TravelDelay_rate", None),
		"TravelDistanceAverage": (1610743833, 2, (4, 0), (), "TravelDistanceAverage", None),
		"TravelDistanceTotal": (1610743823, 2, (4, 0), (), "TravelDistanceTotal", None),
		"TravelSpeed": (1610743835, 2, (4, 0), (), "TravelSpeed", None),
		"TravelTimeAverage": (1610743834, 2, (4, 0), (), "TravelTimeAverage", None),
		"TravelTimeAverage_rate": (1610743845, 2, (4, 0), (), "TravelTimeAverage_rate", None),
		"TravelTimeIndex": (1610743840, 2, (4, 0), (), "TravelTimeIndex", None),
		"TravelTimeTotal": (1610743824, 2, (4, 0), (), "TravelTimeTotal", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputPhase(DispatchBaseClass):
	CLSID = IID('{C186E5B6-87B7-4CBA-8D26-7190FC0709F1}')
	coclass_clsid = IID('{B640710A-977F-4313-BED9-C576EF0C58F1}')

	_prop_map_get_ = {
		"All_red_time": (1610743831, 2, (3, 0), (), "All_red_time", None),
		"Change_time": (1610743811, 2, (3, 0), (), "Change_time", None),
		"Critical_dummy_mov_flag": (1610743821, 2, (3, 0), (), "Critical_dummy_mov_flag", None),
		"Displayed_green_time": (1610743810, 2, (3, 0), (), "Displayed_green_time", None),
		"Dummy_adj_flow_ratio": (1610743825, 2, (4, 0), (), "Dummy_adj_flow_ratio", None),
		"Dummy_adj_lost_time": (1610743824, 2, (4, 0), (), "Dummy_adj_lost_time", None),
		"Dummy_eff_green": (1610743820, 2, (3, 0), (), "Dummy_eff_green", None),
		"Dummy_lost_time": (1610743818, 2, (3, 0), (), "Dummy_lost_time", None),
		"Dummy_min_max_flag": (1610743829, 2, (3, 0), (), "Dummy_min_max_flag", None),
		"Dummy_reqd_green_time_ratio": (1610743826, 2, (4, 0), (), "Dummy_reqd_green_time_ratio", None),
		"Dummy_reqd_time": (1610743819, 2, (4, 0), (), "Dummy_reqd_time", None),
		"Dummy_tmax": (1610743828, 2, (4, 0), (), "Dummy_tmax", None),
		"Dummy_tmin": (1610743827, 2, (4, 0), (), "Dummy_tmin", None),
		"Green_end": (1610743813, 2, (3, 0), (), "Green_end", None),
		"Green_start": (1610743812, 2, (3, 0), (), "Green_start", None),
		"Has_dummy": (1610743817, 2, (11, 0), (), "Has_dummy", None),
		"IsReferencePhase": (1610743822, 2, (11, 0), (), "IsReferencePhase", None),
		"Offset_change_time": (1610743823, 2, (3, 0), (), "Offset_change_time", None),
		"Phase_frequency": (1610743832, 2, (4, 0), (), "Phase_frequency", None),
		"Phase_frequency_option": (1610743833, 2, (3, 0), (), "Phase_frequency_option", None),
		"Phase_split_percent": (1610743816, 2, (4, 0), (), "Phase_split_percent", None),
		"Phase_time": (1610743809, 2, (3, 0), (), "Phase_time", None),
		"Position": (1610743808, 2, (3, 0), (), "Position", None),
		"Start_intergreen": (1610743814, 2, (3, 0), (), "Start_intergreen", None),
		"Terminating_intergreen": (1610743815, 2, (3, 0), (), "Terminating_intergreen", None),
		"Yellow_time": (1610743830, 2, (3, 0), (), "Yellow_time", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputPhaseMovTimingPath(DispatchBaseClass):
	CLSID = IID('{9454248A-D758-4959-98F8-AF6162DF5ACD}')
	coclass_clsid = IID('{84CB4043-3761-4F41-93D0-A36BD048C9F9}')

	_prop_map_get_ = {
		# Method 'OutputPhaseMovTimingPathMovements' returns object of type 'ISIAPIOutputPhaseMovTimingPathMovements'
		"OutputPhaseMovTimingPathMovements": (1610743810, 2, (9, 0), (), "OutputPhaseMovTimingPathMovements", '{136F8B85-9B4F-40DF-8014-2D01E74B6BD4}'),
		# Method 'Outputset' returns object of type 'ISIAPIOutputset'
		"Outputset": (1610743809, 2, (9, 0), (), "Outputset", '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}'),
		"Position": (1610743808, 2, (3, 0), (), "Position", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputPhaseMovTimingPathMovement(DispatchBaseClass):
	CLSID = IID('{68493C00-16A9-4DDA-891E-386354D4D43C}')
	coclass_clsid = IID('{1B8CC9B3-532D-453B-AF77-5CB719ECCA69}')

	_prop_map_get_ = {
		"Critical_mov": (1610743822, 2, (11, 0), (), "Critical_mov", None),
		"Destination": (1610743811, 2, (3, 0), (), "Destination", None),
		"Dummy_phase_original_position": (1610743816, 2, (3, 0), (), "Dummy_phase_original_position", None),
		"Eff_green": (1610743823, 2, (3, 0), (), "Eff_green", None),
		"End_phase": (1610743819, 2, (3, 0), (), "End_phase", None),
		"Green_time": (1610743817, 2, (3, 0), (), "Green_time", None),
		"Greenperiod": (1610743815, 2, (3, 0), (), "Greenperiod", None),
		"MC_class": (1610743812, 2, (3, 0), (), "MC_class", None),
		"MaxGreenPeriod": (1610743825, 2, (3, 0), (), "MaxGreenPeriod", None),
		"Mov_type": (1610743809, 2, (3, 0), (), "Mov_type", None),
		"MovementDisplayID": (1610743820, 2, (8, 0), (), "MovementDisplayID", None),
		"Origin": (1610743810, 2, (3, 0), (), "Origin", None),
		# Method 'OutputPhaseMovTimingPath' returns object of type 'ISIAPIOutputPhaseMovTimingPath'
		"OutputPhaseMovTimingPath": (1610743826, 2, (9, 0), (), "OutputPhaseMovTimingPath", '{9454248A-D758-4959-98F8-AF6162DF5ACD}'),
		"Ped_stage": (1610743814, 2, (3, 0), (), "Ped_stage", None),
		"Ped_type": (1610743813, 2, (3, 0), (), "Ped_type", None),
		"Position": (1610743808, 2, (3, 0), (), "Position", None),
		"Reqd_time": (1610743824, 2, (4, 0), (), "Reqd_time", None),
		"SiteDisplayID": (1610743821, 2, (8, 0), (), "SiteDisplayID", None),
		"Start_phase": (1610743818, 2, (3, 0), (), "Start_phase", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputPhaseMovTimingPathMovements(DispatchBaseClass):
	CLSID = IID('{136F8B85-9B4F-40DF-8014-2D01E74B6BD4}')
	coclass_clsid = IID('{1C744150-30B7-468A-AC2E-262F67C49910}')

	# Result is of type ISIAPIOutputPhaseMovTimingPathMovement
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{68493C00-16A9-4DDA-891E-386354D4D43C}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{68493C00-16A9-4DDA-891E-386354D4D43C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{68493C00-16A9-4DDA-891E-386354D4D43C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputPhaseMovTimingPaths(DispatchBaseClass):
	CLSID = IID('{5D48995D-44C9-40DE-A5EC-9460D1F8417C}')
	coclass_clsid = IID('{50CFC083-8D6F-423C-8C80-B976A18F15AE}')

	# Result is of type ISIAPIOutputPhaseMovTimingPath
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9454248A-D758-4959-98F8-AF6162DF5ACD}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9454248A-D758-4959-98F8-AF6162DF5ACD}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{9454248A-D758-4959-98F8-AF6162DF5ACD}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputPhases(DispatchBaseClass):
	CLSID = IID('{3D49DB13-5D95-4180-BFDE-49B38D78781F}')
	coclass_clsid = IID('{6180E4A3-7220-40A9-B67E-1A1E2980081F}')

	# Result is of type ISIAPIOutputPhase
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C186E5B6-87B7-4CBA-8D26-7190FC0709F1}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C186E5B6-87B7-4CBA-8D26-7190FC0709F1}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C186E5B6-87B7-4CBA-8D26-7190FC0709F1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputRouteMovementBasedPerson(DispatchBaseClass):
	CLSID = IID('{3C6C4EF3-04CC-4AD7-A16B-6643D85352C8}')
	coclass_clsid = IID('{F9033992-8196-424F-9725-D4E387E2110D}')

	_prop_map_get_ = {
		"RouteStopRate": (1610743814, 2, (4, 0), (), "RouteStopRate", None),
		"RouteStopRate_rate": (1610743815, 2, (4, 0), (), "RouteStopRate_rate", None),
		"TravelDelayAverage": (1610743813, 2, (4, 0), (), "TravelDelayAverage", None),
		"TravelDistanceAverage": (1610743809, 2, (4, 0), (), "TravelDistanceAverage", None),
		"TravelDistanceTotal": (1610743811, 2, (4, 0), (), "TravelDistanceTotal", None),
		"TravelSpeed": (1610743808, 2, (4, 0), (), "TravelSpeed", None),
		"TravelTimeAverage": (1610743810, 2, (4, 0), (), "TravelTimeAverage", None),
		"TravelTimeTotal": (1610743812, 2, (4, 0), (), "TravelTimeTotal", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputRouteMovementBasedVehicle(DispatchBaseClass):
	CLSID = IID('{7FE4BECE-3C4E-4607-8CCA-C099AEE0F8B9}')
	coclass_clsid = IID('{FDC3E673-E1B9-4AC2-9503-BCE42A55CD58}')

	_prop_map_get_ = {
		"CongestionCoefficient": (1610743823, 2, (4, 0), (), "CongestionCoefficient", None),
		"DesiredSpeed": (1610743819, 2, (4, 0), (), "DesiredSpeed", None),
		"DesiredSpeedMethod": (1610743818, 2, (3, 0), (), "DesiredSpeedMethod", None),
		"LevelOfService": (1610743820, 2, (3, 0), (), "LevelOfService", None),
		"RouteStopRate": (1610743816, 2, (4, 0), (), "RouteStopRate", None),
		"RouteStopRate_rate": (1610743817, 2, (4, 0), (), "RouteStopRate_rate", None),
		"SpeedEfficiency": (1610743822, 2, (4, 0), (), "SpeedEfficiency", None),
		"SpeedEfficiencyFlag": (1610743824, 2, (3, 0), (), "SpeedEfficiencyFlag", None),
		"TravelDelayAverage": (1610743814, 2, (4, 0), (), "TravelDelayAverage", None),
		"TravelDelayAverage_rate": (1610743815, 2, (4, 0), (), "TravelDelayAverage_rate", None),
		"TravelDistanceAverage": (1610743809, 2, (4, 0), (), "TravelDistanceAverage", None),
		"TravelDistanceTotal": (1610743812, 2, (4, 0), (), "TravelDistanceTotal", None),
		"TravelSpeed": (1610743808, 2, (4, 0), (), "TravelSpeed", None),
		"TravelTimeAverage": (1610743810, 2, (4, 0), (), "TravelTimeAverage", None),
		"TravelTimeAverage_rate": (1610743811, 2, (4, 0), (), "TravelTimeAverage_rate", None),
		"TravelTimeIndex": (1610743821, 2, (4, 0), (), "TravelTimeIndex", None),
		"TravelTimeTotal": (1610743813, 2, (4, 0), (), "TravelTimeTotal", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputSequence(DispatchBaseClass):
	CLSID = IID('{8832ED63-ACD1-45C0-B218-786FDF3B3E5C}')
	coclass_clsid = IID('{606A4EB4-6E73-4DB2-8E4A-610842F7F05B}')

	_prop_map_get_ = {
		"Adjusted_flow_ratio_total": (1610743815, 2, (4, 0), (), "Adjusted_flow_ratio_total", None),
		"Adjusted_lost_time_total": (1610743814, 2, (3, 0), (), "Adjusted_lost_time_total", None),
		"Cmaxsl_flag": (1610743822, 2, (3, 0), (), "Cmaxsl_flag", None),
		"Critical_in_network": (1610743824, 2, (3, 0), (), "Critical_in_network", None),
		"Cycle_time": (1610743809, 2, (3, 0), (), "Cycle_time", None),
		"Cycle_time_maximum": (1610743819, 2, (3, 0), (), "Cycle_time_maximum", None),
		"Cycle_time_maximum_flag": (1610743820, 2, (3, 0), (), "Cycle_time_maximum_flag", None),
		"Cycle_time_minimum": (1610743810, 2, (3, 0), (), "Cycle_time_minimum", None),
		"Cycle_time_minimum_flag": (1610743811, 2, (3, 0), (), "Cycle_time_minimum_flag", None),
		"Cycle_time_option": (1610743808, 2, (3, 0), (), "Cycle_time_option", None),
		"Cycle_time_option_flag": (1610743825, 2, (3, 0), (), "Cycle_time_option_flag", None),
		"Cycle_time_practical": (1610743812, 2, (3, 0), (), "Cycle_time_practical", None),
		"Largeyu_flag": (1610743823, 2, (3, 0), (), "Largeyu_flag", None),
		"Max_green_percent": (1610743813, 2, (4, 0), (), "Max_green_percent", None),
		# Method 'Phases' returns object of type 'ISIAPIOutputPhases'
		"Phases": (1610743818, 2, (9, 0), (), "Phases", '{3D49DB13-5D95-4180-BFDE-49B38D78781F}'),
		"Reqd_green_time_ratio_total": (1610743816, 2, (4, 0), (), "Reqd_green_time_ratio_total", None),
		"Reqd_movement_time_total": (1610743817, 2, (4, 0), (), "Reqd_movement_time_total", None),
		"Seq_position": (1610743826, 2, (3, 0), (), "Seq_position", None),
		"Warning_flag": (1610743821, 2, (3, 0), (), "Warning_flag", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputSitePedestrian(DispatchBaseClass):
	CLSID = IID('{5E3241AA-696A-4DAF-BDCA-C6C9AA13E0EB}')
	coclass_clsid = IID('{270364E1-ECE5-4E2E-A7D4-1337FC506CE9}')

	_prop_map_get_ = {
		"Deg_satn": (1610743825, 2, (4, 0), (), "Deg_satn", None),
		"Delay_control_average": (1610743809, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_average_worstmov": (1610743810, 2, (4, 0), (), "Delay_control_average_worstmov", None),
		"Delay_control_total": (1610743811, 2, (4, 0), (), "Delay_control_total", None),
		"Demand_flow_total": (1610743808, 2, (4, 0), (), "Demand_flow_total", None),
		"Level_of_service": (1610743812, 2, (8, 0), (), "Level_of_service", None),
		"Level_of_service_worstmov": (1610743813, 2, (8, 0), (), "Level_of_service_worstmov", None),
		"Operating_cost_rate": (1610743827, 2, (4, 0), (), "Operating_cost_rate", None),
		"Operating_cost_total": (1610743826, 2, (4, 0), (), "Operating_cost_total", None),
		"Performance_index": (1610743819, 2, (4, 0), (), "Performance_index", None),
		"Proportion_queued": (1610743818, 2, (4, 0), (), "Proportion_queued", None),
		"Queue_dist_maxback_mean": (1610743815, 2, (4, 0), (), "Queue_dist_maxback_mean", None),
		"Queue_maxback_mean": (1610743814, 2, (4, 0), (), "Queue_maxback_mean", None),
		"Stop_rate": (1610743816, 2, (4, 0), (), "Stop_rate", None),
		"Stops_total": (1610743817, 2, (4, 0), (), "Stops_total", None),
		"Travel_distance_average": (1610743821, 2, (4, 0), (), "Travel_distance_average", None),
		"Travel_distance_total": (1610743820, 2, (4, 0), (), "Travel_distance_total", None),
		"Travel_speed": (1610743824, 2, (4, 0), (), "Travel_speed", None),
		"Travel_time_average": (1610743823, 2, (4, 0), (), "Travel_time_average", None),
		"Travel_time_total": (1610743822, 2, (4, 0), (), "Travel_time_total", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputSitePerson(DispatchBaseClass):
	CLSID = IID('{53819F2B-01AB-464E-B46A-1DF4F967E8B7}')
	coclass_clsid = IID('{272D58B6-297A-4958-B030-4C7B65DE12B9}')

	_prop_map_get_ = {
		"Arrival_flow_total": (1610743809, 2, (4, 0), (), "Arrival_flow_total", None),
		"Carbon_dioxide_total": (1610743825, 2, (4, 0), (), "Carbon_dioxide_total", None),
		"Carbon_monoxide_total": (1610743827, 2, (4, 0), (), "Carbon_monoxide_total", None),
		"Delay_control_average": (1610743810, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_average_worstmov": (1610743811, 2, (4, 0), (), "Delay_control_average_worstmov", None),
		"Delay_control_total": (1610743812, 2, (4, 0), (), "Delay_control_total", None),
		"Demand_flow_total": (1610743808, 2, (4, 0), (), "Demand_flow_total", None),
		"Fuel_consumption_total": (1610743824, 2, (4, 0), (), "Fuel_consumption_total", None),
		"Hydrocarbons_total": (1610743826, 2, (4, 0), (), "Hydrocarbons_total", None),
		"Nox_total": (1610743828, 2, (4, 0), (), "Nox_total", None),
		"Operating_cost_rate": (1610743823, 2, (4, 0), (), "Operating_cost_rate", None),
		"Operating_cost_total": (1610743822, 2, (4, 0), (), "Operating_cost_total", None),
		"Performance_index": (1610743816, 2, (4, 0), (), "Performance_index", None),
		"Proportion_queued": (1610743815, 2, (4, 0), (), "Proportion_queued", None),
		"Stop_rate": (1610743813, 2, (4, 0), (), "Stop_rate", None),
		"Stops_total": (1610743814, 2, (4, 0), (), "Stops_total", None),
		"Travel_distance_average": (1610743818, 2, (4, 0), (), "Travel_distance_average", None),
		"Travel_distance_total": (1610743817, 2, (4, 0), (), "Travel_distance_total", None),
		"Travel_speed": (1610743821, 2, (4, 0), (), "Travel_speed", None),
		"Travel_time_average": (1610743820, 2, (4, 0), (), "Travel_time_average", None),
		"Travel_time_total": (1610743819, 2, (4, 0), (), "Travel_time_total", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputSiteRoute(DispatchBaseClass):
	CLSID = IID('{E60C8BBE-4044-4AF0-900F-0840C61D77F7}')
	coclass_clsid = IID('{2E78F5C0-56C2-4BF1-B1D1-1A62D5A8420D}')

	_prop_map_get_ = {
		"Coord_mov_displayed_green_time": (1610743815, 2, (3, 0), (), "Coord_mov_displayed_green_time", None),
		"Coord_mov_displayed_start_time": (1610743814, 2, (3, 0), (), "Coord_mov_displayed_start_time", None),
		"Coord_mov_eff_start_time": (1610743813, 2, (3, 0), (), "Coord_mov_eff_start_time", None),
		"Coord_mov_effgreen": (1610743812, 2, (3, 0), (), "Coord_mov_effgreen", None),
		"Coord_mov_phasetime": (1610743811, 2, (3, 0), (), "Coord_mov_phasetime", None),
		# Method 'Outputset' returns object of type 'ISIAPIOutputset'
		"Outputset": (1610743816, 2, (9, 0), (), "Outputset", '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}'),
		"RouteName": (1610743808, 2, (8, 0), (), "RouteName", None),
		"RouteSignalOffsetPriority": (1610743809, 2, (3, 0), (), "RouteSignalOffsetPriority", None),
		"Route_id": (1610743810, 2, (3, 0), (), "Route_id", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputSiteRoutes(DispatchBaseClass):
	CLSID = IID('{A30A36F9-FA16-4D54-9338-1357D2FF0D24}')
	coclass_clsid = IID('{5507EC83-9958-413B-BF33-40958E76EF71}')

	def Exists(self, RouteName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), ((8, 1),),RouteName
			)

	# Result is of type ISIAPIOutputSiteRoute
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, RouteName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),RouteName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E60C8BBE-4044-4AF0-900F-0840C61D77F7}')
		return ret

	# Result is of type ISIAPIOutputSiteRoute
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{E60C8BBE-4044-4AF0-900F-0840C61D77F7}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743811, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, RouteName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),RouteName
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E60C8BBE-4044-4AF0-900F-0840C61D77F7}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E60C8BBE-4044-4AF0-900F-0840C61D77F7}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743811, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIOutputSiteVehicle(DispatchBaseClass):
	CLSID = IID('{EB43DD42-CCFE-4728-A81E-0246C4344B2F}')
	coclass_clsid = IID('{5AE191CE-B05A-4EC0-93A2-7C18E4C68F62}')

	_prop_map_get_ = {
		"Analysis_method": (1610743863, 2, (3, 0), (), "Analysis_method", None),
		"Avg_num_of_cycles_to_depart": (1610743871, 2, (4, 0), (), "Avg_num_of_cycles_to_depart", None),
		"Capacity_adj_flag_worstlane": (1610743870, 2, (3, 0), (), "Capacity_adj_flag_worstlane", None),
		"Capacity_adj_worstlane": (1610743869, 2, (4, 0), (), "Capacity_adj_worstlane", None),
		"Capacity_effective": (1610743816, 2, (4, 0), (), "Capacity_effective", None),
		"Capacity_lane_total": (1610743817, 2, (4, 0), (), "Capacity_lane_total", None),
		"Capacity_mov_total": (1610743818, 2, (4, 0), (), "Capacity_mov_total", None),
		"Carbon_dioxide_rate": (1610743858, 2, (4, 0), (), "Carbon_dioxide_rate", None),
		"Carbon_dioxide_total": (1610743852, 2, (4, 0), (), "Carbon_dioxide_total", None),
		"Carbon_monoxide_rate": (1610743860, 2, (4, 0), (), "Carbon_monoxide_rate", None),
		"Carbon_monoxide_total": (1610743854, 2, (4, 0), (), "Carbon_monoxide_total", None),
		"CongestionCoefficient": (1610743890, 2, (4, 0), (), "CongestionCoefficient", None),
		"Deg_satn": (1610743819, 2, (4, 0), (), "Deg_satn", None),
		"Delay_control_average": (1610743821, 2, (4, 0), (), "Delay_control_average", None),
		"Delay_control_average_worstlane": (1610743823, 2, (4, 0), (), "Delay_control_average_worstlane", None),
		"Delay_control_average_worstmov": (1610743822, 2, (4, 0), (), "Delay_control_average_worstmov", None),
		"Delay_control_total": (1610743824, 2, (4, 0), (), "Delay_control_total", None),
		"Delay_geometric_average": (1610743826, 2, (4, 0), (), "Delay_geometric_average", None),
		"Delay_stopline_average": (1610743825, 2, (4, 0), (), "Delay_stopline_average", None),
		"DesiredSpeed": (1610743886, 2, (4, 0), (), "DesiredSpeed", None),
		"DesiredSpeedMethod": (1610743887, 2, (3, 0), (), "DesiredSpeedMethod", None),
		"DesiredSpeedProgram": (1610743888, 2, (4, 0), (), "DesiredSpeedProgram", None),
		"Flow_HV": (1610743810, 2, (4, 0), (), "Flow_HV", None),
		"Flow_HV_capconstr": (1610743814, 2, (4, 0), (), "Flow_HV_capconstr", None),
		"Flow_HV_pct": (1610743811, 2, (4, 0), (), "Flow_HV_pct", None),
		"Flow_HV_pct_capconstr": (1610743815, 2, (4, 0), (), "Flow_HV_pct_capconstr", None),
		"Flow_LV": (1610743809, 2, (4, 0), (), "Flow_LV", None),
		"Flow_LV_capconstr": (1610743813, 2, (4, 0), (), "Flow_LV_capconstr", None),
		"Flow_total": (1610743808, 2, (4, 0), (), "Flow_total", None),
		"Flow_total_capconstr": (1610743812, 2, (4, 0), (), "Flow_total_capconstr", None),
		"Fuel_consumption_rate": (1610743857, 2, (4, 0), (), "Fuel_consumption_rate", None),
		"Fuel_consumption_total": (1610743851, 2, (4, 0), (), "Fuel_consumption_total", None),
		"Hydrocarbons_rate": (1610743859, 2, (4, 0), (), "Hydrocarbons_rate", None),
		"Hydrocarbons_total": (1610743853, 2, (4, 0), (), "Hydrocarbons_total", None),
		"Idling_time_average": (1610743862, 2, (4, 0), (), "Idling_time_average", None),
		"Level_of_service": (1610743827, 2, (8, 0), (), "Level_of_service", None),
		"Level_of_service_av_int_delay": (1610743828, 2, (8, 0), (), "Level_of_service_av_int_delay", None),
		"Level_of_service_worstlane": (1610743830, 2, (8, 0), (), "Level_of_service_worstlane", None),
		"Level_of_service_worstmov": (1610743829, 2, (8, 0), (), "Level_of_service_worstmov", None),
		"Max_SubIterations": (1610743883, 2, (3, 0), (), "Max_SubIterations", None),
		"Max_TimIterations": (1610743877, 2, (3, 0), (), "Max_TimIterations", None),
		"Max_subit_capacity_diff": (1610743884, 2, (4, 0), (), "Max_subit_capacity_diff", None),
		"Max_subit_capacity_percent": (1610743885, 2, (4, 0), (), "Max_subit_capacity_percent", None),
		"Max_subit_dx_percent": (1610743879, 2, (4, 0), (), "Max_subit_dx_percent", None),
		"Max_subit_dx_percent_prev": (1610743880, 2, (4, 0), (), "Max_subit_dx_percent_prev", None),
		"Max_subit_dx_percent_prev2": (1610743881, 2, (4, 0), (), "Max_subit_dx_percent_prev2", None),
		"Max_timit_dx_percent": (1610743873, 2, (4, 0), (), "Max_timit_dx_percent", None),
		"Max_timit_dx_percent_prev": (1610743874, 2, (4, 0), (), "Max_timit_dx_percent_prev", None),
		"Max_timit_dx_percent_prev2": (1610743875, 2, (4, 0), (), "Max_timit_dx_percent_prev2", None),
		"Model_flowcap_vari_index": (1610743878, 2, (4, 0), (), "Model_flowcap_vari_index", None),
		"Model_timing_vari_index": (1610743872, 2, (4, 0), (), "Model_timing_vari_index", None),
		"Nox_rate": (1610743861, 2, (4, 0), (), "Nox_rate", None),
		"Nox_total": (1610743855, 2, (4, 0), (), "Nox_total", None),
		"Operating_cost_rate": (1610743856, 2, (4, 0), (), "Operating_cost_rate", None),
		"Operating_cost_total": (1610743850, 2, (4, 0), (), "Operating_cost_total", None),
		"Performance_index": (1610743844, 2, (4, 0), (), "Performance_index", None),
		"Practical_spare_capacity": (1610743820, 2, (4, 0), (), "Practical_spare_capacity", None),
		"Proportion_queued": (1610743843, 2, (4, 0), (), "Proportion_queued", None),
		"Queue_cycav_mean": (1610743831, 2, (4, 0), (), "Queue_cycav_mean", None),
		"Queue_cycav_percentile": (1610743832, 2, (4, 0), (), "Queue_cycav_percentile", None),
		"Queue_dist_cycav_mean": (1610743835, 2, (4, 0), (), "Queue_dist_cycav_mean", None),
		"Queue_dist_cycav_percentile": (1610743836, 2, (4, 0), (), "Queue_dist_cycav_percentile", None),
		"Queue_dist_greenstart_mean": (1610743867, 2, (4, 0), (), "Queue_dist_greenstart_mean", None),
		"Queue_dist_greenstart_percentile": (1610743868, 2, (4, 0), (), "Queue_dist_greenstart_percentile", None),
		"Queue_dist_maxback_mean": (1610743837, 2, (4, 0), (), "Queue_dist_maxback_mean", None),
		"Queue_dist_maxback_percentile": (1610743838, 2, (4, 0), (), "Queue_dist_maxback_percentile", None),
		"Queue_greenstart_mean": (1610743865, 2, (4, 0), (), "Queue_greenstart_mean", None),
		"Queue_greenstart_percentile": (1610743866, 2, (4, 0), (), "Queue_greenstart_percentile", None),
		"Queue_maxback_mean": (1610743833, 2, (4, 0), (), "Queue_maxback_mean", None),
		"Queue_maxback_percentile": (1610743834, 2, (4, 0), (), "Queue_maxback_percentile", None),
		"Queue_storage_ratio_avg": (1610743839, 2, (4, 0), (), "Queue_storage_ratio_avg", None),
		"Queue_storage_ratio_percentile": (1610743840, 2, (4, 0), (), "Queue_storage_ratio_percentile", None),
		"SpeedEfficiency": (1610743864, 2, (4, 0), (), "SpeedEfficiency", None),
		"SpeedEfficiencyFlag": (1610743891, 2, (3, 0), (), "SpeedEfficiencyFlag", None),
		"Stop_rate": (1610743841, 2, (4, 0), (), "Stop_rate", None),
		"Stops_total": (1610743842, 2, (4, 0), (), "Stops_total", None),
		"SubIterationsCount": (1610743882, 2, (3, 0), (), "SubIterationsCount", None),
		"TimIterationsCount": (1610743876, 2, (3, 0), (), "TimIterationsCount", None),
		"TravelTimeIndex": (1610743889, 2, (4, 0), (), "TravelTimeIndex", None),
		"Travel_distance_average": (1610743846, 2, (4, 0), (), "Travel_distance_average", None),
		"Travel_distance_total": (1610743845, 2, (4, 0), (), "Travel_distance_total", None),
		"Travel_speed": (1610743849, 2, (4, 0), (), "Travel_speed", None),
		"Travel_time_average": (1610743848, 2, (4, 0), (), "Travel_time_average", None),
		"Travel_time_total": (1610743847, 2, (4, 0), (), "Travel_time_total", None),
		"Travel_time_total_at_desired_speed": (1610743892, 2, (4, 0), (), "Travel_time_total_at_desired_speed", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIOutputset(DispatchBaseClass):
	CLSID = IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')
	coclass_clsid = IID('{5CCD43AB-186C-4353-BA54-9F5C7081FC75}')

	_prop_map_get_ = {
		"Analysis_method": (1610743822, 2, (3, 0), (), "Analysis_method", None),
		"Analysis_method_flag": (1610743829, 2, (3, 0), (), "Analysis_method_flag", None),
		"Generated": (1610743808, 2, (7, 0), (), "Generated", None),
		"GeneratedByVersion": (1610743821, 2, (8, 0), (), "GeneratedByVersion", None),
		"HasSIDRUNAWSCMsg": (1610743832, 2, (11, 0), (), "HasSIDRUNAWSCMsg", None),
		"HasSIDRUNUnsettledMsg": (1610743831, 2, (11, 0), (), "HasSIDRUNUnsettledMsg", None),
		"NwSiteOffset": (1610743824, 2, (3, 0), (), "NwSiteOffset", None),
		"NwSite_SignalPlatoonMode": (1610743825, 2, (3, 0), (), "NwSite_SignalPlatoonMode", None),
		# Method 'OutputAnalysis' returns object of type 'ISIAPIOutputAnalysis'
		"OutputAnalysis": (1610743817, 2, (9, 0), (), "OutputAnalysis", '{91779742-CF41-42AD-963E-22F788CA96F4}'),
		# Method 'OutputGraphTuples' returns object of type 'ISIAPIOutputGraphTuples'
		"OutputGraphTuples": (1610743818, 2, (9, 0), (), "OutputGraphTuples", '{3E26EBE1-0955-49EB-8E9F-8CC3B645361B}'),
		# Method 'OutputLegPersons' returns object of type 'ISIAPIOutputLegPersons'
		"OutputLegPersons": (1610743826, 2, (9, 0), (), "OutputLegPersons", '{D31B97D0-0C54-45B5-9529-1DFF92F8B457}'),
		# Method 'OutputLegs' returns object of type 'ISIAPIOutputLegs'
		"OutputLegs": (1610743812, 2, (9, 0), (), "OutputLegs", '{7A84E80F-58FD-4C53-94B3-29713CCED51C}'),
		# Method 'OutputMeteredRoundabout' returns object of type 'ISIAPIOutputMeteredRoundabout'
		"OutputMeteredRoundabout": (1610743815, 2, (9, 0), (), "OutputMeteredRoundabout", '{B11203CA-CABF-43DF-9156-6898CA85836F}'),
		# Method 'OutputMovementPeds' returns object of type 'ISIAPIOutputMovementPeds'
		"OutputMovementPeds": (1610743814, 2, (9, 0), (), "OutputMovementPeds", '{3C02979B-5CC8-41CC-86DC-1884428878F1}'),
		# Method 'OutputMovementPersonODs' returns object of type 'ISIAPIOutputMovementPersonODs'
		"OutputMovementPersonODs": (1610743827, 2, (9, 0), (), "OutputMovementPersonODs", '{C1ADE01E-D8D6-44AD-8FB2-18158BD070F1}'),
		# Method 'OutputMovementVehicleODs' returns object of type 'ISIAPIOutputMovementVehicleODs'
		"OutputMovementVehicleODs": (1610743813, 2, (9, 0), (), "OutputMovementVehicleODs", '{F7CF3309-E6B6-4637-93F1-DC805C88F46A}'),
		# Method 'OutputMultiSequenceAnalyses' returns object of type 'ISIAPIOutputMultiSequenceAnalyses'
		"OutputMultiSequenceAnalyses": (1610743833, 2, (9, 0), (), "OutputMultiSequenceAnalyses", '{CD988BB1-BF23-45C3-B098-74FABCE0BDF2}'),
		# Method 'OutputPhaseMovTimingPaths' returns object of type 'ISIAPIOutputPhaseMovTimingPaths'
		"OutputPhaseMovTimingPaths": (1610743830, 2, (9, 0), (), "OutputPhaseMovTimingPaths", '{5D48995D-44C9-40DE-A5EC-9460D1F8417C}'),
		# Method 'OutputSequence' returns object of type 'ISIAPIOutputSequence'
		"OutputSequence": (1610743816, 2, (9, 0), (), "OutputSequence", '{8832ED63-ACD1-45C0-B218-786FDF3B3E5C}'),
		# Method 'OutputSitePedestrian' returns object of type 'ISIAPIOutputSitePedestrian'
		"OutputSitePedestrian": (1610743810, 2, (9, 0), (), "OutputSitePedestrian", '{5E3241AA-696A-4DAF-BDCA-C6C9AA13E0EB}'),
		# Method 'OutputSitePerson' returns object of type 'ISIAPIOutputSitePerson'
		"OutputSitePerson": (1610743811, 2, (9, 0), (), "OutputSitePerson", '{53819F2B-01AB-464E-B46A-1DF4F967E8B7}'),
		# Method 'OutputSiteRoutes' returns object of type 'ISIAPIOutputSiteRoutes'
		"OutputSiteRoutes": (1610743828, 2, (9, 0), (), "OutputSiteRoutes", '{A30A36F9-FA16-4D54-9338-1357D2FF0D24}'),
		# Method 'OutputSiteVehicle' returns object of type 'ISIAPIOutputSiteVehicle'
		"OutputSiteVehicle": (1610743809, 2, (9, 0), (), "OutputSiteVehicle", '{EB43DD42-CCFE-4728-A81E-0246C4344B2F}'),
		# Method 'Site' returns object of type 'ISIAPISite'
		"Site": (1610743819, 2, (9, 0), (), "Site", '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}'),
		"TWSC_calib_adjusted": (1610743823, 2, (3, 0), (), "TWSC_calib_adjusted", None),
		# Method 'networkSite' returns object of type 'ISIAPINetworkSite'
		"networkSite": (1610743820, 2, (9, 0), (), "networkSite", '{4888B50C-984E-4865-B2CE-4FA9B66C2622}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIPhase(DispatchBaseClass):
	CLSID = IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')
	coclass_clsid = IID('{601FC223-4405-429B-A762-BC05946EDE1E}')

	_prop_map_get_ = {
		"All_red_time": (1610743820, 2, (3, 0), (), "All_red_time", None),
		"Dummy_maximum_green_time": (1610743830, 2, (3, 0), (), "Dummy_maximum_green_time", None),
		"Dummy_maximum_green_time_user": (1610743828, 2, (11, 0), (), "Dummy_maximum_green_time_user", None),
		"Dummy_minimum_green_time": (1610743826, 2, (3, 0), (), "Dummy_minimum_green_time", None),
		"Dummy_minimum_green_time_user": (1610743824, 2, (11, 0), (), "Dummy_minimum_green_time_user", None),
		"Has_dummy": (1610743822, 2, (11, 0), (), "Has_dummy", None),
		"IsReferencePhase": (1610743814, 2, (11, 0), (), "IsReferencePhase", None),
		"Is_variable": (1610743812, 2, (11, 0), (), "Is_variable", None),
		"Minimum_time": (1610743832, 2, (3, 0), (), "Minimum_time", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		"Phase_frequency": (1610743839, 2, (4, 0), (), "Phase_frequency", None),
		"Phase_frequency_user": (1610743837, 2, (11, 0), (), "Phase_frequency_user", None),
		"Phase_id": (1610743808, 2, (3, 0), (), "Phase_id", None),
		"Phase_time": (1610743816, 2, (3, 0), (), "Phase_time", None),
		# Method 'Phasemovement_peds' returns object of type 'ISIAPIPhasemovement_peds'
		"Phasemovement_peds": (1610743835, 2, (9, 0), (), "Phasemovement_peds", '{8F802394-B3B4-4D06-8EA2-A0247C600A86}'),
		# Method 'Phasemovement_vehicles' returns object of type 'ISIAPIPhasemovement_vehicles'
		"Phasemovement_vehicles": (1610743834, 2, (9, 0), (), "Phasemovement_vehicles", '{843F1163-A090-4AA1-9AB4-8CF90C0A8BFF}'),
		"Position": (1610743811, 2, (3, 0), (), "Position", None),
		# Method 'Sequence' returns object of type 'ISIAPISequence'
		"Sequence": (1610743836, 2, (9, 0), (), "Sequence", '{B528481B-1627-4D64-9F55-5D7E943539A6}'),
		"Yellow_time": (1610743818, 2, (3, 0), (), "Yellow_time", None),
	}
	_prop_map_put_ = {
		"All_red_time": ((1610743820, LCID, 4, 0),()),
		"Dummy_maximum_green_time": ((1610743830, LCID, 4, 0),()),
		"Dummy_maximum_green_time_user": ((1610743828, LCID, 4, 0),()),
		"Dummy_minimum_green_time": ((1610743826, LCID, 4, 0),()),
		"Dummy_minimum_green_time_user": ((1610743824, LCID, 4, 0),()),
		"Has_dummy": ((1610743822, LCID, 4, 0),()),
		"IsReferencePhase": ((1610743814, LCID, 4, 0),()),
		"Is_variable": ((1610743812, LCID, 4, 0),()),
		"Minimum_time": ((1610743832, LCID, 4, 0),()),
		"Name": ((1610743809, LCID, 4, 0),()),
		"Phase_frequency": ((1610743839, LCID, 4, 0),()),
		"Phase_frequency_user": ((1610743837, LCID, 4, 0),()),
		"Phase_time": ((1610743816, LCID, 4, 0),()),
		"Yellow_time": ((1610743818, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIPhasemovement_ped(DispatchBaseClass):
	CLSID = IID('{77A6AC80-AF80-4EED-9493-561C3B928907}')
	coclass_clsid = IID('{AE225517-D441-49D9-926F-18E976A6A05C}')

	_prop_map_get_ = {
		"Movement_ped_origin": (1610743808, 2, (3, 0), (), "Movement_ped_origin", None),
		"Movement_ped_stage": (1610743810, 2, (3, 0), (), "Movement_ped_stage", None),
		"Movement_ped_type": (1610743809, 2, (3, 0), (), "Movement_ped_type", None),
		# Method 'Phase' returns object of type 'ISIAPIPhase'
		"Phase": (1610743817, 2, (9, 0), (), "Phase", '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}'),
		"Running": (1610743811, 2, (11, 0), (), "Running", None),
		"Terminates": (1610743813, 2, (11, 0), (), "Terminates", None),
		"Undetected": (1610743815, 2, (11, 0), (), "Undetected", None),
	}
	_prop_map_put_ = {
		"Running": ((1610743811, LCID, 4, 0),()),
		"Terminates": ((1610743813, LCID, 4, 0),()),
		"Undetected": ((1610743815, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIPhasemovement_peds(DispatchBaseClass):
	CLSID = IID('{8F802394-B3B4-4D06-8EA2-A0247C600A86}')
	coclass_clsid = IID('{66368ABF-3FE9-46B0-83AB-E291B28BD09D}')

	# Result is of type ISIAPIPhasemovement_ped
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Type=defaultNamedNotOptArg, Origin=defaultNamedNotOptArg, Stage=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1), (3, 1)),Type
			, Origin, Stage)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{77A6AC80-AF80-4EED-9493-561C3B928907}')
		return ret

	def PhasemovementPedExists(self, Type=defaultNamedNotOptArg, Origin=defaultNamedNotOptArg, Stage=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),Type
			, Origin, Stage)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Type=defaultNamedNotOptArg, Origin=defaultNamedNotOptArg, Stage=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1), (3, 1)),Type
			, Origin, Stage)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{77A6AC80-AF80-4EED-9493-561C3B928907}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{77A6AC80-AF80-4EED-9493-561C3B928907}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIPhasemovement_vehicle(DispatchBaseClass):
	CLSID = IID('{96854CD8-BA75-4EB1-8320-7DCC929C2503}')
	coclass_clsid = IID('{B18833B0-DFF8-4104-8CF7-CC6E72B2A0CC}')

	_prop_map_get_ = {
		"Is_red_arrow_drop_off_enabled": (1610743818, 2, (11, 0), (), "Is_red_arrow_drop_off_enabled", None),
		"MC_class": (1610743810, 2, (3, 0), (), "MC_class", None),
		"Movement_vehicle_destination": (1610743809, 2, (3, 0), (), "Movement_vehicle_destination", None),
		"Movement_vehicle_origin": (1610743808, 2, (3, 0), (), "Movement_vehicle_origin", None),
		# Method 'Phase' returns object of type 'ISIAPIPhase'
		"Phase": (1610743817, 2, (9, 0), (), "Phase", '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}'),
		"Red_arrow_drop_off": (1610743820, 2, (3, 0), (), "Red_arrow_drop_off", None),
		"Running": (1610743811, 2, (11, 0), (), "Running", None),
		"Terminates": (1610743813, 2, (11, 0), (), "Terminates", None),
		"Undetected": (1610743815, 2, (11, 0), (), "Undetected", None),
	}
	_prop_map_put_ = {
		"Is_red_arrow_drop_off_enabled": ((1610743818, LCID, 4, 0),()),
		"Red_arrow_drop_off": ((1610743820, LCID, 4, 0),()),
		"Running": ((1610743811, LCID, 4, 0),()),
		"Terminates": ((1610743813, LCID, 4, 0),()),
		"Undetected": ((1610743815, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIPhasemovement_vehicles(DispatchBaseClass):
	CLSID = IID('{843F1163-A090-4AA1-9AB4-8CF90C0A8BFF}')
	coclass_clsid = IID('{3E7EF29A-8A66-4DDE-B091-F3D882406164}')

	# Result is of type ISIAPIPhasemovement_vehicle
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1), (3, 1)),Origin
			, Destination, mcClass)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{96854CD8-BA75-4EB1-8320-7DCC929C2503}')
		return ret

	def PhasemovementVehicleExists(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg, mcClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),Origin
			, Destination, mcClass)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1), (3, 1)),Origin
			, Destination, mcClass)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{96854CD8-BA75-4EB1-8320-7DCC929C2503}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{96854CD8-BA75-4EB1-8320-7DCC929C2503}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIPhases(DispatchBaseClass):
	CLSID = IID('{98B4AB9E-189E-4149-BFE9-0DD10CA8BBEF}')
	coclass_clsid = IID('{B17972E8-D253-40CB-8820-68BBE891708A}')

	# Result is of type ISIAPIPhase
	def GetPhaseByID(self, Phase_id=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743811, LCID, 1, (9, 0), ((3, 1),),Phase_id
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPhaseByID', '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')
		return ret

	# Result is of type ISIAPIPhase
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, phasename=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),phasename
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')
		return ret

	# Result is of type ISIAPIPhase
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')
		return ret

	def PhaseExists(self, phasename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), ((8, 1),),phasename
			)

	_prop_map_get_ = {
		"Count": (1610743812, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, phasename=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),phasename
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743812, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIProject(DispatchBaseClass):
	CLSID = IID('{5817180B-2283-40FB-8068-C2F2D656EF04}')
	coclass_clsid = IID('{AA3D5162-1291-44E3-B6DB-168A66FA698F}')

	# Result is of type ISIAPINetworkFolder
	def AddNetworkFolder(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743818, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddNetworkFolder', '{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')
		return ret

	# Result is of type ISIAPISiteFolder
	def AddSiteFolder(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743815, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddSiteFolder', '{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')
		return ret

	def ImportNetworksFromProject(self, projectFilePath=defaultNamedNotOptArg, networkNames=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (3, 0), ((8, 1), (8, 1)),projectFilePath
			, networkNames)

	def ImportSitesFromProject(self, projectFilePath=defaultNamedNotOptArg, siteNames=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (3, 0), ((8, 1), (8, 1)),projectFilePath
			, siteNames)

	def MoveNetworkFolderTo(self, NetworkFolder=defaultNamedNotOptArg, newPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743820, LCID, 1, (11, 0), ((9, 1), (3, 1)),NetworkFolder
			, newPosition)

	def MoveSiteFolderTo(self, siteFolder=defaultNamedNotOptArg, newPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743817, LCID, 1, (11, 0), ((9, 1), (3, 1)),siteFolder
			, newPosition)

	def RemoveNetworkFolder(self, NetworkFolder=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743819, LCID, 1, (11, 0), ((9, 1),),NetworkFolder
			)

	def RemoveSiteFolder(self, siteFolder=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743816, LCID, 1, (11, 0), ((9, 1),),siteFolder
			)

	def UpdateModifiedInfo(self):
		return self._oleobj_.InvokeTypes(1610743812, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"LastErrorMessage": (1610743809, 2, (8, 0), (), "LastErrorMessage", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		# Method 'NetworkFolders' returns object of type 'ISIAPINetworkFolders'
		"NetworkFolders": (1610743811, 2, (9, 0), (), "NetworkFolders", '{12AD1FBE-8A7B-4CB9-9DD5-F233FC8FC13C}'),
		# Method 'SiteFolders' returns object of type 'ISIAPISiteFolders'
		"SiteFolders": (1610743810, 2, (9, 0), (), "SiteFolders", '{9712E108-061B-4BB9-AC11-8ADECF24EA13}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIRoute(DispatchBaseClass):
	CLSID = IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')
	coclass_clsid = IID('{F41B79F2-95A5-485C-B977-48171C90931E}')

	# Result is of type ISIAPIRouteNwSite
	def AddRouteNwSite(self, networkSite=defaultNamedNotOptArg, Origin=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743841, LCID, 1, (9, 0), ((9, 1), (3, 1), (3, 1)),networkSite
			, Origin, Destination)
		if ret is not None:
			ret = Dispatch(ret, 'AddRouteNwSite', '{58C442E7-0E64-47B5-AFFA-99BABCE5435E}')
		return ret

	def CheckIsValidForSignalOffsetCalc(self):
		return self._oleobj_.InvokeTypes(1610743842, LCID, 1, (11, 0), (),)

	def Process(self):
		return self._oleobj_.InvokeTypes(1610743844, LCID, 1, (11, 0), (),)

	def RemoveOutputData(self):
		return self._oleobj_.InvokeTypes(1610743853, LCID, 1, (11, 0), (),)

	def RemoveRouteNwSite(self, routeNwSite=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743845, LCID, 1, (11, 0), ((9, 1),),routeNwSite
			)

	def UpdateModifiedInfo(self):
		return self._oleobj_.InvokeTypes(1610743843, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"Created_by": (1610743830, 2, (8, 0), (), "Created_by", None),
		"Created_by_company": (1610743831, 2, (8, 0), (), "Created_by_company", None),
		"Created_date": (1610743829, 2, (7, 0), (), "Created_date", None),
		"Created_version": (1610743832, 2, (8, 0), (), "Created_version", None),
		"IsIncludedInOutputNetworkByRoutes": (1610743819, 2, (11, 0), (), "IsIncludedInOutputNetworkByRoutes", None),
		"IsIncludedInProjectSummary": (1610743846, 2, (11, 0), (), "IsIncludedInProjectSummary", None),
		"IsIncludedInSignalOffsetCal": (1610743821, 2, (11, 0), (), "IsIncludedInSignalOffsetCal", None),
		"Is_time_distance_reverse_included": (1610743848, 2, (11, 0), (), "Is_time_distance_reverse_included", None),
		"LOSMethod": (1610743815, 2, (3, 0), (), "LOSMethod", None),
		"LastErrorMessage": (1610743840, 2, (8, 0), (), "LastErrorMessage", None),
		"Modified_by": (1610743834, 2, (8, 0), (), "Modified_by", None),
		"Modified_by_company": (1610743835, 2, (8, 0), (), "Modified_by_company", None),
		"Modified_date": (1610743833, 2, (7, 0), (), "Modified_date", None),
		"Modified_version": (1610743836, 2, (8, 0), (), "Modified_version", None),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		# Method 'Network' returns object of type 'ISIAPINetwork'
		"Network": (1610743838, 2, (9, 0), (), "Network", '{C5A62A3D-7D9C-4544-8547-499D4C770332}'),
		# Method 'OutputRoute' returns object of type 'ISIAPIOutputNetwork'
		"OutputRoute": (1610743839, 2, (9, 0), (), "OutputRoute", '{5E551751-0DA8-4E10-931A-D474F6FFBB27}'),
		"Position": (1610743812, 2, (3, 0), (), "Position", None),
		"RouteID": (1610743810, 2, (8, 0), (), "RouteID", None),
		# Method 'RouteMCs' returns object of type 'ISIAPIRouteMCs'
		"RouteMCs": (1610743852, 2, (9, 0), (), "RouteMCs", '{BBE52DD6-5D32-4984-A42B-E5F24F27EF13}'),
		# Method 'RouteNwSites' returns object of type 'ISIAPIRouteNwSites'
		"RouteNwSites": (1610743837, 2, (9, 0), (), "RouteNwSites", '{8FF9FA61-FA15-4F9C-95E4-3F02656F6F14}'),
		"RouteSummaryOption": (1610743817, 2, (3, 0), (), "RouteSummaryOption", None),
		"ShowSecondaryPlatoons": (1610743854, 2, (11, 0), (), "ShowSecondaryPlatoons", None),
		"SignalOffsetCalMCClass": (1610743827, 2, (3, 0), (), "SignalOffsetCalMCClass", None),
		"SignalOffsetMethod": (1610743825, 2, (3, 0), (), "SignalOffsetMethod", None),
		"SignalOffsetPriority": (1610743823, 2, (3, 0), (), "SignalOffsetPriority", None),
		"Time_distance_direction": (1610743850, 2, (3, 0), (), "Time_distance_direction", None),
		"Title": (1610743813, 2, (8, 0), (), "Title", None),
	}
	_prop_map_put_ = {
		"IsIncludedInOutputNetworkByRoutes": ((1610743819, LCID, 4, 0),()),
		"IsIncludedInProjectSummary": ((1610743846, LCID, 4, 0),()),
		"IsIncludedInSignalOffsetCal": ((1610743821, LCID, 4, 0),()),
		"Is_time_distance_reverse_included": ((1610743848, LCID, 4, 0),()),
		"LOSMethod": ((1610743815, LCID, 4, 0),()),
		"Name": ((1610743808, LCID, 4, 0),()),
		"RouteID": ((1610743810, LCID, 4, 0),()),
		"RouteSummaryOption": ((1610743817, LCID, 4, 0),()),
		"ShowSecondaryPlatoons": ((1610743854, LCID, 4, 0),()),
		"SignalOffsetCalMCClass": ((1610743827, LCID, 4, 0),()),
		"SignalOffsetMethod": ((1610743825, LCID, 4, 0),()),
		"SignalOffsetPriority": ((1610743823, LCID, 4, 0),()),
		"Time_distance_direction": ((1610743850, LCID, 4, 0),()),
		"Title": ((1610743813, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIRouteMC(DispatchBaseClass):
	CLSID = IID('{74F4BB54-522D-4628-B31B-1A74786A6487}')
	coclass_clsid = IID('{E1AE119F-DBA4-4CFC-B95A-58A0F45607D0}')

	_prop_map_get_ = {
		"DesiredSpeed": (1610743811, 2, (4, 0), (), "DesiredSpeed", None),
		"DesiredSpeedMethod": (1610743809, 2, (3, 0), (), "DesiredSpeedMethod", None),
		"LowerLimitOfSpeedEfficiency": (1610743813, 2, (4, 0), (), "LowerLimitOfSpeedEfficiency", None),
		"MC_class": (1610743808, 2, (3, 0), (), "MC_class", None),
		# Method 'route' returns object of type 'ISIAPIRoute'
		"route": (1610743815, 2, (9, 0), (), "route", '{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}'),
	}
	_prop_map_put_ = {
		"DesiredSpeed": ((1610743811, LCID, 4, 0),()),
		"DesiredSpeedMethod": ((1610743809, LCID, 4, 0),()),
		"LowerLimitOfSpeedEfficiency": ((1610743813, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIRouteMCs(DispatchBaseClass):
	CLSID = IID('{BBE52DD6-5D32-4984-A42B-E5F24F27EF13}')
	coclass_clsid = IID('{6968C090-DAA4-4E9B-A7CB-2BDE998AF328}')

	# Result is of type ISIAPIRouteMC
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{74F4BB54-522D-4628-B31B-1A74786A6487}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, mcClass=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),mcClass
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{74F4BB54-522D-4628-B31B-1A74786A6487}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{74F4BB54-522D-4628-B31B-1A74786A6487}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIRouteNwSite(DispatchBaseClass):
	CLSID = IID('{58C442E7-0E64-47B5-AFFA-99BABCE5435E}')
	coclass_clsid = IID('{DE246637-0712-4778-9FE3-1A6E50F0DF60}')

	_prop_map_get_ = {
		"Destination": (1610743811, 2, (3, 0), (), "Destination", None),
		"Origin": (1610743810, 2, (3, 0), (), "Origin", None),
		"Position": (1610743809, 2, (3, 0), (), "Position", None),
		"SiteName": (1610743808, 2, (8, 0), (), "SiteName", None),
		# Method 'networkSite' returns object of type 'ISIAPINetworkSite'
		"networkSite": (1610743813, 2, (9, 0), (), "networkSite", '{4888B50C-984E-4865-B2CE-4FA9B66C2622}'),
		# Method 'route' returns object of type 'ISIAPIRoute'
		"route": (1610743812, 2, (9, 0), (), "route", '{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPIRouteNwSites(DispatchBaseClass):
	CLSID = IID('{8FF9FA61-FA15-4F9C-95E4-3F02656F6F14}')
	coclass_clsid = IID('{3F421D2F-DDB0-4089-AFE4-8BED7C14BFA8}')

	# Result is of type ISIAPIRouteNwSite
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, SiteName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),SiteName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{58C442E7-0E64-47B5-AFFA-99BABCE5435E}')
		return ret

	# Result is of type ISIAPIRouteNwSite
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{58C442E7-0E64-47B5-AFFA-99BABCE5435E}')
		return ret

	def RouteNwSiteExists(self, SiteName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), ((8, 1),),SiteName
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, SiteName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),SiteName
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{58C442E7-0E64-47B5-AFFA-99BABCE5435E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{58C442E7-0E64-47B5-AFFA-99BABCE5435E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPIRoutes(DispatchBaseClass):
	CLSID = IID('{DE44AC02-4804-4587-87BB-AC8E0ED05EEB}')
	coclass_clsid = IID('{14C9EB51-3E0F-407C-BD50-FB301D141A8A}')

	# Result is of type ISIAPIRoute
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, RouteName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),RouteName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')
		return ret

	# Result is of type ISIAPIRoute
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')
		return ret

	def RouteExists(self, RouteName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), ((8, 1),),RouteName
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, RouteName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),RouteName
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPISensitivity(DispatchBaseClass):
	CLSID = IID('{D025138A-4F4C-4613-8FA7-D1FD5550A50C}')
	coclass_clsid = IID('{562BD1F6-FCD9-4F3E-8F07-F2AA2274B12A}')

	_prop_map_get_ = {
		"Constant_factor": (1610743819, 2, (4, 0), (), "Constant_factor", None),
		"Groupno": (1610743808, 2, (3, 0), (), "Groupno", None),
		"Increment": (1610743815, 2, (4, 0), (), "Increment", None),
		"Is_constant_factor_applied": (1610743817, 2, (11, 0), (), "Is_constant_factor_applied", None),
		"Lower": (1610743811, 2, (4, 0), (), "Lower", None),
		"Selected_parameter": (1610743809, 2, (3, 0), (), "Selected_parameter", None),
		"Upper": (1610743813, 2, (4, 0), (), "Upper", None),
	}
	_prop_map_put_ = {
		"Constant_factor": ((1610743819, LCID, 4, 0),()),
		"Increment": ((1610743815, LCID, 4, 0),()),
		"Is_constant_factor_applied": ((1610743817, LCID, 4, 0),()),
		"Lower": ((1610743811, LCID, 4, 0),()),
		"Selected_parameter": ((1610743809, LCID, 4, 0),()),
		"Upper": ((1610743813, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPISequence(DispatchBaseClass):
	CLSID = IID('{B528481B-1627-4D64-9F55-5D7E943539A6}')
	coclass_clsid = IID('{93907DC0-76DC-4B13-BE89-09CC209EC779}')

	# Result is of type ISIAPIPhase
	def AddPhase(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743863, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddPhase', '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')
		return ret

	# Result is of type ISIAPIPhase
	def ClonePhase(self, Phase=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743866, LCID, 1, (9, 0), ((9, 1),),Phase
			)
		if ret is not None:
			ret = Dispatch(ret, 'ClonePhase', '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')
		return ret

	# Result is of type ISIAPIPhase
	def InsertPhase(self, Position=defaultNamedNotOptArg, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743865, LCID, 1, (9, 0), ((3, 1), (8, 1)),Position
			, Name)
		if ret is not None:
			ret = Dispatch(ret, 'InsertPhase', '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')
		return ret

	def MovePhaseTo(self, Phase=defaultNamedNotOptArg, newPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743867, LCID, 1, (11, 0), ((9, 1), (3, 1)),Phase
			, newPosition)

	def RemovePhase(self, Phase=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743864, LCID, 1, (11, 0), ((9, 1),),Phase
			)

	_prop_map_get_ = {
		"Actuated_gap_major_mov": (1610743852, 2, (4, 0), (), "Actuated_gap_major_mov", None),
		"Actuated_gap_minor_mov": (1610743854, 2, (4, 0), (), "Actuated_gap_minor_mov", None),
		"Actuated_max_green_major_mov": (1610743848, 2, (4, 0), (), "Actuated_max_green_major_mov", None),
		"Actuated_max_green_minor_mov": (1610743850, 2, (4, 0), (), "Actuated_max_green_minor_mov", None),
		"Cycle_time_option": (1610743814, 2, (3, 0), (), "Cycle_time_option", None),
		"Eff_det_zone_len_major_mov": (1610743856, 2, (4, 0), (), "Eff_det_zone_len_major_mov", None),
		"Eff_det_zone_len_minor_mov": (1610743858, 2, (4, 0), (), "Eff_det_zone_len_minor_mov", None),
		"Green_split_priority_option": (1610743846, 2, (3, 0), (), "Green_split_priority_option", None),
		"Is_selected": (1610743812, 2, (11, 0), (), "Is_selected", None),
		"Is_timing_optimised_for_selected_result": (1610743870, 2, (11, 0), (), "Is_timing_optimised_for_selected_result", None),
		"Lane_blockage_effect_option": (1610743868, 2, (3, 0), (), "Lane_blockage_effect_option", None),
		"LastErrorMessage": (1610743862, 2, (8, 0), (), "LastErrorMessage", None),
		"Name": (1610743809, 2, (8, 0), (), "Name", None),
		"Optimum_cycle_time_increment": (1610743826, 2, (3, 0), (), "Optimum_cycle_time_increment", None),
		"Optimum_cycle_time_lower": (1610743822, 2, (3, 0), (), "Optimum_cycle_time_lower", None),
		"Optimum_cycle_time_lower_user": (1610743820, 2, (11, 0), (), "Optimum_cycle_time_lower_user", None),
		"Optimum_cycle_time_optim_method": (1610743830, 2, (3, 0), (), "Optimum_cycle_time_optim_method", None),
		"Optimum_cycle_time_perf_measure": (1610743828, 2, (3, 0), (), "Optimum_cycle_time_perf_measure", None),
		"Optimum_cycle_time_upper": (1610743824, 2, (3, 0), (), "Optimum_cycle_time_upper", None),
		"Optimum_max_green_optim_method": (1610743840, 2, (3, 0), (), "Optimum_max_green_optim_method", None),
		"Optimum_max_green_percent_increment": (1610743836, 2, (3, 0), (), "Optimum_max_green_percent_increment", None),
		"Optimum_max_green_percent_lower": (1610743832, 2, (3, 0), (), "Optimum_max_green_percent_lower", None),
		"Optimum_max_green_percent_upper": (1610743834, 2, (3, 0), (), "Optimum_max_green_percent_upper", None),
		"Optimum_max_green_perf_measure": (1610743838, 2, (3, 0), (), "Optimum_max_green_perf_measure", None),
		# Method 'Phases' returns object of type 'ISIAPIPhases'
		"Phases": (1610743861, 2, (9, 0), (), "Phases", '{98B4AB9E-189E-4149-BFE9-0DD10CA8BBEF}'),
		"Position": (1610743811, 2, (3, 0), (), "Position", None),
		"Practical_cycle_rounding": (1610743818, 2, (3, 0), (), "Practical_cycle_rounding", None),
		"Practical_max_cycle_time": (1610743816, 2, (3, 0), (), "Practical_max_cycle_time", None),
		"Sequence_id": (1610743808, 2, (3, 0), (), "Sequence_id", None),
		# Method 'Site' returns object of type 'ISIAPISite'
		"Site": (1610743860, 2, (9, 0), (), "Site", '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}'),
		"Usergiven_cycle_time": (1610743844, 2, (3, 0), (), "Usergiven_cycle_time", None),
		"Variable_phasing_perf_measure": (1610743842, 2, (3, 0), (), "Variable_phasing_perf_measure", None),
	}
	_prop_map_put_ = {
		"Actuated_gap_major_mov": ((1610743852, LCID, 4, 0),()),
		"Actuated_gap_minor_mov": ((1610743854, LCID, 4, 0),()),
		"Actuated_max_green_major_mov": ((1610743848, LCID, 4, 0),()),
		"Actuated_max_green_minor_mov": ((1610743850, LCID, 4, 0),()),
		"Cycle_time_option": ((1610743814, LCID, 4, 0),()),
		"Eff_det_zone_len_major_mov": ((1610743856, LCID, 4, 0),()),
		"Eff_det_zone_len_minor_mov": ((1610743858, LCID, 4, 0),()),
		"Green_split_priority_option": ((1610743846, LCID, 4, 0),()),
		"Is_selected": ((1610743812, LCID, 4, 0),()),
		"Is_timing_optimised_for_selected_result": ((1610743870, LCID, 4, 0),()),
		"Lane_blockage_effect_option": ((1610743868, LCID, 4, 0),()),
		"Name": ((1610743809, LCID, 4, 0),()),
		"Optimum_cycle_time_increment": ((1610743826, LCID, 4, 0),()),
		"Optimum_cycle_time_lower": ((1610743822, LCID, 4, 0),()),
		"Optimum_cycle_time_lower_user": ((1610743820, LCID, 4, 0),()),
		"Optimum_cycle_time_optim_method": ((1610743830, LCID, 4, 0),()),
		"Optimum_cycle_time_perf_measure": ((1610743828, LCID, 4, 0),()),
		"Optimum_cycle_time_upper": ((1610743824, LCID, 4, 0),()),
		"Optimum_max_green_optim_method": ((1610743840, LCID, 4, 0),()),
		"Optimum_max_green_percent_increment": ((1610743836, LCID, 4, 0),()),
		"Optimum_max_green_percent_lower": ((1610743832, LCID, 4, 0),()),
		"Optimum_max_green_percent_upper": ((1610743834, LCID, 4, 0),()),
		"Optimum_max_green_perf_measure": ((1610743838, LCID, 4, 0),()),
		"Practical_cycle_rounding": ((1610743818, LCID, 4, 0),()),
		"Practical_max_cycle_time": ((1610743816, LCID, 4, 0),()),
		"Usergiven_cycle_time": ((1610743844, LCID, 4, 0),()),
		"Variable_phasing_perf_measure": ((1610743842, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPISequences(DispatchBaseClass):
	CLSID = IID('{838EB6A8-198A-4409-B1A5-0267857AD7F1}')
	coclass_clsid = IID('{EC6DC582-D6C0-4DAA-B2A6-8A1E7C9E6ED2}')

	# Result is of type ISIAPISequence
	def GetSequenceByID(self, Sequence_id=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743811, LCID, 1, (9, 0), ((3, 1),),Sequence_id
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSequenceByID', '{B528481B-1627-4D64-9F55-5D7E943539A6}')
		return ret

	# Result is of type ISIAPISequence
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B528481B-1627-4D64-9F55-5D7E943539A6}')
		return ret

	# Result is of type ISIAPISequence
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{B528481B-1627-4D64-9F55-5D7E943539A6}')
		return ret

	def SequenceExists(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), ((8, 1),),Name
			)

	_prop_map_get_ = {
		"Count": (1610743812, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B528481B-1627-4D64-9F55-5D7E943539A6}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{B528481B-1627-4D64-9F55-5D7E943539A6}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743812, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPISite(DispatchBaseClass):
	CLSID = IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
	coclass_clsid = IID('{1D0A3CAF-D0CF-4AC2-BCD6-FD377579759B}')

	# Result is of type ISIAPILeg
	def AddLeg(self, Orientation=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743877, LCID, 1, (9, 0), ((3, 1),),Orientation
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddLeg', '{24A8E5D9-0016-45F2-9941-12E58EE54A05}')
		return ret

	# Result is of type ISIAPILeg
	def AddLegWithLanes(self, Orientation=defaultNamedNotOptArg, LegGeometry=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743878, LCID, 1, (9, 0), ((3, 1), (3, 1)),Orientation
			, LegGeometry)
		if ret is not None:
			ret = Dispatch(ret, 'AddLegWithLanes', '{24A8E5D9-0016-45F2-9941-12E58EE54A05}')
		return ret

	# Result is of type ISIAPISequence
	def AddSequence(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743882, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddSequence', '{B528481B-1627-4D64-9F55-5D7E943539A6}')
		return ret

	# Result is of type ISIAPISequence
	def CloneSequence(self, Sequence=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743886, LCID, 1, (9, 0), ((9, 1),),Sequence
			)
		if ret is not None:
			ret = Dispatch(ret, 'CloneSequence', '{B528481B-1627-4D64-9F55-5D7E943539A6}')
		return ret

	def CreateLayoutPngData(self):
		return self._ApplyTypes_(1610743884, 1, (8209, 0), (), 'CreateLayoutPngData', None,)

	def CreateLayoutPngFile(self, filename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743885, LCID, 1, (11, 0), ((8, 1),),filename
			)

	def MoveSequenceTo(self, Sequence=defaultNamedNotOptArg, newPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743887, LCID, 1, (11, 0), ((9, 1), (3, 1)),Sequence
			, newPosition)

	def Process(self):
		return self._oleobj_.InvokeTypes(1610743872, LCID, 1, (11, 0), (),)

	def RemoveLeg(self, Orientation=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743879, LCID, 1, (11, 0), ((3, 1),),Orientation
			)

	def RemoveOutputData(self):
		return self._oleobj_.InvokeTypes(1610743895, LCID, 1, (11, 0), (),)

	def RemoveSequence(self, Sequence=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743883, LCID, 1, (11, 0), ((9, 1),),Sequence
			)

	def ResetLaneMovements(self):
		return self._oleobj_.InvokeTypes(1610743874, LCID, 1, (11, 0), (),)

	def ResetMovementVehicleODMCExists(self):
		return self._oleobj_.InvokeTypes(1610743873, LCID, 1, (11, 0), (),)

	def ResetSitePrioritiesData(self):
		return self._oleobj_.InvokeTypes(1610743875, LCID, 1, (11, 0), (),)

	def Rotate(self, step=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743880, LCID, 1, (11, 0), ((3, 1),),step
			)

	def UpdateGeometryData(self):
		return self._oleobj_.InvokeTypes(1610743881, LCID, 1, (11, 0), (),)

	def UpdateModifiedInfo(self):
		return self._oleobj_.InvokeTypes(1610743876, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Analysis' returns object of type 'ISIAPIAnalysis'
		"Analysis": (1610743820, 2, (9, 0), (), "Analysis", '{C3D8FE89-6620-45E7-898A-F4108FA95E6F}'),
		"Category": (1610743888, 2, (8, 0), (), "Category", None),
		"CostUnit": (1610743858, 2, (8, 0), (), "CostUnit", None),
		"Created_by": (1610743841, 2, (8, 0), (), "Created_by", None),
		"Created_by_company": (1610743842, 2, (8, 0), (), "Created_by_company", None),
		"Created_date": (1610743840, 2, (7, 0), (), "Created_date", None),
		"Created_version": (1610743843, 2, (8, 0), (), "Created_version", None),
		"Description": (1610743848, 2, (8, 0), (), "Description", None),
		# Method 'DiagnosticMsgs' returns object of type 'ISIAPIDiagnosticMsgs'
		"DiagnosticMsgs": (1610743831, 2, (9, 0), (), "DiagnosticMsgs", '{CBFD7927-0588-4CF2-BEB4-052B1F31A027}'),
		"DiagnosticStatus": (1610743830, 2, (3, 0), (), "DiagnosticStatus", None),
		"DriveOnLeft": (1610743834, 2, (11, 0), (), "DriveOnLeft", None),
		"Freeway_orientation": (1610743839, 2, (3, 0), (), "Freeway_orientation", None),
		# Method 'GapAcceptanceTurnOnRed' returns object of type 'ISIAPIGapAcceptanceSpecificApp'
		"GapAcceptanceTurnOnRed": (1610743821, 2, (9, 0), (), "GapAcceptanceTurnOnRed", '{8860D705-1B2F-4F1E-B59A-6C4992A3FE9A}'),
		"HasWarnings": (1610743828, 2, (11, 0), (), "HasWarnings", None),
		"Hcm": (1610743836, 2, (11, 0), (), "Hcm", None),
		"Intersectionid": (1610743810, 2, (8, 0), (), "Intersectionid", None),
		"IsIncludedInProjectSummary": (1610743890, 2, (11, 0), (), "IsIncludedInProjectSummary", None),
		"Is_multi_sequence_enabled": (1610743893, 2, (11, 0), (), "Is_multi_sequence_enabled", None),
		"LastErrorMessage": (1610743829, 2, (8, 0), (), "LastErrorMessage", None),
		# Method 'Legs' returns object of type 'ISIAPILegs'
		"Legs": (1610743815, 2, (9, 0), (), "Legs", '{D7F45026-862A-432F-BC67-E0557FED8203}'),
		"ModelName": (1610743838, 2, (8, 0), (), "ModelName", None),
		# Method 'ModelSetting' returns object of type 'ISIAPIModelSetting'
		"ModelSetting": (1610743819, 2, (9, 0), (), "ModelSetting", '{DB0EFBA0-673A-4E4B-B359-ED0CAFA0643F}'),
		"ModelSignature": (1610743837, 2, (8, 0), (), "ModelSignature", None),
		"Modified_by": (1610743845, 2, (8, 0), (), "Modified_by", None),
		"Modified_by_company": (1610743846, 2, (8, 0), (), "Modified_by_company", None),
		"Modified_date": (1610743844, 2, (7, 0), (), "Modified_date", None),
		"Modified_version": (1610743847, 2, (8, 0), (), "Modified_version", None),
		# Method 'MovementClasses' returns object of type 'ISIAPIMovementClasses'
		"MovementClasses": (1610743814, 2, (9, 0), (), "MovementClasses", '{39B087B7-EB2C-4B47-8923-F8DD4238C771}'),
		# Method 'MovementPeds' returns object of type 'ISIAPIMovement_peds'
		"MovementPeds": (1610743817, 2, (9, 0), (), "MovementPeds", '{DE5491F4-C24E-4505-A74A-DC4E93712375}'),
		# Method 'MovementVehicleODs' returns object of type 'ISIAPIMovement_vehicle_ods'
		"MovementVehicleODs": (1610743816, 2, (9, 0), (), "MovementVehicleODs", '{87B16289-A709-4781-ADA1-92C6D1F3EB3D}'),
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		# Method 'Outputset' returns object of type 'ISIAPIOutputset'
		"Outputset": (1610743824, 2, (9, 0), (), "Outputset", '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}'),
		"Peakflowperiod": (1610743854, 2, (3, 0), (), "Peakflowperiod", None),
		"Position": (1610743812, 2, (3, 0), (), "Position", None),
		"ProcessingError": (1610743826, 2, (8, 0), (), "ProcessingError", None),
		"ProcessingWarnings": (1610743827, 2, (8, 0), (), "ProcessingWarnings", None),
		# Method 'Project' returns object of type 'ISIAPIProject'
		"Project": (1610743825, 2, (9, 0), (), "Project", '{5817180B-2283-40FB-8068-C2F2D656EF04}'),
		"Rou_controlling_detector_setback_dist": (1610743866, 2, (4, 0), (), "Rou_controlling_detector_setback_dist", None),
		"Rou_controlling_leg_orientation": (1610743870, 2, (3, 0), (), "Rou_controlling_leg_orientation", None),
		"Rou_metered_end_gain": (1610743864, 2, (3, 0), (), "Rou_metered_end_gain", None),
		"Rou_metered_leg_orientation": (1610743868, 2, (3, 0), (), "Rou_metered_leg_orientation", None),
		"Rou_metered_start_loss": (1610743862, 2, (3, 0), (), "Rou_metered_start_loss", None),
		"Rou_stopline_setback_dist": (1610743860, 2, (4, 0), (), "Rou_stopline_setback_dist", None),
		# Method 'Sequences' returns object of type 'ISIAPISequences'
		"Sequences": (1610743818, 2, (9, 0), (), "Sequences", '{838EB6A8-198A-4409-B1A5-0267857AD7F1}'),
		"Signal_analysis_method": (1610743856, 2, (3, 0), (), "Signal_analysis_method", None),
		"Site_id": (1610743813, 2, (3, 0), (), "Site_id", None),
		"Sitecontroltype": (1610743833, 2, (3, 0), (), "Sitecontroltype", None),
		"Sitesubtype": (1610743896, 2, (3, 0), (), "Sitesubtype", None),
		"Sitetype": (1610743832, 2, (3, 0), (), "Sitetype", None),
		"Title": (1610743850, 2, (8, 0), (), "Title", None),
		# Method 'TwoWaySignControlAdjGeometryControls' returns object of type 'ISIAPITwoWaySignControlAdjGeometryControls'
		"TwoWaySignControlAdjGeometryControls": (1610743823, 2, (9, 0), (), "TwoWaySignControlAdjGeometryControls", '{89002DC5-ADA3-4304-B64C-1A38C0D522A3}'),
		# Method 'TwoWaySignControlAdjMajorNumLanes' returns object of type 'ISIAPITwoWaySignControlAdjMajorNumLanes'
		"TwoWaySignControlAdjMajorNumLanes": (1610743822, 2, (9, 0), (), "TwoWaySignControlAdjMajorNumLanes", '{546F1C93-6CF2-44A4-B963-E18FBA6A7A61}'),
		"Units": (1610743835, 2, (3, 0), (), "Units", None),
		"Unittimeforvolumes": (1610743852, 2, (3, 0), (), "Unittimeforvolumes", None),
		# Method 'siteFolder' returns object of type 'ISIAPISiteFolder'
		"siteFolder": (1610743892, 2, (9, 0), (), "siteFolder", '{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}'),
	}
	_prop_map_put_ = {
		"Category": ((1610743888, LCID, 4, 0),()),
		"CostUnit": ((1610743858, LCID, 4, 0),()),
		"Description": ((1610743848, LCID, 4, 0),()),
		"Intersectionid": ((1610743810, LCID, 4, 0),()),
		"IsIncludedInProjectSummary": ((1610743890, LCID, 4, 0),()),
		"Is_multi_sequence_enabled": ((1610743893, LCID, 4, 0),()),
		"Name": ((1610743808, LCID, 4, 0),()),
		"Peakflowperiod": ((1610743854, LCID, 4, 0),()),
		"Rou_controlling_detector_setback_dist": ((1610743866, LCID, 4, 0),()),
		"Rou_controlling_leg_orientation": ((1610743870, LCID, 4, 0),()),
		"Rou_metered_end_gain": ((1610743864, LCID, 4, 0),()),
		"Rou_metered_leg_orientation": ((1610743868, LCID, 4, 0),()),
		"Rou_metered_start_loss": ((1610743862, LCID, 4, 0),()),
		"Rou_stopline_setback_dist": ((1610743860, LCID, 4, 0),()),
		"Signal_analysis_method": ((1610743856, LCID, 4, 0),()),
		"Sitesubtype": ((1610743896, LCID, 4, 0),()),
		"Title": ((1610743850, LCID, 4, 0),()),
		"Unittimeforvolumes": ((1610743852, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPISiteFolder(DispatchBaseClass):
	CLSID = IID('{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')
	coclass_clsid = IID('{51678BC8-2907-4D52-AB68-95CFCA3C029C}')

	# Result is of type ISIAPISite
	def AddSite(self, Sitetype=defaultNamedNotOptArg, softwareSetup=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743813, LCID, 1, (9, 0), ((3, 1), (3, 1)),Sitetype
			, softwareSetup)
		if ret is not None:
			ret = Dispatch(ret, 'AddSite', '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
		return ret

	# Result is of type ISIAPISite
	def AddSiteWithGeometry(self, Sitetype=defaultNamedNotOptArg, softwareSetup=defaultNamedNotOptArg, majorRoadOrientation=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743814, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),Sitetype
			, softwareSetup, majorRoadOrientation)
		if ret is not None:
			ret = Dispatch(ret, 'AddSiteWithGeometry', '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
		return ret

	# Result is of type ISIAPISite
	def AddSiteWithGeometry_2(self, Sitetype=defaultNamedNotOptArg, softwareSetupSignature=defaultNamedNotOptArg, majorRoadOrientation=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743816, LCID, 1, (9, 0), ((3, 1), (8, 1), (3, 1)),Sitetype
			, softwareSetupSignature, majorRoadOrientation)
		if ret is not None:
			ret = Dispatch(ret, 'AddSiteWithGeometry_2', '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
		return ret

	# Result is of type ISIAPISite
	def AddSite_2(self, Sitetype=defaultNamedNotOptArg, softwareSetupSignature=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743815, LCID, 1, (9, 0), ((3, 1), (8, 1)),Sitetype
			, softwareSetupSignature)
		if ret is not None:
			ret = Dispatch(ret, 'AddSite_2', '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
		return ret

	# Result is of type ISIAPISite
	def CloneSite(self, Site=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743818, LCID, 1, (9, 0), ((9, 1),),Site
			)
		if ret is not None:
			ret = Dispatch(ret, 'CloneSite', '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
		return ret

	def MoveSiteTo(self, Site=defaultNamedNotOptArg, newPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743819, LCID, 1, (11, 0), ((9, 1), (3, 1)),Site
			, newPosition)

	def MoveSitesToFolder(self, siteNames=defaultNamedNotOptArg, destFolder=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743820, LCID, 1, (3, 0), ((8, 1), (9, 1)),siteNames
			, destFolder)

	def RemoveSite(self, Site=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743817, LCID, 1, (11, 0), ((9, 1),),Site
			)

	_prop_map_get_ = {
		"Name": (1610743808, 2, (8, 0), (), "Name", None),
		"Position": (1610743810, 2, (3, 0), (), "Position", None),
		# Method 'Project' returns object of type 'ISIAPIProject'
		"Project": (1610743812, 2, (9, 0), (), "Project", '{5817180B-2283-40FB-8068-C2F2D656EF04}'),
		# Method 'Sites' returns object of type 'ISIAPISites'
		"Sites": (1610743811, 2, (9, 0), (), "Sites", '{8938DB91-E714-4703-8C7D-18B0DD89A19C}'),
	}
	_prop_map_put_ = {
		"Name": ((1610743808, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPISiteFolders(DispatchBaseClass):
	CLSID = IID('{9712E108-061B-4BB9-AC11-8ADECF24EA13}')
	coclass_clsid = IID('{B1DB958A-0F80-4845-B4FD-FED3BEDAFE13}')

	# Result is of type ISIAPISiteFolder
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')
		return ret

	# Result is of type ISIAPISiteFolder
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')
		return ret

	def SiteFolderExists(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), ((8, 1),),Name
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPISites(DispatchBaseClass):
	CLSID = IID('{8938DB91-E714-4703-8C7D-18B0DD89A19C}')
	coclass_clsid = IID('{2322E0C4-40D9-46EF-9ACA-52AF8BA62A2D}')

	# Result is of type ISIAPISite
	def GetSiteByID(self, Site_id=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743812, LCID, 1, (9, 0), ((3, 1),),Site_id
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSiteByID', '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
		return ret

	# Result is of type ISIAPISite
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, SiteName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),SiteName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
		return ret

	# Result is of type ISIAPISite
	# The method Item_2 is actually a property, but must be used as a method to correctly pass the arguments
	def Item_2(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610743809, LCID, 2, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item_2', '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
		return ret

	def SiteExists(self, SiteName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), ((8, 1),),SiteName
			)

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, SiteName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((8, 1),),SiteName
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPITwoWaySignControlAdjGeometryControl(DispatchBaseClass):
	CLSID = IID('{06229DBD-9E71-4D04-A6DA-B7B0524A7302}')
	coclass_clsid = IID('{F2A4712E-4165-42F8-9336-30DA604C4279}')

	_prop_map_get_ = {
		"Critical_gap_adj": (1610743809, 2, (4, 0), (), "Critical_gap_adj", None),
		"Followup_headway_adj": (1610743811, 2, (4, 0), (), "Followup_headway_adj", None),
		"Type": (1610743808, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Critical_gap_adj": ((1610743809, LCID, 4, 0),()),
		"Followup_headway_adj": ((1610743811, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPITwoWaySignControlAdjGeometryControls(DispatchBaseClass):
	CLSID = IID('{89002DC5-ADA3-4304-B64C-1A38C0D522A3}')
	coclass_clsid = IID('{CD5FBEDB-CBE3-4A86-A2E8-BF71E507C463}')

	def Exists(self, geoControlType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1),),geoControlType
			)

	# Result is of type ISIAPITwoWaySignControlAdjGeometryControl
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, geoControlType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),geoControlType
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{06229DBD-9E71-4D04-A6DA-B7B0524A7302}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, geoControlType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),geoControlType
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{06229DBD-9E71-4D04-A6DA-B7B0524A7302}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{06229DBD-9E71-4D04-A6DA-B7B0524A7302}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISIAPITwoWaySignControlAdjMajorNumLane(DispatchBaseClass):
	CLSID = IID('{77FFB02C-F596-4F32-907B-D5CF292B0686}')
	coclass_clsid = IID('{17E1A63D-976D-4A05-9151-8491AD5D8712}')

	_prop_map_get_ = {
		"Critical_gap_adj": (1610743810, 2, (4, 0), (), "Critical_gap_adj", None),
		"Followup_headway_adj": (1610743812, 2, (4, 0), (), "Followup_headway_adj", None),
		"Major_num_lane": (1610743808, 2, (3, 0), (), "Major_num_lane", None),
		"Movement_type": (1610743809, 2, (3, 0), (), "Movement_type", None),
	}
	_prop_map_put_ = {
		"Critical_gap_adj": ((1610743810, LCID, 4, 0),()),
		"Followup_headway_adj": ((1610743812, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISIAPITwoWaySignControlAdjMajorNumLanes(DispatchBaseClass):
	CLSID = IID('{546F1C93-6CF2-44A4-B963-E18FBA6A7A61}')
	coclass_clsid = IID('{A5050181-1C6A-4BF4-A8C5-4A712A954A90}')

	def Exists(self, majorRoadNumOfLane=defaultNamedNotOptArg, movType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((3, 1), (3, 1)),majorRoadNumOfLane
			, movType)

	# Result is of type ISIAPITwoWaySignControlAdjMajorNumLane
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, majorRoadNumOfLane=defaultNamedNotOptArg, movType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),majorRoadNumOfLane
			, movType)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{77FFB02C-F596-4F32-907B-D5CF292B0686}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743810, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, majorRoadNumOfLane=defaultNamedNotOptArg, movType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1), (3, 1)),majorRoadNumOfLane
			, movType)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{77FFB02C-F596-4F32-907B-D5CF292B0686}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{77FFB02C-F596-4F32-907B-D5CF292B0686}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743810, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class _AuthorizationDecisionItem(DispatchBaseClass):
	CLSID = IID('{C3A9F3D6-00FB-3F9D-81C4-0D629824F518}')
	coclass_clsid = IID('{CB77544E-8929-37BB-B618-3978421B885A}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _Object(DispatchBaseClass):
	CLSID = IID('{65074F7F-63C0-304E-AF0A-D51741CB4A8D}')
	coclass_clsid = IID('{035BB123-A169-3E54-84A2-35F3A2E4521B}')

	def Equals(self, obj=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (11, 0), ((12, 1),),obj
			)

	def GetHashCode(self):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (3, 0), (),)

	# Result is of type _Type
	def GetType(self):
		ret = self._oleobj_.InvokeTypes(1610743811, LCID, 1, (13, 0), (),)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, 'GetType', '{BCA8B44D-AAD6-3A86-8AB7-03349F4F2DA2}')
		return ret

	_prop_map_get_ = {
		"ToString": (0, 2, (8, 0), (), "ToString", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'ToString'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "ToString", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _SIOptionCustomData(DispatchBaseClass):
	CLSID = IID('{8977B4BE-3893-3D2D-8BCA-3B4120278FE3}')
	coclass_clsid = IID('{035BB123-A169-3E54-84A2-35F3A2E4521B}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
class AuthorizationDecisionItem(CoClassBaseClass): # A CoClass
	CLSID = IID('{CB77544E-8929-37BB-B618-3978421B885A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_AuthorizationDecisionItem,
		_Object,
	]
	default_interface = _AuthorizationDecisionItem

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPI'
class SIAPI(CoClassBaseClass): # A CoClass
	CLSID = IID('{D92122F2-74F7-4A2B-953E-B75CF1B2738D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPI,
		IDisposable,
	]
	default_interface = ISIAPI

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIAnalysis'
class SIAPIAnalysis(CoClassBaseClass): # A CoClass
	CLSID = IID('{3988FB26-C8F8-4AA9-8FCB-B803193F4D50}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIAnalysis,
	]
	default_interface = ISIAPIAnalysis

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIDiagnosticMsg'
class SIAPIDiagnosticMsg(CoClassBaseClass): # A CoClass
	CLSID = IID('{6BD716CD-F4A3-4CAF-A052-24F92F02130D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIDiagnosticMsg,
	]
	default_interface = ISIAPIDiagnosticMsg

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIDiagnosticMsgs'
class SIAPIDiagnosticMsgs(CoClassBaseClass): # A CoClass
	CLSID = IID('{98563BD9-ED3E-4ECA-ABAD-FCC3D86B1021}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIDiagnosticMsgs,
		IEnumerable,
	]
	default_interface = ISIAPIDiagnosticMsgs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIGapAcceptanceSpecificApp'
class SIAPIGapAcceptanceSpecificApp(CoClassBaseClass): # A CoClass
	CLSID = IID('{8FAEAC43-040F-48C1-9FF0-D8883FFFFE11}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIGapAcceptanceSpecificApp,
	]
	default_interface = ISIAPIGapAcceptanceSpecificApp

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIIsland'
class SIAPIIsland(CoClassBaseClass): # A CoClass
	CLSID = IID('{EA335953-2755-4056-860C-5355FA753978}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIIsland,
	]
	default_interface = ISIAPIIsland

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIIslands'
class SIAPIIslands(CoClassBaseClass): # A CoClass
	CLSID = IID('{F797F2BF-20A2-4353-9E76-14B778448B3B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIIslands,
		IEnumerable,
	]
	default_interface = ISIAPIIslands

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneApproach'
class SIAPILaneApproach(CoClassBaseClass): # A CoClass
	CLSID = IID('{C64B58F7-7E6C-4D01-B73F-74EE785691D5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneApproach,
	]
	default_interface = ISIAPILaneApproach

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneApproachMovement'
class SIAPILaneApproachMovement(CoClassBaseClass): # A CoClass
	CLSID = IID('{A5CA350D-1764-431A-B3DE-4E66AEC098CE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneApproachMovement,
	]
	default_interface = ISIAPILaneApproachMovement

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneApproachMovementMC'
class SIAPILaneApproachMovementMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{A8FE0EAC-41F7-4B6D-A03E-BD4296549E04}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneApproachMovementMC,
	]
	default_interface = ISIAPILaneApproachMovementMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneApproachMovementMCs'
class SIAPILaneApproachMovementMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{D0F9DE87-E61E-43C9-AB12-A81DCCF2BE76}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneApproachMovementMCs,
		IEnumerable,
	]
	default_interface = ISIAPILaneApproachMovementMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneApproachMovements'
class SIAPILaneApproachMovements(CoClassBaseClass): # A CoClass
	CLSID = IID('{3C6FB29C-52F6-426B-AE37-987D1910CF22}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneApproachMovements,
		IEnumerable,
	]
	default_interface = ISIAPILaneApproachMovements

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneApproachs'
class SIAPILaneApproachs(CoClassBaseClass): # A CoClass
	CLSID = IID('{78A0E9B9-165B-4790-8B63-0003CEE1381F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneApproachs,
		IEnumerable,
	]
	default_interface = ISIAPILaneApproachs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneExit'
class SIAPILaneExit(CoClassBaseClass): # A CoClass
	CLSID = IID('{F142FCA8-DBFF-4477-BA9B-4B6F416B3642}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneExit,
	]
	default_interface = ISIAPILaneExit

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneExitMergeParam'
class SIAPILaneExitMergeParam(CoClassBaseClass): # A CoClass
	CLSID = IID('{4E294323-0877-4866-8E42-50BDE4F0FC69}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneExitMergeParam,
	]
	default_interface = ISIAPILaneExitMergeParam

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneExits'
class SIAPILaneExits(CoClassBaseClass): # A CoClass
	CLSID = IID('{6B84632B-C622-4C79-BCDB-16DBC5FE472E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneExits,
		IEnumerable,
	]
	default_interface = ISIAPILaneExits

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneMovement'
class SIAPILaneMovement(CoClassBaseClass): # A CoClass
	CLSID = IID('{62BB3A21-AE88-44DE-83A4-68663A3C1A09}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneMovement,
	]
	default_interface = ISIAPILaneMovement

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneMovementMC'
class SIAPILaneMovementMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{61E72EEE-F3BA-4B3D-8733-017C4F399459}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneMovementMC,
	]
	default_interface = ISIAPILaneMovementMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneMovementMCs'
class SIAPILaneMovementMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{1C1577BA-CBAC-4781-9A9F-40C6A2AD215D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneMovementMCs,
		IEnumerable,
	]
	default_interface = ISIAPILaneMovementMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneMovements'
class SIAPILaneMovements(CoClassBaseClass): # A CoClass
	CLSID = IID('{6C29D3CD-B050-411A-9B2B-F7A008C9342E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneMovements,
		IEnumerable,
	]
	default_interface = ISIAPILaneMovements

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneSegment'
class SIAPILaneSegment(CoClassBaseClass): # A CoClass
	CLSID = IID('{8A1FCFC4-08FB-4CB6-A9BC-E58D495ACAB6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneSegment,
	]
	default_interface = ISIAPILaneSegment

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneSegmentMC'
class SIAPILaneSegmentMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{34AA399B-6B65-46DE-8F64-9A59ACECCF8E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneSegmentMC,
	]
	default_interface = ISIAPILaneSegmentMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILaneSegmentMCs'
class SIAPILaneSegmentMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{CDB7B33D-887D-4EAE-9596-1207BFC72BB5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILaneSegmentMCs,
		IEnumerable,
	]
	default_interface = ISIAPILaneSegmentMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILeg'
class SIAPILeg(CoClassBaseClass): # A CoClass
	CLSID = IID('{D8B9A97D-F4E1-4E42-81D2-C370A157DC13}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILeg,
	]
	default_interface = ISIAPILeg

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILeg_rou_hcm'
class SIAPILeg_rou_hcm(CoClassBaseClass): # A CoClass
	CLSID = IID('{3824A747-9BC3-4304-B6C1-0969796A33EA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILeg_rou_hcm,
	]
	default_interface = ISIAPILeg_rou_hcm

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILeg_rou_hcm6_extended'
class SIAPILeg_rou_hcm6_extended(CoClassBaseClass): # A CoClass
	CLSID = IID('{FDA1F3A6-FA03-4937-99CB-AA207DD504F9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILeg_rou_hcm6_extended,
	]
	default_interface = ISIAPILeg_rou_hcm6_extended

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILeg_roundabout'
class SIAPILeg_roundabout(CoClassBaseClass): # A CoClass
	CLSID = IID('{B9DD66CB-2900-4C0D-A7F9-A0BDF06656E9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILeg_roundabout,
	]
	default_interface = ISIAPILeg_roundabout

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPILegs'
class SIAPILegs(CoClassBaseClass): # A CoClass
	CLSID = IID('{CB79F519-887E-4349-B499-5FFF86EB475D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPILegs,
		IEnumerable,
	]
	default_interface = ISIAPILegs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIModelSetting'
class SIAPIModelSetting(CoClassBaseClass): # A CoClass
	CLSID = IID('{4F6A34D7-8E26-4D62-819E-6A100FB00AC9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIModelSetting,
	]
	default_interface = ISIAPIModelSetting

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovementClass'
class SIAPIMovementClass(CoClassBaseClass): # A CoClass
	CLSID = IID('{22DCD1A6-1C92-478E-ABAB-FA0AFBE2F235}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovementClass,
	]
	default_interface = ISIAPIMovementClass

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovementClassFuelEmission'
class SIAPIMovementClassFuelEmission(CoClassBaseClass): # A CoClass
	CLSID = IID('{7C2A53C7-B12F-4C83-A409-1BDD05DADB5C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovementClassFuelEmission,
	]
	default_interface = ISIAPIMovementClassFuelEmission

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovementClassFuelEmissions'
class SIAPIMovementClassFuelEmissions(CoClassBaseClass): # A CoClass
	CLSID = IID('{7D7AAA7B-6F56-44C2-A439-22A50FA85997}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovementClassFuelEmissions,
		IEnumerable,
	]
	default_interface = ISIAPIMovementClassFuelEmissions

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovementClassMergeParam'
class SIAPIMovementClassMergeParam(CoClassBaseClass): # A CoClass
	CLSID = IID('{E567F5BB-9F02-452E-8633-568913739EBC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovementClassMergeParam,
	]
	default_interface = ISIAPIMovementClassMergeParam

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovementClasses'
class SIAPIMovementClasses(CoClassBaseClass): # A CoClass
	CLSID = IID('{ECE0790E-AA84-41A3-A0E2-74E3E2E4E2C5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovementClasses,
		IEnumerable,
	]
	default_interface = ISIAPIMovementClasses

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovement_ped'
class SIAPIMovement_ped(CoClassBaseClass): # A CoClass
	CLSID = IID('{695474FC-BF40-4A63-B1D3-0E9D5974BB68}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovement_ped,
	]
	default_interface = ISIAPIMovement_ped

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovement_peds'
class SIAPIMovement_peds(CoClassBaseClass): # A CoClass
	CLSID = IID('{2680FEE3-C577-402C-BEC4-ED25E864B1C4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovement_peds,
		IEnumerable,
	]
	default_interface = ISIAPIMovement_peds

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovement_vehicle_od'
class SIAPIMovement_vehicle_od(CoClassBaseClass): # A CoClass
	CLSID = IID('{BDA8A10E-42F8-4CDB-961D-7B85BB245C66}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovement_vehicle_od,
	]
	default_interface = ISIAPIMovement_vehicle_od

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovement_vehicle_od_mc'
class SIAPIMovement_vehicle_od_mc(CoClassBaseClass): # A CoClass
	CLSID = IID('{23B2A7F0-0A7C-4DD8-BB86-8613CA079749}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovement_vehicle_od_mc,
	]
	default_interface = ISIAPIMovement_vehicle_od_mc

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovement_vehicle_od_mcs'
class SIAPIMovement_vehicle_od_mcs(CoClassBaseClass): # A CoClass
	CLSID = IID('{8447273B-5B6D-438B-A672-27CE30624350}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovement_vehicle_od_mcs,
		IEnumerable,
	]
	default_interface = ISIAPIMovement_vehicle_od_mcs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIMovement_vehicle_ods'
class SIAPIMovement_vehicle_ods(CoClassBaseClass): # A CoClass
	CLSID = IID('{954FF861-147D-46C1-BBBD-3B1FC1EEE70C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIMovement_vehicle_ods,
		IEnumerable,
	]
	default_interface = ISIAPIMovement_vehicle_ods

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetwork'
class SIAPINetwork(CoClassBaseClass): # A CoClass
	CLSID = IID('{2756D52B-FF46-4C94-8B37-0443810347CB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetwork,
	]
	default_interface = ISIAPINetwork

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkCCG'
class SIAPINetworkCCG(CoClassBaseClass): # A CoClass
	CLSID = IID('{6D2F736E-A370-4F0A-ADBB-415015499B40}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkCCG,
	]
	default_interface = ISIAPINetworkCCG

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkCCGPhase'
class SIAPINetworkCCGPhase(CoClassBaseClass): # A CoClass
	CLSID = IID('{1D63D43D-AE3E-4580-A807-1D8F60277E86}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkCCGPhase,
	]
	default_interface = ISIAPINetworkCCGPhase

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkCCGPhases'
class SIAPINetworkCCGPhases(CoClassBaseClass): # A CoClass
	CLSID = IID('{7A5CF9F9-A024-451D-8C83-60F453170DC4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkCCGPhases,
		IEnumerable,
	]
	default_interface = ISIAPINetworkCCGPhases

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkCCGSequence'
class SIAPINetworkCCGSequence(CoClassBaseClass): # A CoClass
	CLSID = IID('{0C3B93A9-7DEE-4339-9CF8-1E5F7F64653C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkCCGSequence,
	]
	default_interface = ISIAPINetworkCCGSequence

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkCCGSequences'
class SIAPINetworkCCGSequences(CoClassBaseClass): # A CoClass
	CLSID = IID('{10A357EA-76F6-4197-B4DC-BA4E0B877F70}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkCCGSequences,
		IEnumerable,
	]
	default_interface = ISIAPINetworkCCGSequences

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkCCGs'
class SIAPINetworkCCGs(CoClassBaseClass): # A CoClass
	CLSID = IID('{F42C1BFD-FE64-49F5-9EA9-97A29C94E9A8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkCCGs,
		IEnumerable,
	]
	default_interface = ISIAPINetworkCCGs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkDemandSensitivity'
class SIAPINetworkDemandSensitivity(CoClassBaseClass): # A CoClass
	CLSID = IID('{75BDF116-4417-40F7-9D85-0E70C279A0E0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkDemandSensitivity,
	]
	default_interface = ISIAPINetworkDemandSensitivity

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkFolder'
class SIAPINetworkFolder(CoClassBaseClass): # A CoClass
	CLSID = IID('{EABC402D-EA39-45D4-B70C-57ABA79EE4AE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkFolder,
	]
	default_interface = ISIAPINetworkFolder

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkFolders'
class SIAPINetworkFolders(CoClassBaseClass): # A CoClass
	CLSID = IID('{14AB4741-60D5-4E2C-A7D9-391036F4ADA2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkFolders,
		IEnumerable,
	]
	default_interface = ISIAPINetworkFolders

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkLegConnection'
class SIAPINetworkLegConnection(CoClassBaseClass): # A CoClass
	CLSID = IID('{16F09299-E4AE-446A-961B-8EE1ABB10071}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkLegConnection,
	]
	default_interface = ISIAPINetworkLegConnection

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkLegConnections'
class SIAPINetworkLegConnections(CoClassBaseClass): # A CoClass
	CLSID = IID('{01B7EA08-A88F-45BE-903F-FB14E5182042}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkLegConnections,
		IEnumerable,
	]
	default_interface = ISIAPINetworkLegConnections

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkMC'
class SIAPINetworkMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{2574B151-F7F0-4022-9BA1-A341BC5D729C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkMC,
	]
	default_interface = ISIAPINetworkMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkMCs'
class SIAPINetworkMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{CEE4DFD4-600F-4DAC-BA31-BE8B7F1DF783}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkMCs,
		IEnumerable,
	]
	default_interface = ISIAPINetworkMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkSite'
class SIAPINetworkSite(CoClassBaseClass): # A CoClass
	CLSID = IID('{37361C6E-E0EE-4D90-AA13-88732732B094}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkSite,
	]
	default_interface = ISIAPINetworkSite

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworkSites'
class SIAPINetworkSites(CoClassBaseClass): # A CoClass
	CLSID = IID('{380DA3D4-9F8D-4C74-935B-707EA324270C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworkSites,
		IEnumerable,
	]
	default_interface = ISIAPINetworkSites

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPINetworks'
class SIAPINetworks(CoClassBaseClass): # A CoClass
	CLSID = IID('{19F0570A-094B-4C3E-A770-FFCA0601ADDA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPINetworks,
		IEnumerable,
	]
	default_interface = ISIAPINetworks

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOpposingmovement_ped'
class SIAPIOpposingmovement_ped(CoClassBaseClass): # A CoClass
	CLSID = IID('{5AC30B47-D990-41E3-A4E7-A6EB907B1552}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOpposingmovement_ped,
	]
	default_interface = ISIAPIOpposingmovement_ped

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOpposingmovement_peds'
class SIAPIOpposingmovement_peds(CoClassBaseClass): # A CoClass
	CLSID = IID('{D9E4FBC3-03B6-41E7-A725-5D0300B1D687}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOpposingmovement_peds,
		IEnumerable,
	]
	default_interface = ISIAPIOpposingmovement_peds

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOpposingmovement_vehicle'
class SIAPIOpposingmovement_vehicle(CoClassBaseClass): # A CoClass
	CLSID = IID('{99EEB0D9-CD36-4CC6-B8D7-924CE09C963D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOpposingmovement_vehicle,
	]
	default_interface = ISIAPIOpposingmovement_vehicle

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOpposingmovement_vehicles'
class SIAPIOpposingmovement_vehicles(CoClassBaseClass): # A CoClass
	CLSID = IID('{EAEECED7-036B-4734-BCA8-8EF70D134D28}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOpposingmovement_vehicles,
		IEnumerable,
	]
	default_interface = ISIAPIOpposingmovement_vehicles

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputAnalysis'
class SIAPIOutputAnalysis(CoClassBaseClass): # A CoClass
	CLSID = IID('{2B3CCFD8-4A9C-4A0E-B589-3D1F3A6FFEA1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputAnalysis,
	]
	default_interface = ISIAPIOutputAnalysis

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputCirculatingLane'
class SIAPIOutputCirculatingLane(CoClassBaseClass): # A CoClass
	CLSID = IID('{207A9ACF-CDFD-415C-8D9F-07019F6CF7AB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputCirculatingLane,
	]
	default_interface = ISIAPIOutputCirculatingLane

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputCirculatingLaneMC'
class SIAPIOutputCirculatingLaneMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{AC1E9E02-F9EB-4AE2-91B7-8E0656BB3918}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputCirculatingLaneMC,
	]
	default_interface = ISIAPIOutputCirculatingLaneMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputCirculatingLaneMCs'
class SIAPIOutputCirculatingLaneMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{FF4EC6A5-5840-4E3D-84E1-86F02CC3F788}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputCirculatingLaneMCs,
		IEnumerable,
	]
	default_interface = ISIAPIOutputCirculatingLaneMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputCirculatingLanes'
class SIAPIOutputCirculatingLanes(CoClassBaseClass): # A CoClass
	CLSID = IID('{B191000C-58A2-414D-AE1C-4EFC68B3827A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputCirculatingLanes,
		IEnumerable,
	]
	default_interface = ISIAPIOutputCirculatingLanes

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputGraphTuple'
class SIAPIOutputGraphTuple(CoClassBaseClass): # A CoClass
	CLSID = IID('{F7AAE6AF-D859-4522-A447-CD18941AE963}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputGraphTuple,
	]
	default_interface = ISIAPIOutputGraphTuple

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputGraphTuples'
class SIAPIOutputGraphTuples(CoClassBaseClass): # A CoClass
	CLSID = IID('{8177D1E3-5454-4BB5-AE18-D7147D4C8A35}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputGraphTuples,
		IEnumerable,
	]
	default_interface = ISIAPIOutputGraphTuples

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLane'
class SIAPIOutputLane(CoClassBaseClass): # A CoClass
	CLSID = IID('{F51F3BC3-A54E-4748-9886-5D4F3C30D4F0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLane,
	]
	default_interface = ISIAPIOutputLane

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLaneExit'
class SIAPIOutputLaneExit(CoClassBaseClass): # A CoClass
	CLSID = IID('{BF2C2275-C235-40CF-A2AB-54A9C372C1D9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLaneExit,
	]
	default_interface = ISIAPIOutputLaneExit

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLaneExits'
class SIAPIOutputLaneExits(CoClassBaseClass): # A CoClass
	CLSID = IID('{DEBB105B-76D0-4FD5-A113-447035DC51FC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLaneExits,
		IEnumerable,
	]
	default_interface = ISIAPIOutputLaneExits

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLaneGreenPeriod'
class SIAPIOutputLaneGreenPeriod(CoClassBaseClass): # A CoClass
	CLSID = IID('{1E733D74-F977-426E-93F7-2A8BF1454878}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLaneGreenPeriod,
	]
	default_interface = ISIAPIOutputLaneGreenPeriod

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLaneGreenPeriods'
class SIAPIOutputLaneGreenPeriods(CoClassBaseClass): # A CoClass
	CLSID = IID('{2FF0DB72-0FE3-4A4D-B5CF-904BB39595AA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLaneGreenPeriods,
		IEnumerable,
	]
	default_interface = ISIAPIOutputLaneGreenPeriods

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLaneMC'
class SIAPIOutputLaneMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{AD35D08C-C0AF-4D8F-9B88-751892BB25E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLaneMC,
	]
	default_interface = ISIAPIOutputLaneMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLaneMCs'
class SIAPIOutputLaneMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{1FBBD5AB-E682-4C06-BEFC-6EDB64D3666A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLaneMCs,
		IEnumerable,
	]
	default_interface = ISIAPIOutputLaneMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLaneOD'
class SIAPIOutputLaneOD(CoClassBaseClass): # A CoClass
	CLSID = IID('{B378D9C3-4E9D-4819-8762-BD68819E5CB2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLaneOD,
	]
	default_interface = ISIAPIOutputLaneOD

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLaneODMC'
class SIAPIOutputLaneODMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{4F4B3FF2-23D4-4461-AACB-6E2F84E31DC0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLaneODMC,
	]
	default_interface = ISIAPIOutputLaneODMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLaneODMCs'
class SIAPIOutputLaneODMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{BA8AE905-D5B8-4CAB-B5F4-FCA3F78E9E63}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLaneODMCs,
		IEnumerable,
	]
	default_interface = ISIAPIOutputLaneODMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLaneODs'
class SIAPIOutputLaneODs(CoClassBaseClass): # A CoClass
	CLSID = IID('{AF3C822E-8BAC-4DA0-819B-9312B69AD052}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLaneODs,
		IEnumerable,
	]
	default_interface = ISIAPIOutputLaneODs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLanes'
class SIAPIOutputLanes(CoClassBaseClass): # A CoClass
	CLSID = IID('{0D940366-6119-4660-8B95-80796E0695DB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLanes,
		IEnumerable,
	]
	default_interface = ISIAPIOutputLanes

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLeg'
class SIAPIOutputLeg(CoClassBaseClass): # A CoClass
	CLSID = IID('{E9A07B34-F024-4B0D-8F6E-54F6E743AC2C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLeg,
	]
	default_interface = ISIAPIOutputLeg

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLegMC'
class SIAPIOutputLegMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{F3741C26-DB83-4B1A-B27C-3A77398B820D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLegMC,
	]
	default_interface = ISIAPIOutputLegMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLegMCs'
class SIAPIOutputLegMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{A8384538-2E01-41E9-B927-A1B92997CBAE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLegMCs,
		IEnumerable,
	]
	default_interface = ISIAPIOutputLegMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLegPerson'
class SIAPIOutputLegPerson(CoClassBaseClass): # A CoClass
	CLSID = IID('{437CCE51-F160-474A-9E8C-2F4563AB7972}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLegPerson,
	]
	default_interface = ISIAPIOutputLegPerson

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLegPersons'
class SIAPIOutputLegPersons(CoClassBaseClass): # A CoClass
	CLSID = IID('{6894003C-85BB-4C7D-AF06-4DA6296A53CD}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLegPersons,
		IEnumerable,
	]
	default_interface = ISIAPIOutputLegPersons

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputLegs'
class SIAPIOutputLegs(CoClassBaseClass): # A CoClass
	CLSID = IID('{CC917735-7108-44B2-AB13-4CA33F9BF15E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputLegs,
		IEnumerable,
	]
	default_interface = ISIAPIOutputLegs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMeteredRoundabout'
class SIAPIOutputMeteredRoundabout(CoClassBaseClass): # A CoClass
	CLSID = IID('{8E03F3A5-D77C-4D28-834D-5CEC97CB8B93}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMeteredRoundabout,
	]
	default_interface = ISIAPIOutputMeteredRoundabout

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementPed'
class SIAPIOutputMovementPed(CoClassBaseClass): # A CoClass
	CLSID = IID('{B3EBCA38-6BD7-47EE-860F-3CBAA18B0A8E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementPed,
	]
	default_interface = ISIAPIOutputMovementPed

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementPed_GreenPeriod'
class SIAPIOutputMovementPed_GreenPeriod(CoClassBaseClass): # A CoClass
	CLSID = IID('{84D7F6CD-F5FA-4A63-AAD3-A0836A53E19D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementPed_GreenPeriod,
	]
	default_interface = ISIAPIOutputMovementPed_GreenPeriod

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementPed_GreenPeriods'
class SIAPIOutputMovementPed_GreenPeriods(CoClassBaseClass): # A CoClass
	CLSID = IID('{9A430652-1CDD-473B-B7B7-30803DDFA31B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementPed_GreenPeriods,
		IEnumerable,
	]
	default_interface = ISIAPIOutputMovementPed_GreenPeriods

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementPeds'
class SIAPIOutputMovementPeds(CoClassBaseClass): # A CoClass
	CLSID = IID('{1365E5D6-A5D4-4F25-9103-C306C6367EDB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementPeds,
		IEnumerable,
	]
	default_interface = ISIAPIOutputMovementPeds

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementPersonOD'
class SIAPIOutputMovementPersonOD(CoClassBaseClass): # A CoClass
	CLSID = IID('{A72FF5DE-CE06-4986-AE4E-6A0264AC85FE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementPersonOD,
	]
	default_interface = ISIAPIOutputMovementPersonOD

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementPersonODMC'
class SIAPIOutputMovementPersonODMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{32E2E2DA-8053-4562-9511-995FAED66C61}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementPersonODMC,
	]
	default_interface = ISIAPIOutputMovementPersonODMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementPersonODMCs'
class SIAPIOutputMovementPersonODMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{701F5599-2068-4533-BBE9-1BEAE64344EB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementPersonODMCs,
		IEnumerable,
	]
	default_interface = ISIAPIOutputMovementPersonODMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementPersonODs'
class SIAPIOutputMovementPersonODs(CoClassBaseClass): # A CoClass
	CLSID = IID('{7448B67E-5F38-4E37-BF4C-A475561C7EFF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementPersonODs,
		IEnumerable,
	]
	default_interface = ISIAPIOutputMovementPersonODs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementVehicleOD'
class SIAPIOutputMovementVehicleOD(CoClassBaseClass): # A CoClass
	CLSID = IID('{62FF9ABF-31EF-46B7-A288-2B9074A70F87}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementVehicleOD,
	]
	default_interface = ISIAPIOutputMovementVehicleOD

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementVehicleODMC'
class SIAPIOutputMovementVehicleODMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{DE724601-782C-4198-A2CD-745C397898D4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementVehicleODMC,
	]
	default_interface = ISIAPIOutputMovementVehicleODMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementVehicleODMC_GreenPeriod'
class SIAPIOutputMovementVehicleODMC_GreenPeriod(CoClassBaseClass): # A CoClass
	CLSID = IID('{A3C07D6F-05EB-4636-96F4-2F2E21B76559}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementVehicleODMC_GreenPeriod,
	]
	default_interface = ISIAPIOutputMovementVehicleODMC_GreenPeriod

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementVehicleODMC_GreenPeriods'
class SIAPIOutputMovementVehicleODMC_GreenPeriods(CoClassBaseClass): # A CoClass
	CLSID = IID('{3B2A414F-F47E-46DA-A129-8FA0E569A68E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementVehicleODMC_GreenPeriods,
		IEnumerable,
	]
	default_interface = ISIAPIOutputMovementVehicleODMC_GreenPeriods

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementVehicleODMCs'
class SIAPIOutputMovementVehicleODMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{D8D3C9FE-9684-4EA9-AC7D-3E1533984744}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementVehicleODMCs,
		IEnumerable,
	]
	default_interface = ISIAPIOutputMovementVehicleODMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMovementVehicleODs'
class SIAPIOutputMovementVehicleODs(CoClassBaseClass): # A CoClass
	CLSID = IID('{1D7046CE-4C37-4EE0-957D-F78BD3FE40E0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMovementVehicleODs,
		IEnumerable,
	]
	default_interface = ISIAPIOutputMovementVehicleODs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMultiSequenceAnalyses'
class SIAPIOutputMultiSequenceAnalyses(CoClassBaseClass): # A CoClass
	CLSID = IID('{41E3DF9C-C236-47ED-A1C3-30A9F5C14C9A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMultiSequenceAnalyses,
		IEnumerable,
	]
	default_interface = ISIAPIOutputMultiSequenceAnalyses

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputMultiSequenceAnalysis'
class SIAPIOutputMultiSequenceAnalysis(CoClassBaseClass): # A CoClass
	CLSID = IID('{BD186FED-F0F8-49DA-B585-FBE8ED785FE5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputMultiSequenceAnalysis,
	]
	default_interface = ISIAPIOutputMultiSequenceAnalysis

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputNetwork'
class SIAPIOutputNetwork(CoClassBaseClass): # A CoClass
	CLSID = IID('{2AACA59E-CEC2-4BF8-B07B-C12BD329A7E9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputNetwork,
	]
	default_interface = ISIAPIOutputNetwork

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputNetworkGraphTuple'
class SIAPIOutputNetworkGraphTuple(CoClassBaseClass): # A CoClass
	CLSID = IID('{761871EA-EF42-4D9E-AD88-1363E5E9CCD9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputNetworkGraphTuple,
	]
	default_interface = ISIAPIOutputNetworkGraphTuple

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputNetworkGraphTuples'
class SIAPIOutputNetworkGraphTuples(CoClassBaseClass): # A CoClass
	CLSID = IID('{C4474735-1E00-4BA4-A903-A89A9D95381D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputNetworkGraphTuples,
		IEnumerable,
	]
	default_interface = ISIAPIOutputNetworkGraphTuples

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputNetworkPedestrian'
class SIAPIOutputNetworkPedestrian(CoClassBaseClass): # A CoClass
	CLSID = IID('{BBEAE5FC-9424-4977-9EE8-1177608D1825}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputNetworkPedestrian,
	]
	default_interface = ISIAPIOutputNetworkPedestrian

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputNetworkPerson'
class SIAPIOutputNetworkPerson(CoClassBaseClass): # A CoClass
	CLSID = IID('{6183EA81-DA0E-44B6-B40D-F1DAF0933E78}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputNetworkPerson,
	]
	default_interface = ISIAPIOutputNetworkPerson

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputNetworkVehicle'
class SIAPIOutputNetworkVehicle(CoClassBaseClass): # A CoClass
	CLSID = IID('{82306492-4410-44E4-BBEE-D4223CB0DA23}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputNetworkVehicle,
	]
	default_interface = ISIAPIOutputNetworkVehicle

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputPhase'
class SIAPIOutputPhase(CoClassBaseClass): # A CoClass
	CLSID = IID('{B640710A-977F-4313-BED9-C576EF0C58F1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputPhase,
	]
	default_interface = ISIAPIOutputPhase

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputPhaseMovTimingPath'
class SIAPIOutputPhaseMovTimingPath(CoClassBaseClass): # A CoClass
	CLSID = IID('{84CB4043-3761-4F41-93D0-A36BD048C9F9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputPhaseMovTimingPath,
	]
	default_interface = ISIAPIOutputPhaseMovTimingPath

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputPhaseMovTimingPathMovement'
class SIAPIOutputPhaseMovTimingPathMovement(CoClassBaseClass): # A CoClass
	CLSID = IID('{1B8CC9B3-532D-453B-AF77-5CB719ECCA69}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputPhaseMovTimingPathMovement,
	]
	default_interface = ISIAPIOutputPhaseMovTimingPathMovement

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputPhaseMovTimingPathMovements'
class SIAPIOutputPhaseMovTimingPathMovements(CoClassBaseClass): # A CoClass
	CLSID = IID('{1C744150-30B7-468A-AC2E-262F67C49910}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputPhaseMovTimingPathMovements,
		IEnumerable,
	]
	default_interface = ISIAPIOutputPhaseMovTimingPathMovements

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputPhaseMovTimingPaths'
class SIAPIOutputPhaseMovTimingPaths(CoClassBaseClass): # A CoClass
	CLSID = IID('{50CFC083-8D6F-423C-8C80-B976A18F15AE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputPhaseMovTimingPaths,
		IEnumerable,
	]
	default_interface = ISIAPIOutputPhaseMovTimingPaths

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputPhases'
class SIAPIOutputPhases(CoClassBaseClass): # A CoClass
	CLSID = IID('{6180E4A3-7220-40A9-B67E-1A1E2980081F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputPhases,
		IEnumerable,
	]
	default_interface = ISIAPIOutputPhases

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputRouteMovementBasedPerson'
class SIAPIOutputRouteMovementBasedPerson(CoClassBaseClass): # A CoClass
	CLSID = IID('{F9033992-8196-424F-9725-D4E387E2110D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputRouteMovementBasedPerson,
	]
	default_interface = ISIAPIOutputRouteMovementBasedPerson

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputRouteMovementBasedVehicle'
class SIAPIOutputRouteMovementBasedVehicle(CoClassBaseClass): # A CoClass
	CLSID = IID('{FDC3E673-E1B9-4AC2-9503-BCE42A55CD58}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputRouteMovementBasedVehicle,
	]
	default_interface = ISIAPIOutputRouteMovementBasedVehicle

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputSequence'
class SIAPIOutputSequence(CoClassBaseClass): # A CoClass
	CLSID = IID('{606A4EB4-6E73-4DB2-8E4A-610842F7F05B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputSequence,
	]
	default_interface = ISIAPIOutputSequence

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputSitePedestrian'
class SIAPIOutputSitePedestrian(CoClassBaseClass): # A CoClass
	CLSID = IID('{270364E1-ECE5-4E2E-A7D4-1337FC506CE9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputSitePedestrian,
	]
	default_interface = ISIAPIOutputSitePedestrian

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputSitePerson'
class SIAPIOutputSitePerson(CoClassBaseClass): # A CoClass
	CLSID = IID('{272D58B6-297A-4958-B030-4C7B65DE12B9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputSitePerson,
	]
	default_interface = ISIAPIOutputSitePerson

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputSiteRoute'
class SIAPIOutputSiteRoute(CoClassBaseClass): # A CoClass
	CLSID = IID('{2E78F5C0-56C2-4BF1-B1D1-1A62D5A8420D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputSiteRoute,
	]
	default_interface = ISIAPIOutputSiteRoute

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputSiteRoutes'
class SIAPIOutputSiteRoutes(CoClassBaseClass): # A CoClass
	CLSID = IID('{5507EC83-9958-413B-BF33-40958E76EF71}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputSiteRoutes,
		IEnumerable,
	]
	default_interface = ISIAPIOutputSiteRoutes

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputSiteVehicle'
class SIAPIOutputSiteVehicle(CoClassBaseClass): # A CoClass
	CLSID = IID('{5AE191CE-B05A-4EC0-93A2-7C18E4C68F62}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputSiteVehicle,
	]
	default_interface = ISIAPIOutputSiteVehicle

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIOutputset'
class SIAPIOutputset(CoClassBaseClass): # A CoClass
	CLSID = IID('{5CCD43AB-186C-4353-BA54-9F5C7081FC75}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIOutputset,
	]
	default_interface = ISIAPIOutputset

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIPhase'
class SIAPIPhase(CoClassBaseClass): # A CoClass
	CLSID = IID('{601FC223-4405-429B-A762-BC05946EDE1E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIPhase,
	]
	default_interface = ISIAPIPhase

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIPhasemovement_ped'
class SIAPIPhasemovement_ped(CoClassBaseClass): # A CoClass
	CLSID = IID('{AE225517-D441-49D9-926F-18E976A6A05C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIPhasemovement_ped,
	]
	default_interface = ISIAPIPhasemovement_ped

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIPhasemovement_peds'
class SIAPIPhasemovement_peds(CoClassBaseClass): # A CoClass
	CLSID = IID('{66368ABF-3FE9-46B0-83AB-E291B28BD09D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIPhasemovement_peds,
		IEnumerable,
	]
	default_interface = ISIAPIPhasemovement_peds

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIPhasemovement_vehicle'
class SIAPIPhasemovement_vehicle(CoClassBaseClass): # A CoClass
	CLSID = IID('{B18833B0-DFF8-4104-8CF7-CC6E72B2A0CC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIPhasemovement_vehicle,
	]
	default_interface = ISIAPIPhasemovement_vehicle

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIPhasemovement_vehicles'
class SIAPIPhasemovement_vehicles(CoClassBaseClass): # A CoClass
	CLSID = IID('{3E7EF29A-8A66-4DDE-B091-F3D882406164}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIPhasemovement_vehicles,
		IEnumerable,
	]
	default_interface = ISIAPIPhasemovement_vehicles

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIPhases'
class SIAPIPhases(CoClassBaseClass): # A CoClass
	CLSID = IID('{B17972E8-D253-40CB-8820-68BBE891708A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIPhases,
		IEnumerable,
	]
	default_interface = ISIAPIPhases

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIProject'
class SIAPIProject(CoClassBaseClass): # A CoClass
	CLSID = IID('{AA3D5162-1291-44E3-B6DB-168A66FA698F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIProject,
	]
	default_interface = ISIAPIProject

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIRoute'
class SIAPIRoute(CoClassBaseClass): # A CoClass
	CLSID = IID('{F41B79F2-95A5-485C-B977-48171C90931E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIRoute,
	]
	default_interface = ISIAPIRoute

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIRouteMC'
class SIAPIRouteMC(CoClassBaseClass): # A CoClass
	CLSID = IID('{E1AE119F-DBA4-4CFC-B95A-58A0F45607D0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIRouteMC,
	]
	default_interface = ISIAPIRouteMC

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIRouteMCs'
class SIAPIRouteMCs(CoClassBaseClass): # A CoClass
	CLSID = IID('{6968C090-DAA4-4E9B-A7CB-2BDE998AF328}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIRouteMCs,
		IEnumerable,
	]
	default_interface = ISIAPIRouteMCs

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIRouteNwSite'
class SIAPIRouteNwSite(CoClassBaseClass): # A CoClass
	CLSID = IID('{DE246637-0712-4778-9FE3-1A6E50F0DF60}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIRouteNwSite,
	]
	default_interface = ISIAPIRouteNwSite

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIRouteNwSites'
class SIAPIRouteNwSites(CoClassBaseClass): # A CoClass
	CLSID = IID('{3F421D2F-DDB0-4089-AFE4-8BED7C14BFA8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIRouteNwSites,
		IEnumerable,
	]
	default_interface = ISIAPIRouteNwSites

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPIRoutes'
class SIAPIRoutes(CoClassBaseClass): # A CoClass
	CLSID = IID('{14C9EB51-3E0F-407C-BD50-FB301D141A8A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPIRoutes,
		IEnumerable,
	]
	default_interface = ISIAPIRoutes

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPISensitivity'
class SIAPISensitivity(CoClassBaseClass): # A CoClass
	CLSID = IID('{562BD1F6-FCD9-4F3E-8F07-F2AA2274B12A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPISensitivity,
	]
	default_interface = ISIAPISensitivity

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPISequence'
class SIAPISequence(CoClassBaseClass): # A CoClass
	CLSID = IID('{93907DC0-76DC-4B13-BE89-09CC209EC779}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPISequence,
	]
	default_interface = ISIAPISequence

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPISequences'
class SIAPISequences(CoClassBaseClass): # A CoClass
	CLSID = IID('{EC6DC582-D6C0-4DAA-B2A6-8A1E7C9E6ED2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPISequences,
		IEnumerable,
	]
	default_interface = ISIAPISequences

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPISite'
class SIAPISite(CoClassBaseClass): # A CoClass
	CLSID = IID('{1D0A3CAF-D0CF-4AC2-BCD6-FD377579759B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPISite,
	]
	default_interface = ISIAPISite

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPISiteFolder'
class SIAPISiteFolder(CoClassBaseClass): # A CoClass
	CLSID = IID('{51678BC8-2907-4D52-AB68-95CFCA3C029C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPISiteFolder,
	]
	default_interface = ISIAPISiteFolder

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPISiteFolders'
class SIAPISiteFolders(CoClassBaseClass): # A CoClass
	CLSID = IID('{B1DB958A-0F80-4845-B4FD-FED3BEDAFE13}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPISiteFolders,
		IEnumerable,
	]
	default_interface = ISIAPISiteFolders

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPISites'
class SIAPISites(CoClassBaseClass): # A CoClass
	CLSID = IID('{2322E0C4-40D9-46EF-9ACA-52AF8BA62A2D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPISites,
		IEnumerable,
	]
	default_interface = ISIAPISites

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPITwoWaySignControlAdjGeometryControl'
class SIAPITwoWaySignControlAdjGeometryControl(CoClassBaseClass): # A CoClass
	CLSID = IID('{F2A4712E-4165-42F8-9336-30DA604C4279}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPITwoWaySignControlAdjGeometryControl,
	]
	default_interface = ISIAPITwoWaySignControlAdjGeometryControl

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPITwoWaySignControlAdjGeometryControls'
class SIAPITwoWaySignControlAdjGeometryControls(CoClassBaseClass): # A CoClass
	CLSID = IID('{CD5FBEDB-CBE3-4A86-A2E8-BF71E507C463}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPITwoWaySignControlAdjGeometryControls,
		IEnumerable,
	]
	default_interface = ISIAPITwoWaySignControlAdjGeometryControls

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPITwoWaySignControlAdjMajorNumLane'
class SIAPITwoWaySignControlAdjMajorNumLane(CoClassBaseClass): # A CoClass
	CLSID = IID('{17E1A63D-976D-4A05-9151-8491AD5D8712}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPITwoWaySignControlAdjMajorNumLane,
	]
	default_interface = ISIAPITwoWaySignControlAdjMajorNumLane

# This CoClass is known by the name 'SIDRASolutions.SI.API.SIAPITwoWaySignControlAdjMajorNumLanes'
class SIAPITwoWaySignControlAdjMajorNumLanes(CoClassBaseClass): # A CoClass
	CLSID = IID('{A5050181-1C6A-4BF4-A8C5-4A712A954A90}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Object,
		ISIAPITwoWaySignControlAdjMajorNumLanes,
		IEnumerable,
	]
	default_interface = ISIAPITwoWaySignControlAdjMajorNumLanes

# This CoClass is known by the name 'SIDRASolutions.SI.Licensing.SIOptionCustomData'
class SIOptionCustomData(CoClassBaseClass): # A CoClass
	CLSID = IID('{035BB123-A169-3E54-84A2-35F3A2E4521B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_SIOptionCustomData,
		_Object,
	]
	default_interface = _SIOptionCustomData

IDisposable_vtables_dispatch_ = 1
IDisposable_vtables_ = [
	(( 'Dispose' , ), 1610743808, (1610743808, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IEnumerable_vtables_dispatch_ = 1
IEnumerable_vtables_ = [
	(( 'GetEnumerator' , 'pRetVal' , ), -4, (-4, (), [ (16397, 10, None, "IID('{00020404-0000-0000-C000-000000000046}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

ISIAPI_vtables_dispatch_ = 1
ISIAPI_vtables_ = [
	(( 'Project' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{5817180B-2283-40FB-8068-C2F2D656EF04}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'IsLicensed' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IntPtrSize' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'OpenProject' , 'filename' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'CloseProject' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SubmitDataChanges' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'OpenDbConnection' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'CloseDbConnection' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Close' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'CreateAndOpenProject' , 'filename' , 'newProjectName' , 'pRetVal' , ), 1610743819, (1610743819, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

ISIAPIAnalysis_vtables_dispatch_ = 1
ISIAPIAnalysis_vtables_ = [
	(( 'Site' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Analysis_option' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Analysis_option' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Selected_sensitivity_groupno' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Selected_sensitivity_groupno' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Objective' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Objective' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Growth_Model' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Growth_Model' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Years' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Years' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Is_constant_num_years_applied' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Is_constant_num_years_applied' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Constant_num_years' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Constant_num_years' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Objective' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Objective' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Lower' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Lower' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Upper' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Upper' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Is_constant_factor_applied' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Is_constant_factor_applied' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Constant_factor' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Constant_factor' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'SensitivityGeneralParameterGroup' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16393, 10, None, "IID('{D025138A-4F4C-4613-8FA7-D1FD5550A50C}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'SensitivityRoundaboutParameterGroup' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16393, 10, None, "IID('{D025138A-4F4C-4613-8FA7-D1FD5550A50C}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Result_option' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Result_option' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Result_leg_origin' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Result_leg_origin' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Result_lane_origin' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Result_lane_origin' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Result_laneno' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Result_laneno' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Result_vehmov_origin' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Result_vehmov_origin' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Result_vehmov_dest' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Result_vehmov_dest' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Result_mc_class' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Result_mc_class' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Result_pedmov_option' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Result_pedmov_option' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Result_pedmov_origin' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Result_pedmov_origin' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Result_pedmov_type' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Result_pedmov_type' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Result_pedmov_stage_no' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Result_pedmov_stage_no' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
]

ISIAPIDiagnosticMsg_vtables_dispatch_ = 1
ISIAPIDiagnosticMsg_vtables_ = [
	(( 'Message' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Message_type' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Log_time' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIDiagnosticMsgs_vtables_dispatch_ = 1
ISIAPIDiagnosticMsgs_vtables_ = [
	(( 'Item' , 'index' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{CC6E10F5-9A73-41A2-BCA8-235D7FB0091A}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPIGapAcceptanceSpecificApp_vtables_dispatch_ = 1
ISIAPIGapAcceptanceSpecificApp_vtables_ = [
	(( 'Critical_gap' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'End_departures' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'End_departures' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Exit_flow_effect' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Exit_flow_effect' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Percent_opposed_by_nearest' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Percent_opposed_by_nearest' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

ISIAPIIsland_vtables_dispatch_ = 1
ISIAPIIsland_vtables_ = [
	(( 'Island_no' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Is_pedstage_separator' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Is_pedstage_separator' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Is_rou_splitter' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Width_back' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Width_back' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Fill_style' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Fill_style' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Leg' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16393, 10, None, "IID('{24A8E5D9-0016-45F2-9941-12E58EE54A05}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Is_short' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Is_short' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Is_for_freeway' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Is_for_freeway' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ConnectedIsland' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16393, 10, None, "IID('{E741707B-9A4C-414A-A4F0-482E5F098534}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ConnectedIsland' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (9, 1, None, "IID('{E741707B-9A4C-414A-A4F0-482E5F098534}')") , ], 1 , 8 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

ISIAPIIslands_vtables_dispatch_ = 1
ISIAPIIslands_vtables_ = [
	(( 'Item' , 'Island_no' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E741707B-9A4C-414A-A4F0-482E5F098534}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'IslandExists' , 'Island_no' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneApproach_vtables_dispatch_ = 1
ISIAPILaneApproach_vtables_ = [
	(( 'Laneno' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Configuration' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Configuration' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Control_type' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Control_type' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Grade' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Grade' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Slip_control_type' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Slip_control_type' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Basic_saturation_flow' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Basic_saturation_flow' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Utilisation_user' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Utilisation_user' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Utilisation' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Utilisation' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Saturation_speed_user' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Saturation_speed_user' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Saturation_speed' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Saturation_speed' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adjustment' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adjustment' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Is_capacity_adj_for_network' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Is_capacity_adj_for_network' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Is_dominant_lane' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Is_dominant_lane' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Is_sliplane_included_in_entry_lane_count' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Is_sliplane_included_in_entry_lane_count' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Buses_stopping_user' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Buses_stopping_user' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Buses_stopping' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Buses_stopping' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Parking_manoeuvres_user' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Parking_manoeuvres_user' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Parking_manoeuvres' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Parking_manoeuvres' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Is_sliplane_excluded_from_signal_analysis' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Is_sliplane_excluded_from_signal_analysis' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'LaneApproachMovements' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16393, 10, None, "IID('{881029ED-4A7E-4469-A782-F48BF5E0F373}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'LaneMovements' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16393, 10, None, "IID('{C1711C63-BCCC-41F6-94CC-80BFBF951D74}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Segment1' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16393, 10, None, "IID('{6BE9B7D6-A12E-4CB5-A938-08260963BE84}')") , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Segment2' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16393, 10, None, "IID('{6BE9B7D6-A12E-4CB5-A938-08260963BE84}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Leg' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16393, 10, None, "IID('{24A8E5D9-0016-45F2-9941-12E58EE54A05}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Is_departure_headway_awsc_applied' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Is_departure_headway_awsc_applied' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Departure_headway_awsc' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Departure_headway_awsc' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'RemoveDisciplines' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Is_satn_flow_estimation_applied' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Is_satn_flow_estimation_applied' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_capacity_option' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_capacity_option' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_capacity_factor' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_capacity_factor' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Delay_model_param_user' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Delay_model_param_user' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Delay_model_param' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Delay_model_param' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Initial_demand_vol' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Initial_demand_vol' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneApproachMovement_vtables_dispatch_ = 1
ISIAPILaneApproachMovement_vtables_ = [
	(( 'Destination' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Free_queue' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Free_queue' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LaneApproachMovementMCs' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{E94C2A89-6DE0-4AE6-82E9-48DD3B752E1A}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LaneApproach' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneApproachMovementMC_vtables_dispatch_ = 1
ISIAPILaneApproachMovementMC_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LaneApproachMovement' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{5C8E5D1E-E796-4190-8965-8BBD365D0D7F}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneApproachMovementMCs_vtables_dispatch_ = 1
ISIAPILaneApproachMovementMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{92115A53-7558-433A-AC10-E109B19E83ED}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneApproachMovements_vtables_dispatch_ = 1
ISIAPILaneApproachMovements_vtables_ = [
	(( 'Item' , 'Destination' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{5C8E5D1E-E796-4190-8965-8BBD365D0D7F}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneApproachs_vtables_dispatch_ = 1
ISIAPILaneApproachs_vtables_ = [
	(( 'Item' , 'Laneno' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LaneApproachExists' , 'Laneno' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AddLane' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RemoveLane' , ), 1610743811, (1610743811, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneExit_vtables_dispatch_ = 1
ISIAPILaneExit_vtables_ = [
	(( 'Laneno' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Configuration' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Configuration' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Grade' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Grade' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'LaneMovements' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16393, 10, None, "IID('{C1711C63-BCCC-41F6-94CC-80BFBF951D74}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Segment1' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16393, 10, None, "IID('{6BE9B7D6-A12E-4CB5-A938-08260963BE84}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Segment2' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16393, 10, None, "IID('{6BE9B7D6-A12E-4CB5-A938-08260963BE84}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Leg' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16393, 10, None, "IID('{24A8E5D9-0016-45F2-9941-12E58EE54A05}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Is_merge_applied' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Is_merge_applied' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Merge_type' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Merge_type' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'PriorityMergeParam' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16393, 10, None, "IID('{9702C419-60FE-48C2-8412-23B83BF5C78C}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ZipperMergeParam' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16393, 10, None, "IID('{9702C419-60FE-48C2-8412-23B83BF5C78C}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneExitMergeParam_vtables_dispatch_ = 1
ISIAPILaneExitMergeParam_vtables_ = [
	(( 'Percent_opposing_shortlane' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Percent_opposing_shortlane' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Percent_opposing_mergelane' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Percent_opposing_mergelane' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_departures' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_departures' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'LaneExit' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16393, 10, None, "IID('{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneExits_vtables_dispatch_ = 1
ISIAPILaneExits_vtables_ = [
	(( 'Item' , 'Laneno' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LaneExitExists' , 'Laneno' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AddLane' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RemoveLane' , ), 1610743811, (1610743811, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneMovement_vtables_dispatch_ = 1
ISIAPILaneMovement_vtables_ = [
	(( 'Origin' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'OriginLaneno' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Destination' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DestinationLaneno' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Lane_blockage_calib_factor' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Lane_blockage_calib_factor' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LaneMovementMCs' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{D8D650BB-D92A-4A21-9F34-F76F1C225497}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneMovementMC_vtables_dispatch_ = 1
ISIAPILaneMovementMC_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Flow_proportion' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Flow_proportion' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LaneMovement' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{6DC82697-7A67-4BB3-8DA8-3F51C1D71135}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneMovementMCs_vtables_dispatch_ = 1
ISIAPILaneMovementMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{D1EA4B6C-DC27-44B5-B0BE-233F53D81B6C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneMovements_vtables_dispatch_ = 1
ISIAPILaneMovements_vtables_ = [
	(( 'Item' , 'Leg' , 'Laneno' , 'pRetVal' , ), 0, (0, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{6DC82697-7A67-4BB3-8DA8-3F51C1D71135}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LaneMovementExists' , 'Leg' , 'Laneno' , 'pRetVal' , ), 1610743809, (1610743809, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneSegment_vtables_dispatch_ = 1
ISIAPILaneSegment_vtables_ = [
	(( 'Segment_no' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Colour' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Colour' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Display_id' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Display_id' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Overflow_merge_lane_num_1' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Overflow_merge_lane_num_1' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'LaneSegmentMCs' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16393, 10, None, "IID('{4962E57C-6B9E-4331-94DB-F141DA807485}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'LaneApproach' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16393, 10, None, "IID('{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'LaneExit' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16393, 10, None, "IID('{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneSegmentMC_vtables_dispatch_ = 1
ISIAPILaneSegmentMC_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Percent_change_to_left' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Percent_change_to_left' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Percent_change_to_right' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Percent_change_to_right' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'LaneSegment' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{6BE9B7D6-A12E-4CB5-A938-08260963BE84}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISIAPILaneSegmentMCs_vtables_dispatch_ = 1
ISIAPILaneSegmentMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{52442B71-F816-4AA6-9A01-9F66957C3925}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPILeg_vtables_dispatch_ = 1
ISIAPILeg_vtables_ = [
	(( 'Orientation' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Approach_distance' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Approach_distance' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Exit_distance_user' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Exit_distance_user' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Exit_distance' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Exit_distance' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Extra_bunching_user' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Extra_bunching_user' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Extra_bunching' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Extra_bunching' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Area_type_factor' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Area_type_factor' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Approach_control' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Approach_control' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Is_departure_headway_awsc_applied' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Is_departure_headway_awsc_applied' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'LegGeometry' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'LegGeometry' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Site' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Leg_roundabout' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16393, 10, None, "IID('{25BFA806-8BFC-4ADF-9A0B-9DA47FE86246}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'LaneApproachs' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16393, 10, None, "IID('{148779D1-5A0D-48B1-9CBB-7002DAB05D95}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'LaneExits' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16393, 10, None, "IID('{99F74111-A47C-45B1-94DE-16E6F4194A60}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Islands' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16393, 10, None, "IID('{6B55FEF0-D591-4E75-B2BA-81E22B796325}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'InsertApproachLane' , 'positionOnLeg' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{5F156412-3EAE-40A0-99B2-06D8E48D87D1}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'InsertExitLane' , 'positionOnLeg' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{FE1B8A3D-ECC2-4B36-876E-FDB052503918}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'InsertIsland' , 'positionOnLeg' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E741707B-9A4C-414A-A4F0-482E5F098534}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'InsertIsland_RoundaboutSplitter' , 'positionOnLeg' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E741707B-9A4C-414A-A4F0-482E5F098534}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RemoveItem' , 'positionOnLeg' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'MovementPedSlipLane_Existing' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16393, 10, None, "IID('{0099AEAC-F9B6-4DCE-9C0E-1434E9D603D7}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Is_uturn_before_intersection' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Is_uturn_before_intersection' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Is_uturn_before_intersection_excluded_from_signal_analysis' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Is_uturn_before_intersection_excluded_from_signal_analysis' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Extra_bunching_nw_user' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Extra_bunching_nw_user' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Extra_bunching_nw' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Extra_bunching_nw' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
]

ISIAPILeg_rou_hcm_vtables_dispatch_ = 1
ISIAPILeg_rou_hcm_vtables_ = [
	(( 'Hcm_model' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Model_calib_factor' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Model_calib_factor' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Entry_circ_adj' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Entry_circ_adj' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_single_entry_param_a' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_single_entry_param_a' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_single_entry_param_b' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_single_entry_param_b' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_multi_entry_param_a' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_multi_entry_param_a' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_multi_entry_param_b' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_multi_entry_param_b' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_single_entry_param_a' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_single_entry_param_a' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_single_entry_param_b' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_single_entry_param_b' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_multi_entry_dominant_param_a' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_multi_entry_dominant_param_a' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_multi_entry_dominant_param_b' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_multi_entry_dominant_param_b' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_multi_entry_subdominant_param_a' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_multi_entry_subdominant_param_a' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_multi_entry_subdominant_param_b' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_multi_entry_subdominant_param_b' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Leg_roundabout' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16393, 10, None, "IID('{25BFA806-8BFC-4ADF-9A0B-9DA47FE86246}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

ISIAPILeg_rou_hcm6_extended_vtables_dispatch_ = 1
ISIAPILeg_rou_hcm6_extended_vtables_ = [
	(( 'Model_calib_factor' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Model_calib_factor' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Entry_circ_adj' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Entry_circ_adj' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_single_entry_param_a' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_single_entry_param_a' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_single_entry_param_b' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_single_entry_param_b' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_two_entry_dominant_param_a' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_two_entry_dominant_param_a' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_two_entry_dominant_param_b' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_two_entry_dominant_param_b' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_two_entry_subdominant_param_a' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_two_entry_subdominant_param_a' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_two_entry_subdominant_param_b' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_two_entry_subdominant_param_b' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_slip_entry_param_a' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_slip_entry_param_a' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_slip_entry_param_b' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Single_circ_slip_entry_param_b' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_single_entry_param_a' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_single_entry_param_a' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_single_entry_param_b' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_single_entry_param_b' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_two_entry_dominant_param_a' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_two_entry_dominant_param_a' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_two_entry_dominant_param_b' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_two_entry_dominant_param_b' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_two_entry_subdominant_param_a' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_two_entry_subdominant_param_a' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_two_entry_subdominant_param_b' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_two_entry_subdominant_param_b' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_three_entry_dominant_param_a' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_three_entry_dominant_param_a' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_three_entry_dominant_param_b' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_three_entry_dominant_param_b' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_three_entry_subdominant_param_a' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_three_entry_subdominant_param_a' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_three_entry_subdominant_param_b' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_three_entry_subdominant_param_b' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_slip_entry_param_a' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_slip_entry_param_a' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_slip_entry_param_b' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Multi_circ_slip_entry_param_b' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Leg_roundabout' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16393, 10, None, "IID('{25BFA806-8BFC-4ADF-9A0B-9DA47FE86246}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
]

ISIAPILeg_roundabout_vtables_dispatch_ = 1
ISIAPILeg_roundabout_vtables_ = [
	(( 'Num_circulating_lanes' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Num_circulating_lanes' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Num_downstream_circulating_lanes_user' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Num_downstream_circulating_lanes_user' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Num_downstream_circulating_lanes' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Num_downstream_circulating_lanes' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Circulating_width' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Circulating_width' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Island_diameter' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Island_diameter' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Inscribed_diameter_user' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Inscribed_diameter_user' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Inscribed_diameter' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Inscribed_diameter' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Entry_radius' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Entry_radius' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Entry_angle' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Entry_angle' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Is_raindrop_design' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Is_raindrop_design' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Circulating_transition_line' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Circulating_transition_line' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Environment_factor_user' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Environment_factor_user' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Environment_factor' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Environment_factor' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Entry_circ_adj_user' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Entry_circ_adj_user' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Entry_circ_adj' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Entry_circ_adj' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'App_half_width' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'App_half_width' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Flare_length' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Flare_length' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_at_zero_flow_user' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_at_zero_flow_user' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_at_zero_flow' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_at_zero_flow' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Grade_separated' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Grade_separated' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Leg' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16393, 10, None, "IID('{24A8E5D9-0016-45F2-9941-12E58EE54A05}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'LegRouHCM2010' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16393, 10, None, "IID('{13F6A490-E35F-4AF3-9FCE-843062E81CCD}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'LegRouHCM6' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16393, 10, None, "IID('{13F6A490-E35F-4AF3-9FCE-843062E81CCD}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'LegRouHCM6Extended' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16393, 10, None, "IID('{BD507F2C-6D0F-4256-8E40-79299F021130}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
]

ISIAPILegs_vtables_dispatch_ = 1
ISIAPILegs_vtables_ = [
	(( 'Item' , 'Orientation' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{24A8E5D9-0016-45F2-9941-12E58EE54A05}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LegExists' , 'Orientation' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIModelSetting_vtables_dispatch_ = 1
ISIAPIModelSetting_vtables_ = [
	(( 'LOS_Method' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LOS_Method' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LOS_Target' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LOS_Target' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Performance_Measure' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Performance_Measure' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Percentile_Queue' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Percentile_Queue' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Hours_per_Year' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Hours_per_Year' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Reduct_opposing_flow_rate_level' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Reduct_opposing_flow_rate_level' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Major_road_turn_flow_factor' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Major_road_turn_flow_factor' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Gap_Acceptance_Capacity' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Gap_Acceptance_Capacity' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Rou_Capacity_Model' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Rou_Capacity_Model' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Rou_LOS_Method' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Rou_LOS_Method' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Rou_HCM_2010_OD_pattern_effects_included' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Rou_HCM_2010_OD_pattern_effects_included' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Rou_FHWA_2000_model_applied' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Rou_FHWA_2000_model_applied' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Rou_FHWA_2000_Urban_compact_applied' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Rou_FHWA_2000_Urban_compact_applied' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Rou_HCM_2000_model_applied' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Rou_HCM_2000_model_applied' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Rou_NAASRA_1986_model_applied' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Rou_NAASRA_1986_model_applied' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Is_ped_cost_included' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Is_ped_cost_included' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Ped_average_income' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Ped_average_income' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Ped_time_value_factor' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Ped_time_value_factor' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_queue_storage_ratio_incl' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_queue_storage_ratio_incl' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Min_prob_blockage' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Min_prob_blockage' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Is_geometric_delay_excluded' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Is_geometric_delay_excluded' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Is_hcm_delay_formula_applied' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Is_hcm_delay_formula_applied' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Downstream_SL_Util_Ratio_Min' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Downstream_SL_Util_Ratio_Min' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Downstream_SL_Distance_Min' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Downstream_SL_Distance_Min' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Downstream_SL_Distance_FullLaneUtil' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Downstream_SL_Distance_FullLaneUtil' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Downstream_SL_CalibrationParameter' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Downstream_SL_CalibrationParameter' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Ped_los_target' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Ped_los_target' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Percentile_queue_option' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Percentile_queue_option' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Rou_HCM_6_OD_pattern_effects_included' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Rou_HCM_6_OD_pattern_effects_included' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Is_hcm_queue_formula_applied' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Is_hcm_queue_formula_applied' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_front_factor' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_front_factor' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_disp_factor_min' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_disp_factor_min' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_disp_factor_max' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_disp_factor_max' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_disp_distance_min' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_disp_distance_min' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_disp_distance_max' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_disp_distance_max' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_disp_n' , 'pRetVal' , ), 1610743878, (1610743878, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_disp_n' , 'pRetVal' , ), 1610743878, (1610743878, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Ped_LOS_Method' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'Ped_LOS_Method' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'Calibration_note' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'Calibration_note' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'Midblock_eff_det_zone_len' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'Midblock_eff_det_zone_len' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'Is_hcm6_extended_applied' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'Is_hcm6_extended_applied' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_upstream_delay_stops_included' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_upstream_delay_stops_included' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovementClass_vtables_dispatch_ = 1
ISIAPIMovementClass_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Is_included' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Is_included' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Is_userclass' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Display_id' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Display_id' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Base_class' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Base_class' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Model_designation' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MovementClassFuelEmissions' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16393, 10, None, "IID('{BF9EA147-CE73-49C5-A6DB-7FAA6DFC663E}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Site' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Pc_equivalent' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Pc_equivalent' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Is_cost_included' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Cost_method' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Cost_method' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_pump_price' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_pump_price' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Resource_cost_factor' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Resource_cost_factor' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Run_cost_fuel_ratio' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Run_cost_fuel_ratio' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Average_income' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Average_income' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Time_value_factor' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Time_value_factor' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Max_power' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Max_power' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Co2_to_fuel_ratio' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Co2_to_fuel_ratio' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'LowerLimitOfSpeedEfficiency' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'LowerLimitOfSpeedEfficiency' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Gap_acceptance_factor_sliplane_zebra' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Gap_acceptance_factor_sliplane_zebra' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Gap_acceptance_factor_midblock_zebra' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Gap_acceptance_factor_midblock_zebra' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'MergeParam' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16393, 10, None, "IID('{86D55C22-E6CE-4FF9-89A9-F53001A61501}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovementClassFuelEmission_vtables_dispatch_ = 1
ISIAPIMovementClassFuelEmission_vtables_ = [
	(( 'Emission_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Idle' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Idle' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'A' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'A' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'B' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'B' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Beta1' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Beta1' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'MovementClass' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16393, 10, None, "IID('{69AB3019-BCEB-413C-90C3-09A8DA0144DD}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovementClassFuelEmissions_vtables_dispatch_ = 1
ISIAPIMovementClassFuelEmissions_vtables_ = [
	(( 'Item' , 'emissionClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{94958D62-C2A0-40CD-A631-894BD1A1BC00}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'emissionClass' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovementClassMergeParam_vtables_dispatch_ = 1
ISIAPIMovementClassMergeParam_vtables_ = [
	(( 'Gap_acceptance_factor_shortlane' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Gap_acceptance_factor_shortlane' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_veh_factor_shortlane' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_veh_factor_shortlane' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Contlane_cap_shortlane' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Contlane_cap_shortlane' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Gap_acceptance_factor_mergelane' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Gap_acceptance_factor_mergelane' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_veh_factor_mergelane' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_veh_factor_mergelane' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Contlane_cap_mergelane' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Contlane_cap_mergelane' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'MovementClass' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16393, 10, None, "IID('{69AB3019-BCEB-413C-90C3-09A8DA0144DD}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovementClasses_vtables_dispatch_ = 1
ISIAPIMovementClasses_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{69AB3019-BCEB-413C-90C3-09A8DA0144DD}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementClassExists' , 'mcClass' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovement_ped_vtables_dispatch_ = 1
ISIAPIMovement_ped_vtables_ = [
	(( 'Type' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Stage' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Site' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Display_id' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Display_id' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Volume' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Volume' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Peak_flow_factor' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Peak_flow_factor' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Flow_scale' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Flow_scale' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Growth_rate' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Growth_rate' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_ped_factor' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_ped_factor' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation_user' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation_user' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Approach_distance' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Approach_distance' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Queue_space' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Queue_space' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Walking_speed' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Walking_speed' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Exit_distance' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Exit_distance' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Saturation_flow_rate' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Saturation_flow_rate' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Crossing_distance_user' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Crossing_distance_user' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Crossing_distance' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Crossing_distance' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_green_time_user' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_green_time_user' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_green_time' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_green_time' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Maximum_green_time_user' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Maximum_green_time_user' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Maximum_green_time' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Maximum_green_time' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Is_walk_time_extended' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Is_walk_time_extended' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Crossing_speed' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Crossing_speed' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_walk_time' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_walk_time' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_clearance_time' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_clearance_time' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Clearance1_time_user' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Clearance1_time_user' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Clearance1_time' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Clearance1_time' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Clearance2_time_option' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Clearance2_time_option' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Clearance2_time' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Clearance2_time' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Start_loss' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Start_loss' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'End_gain' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'End_gain' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Actuation_option' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Actuation_option' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Actuation_percent' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'Actuation_percent' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'Is_high_priority' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'Is_high_priority' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'Crosswalk_space' , 'pRetVal' , ), 1610743878, (1610743878, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'Crosswalk_space' , 'pRetVal' , ), 1610743878, (1610743878, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Conflict_zone_length_user' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'Conflict_zone_length_user' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'Conflict_zone_length' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'Conflict_zone_length' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'Control_type' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'Control_type' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovement_peds_vtables_dispatch_ = 1
ISIAPIMovement_peds_vtables_ = [
	(( 'Item' , 'Type' , 'Origin' , 'Stage' , 'pRetVal' , 
			 ), 0, (0, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{0099AEAC-F9B6-4DCE-9C0E-1434E9D603D7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementExists' , 'Type' , 'Origin' , 'Stage' , 'pRetVal' , 
			 ), 1610743809, (1610743809, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovement_vehicle_od_vtables_dispatch_ = 1
ISIAPIMovement_vehicle_od_vtables_ = [
	(( 'Origin' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Destination' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ODMovDesignation' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IsPossible' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MovementVehicleODMCs' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{69A455C4-0A3C-4A69-8A20-DFC672995EDC}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Site' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Opposingmovement_vehicles' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{677C1F98-D3D5-40B3-A5E5-5AEBD3A33CCC}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Opposingmovement_peds' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{580C5233-F043-4662-8C1D-2E0C31C568B9}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Turndesignation' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Turndesignation' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Display_od_id' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Display_od_id' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Display_ltr_id' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Display_ltr_id' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Is_TWSC_adj_applied' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Is_TWSC_adj_applied' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Is_gap_acceptance_usergiven' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Is_gap_acceptance_usergiven' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'End_departures' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'End_departures' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_departures' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_departures' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Exit_flow_effect' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Exit_flow_effect' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Percent_opposed_by_nearest' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Percent_opposed_by_nearest' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_ped_effect_option_signals' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_ped_effect_option_signals' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_ped_effect_option' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_ped_effect_option' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_ped_effect_start_loss' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_ped_effect_start_loss' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Total_volume' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Zebra_ped_gap_acceptance_option' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Zebra_ped_gap_acceptance_option' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Zebra_ped_critical_gap' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Zebra_ped_critical_gap' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Zebra_ped_followup_headway' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Zebra_ped_followup_headway' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Zebra_ped_minimum_departures' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Zebra_ped_minimum_departures' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovement_vehicle_od_mc_vtables_dispatch_ = 1
ISIAPIMovement_vehicle_od_mc_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Movement_vehicle_od' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Volume' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Volume' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Occupancy' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Occupancy' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Growth_rate' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Growth_rate' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Flow_scale' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Flow_scale' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Peak_flow_factor' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Peak_flow_factor' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Approach_speed' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Approach_speed' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Exit_speed' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Exit_speed' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Exit_distance_user' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Exit_distance_user' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Exit_distance' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Exit_distance' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_distance_user' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_distance_user' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_distance' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_distance' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_radius_option' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_radius_option' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_radius' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_radius' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_speed_user' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_speed_user' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_speed' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_speed' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Queue_space' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Queue_space' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Vehicle_length' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Vehicle_length' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Turn_veh_effect_option' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Turn_veh_effect_option' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Turning_veh_factor' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Turning_veh_factor' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Turn_radius' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Turn_radius' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Gap_acceptance_factor' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Gap_acceptance_factor' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_veh_factor' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_veh_factor' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation_user' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation_user' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Coordination_type' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Coordination_type' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_type' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_type' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_percentage' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_percentage' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Non_actuated' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Non_actuated' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Turn_on_red' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Turn_on_red' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Start_loss' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Start_loss' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'End_gain' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'End_gain' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_green_time_user' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_green_time_user' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_green_time' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_green_time' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'Maximum_green_time_user' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'Maximum_green_time_user' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'Maximum_green_time' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Maximum_green_time' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'Stopline_travel_time_user' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'Stopline_travel_time_user' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'Stopline_travel_time' , 'pRetVal' , ), 1610743883, (1610743883, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'Stopline_travel_time' , 'pRetVal' , ), 1610743883, (1610743883, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'Is_early_cutoff' , 'pRetVal' , ), 1610743885, (1610743885, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'Is_early_cutoff' , 'pRetVal' , ), 1610743885, (1610743885, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'Early_cutoff' , 'pRetVal' , ), 1610743887, (1610743887, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'Early_cutoff' , 'pRetVal' , ), 1610743887, (1610743887, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'Is_late_release' , 'pRetVal' , ), 1610743889, (1610743889, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'Is_late_release' , 'pRetVal' , ), 1610743889, (1610743889, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'Late_release' , 'pRetVal' , ), 1610743891, (1610743891, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'Late_release' , 'pRetVal' , ), 1610743891, (1610743891, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'Phase_actuation_option' , 'pRetVal' , ), 1610743893, (1610743893, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'Phase_actuation_option' , 'pRetVal' , ), 1610743893, (1610743893, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'Phase_actuation_percent' , 'pRetVal' , ), 1610743895, (1610743895, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'Phase_actuation_percent' , 'pRetVal' , ), 1610743895, (1610743895, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'Is_high_priority' , 'pRetVal' , ), 1610743897, (1610743897, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'Is_high_priority' , 'pRetVal' , ), 1610743897, (1610743897, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'Has_extra_midblock_delay' , 'pRetVal' , ), 1610743899, (1610743899, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'Has_extra_midblock_delay' , 'pRetVal' , ), 1610743899, (1610743899, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'Extra_midblock_delay' , 'pRetVal' , ), 1610743901, (1610743901, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'Extra_midblock_delay' , 'pRetVal' , ), 1610743901, (1610743901, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovement_vehicle_od_mcs_vtables_dispatch_ = 1
ISIAPIMovement_vehicle_od_mcs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{55D25294-3468-41D8-96A1-B5B6E06AFF99}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementClassExists' , 'mcClass' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIMovement_vehicle_ods_vtables_dispatch_ = 1
ISIAPIMovement_vehicle_ods_vtables_ = [
	(( 'Item' , 'Origin' , 'Destination' , 'pRetVal' , ), 0, (0, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementExists' , 'Origin' , 'Destination' , 'pRetVal' , ), 1610743809, (1610743809, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPINetwork_vtables_dispatch_ = 1
ISIAPINetwork_vtables_ = [
	(( 'Network_id' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NetworkID' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'NetworkID' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ModelSignature' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ModelName' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DriveOnLeft' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Units' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CostUnit' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CostUnit' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'IsShortlaneQueueStorageRatioIncl' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'IsShortlaneQueueStorageRatioIncl' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LOSMethod' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'LOSMethod' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'LOSTarget' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'LOSTarget' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'HoursPerYear' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'HoursPerYear' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MaxIterations' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'MaxIterations' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'StoppingDxPercent' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'StoppingDxPercent' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'SignalOffsetOption' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'SignalOffsetOption' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'OffsetDefinition' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'OffsetDefinition' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'IsPlatoonDispersionApplied' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'IsPlatoonDispersionApplied' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_option' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_option' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'NetworkCycleTime' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'NetworkCycleTime' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Practical_max_cycle_time' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Practical_max_cycle_time' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Practical_cycle_rounding' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Practical_cycle_rounding' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'SitePhaseTimesOption' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'SitePhaseTimesOption' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'MultiRoutesSummaryOption' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'MultiRoutesSummaryOption' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Created_date' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Created_by' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Created_by_company' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Created_version' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Modified_date' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Modified_by' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Modified_by_company' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Modified_version' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'ProcessingError' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'NetworkSites' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16393, 10, None, "IID('{8B19120E-37DE-43E9-AB2F-9F1743650053}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'NetworkLegConnections' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16393, 10, None, "IID('{F29A35EA-9B6B-46B7-839B-EC921C94A479}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'OutputNetwork' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16393, 10, None, "IID('{5E551751-0DA8-4E10-931A-D474F6FFBB27}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'OutputNetworkByRoutes' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16393, 10, None, "IID('{5E551751-0DA8-4E10-931A-D474F6FFBB27}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Site_los_method' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Site_los_method' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Performance_Measure' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Performance_Measure' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Percentile_queue_option' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Percentile_queue_option' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Percentile_Queue' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Percentile_Queue' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'DiagnosticStatus' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'DiagnosticMsgs' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (16393, 10, None, "IID('{CBFD7927-0588-4CF2-BEB4-052B1F31A027}')") , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'Project' , 'pRetVal' , ), 1610743878, (1610743878, (), [ (16393, 10, None, "IID('{5817180B-2283-40FB-8068-C2F2D656EF04}')") , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'NetworkCCGs' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (16393, 10, None, "IID('{AFE37B56-E6C5-4F98-8853-6FFF575C25BC}')") , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Routes' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (16393, 10, None, "IID('{DE44AC02-4804-4587-87BB-AC8E0ED05EEB}')") , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'Process' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'UpdateModifiedInfo' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'AddNetworkSite' , 'Site' , 'layoutX' , 'layoutY' , 'pRetVal' , 
			 ), 1610743883, (1610743883, (), [ (9, 1, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , (4, 1, None, None) , (4, 1, None, None) , (16393, 10, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , ], 1 , 1 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'RemoveNetworkSite' , 'networkSite' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (9, 1, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'AddNetworkLegConnection' , 'nwSite1' , 'legOrientation1' , 'nwSite2' , 'legOrientation2' , 
			 'pRetVal' , ), 1610743885, (1610743885, (), [ (9, 1, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , (3, 1, None, None) , (9, 1, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}')") , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'RemoveNetworkLegConnection' , 'nwLegConn' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (9, 1, None, "IID('{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'AddNetworkCCG' , 'pRetVal' , ), 1610743887, (1610743887, (), [ (16393, 10, None, "IID('{6635581E-7C13-461E-9917-85B7CA3F7B07}')") , ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'RemoveNetworkCCG' , 'ccg' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (9, 1, None, "IID('{6635581E-7C13-461E-9917-85B7CA3F7B07}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'AddRoute' , 'pRetVal' , ), 1610743889, (1610743889, (), [ (16393, 10, None, "IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')") , ], 1 , 1 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'RemoveRoute' , 'route' , 'pRetVal' , ), 1610743890, (1610743890, (), [ (9, 1, None, "IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'ProcessByRoutes' , 'pRetVal' , ), 1610743891, (1610743891, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'MoveNetworkCCGTo' , 'ccg' , 'newPosition' , 'pRetVal' , ), 1610743892, (1610743892, (), [ 
			 (9, 1, None, "IID('{6635581E-7C13-461E-9917-85B7CA3F7B07}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'ResetRouteSignalOffsetPriority' , 'pRetVal' , ), 1610743893, (1610743893, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'CloneRoute' , 'route' , 'pRetVal' , ), 1610743894, (1610743894, (), [ (9, 1, None, "IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')") , 
			 (16393, 10, None, "IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')") , ], 1 , 1 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'MoveRouteTo' , 'route' , 'newPosition' , 'pRetVal' , ), 1610743895, (1610743895, (), [ 
			 (9, 1, None, "IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'CreateLayoutPngData' , 'pRetVal' , ), 1610743896, (1610743896, (), [ (24593, 10, None, None) , ], 1 , 1 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'CreateLayoutPngFile' , 'filename' , 'pRetVal' , ), 1610743897, (1610743897, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'Category' , 'pRetVal' , ), 1610743898, (1610743898, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'Category' , 'pRetVal' , ), 1610743898, (1610743898, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'Peakflowperiod' , 'pRetVal' , ), 1610743900, (1610743900, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'Peakflowperiod' , 'pRetVal' , ), 1610743900, (1610743900, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'Lane_blockage_effect_option' , 'pRetVal' , ), 1610743902, (1610743902, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'Lane_blockage_effect_option' , 'pRetVal' , ), 1610743902, (1610743902, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower_user' , 'pRetVal' , ), 1610743904, (1610743904, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower_user' , 'pRetVal' , ), 1610743904, (1610743904, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower' , 'pRetVal' , ), 1610743906, (1610743906, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower' , 'pRetVal' , ), 1610743906, (1610743906, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_upper' , 'pRetVal' , ), 1610743908, (1610743908, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_upper' , 'pRetVal' , ), 1610743908, (1610743908, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_increment' , 'pRetVal' , ), 1610743910, (1610743910, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_increment' , 'pRetVal' , ), 1610743910, (1610743910, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_perf_measure' , 'pRetVal' , ), 1610743912, (1610743912, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_perf_measure' , 'pRetVal' , ), 1610743912, (1610743912, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_optim_method' , 'pRetVal' , ), 1610743914, (1610743914, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_optim_method' , 'pRetVal' , ), 1610743914, (1610743914, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_lower' , 'pRetVal' , ), 1610743916, (1610743916, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 920 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_lower' , 'pRetVal' , ), 1610743916, (1610743916, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 928 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_upper' , 'pRetVal' , ), 1610743918, (1610743918, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 936 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_upper' , 'pRetVal' , ), 1610743918, (1610743918, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 944 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_increment' , 'pRetVal' , ), 1610743920, (1610743920, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 952 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_increment' , 'pRetVal' , ), 1610743920, (1610743920, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 960 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_perf_measure' , 'pRetVal' , ), 1610743922, (1610743922, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 968 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_perf_measure' , 'pRetVal' , ), 1610743922, (1610743922, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 976 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_optim_method' , 'pRetVal' , ), 1610743924, (1610743924, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 984 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_optim_method' , 'pRetVal' , ), 1610743924, (1610743924, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 992 , (3, 0, None, None) , 0 , )),
	(( 'Variable_phasing_perf_measure' , 'pRetVal' , ), 1610743926, (1610743926, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1000 , (3, 0, None, None) , 0 , )),
	(( 'Variable_phasing_perf_measure' , 'pRetVal' , ), 1610743926, (1610743926, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
	(( 'Green_split_priority_option' , 'pRetVal' , ), 1610743928, (1610743928, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1016 , (3, 0, None, None) , 0 , )),
	(( 'Green_split_priority_option' , 'pRetVal' , ), 1610743928, (1610743928, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 1024 , (3, 0, None, None) , 0 , )),
	(( 'Is_timing_optimised_for_selected_result' , 'pRetVal' , ), 1610743930, (1610743930, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1032 , (3, 0, None, None) , 0 , )),
	(( 'Is_timing_optimised_for_selected_result' , 'pRetVal' , ), 1610743930, (1610743930, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1040 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInProjectSummary' , 'pRetVal' , ), 1610743932, (1610743932, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1048 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInProjectSummary' , 'pRetVal' , ), 1610743932, (1610743932, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1056 , (3, 0, None, None) , 0 , )),
	(( 'DemandSensitivity' , 'pRetVal' , ), 1610743934, (1610743934, (), [ (16393, 10, None, "IID('{B8795F7C-B342-4E4D-9F88-398D704B4453}')") , ], 1 , 2 , 4 , 0 , 1064 , (3, 0, None, None) , 0 , )),
	(( 'NetworkFolder' , 'pRetVal' , ), 1610743935, (1610743935, (), [ (16393, 10, None, "IID('{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')") , ], 1 , 2 , 4 , 0 , 1072 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyLOSUpperLimit_B' , 'pRetVal' , ), 1610743936, (1610743936, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1080 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyLOSUpperLimit_B' , 'pRetVal' , ), 1610743936, (1610743936, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 1088 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyLOSUpperLimit_C' , 'pRetVal' , ), 1610743938, (1610743938, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1096 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyLOSUpperLimit_C' , 'pRetVal' , ), 1610743938, (1610743938, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 1104 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyLOSUpperLimit_D' , 'pRetVal' , ), 1610743940, (1610743940, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1112 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyLOSUpperLimit_D' , 'pRetVal' , ), 1610743940, (1610743940, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 1120 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyLOSUpperLimit_E' , 'pRetVal' , ), 1610743942, (1610743942, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1128 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyLOSUpperLimit_E' , 'pRetVal' , ), 1610743942, (1610743942, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 1136 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyLOSUpperLimit_F' , 'pRetVal' , ), 1610743944, (1610743944, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1144 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyLOSUpperLimit_F' , 'pRetVal' , ), 1610743944, (1610743944, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 1152 , (3, 0, None, None) , 0 , )),
	(( 'Is_geometric_delay_excluded' , 'pRetVal' , ), 1610743946, (1610743946, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1160 , (3, 0, None, None) , 0 , )),
	(( 'Is_geometric_delay_excluded' , 'pRetVal' , ), 1610743946, (1610743946, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1168 , (3, 0, None, None) , 0 , )),
	(( 'Is_hcm_delay_formula_applied' , 'pRetVal' , ), 1610743948, (1610743948, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1176 , (3, 0, None, None) , 0 , )),
	(( 'Is_hcm_delay_formula_applied' , 'pRetVal' , ), 1610743948, (1610743948, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1184 , (3, 0, None, None) , 0 , )),
	(( 'Is_hcm_queue_formula_applied' , 'pRetVal' , ), 1610743950, (1610743950, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1192 , (3, 0, None, None) , 0 , )),
	(( 'Is_hcm_queue_formula_applied' , 'pRetVal' , ), 1610743950, (1610743950, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1200 , (3, 0, None, None) , 0 , )),
	(( 'IsLaneBlockageModelApplied' , 'pRetVal' , ), 1610743952, (1610743952, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1208 , (3, 0, None, None) , 0 , )),
	(( 'IsLaneBlockageModelApplied' , 'pRetVal' , ), 1610743952, (1610743952, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1216 , (3, 0, None, None) , 0 , )),
	(( 'NetworkMCs' , 'pRetVal' , ), 1610743954, (1610743954, (), [ (16393, 10, None, "IID('{EA51880D-3150-4EF5-B203-17CC4EAC2214}')") , ], 1 , 2 , 4 , 0 , 1224 , (3, 0, None, None) , 0 , )),
	(( 'RemoveOutputData' , 'pRetVal' , ), 1610743955, (1610743955, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1232 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkCCG_vtables_dispatch_ = 1
ISIAPINetworkCCG_vtables_ = [
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'NetworkCCGID' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NetworkCCGID' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsReference' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'IsReference' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Offset' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Offset' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'CoordinatedOption' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'CoordinatedOption' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Signal_analysis_method' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Signal_analysis_method' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NetworkSites' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16393, 10, None, "IID('{8B19120E-37DE-43E9-AB2F-9F1743650053}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CCGSequences' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16393, 10, None, "IID('{833D5364-D498-47D7-BE84-44624D8D16B5}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'AddNetworkSite' , 'networkSite' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (9, 1, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'RemoveNetworkSite' , 'networkSite' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (9, 1, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'AddCCGSequence' , 'Name' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RemoveCCGSequence' , 'ccgSequence' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (9, 1, None, "IID('{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CloneCCGSequence' , 'ccgSequence' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (9, 1, None, "IID('{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')") , 
			 (16393, 10, None, "IID('{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'MoveCCGSequenceTo' , 'ccgSequence' , 'newPosition' , 'pRetVal' , ), 1610743830, (1610743830, (), [ 
			 (9, 1, None, "IID('{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Is_multi_sequence_enabled' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Is_multi_sequence_enabled' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkCCGPhase_vtables_dispatch_ = 1
ISIAPINetworkCCGPhase_vtables_ = [
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Is_variable' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Is_variable' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsReferencePhase' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'IsReferencePhase' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Phase_time' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Phase_time' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Yellow_time' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Yellow_time' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'All_red_time' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'All_red_time' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Has_dummy' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Has_dummy' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_minimum_green_time_user' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_minimum_green_time_user' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_minimum_green_time' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_minimum_green_time' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_maximum_green_time_user' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_maximum_green_time_user' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_maximum_green_time' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_maximum_green_time' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_time' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_time' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Phase_frequency_user' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Phase_frequency_user' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Phase_frequency' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Phase_frequency' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ccgSequence' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16393, 10, None, "IID('{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'GetPhasemovementVehiclesByNetworkSite' , 'networkSite' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (9, 1, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , 
			 (16393, 10, None, "IID('{843F1163-A090-4AA1-9AB4-8CF90C0A8BFF}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'GetPhasemovementPedsByNetworkSite' , 'networkSite' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (9, 1, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , 
			 (16393, 10, None, "IID('{8F802394-B3B4-4D06-8EA2-A0247C600A86}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkCCGPhases_vtables_dispatch_ = 1
ISIAPINetworkCCGPhases_vtables_ = [
	(( 'Item' , 'phasename' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PhaseExists' , 'phasename' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkCCGSequence_vtables_dispatch_ = 1
ISIAPINetworkCCGSequence_vtables_ = [
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Is_selected' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Is_selected' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_option' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_option' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Practical_max_cycle_time' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Practical_max_cycle_time' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Practical_cycle_rounding' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Practical_cycle_rounding' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower_user' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower_user' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_upper' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_upper' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_increment' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_increment' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_perf_measure' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_perf_measure' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_optim_method' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_optim_method' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_lower' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_lower' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_upper' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_upper' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_increment' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_increment' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_perf_measure' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_perf_measure' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_optim_method' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_optim_method' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Variable_phasing_perf_measure' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Variable_phasing_perf_measure' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Usergiven_cycle_time' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Usergiven_cycle_time' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Green_split_priority_option' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Green_split_priority_option' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_max_green_major_mov' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_max_green_major_mov' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_max_green_minor_mov' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_max_green_minor_mov' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_gap_major_mov' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_gap_major_mov' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_gap_minor_mov' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_gap_minor_mov' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Eff_det_zone_len_major_mov' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Eff_det_zone_len_major_mov' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Eff_det_zone_len_minor_mov' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Eff_det_zone_len_minor_mov' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'NetworkCCG' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16393, 10, None, "IID('{6635581E-7C13-461E-9917-85B7CA3F7B07}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'CCGPhases' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16393, 10, None, "IID('{A2B9F260-C553-40A5-99CB-16F98407645F}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'AddCCGPhase' , 'Name' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')") , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'InsertCCGPhase' , 'Position' , 'Name' , 'pRetVal' , ), 1610743863, (1610743863, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')") , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'RemoveCCGPhase' , 'ccgPhase' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (9, 1, None, "IID('{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'CloneCCGPhase' , 'ccgPhase' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (9, 1, None, "IID('{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')") , 
			 (16393, 10, None, "IID('{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')") , ], 1 , 1 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'MoveCCGPhaseTo' , 'ccgPhase' , 'newPosition' , 'pRetVal' , ), 1610743866, (1610743866, (), [ 
			 (9, 1, None, "IID('{110BF49A-6953-499B-9648-8C1EFDA2B4CC}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkCCGSequences_vtables_dispatch_ = 1
ISIAPINetworkCCGSequences_vtables_ = [
	(( 'Item' , 'Name' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SequenceExists' , 'Name' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkCCGs_vtables_dispatch_ = 1
ISIAPINetworkCCGs_vtables_ = [
	(( 'Item' , 'ccgName' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{6635581E-7C13-461E-9917-85B7CA3F7B07}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{6635581E-7C13-461E-9917-85B7CA3F7B07}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NetworkCCGExists' , 'ccgName' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkDemandSensitivity_vtables_dispatch_ = 1
ISIAPINetworkDemandSensitivity_vtables_ = [
	(( 'Network' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Analysis_option' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Analysis_option' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Objective' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Objective' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Growth_Model' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Growth_Model' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Years' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Years' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Is_constant_num_years_applied' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Is_constant_num_years_applied' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Constant_num_years' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Constant_num_years' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Objective' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Objective' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Lower' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Lower' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Upper' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Upper' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Is_constant_factor_applied' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Is_constant_factor_applied' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Constant_factor' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Constant_factor' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SensitivityGeneralParameterGroup' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16393, 10, None, "IID('{D025138A-4F4C-4613-8FA7-D1FD5550A50C}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Result_option' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Result_option' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkFolder_vtables_dispatch_ = 1
ISIAPINetworkFolder_vtables_ = [
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Networks' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{98CE5F37-494C-484F-B8F5-50993C839B3B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Project' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{5817180B-2283-40FB-8068-C2F2D656EF04}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AddNetwork' , 'softwareSetup' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AddNetwork_2' , 'softwareSetupSignature' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RemoveNetwork' , 'Network' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (9, 1, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CloneNetwork' , 'Network' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (9, 1, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , 
			 (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'CloneNetworkWithSites' , 'Network' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (9, 1, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , 
			 (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'MoveNetworkTo' , 'Network' , 'newPosition' , 'pRetVal' , ), 1610743818, (1610743818, (), [ 
			 (9, 1, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MoveNetworksToFolder' , 'networkNames' , 'destFolder' , 'pRetVal' , ), 1610743819, (1610743819, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')") , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkFolders_vtables_dispatch_ = 1
ISIAPINetworkFolders_vtables_ = [
	(( 'Item' , 'Name' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NetworkFolderExists' , 'Name' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkLegConnection_vtables_dispatch_ = 1
ISIAPINetworkLegConnection_vtables_ = [
	(( 'Site1_Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Leg1_Orientation' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Site2_Name' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Leg2_Orientation' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'NetworkSite1' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NetworkSite2' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionType' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionType' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ZIndex' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ZIndex' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkLegConnections_vtables_dispatch_ = 1
ISIAPINetworkLegConnections_vtables_ = [
	(( 'Item' , 'index' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkMC_vtables_dispatch_ = 1
ISIAPINetworkMC_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LowerLimitOfSpeedEfficiency' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LowerLimitOfSpeedEfficiency' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkMCs_vtables_dispatch_ = 1
ISIAPINetworkMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{213E3AC6-7026-49A5-A65E-B5E2CE167E8D}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkSite_vtables_dispatch_ = 1
ISIAPINetworkSite_vtables_ = [
	(( 'NetworkSite_id' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SiteName' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SiteOutputset' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsReference' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsReference' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Offset' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Offset' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'layoutX' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'layoutX' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'layoutY' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'layoutY' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CoordinatedOption' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CoordinatedOption' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NetworkLegConnections' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16393, 10, None, "IID('{F29A35EA-9B6B-46B7-839B-EC921C94A479}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NetworkCCG' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16393, 10, None, "IID('{6635581E-7C13-461E-9917-85B7CA3F7B07}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Site' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DiagnosticStatus' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DiagnosticMsgs' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16393, 10, None, "IID('{CBFD7927-0588-4CF2-BEB4-052B1F31A027}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInProjectSummary' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInProjectSummary' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworkSites_vtables_dispatch_ = 1
ISIAPINetworkSites_vtables_ = [
	(( 'Item' , 'SiteName' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NetworkSiteExists' , 'SiteName' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPINetworks_vtables_dispatch_ = 1
ISIAPINetworks_vtables_ = [
	(( 'Item' , 'networkname' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NetworkExists' , 'networkname' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetNetworkByID' , 'Network_id' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISIAPIOpposingmovement_ped_vtables_dispatch_ = 1
ISIAPIOpposingmovement_ped_vtables_ = [
	(( 'Opposingmovement_ped_type' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Opposingmovement_ped_origin' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Opposingmovement_ped_stage' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Opposing' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Opposing' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Movement_vehicle_od' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ISIAPIOpposingmovement_peds_vtables_dispatch_ = 1
ISIAPIOpposingmovement_peds_vtables_ = [
	(( 'Item' , 'opposing_ped_type' , 'opposing_ped_origin' , 'opposin_ped_stage' , 'pRetVal' , 
			 ), 0, (0, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{1602B72A-4010-4F67-B45D-5C8A493BC687}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{1602B72A-4010-4F67-B45D-5C8A493BC687}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OpposingmovementPedExists' , 'opposing_ped_type' , 'opposing_ped_origin' , 'opposin_ped_stage' , 'pRetVal' , 
			 ), 1610743810, (1610743810, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPIOpposingmovement_vehicle_vtables_dispatch_ = 1
ISIAPIOpposingmovement_vehicle_vtables_ = [
	(( 'Opposingmovement_vehicle_origin' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Opposingmovement_vehicle_destination' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Opposing' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Opposing' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Movement_vehicle_od' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISIAPIOpposingmovement_vehicles_vtables_dispatch_ = 1
ISIAPIOpposingmovement_vehicles_vtables_ = [
	(( 'Item' , 'opposing_veh_origin' , 'opposing_veh_destination' , 'pRetVal' , ), 0, (0, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{CDC74ADC-2CF3-49D5-8DC5-3821AC96AA91}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{CDC74ADC-2CF3-49D5-8DC5-3821AC96AA91}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OpposingmovementVehicleExists' , 'opposing_veh_origin' , 'opposing_veh_destination' , 'pRetVal' , ), 1610743810, (1610743810, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputAnalysis_vtables_dispatch_ = 1
ISIAPIOutputAnalysis_vtables_ = [
	(( 'Design_Life_Selected_future_year' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Design_Life_Analysis_status' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Largest_movement_flow_scale' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Flow_Scale_Analysis_status' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Sensitivity_Selected_parameter_scale' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Sensitivity_Analysis_status' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputCirculatingLane_vtables_dispatch_ = 1
ISIAPIOutputCirculatingLane_vtables_ = [
	(( 'Orientation' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Laneno' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Roucircf_veh' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Roucircf_pcu' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Roucircf_percent' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'OutputLeg' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{4D03B4B2-FBC7-4EC5-B7D8-984398036302}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'OutputCirculatingLaneMCs' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{E3D1A42E-AA21-4472-B566-8EAE73EAB615}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputCirculatingLaneMC_vtables_dispatch_ = 1
ISIAPIOutputCirculatingLaneMC_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Roucircf_veh' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Roucircf_pcu' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Roucircf_percent' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'OutputCirculatingLane' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{7F03E897-A19D-41C6-A6EA-FECCF36A3358}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputCirculatingLaneMCs_vtables_dispatch_ = 1
ISIAPIOutputCirculatingLaneMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{FA80BAB6-860C-4FA9-841D-3ECB6EA78605}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementClassExists' , 'mcClass' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputCirculatingLanes_vtables_dispatch_ = 1
ISIAPIOutputCirculatingLanes_vtables_ = [
	(( 'Item' , 'Laneno' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{7F03E897-A19D-41C6-A6EA-FECCF36A3358}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LaneExists' , 'Laneno' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputGraphTuple_vtables_dispatch_ = 1
ISIAPIOutputGraphTuple_vtables_ = [
	(( 'X_value' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Demand_flow_total' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_effective' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Practical_spare_capacity' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_percentile' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_percentile' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_total' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_total' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Nox_total' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_total' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_total' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Unsettled' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Demand_flow_total_ped' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Demand_flow_total_person' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Perc_heavy_veh' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn_ped' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total_veh' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total_ped' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total_person' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_veh' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_ped' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstlane' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov_ped' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov_person' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Delay_geometric_average' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Delay_stopline_average' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service_veh' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service_ped' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Total_stops_veh' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Total_stops_ped' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Total_stops_person' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate_veh' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate_ped' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Prop_queued_veh' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Prop_queued_ped' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Prop_queued_person' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index_veh' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index_ped' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_total_veh' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_total_ped' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_total_person' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_av_veh' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_av_ped' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_av_person' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total_veh' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total_ped' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total_person' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_av_veh' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_av_ped' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_av_person' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed_ped' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed_person' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total_veh' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total_ped' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_total' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_total_person' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputGraphTuples_vtables_dispatch_ = 1
ISIAPIOutputGraphTuples_vtables_ = [
	(( 'Item' , 'index' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E69891AB-798F-4534-9C25-8BCD74AF811A}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLane_vtables_dispatch_ = 1
ISIAPIOutputLane_vtables_ = [
	(( 'Orientation' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Laneno' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_end_deps' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_min' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Delay_ctrl' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delay_geo' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Delay_idle' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Delay_model_1' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Delay_model_2' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Delay_n' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Delay_q' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Flow_total' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Flow_LV' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_pct' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Flow_total_capconstr' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Flow_LV_capconstr' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_capconstr' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_pct_capconstr' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Prop_queued' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Prob_blockage' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Queue_space' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_1' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_2' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_mean' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_percentile' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_1' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_2' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_mean' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_percentile' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_mean' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_percentile' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Queue_overflow' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Satflow_basic' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Satflow_scats' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Satflow_scats_mf' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_flow_moved' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Stoprate_1' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Stoprate_2' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Stoprate_geo' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Stoprate_overall' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Stoprate_qmovup' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'T2_reduced' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Underutil_flag' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Util_factor' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_shortlane_affected' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'X1_flag' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Delay_acc_dec_dn' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Delay_queue_moveup' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_percentile' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_avg' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Total_stops' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Flag_na' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Satn_speed' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Satn_flow' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Satn_headway' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Satn_spacing' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Average_queue_space' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Driver_response_time' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Is_dominant' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adj' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adj_flag' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'OutputLaneODs' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16393, 10, None, "IID('{83C46DBA-91A4-4A1F-9EC4-7ECEB223C6DA}')") , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'OutputLaneGreenPeriods' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (16393, 10, None, "IID('{472D3454-925A-442D-8498-E4A01EF86C20}')") , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'OutputLeg' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (16393, 10, None, "IID('{4D03B4B2-FBC7-4EC5-B7D8-984398036302}')") , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'OutputLaneMCs' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (16393, 10, None, "IID('{A04D1E92-C344-4E0E-850A-1B97D38BD7B8}')") , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'Lane_block_adj' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'Residual_demand_vol' , 'pRetVal' , ), 1610743878, (1610743878, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'Initial_demand_vol_clear_time' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Residual_demand_vol_clear_time' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'Oversatn_duration' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'Perc_arriving_during_green' , 'pRetVal' , ), 1610743883, (1610743883, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_ratio' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'Progression_factor_delay' , 'pRetVal' , ), 1610743885, (1610743885, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'Progression_factor_queue' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'Headway_scats_mf' , 'pRetVal' , ), 1610743887, (1610743887, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'Occupancy_scats_mf' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'Space_scats_mf' , 'pRetVal' , ), 1610743889, (1610743889, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'Calc_mf_flag' , 'pRetVal' , ), 1610743890, (1610743890, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'Queue_constraint_flag' , 'pRetVal' , ), 1610743891, (1610743891, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'Green_periods' , 'pRetVal' , ), 1610743892, (1610743892, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'Upstr_flow_after_exit_sl' , 'pRetVal' , ), 1610743893, (1610743893, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'Lane_change_from_left' , 'pRetVal' , ), 1610743894, (1610743894, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'Lane_change_to_left' , 'pRetVal' , ), 1610743895, (1610743895, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'Lane_change_from_right' , 'pRetVal' , ), 1610743896, (1610743896, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'Lane_change_to_right' , 'pRetVal' , ), 1610743897, (1610743897, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'Is_nw_connected' , 'pRetVal' , ), 1610743898, (1610743898, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'Net_inflow' , 'pRetVal' , ), 1610743899, (1610743899, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'Net_inflow_capconstr' , 'pRetVal' , ), 1610743900, (1610743900, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_flag' , 'pRetVal' , ), 1610743901, (1610743901, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'Queue_greenstart_mean' , 'pRetVal' , ), 1610743902, (1610743902, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'Queue_greenstart_percentile' , 'pRetVal' , ), 1610743903, (1610743903, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_cycav_mean' , 'pRetVal' , ), 1610743904, (1610743904, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_cycav_percentile' , 'pRetVal' , ), 1610743905, (1610743905, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_greenstart_mean' , 'pRetVal' , ), 1610743906, (1610743906, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_greenstart_percentile' , 'pRetVal' , ), 1610743907, (1610743907, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'Initial_demand_vol' , 'pRetVal' , ), 1610743908, (1610743908, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'Avg_num_of_cycles_to_depart' , 'pRetVal' , ), 1610743909, (1610743909, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'Prob_shortlane_overflow' , 'pRetVal' , ), 1610743910, (1610743910, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'Satflow_basic_adj' , 'pRetVal' , ), 1610743911, (1610743911, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'Adjfactor_lanewidth' , 'pRetVal' , ), 1610743912, (1610743912, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'Adjfactor_grade' , 'pRetVal' , ), 1610743913, (1610743913, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( 'Adjfactor_parking' , 'pRetVal' , ), 1610743914, (1610743914, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
	(( 'Adjfactor_buses' , 'pRetVal' , ), 1610743915, (1610743915, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( 'Adjfactor_flowscale' , 'pRetVal' , ), 1610743916, (1610743916, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 920 , (3, 0, None, None) , 0 , )),
	(( 'Adjfactor_trafficflow' , 'pRetVal' , ), 1610743917, (1610743917, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 928 , (3, 0, None, None) , 0 , )),
	(( 'Equivalent_AT' , 'pRetVal' , ), 1610743918, (1610743918, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 936 , (3, 0, None, None) , 0 , )),
	(( 'Control_type' , 'pRetVal' , ), 1610743919, (1610743919, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 944 , (3, 0, None, None) , 0 , )),
	(( 'Contlane_affect_by_adjshortlane' , 'pRetVal' , ), 1610743920, (1610743920, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 952 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_ped_factor' , 'pRetVal' , ), 1610743921, (1610743921, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 960 , (3, 0, None, None) , 0 , )),
	(( 'Unblocked_time_ratio' , 'pRetVal' , ), 1610743922, (1610743922, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 968 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_cycle_time' , 'pRetVal' , ), 1610743923, (1610743923, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 976 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_blocked_time' , 'pRetVal' , ), 1610743924, (1610743924, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 984 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_unblocked_time' , 'pRetVal' , ), 1610743925, (1610743925, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 992 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_delay' , 'pRetVal' , ), 1610743926, (1610743926, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1000 , (3, 0, None, None) , 0 , )),
	(( 'Net_outflow' , 'pRetVal' , ), 1610743927, (1610743927, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
	(( 'Net_outflow_capconstr' , 'pRetVal' , ), 1610743928, (1610743928, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1016 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_overflow' , 'pRetVal' , ), 1610743929, (1610743929, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1024 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743930, (1610743930, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1032 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyFlag' , 'pRetVal' , ), 1610743931, (1610743931, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1040 , (3, 0, None, None) , 0 , )),
	(( 'CongestionCoefficient' , 'pRetVal' , ), 1610743932, (1610743932, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1048 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeIndex' , 'pRetVal' , ), 1610743933, (1610743933, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1056 , (3, 0, None, None) , 0 , )),
	(( 'Uninterrupted_speed' , 'pRetVal' , ), 1610743934, (1610743934, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1064 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pRetVal' , ), 1610743935, (1610743935, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1072 , (3, 0, None, None) , 0 , )),
	(( 'Spacing' , 'pRetVal' , ), 1610743936, (1610743936, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1080 , (3, 0, None, None) , 0 , )),
	(( 'Headway' , 'pRetVal' , ), 1610743937, (1610743937, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1088 , (3, 0, None, None) , 0 , )),
	(( 'Occupancy_time' , 'pRetVal' , ), 1610743938, (1610743938, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1096 , (3, 0, None, None) , 0 , )),
	(( 'Space_time' , 'pRetVal' , ), 1610743939, (1610743939, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1104 , (3, 0, None, None) , 0 , )),
	(( 'Avg_veh_length' , 'pRetVal' , ), 1610743940, (1610743940, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1112 , (3, 0, None, None) , 0 , )),
	(( 'Space_occupancy_ratio' , 'pRetVal' , ), 1610743941, (1610743941, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1120 , (3, 0, None, None) , 0 , )),
	(( 'Time_occupancy_ratio' , 'pRetVal' , ), 1610743942, (1610743942, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1128 , (3, 0, None, None) , 0 , )),
	(( 'Uninterrupted_travel_delay' , 'pRetVal' , ), 1610743943, (1610743943, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1136 , (3, 0, None, None) , 0 , )),
	(( 'Queue_unrestr_mean' , 'pRetVal' , ), 1610743944, (1610743944, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1144 , (3, 0, None, None) , 0 , )),
	(( 'Cum_storage_space' , 'pRetVal' , ), 1610743945, (1610743945, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1152 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_mean_flag' , 'pRetVal' , ), 1610743946, (1610743946, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1160 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_percentile_flag' , 'pRetVal' , ), 1610743947, (1610743947, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1168 , (3, 0, None, None) , 0 , )),
	(( 'LOS_density' , 'pRetVal' , ), 1610743948, (1610743948, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1176 , (3, 0, None, None) , 0 , )),
	(( 'Density_pcu' , 'pRetVal' , ), 1610743949, (1610743949, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 1184 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLaneExit_vtables_dispatch_ = 1
ISIAPIOutputLaneExit_vtables_ = [
	(( 'Orientation' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Laneno' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Flow' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Flow_capconstr' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Merge_analysis_applied' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_flow_rate_veh_sl' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_flow_rate_pcu_sl' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap_sl' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway_sl' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Lane_flow_rate_sl' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_sl' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn_sl' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Min_delay_sl' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Merge_delay_sl' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_flow_rate_veh_ml' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_flow_rate_pcu_ml' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap_ml' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway_ml' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Lane_flow_rate_ml' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_ml' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn_ml' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Min_delay_ml' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Merge_delay_ml' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'OutputLeg' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16393, 10, None, "IID('{4D03B4B2-FBC7-4EC5-B7D8-984398036302}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLaneExits_vtables_dispatch_ = 1
ISIAPIOutputLaneExits_vtables_ = [
	(( 'Item' , 'Laneno' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{00351D05-37F3-4949-BC7C-186B4F6231E7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LaneExists' , 'Laneno' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLaneGreenPeriod_vtables_dispatch_ = 1
ISIAPIOutputLaneGreenPeriod_vtables_ = [
	(( 'Greenperiod' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Capacity' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Green_start_time' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Green_end_time' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Satflow_full' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Satflow_reduced' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Satflow_laneblock_adj' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Satflow_queuecleartime_adj' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_effect' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Eff_green_start' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'End_sat_green' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Eff_green_end' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Green_satn_time' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Queclearance_time' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Residual_queue' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Flow_ratio' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Green_ratio' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Subcycle' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Queue_discharge_rate' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Depflow_gt_adjsatn' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'OutputLane' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16393, 10, None, "IID('{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLaneGreenPeriods_vtables_dispatch_ = 1
ISIAPIOutputLaneGreenPeriods_vtables_ = [
	(( 'Item' , 'Greenperiod' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{2A8E738C-3173-41EB-A45C-AEDD77B5D649}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GreenPeriodExists' , 'Greenperiod' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLaneMC_vtables_dispatch_ = 1
ISIAPIOutputLaneMC_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Calc_exists' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Flow_total' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Flow_total_capconstr' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Upstr_flow_after_exit_sl' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Lane_change_from_left' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Lane_change_to_left' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Lane_change_from_right' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Lane_change_to_right' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Exist_in_nw_upstream_only' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Net_inflow' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Net_inflow_capconstr' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'OutputLane' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16393, 10, None, "IID('{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_flag' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLaneMCs_vtables_dispatch_ = 1
ISIAPIOutputLaneMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{96DB0ABD-FA20-4F9D-B2C8-4441009B4B88}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementClassExists' , 'mcClass' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLaneOD_vtables_dispatch_ = 1
ISIAPIOutputLaneOD_vtables_ = [
	(( 'Destination' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Crit_gap' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Foll_up_hdwy' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Flow' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Flow_capconstr' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Subdom_eq_dom' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'OutputLane' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'OutputLaneODMCs' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{8B1F140D-9817-413B-9AE1-7BF9777B4EB8}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Calc_exists' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Critical_spacing' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Lane_output_type' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_flow' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'HVE_pcu' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_flow_pcu' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_flow_ped' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Percent_nearest_lane_only' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Percent_exit_flow_incl' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Cap_constraint_effect' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'OD_factor' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Average_speed' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_bunched_flag' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_bunched' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Intrabunch_headway' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Priority_sharing_flag' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'HVE_for_entry' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'OD_factor_flag' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Average_speed_flag' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Intrabunch_headway_flag' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Crit_gap_flag' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Foll_up_hdwy_flag' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_flow_flag' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Opposing_flow_ped_flag' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_flag' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Unblocked_time_ratio' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_cycle_time' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_blocked_time' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_unblocked_time' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_delay' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLaneODMC_vtables_dispatch_ = 1
ISIAPIOutputLaneODMC_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Calc_exists' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Flow' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Flow_capconstr' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Shortlane_overflow' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Sl_overflow' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'OutputLaneOD' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{BD4E1996-A933-4CEA-A1FD-9B0C7B81E9F3}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Unblocked_time_ratio' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_cycle_time' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_blocked_time' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_unblocked_time' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_flag' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_delay' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLaneODMCs_vtables_dispatch_ = 1
ISIAPIOutputLaneODMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{BD6E29F3-4E14-4A9C-AA40-65954AB6BE78}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementClassExists' , 'mcClass' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLaneODs_vtables_dispatch_ = 1
ISIAPIOutputLaneODs_vtables_ = [
	(( 'Item' , 'Destination' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{BD4E1996-A933-4CEA-A1FD-9B0C7B81E9F3}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LaneODExists' , 'Destination' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLanes_vtables_dispatch_ = 1
ISIAPIOutputLanes_vtables_ = [
	(( 'Item' , 'Laneno' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LaneExists' , 'Laneno' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLeg_vtables_dispatch_ = 1
ISIAPIOutputLeg_vtables_ = [
	(( 'Orientation' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Flow_total' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Flow_LV' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_pct' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Flow_total_capconstr' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Flow_LV_capconstr' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_capconstr' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_pct_capconstr' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_effective' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_lane_total' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_mov_total' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service_worstmov' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service_worstlane' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_mean' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_percentile' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_mean' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_percentile' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_cycav_mean' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_cycav_percentile' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_mean' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_percentile' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_avg' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_percentile' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Stops_total' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_total' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_average' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_average' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_total' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_total' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_total' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_total' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Nox_total' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_rate' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_rate' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_rate' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_rate' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_rate' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Nox_rate' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Exiting_flow' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Circulating_flow' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'X1_flag' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'OutputLegMCs' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16393, 10, None, "IID('{C2BFE7C1-8AED-441A-AA66-B016245FC854}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'OutputLanes' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16393, 10, None, "IID('{376D0161-59D0-4F0E-911E-A7DD6774983E}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'OutputCirculatingLanes' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16393, 10, None, "IID('{0FC1F22D-8C53-40A4-B9AB-B8B9D664B8EE}')") , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstlane' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Delay_geometric' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Delay_stopline_average' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Exiting_flow_capconstr' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Circulating_flow_pcu' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'FHWA_capacity_zero_circ_flow' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Inscribed_diameter' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Num_entry_lanes' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Average_entry_lane_width' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Prop_queued_upstr_signal' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Prop_queued_upstr_signal_flag' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'Extra_bunching' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'Extra_bunching_flag' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'Idling_time_average' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743878, (1610743878, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'Net_inflow' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Net_inflow_capconstr' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'Net_outflow' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_flag' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'Queue_greenstart_mean' , 'pRetVal' , ), 1610743883, (1610743883, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'Queue_greenstart_percentile' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_greenstart_mean' , 'pRetVal' , ), 1610743885, (1610743885, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_greenstart_percentile' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adj_worstlane' , 'pRetVal' , ), 1610743887, (1610743887, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adj_flag_worstlane' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'Avg_num_of_cycles_to_depart' , 'pRetVal' , ), 1610743889, (1610743889, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'Total_lane_changes' , 'pRetVal' , ), 1610743890, (1610743890, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'Net_outflow_capconstr' , 'pRetVal' , ), 1610743891, (1610743891, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'Platoonmode_type' , 'pRetVal' , ), 1610743892, (1610743892, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyFlag' , 'pRetVal' , ), 1610743893, (1610743893, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'CongestionCoefficient' , 'pRetVal' , ), 1610743894, (1610743894, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeIndex' , 'pRetVal' , ), 1610743895, (1610743895, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'Prob_blockage' , 'pRetVal' , ), 1610743896, (1610743896, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743897, (1610743897, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743898, (1610743898, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedProgram' , 'pRetVal' , ), 1610743899, (1610743899, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'Uninterrupted_speed' , 'pRetVal' , ), 1610743900, (1610743900, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pRetVal' , ), 1610743901, (1610743901, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'Density_pcu' , 'pRetVal' , ), 1610743902, (1610743902, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'Spacing' , 'pRetVal' , ), 1610743903, (1610743903, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'Headway' , 'pRetVal' , ), 1610743904, (1610743904, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'Occupancy_time' , 'pRetVal' , ), 1610743905, (1610743905, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'Space_time' , 'pRetVal' , ), 1610743906, (1610743906, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'Avg_veh_length' , 'pRetVal' , ), 1610743907, (1610743907, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'Space_occupancy_ratio' , 'pRetVal' , ), 1610743908, (1610743908, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'Time_occupancy_ratio' , 'pRetVal' , ), 1610743909, (1610743909, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'Uninterrupted_travel_delay' , 'pRetVal' , ), 1610743910, (1610743910, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'LOS_density' , 'pRetVal' , ), 1610743911, (1610743911, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'OutputLaneExits' , 'pRetVal' , ), 1610743912, (1610743912, (), [ (16393, 10, None, "IID('{91DFAD2B-DD5C-40FE-B5DB-B4C40175952C}')") , ], 1 , 2 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'Outputset' , 'pRetVal' , ), 1610743913, (1610743913, (), [ (16393, 10, None, "IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')") , ], 1 , 2 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLegMC_vtables_dispatch_ = 1
ISIAPIOutputLegMC_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Flow' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Flow_capconstr' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'OutputLeg' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{4D03B4B2-FBC7-4EC5-B7D8-984398036302}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Exiting_flow' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Exiting_flow_capconstr' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Circulating_flow' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Circulating_flow_pcu' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Exist_in_nw_upstream_only' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Net_inflow' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Net_inflow_capconstr' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_flag' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Total_lane_changes' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Net_outflow' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Net_outflow_capconstr' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Calc_exists' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_mean' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_percentile' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_mean' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_percentile' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Avg_num_of_cycles_to_depart' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyFlag' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CongestionCoefficient' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeIndex' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Prob_blockage' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_avg' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_percentile' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adj_worstlane' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adj_flag_worstlane' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedProgram' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLegMCs_vtables_dispatch_ = 1
ISIAPIOutputLegMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{2E9D2343-958B-4C06-9CD9-C004A4B481ED}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementClassExists' , 'mcClass' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLegPerson_vtables_dispatch_ = 1
ISIAPIOutputLegPerson_vtables_ = [
	(( 'Orientation' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Demand_flow_total' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_total' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Stops_total' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_total' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_average' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_average' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Outputset' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16393, 10, None, "IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLegPersons_vtables_dispatch_ = 1
ISIAPIOutputLegPersons_vtables_ = [
	(( 'Item' , 'Orientation' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{F402DAA3-8B5C-47C7-BAB5-F124A4A16AC7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LegPersonExists' , 'Orientation' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputLegs_vtables_dispatch_ = 1
ISIAPIOutputLegs_vtables_ = [
	(( 'Item' , 'Orientation' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{4D03B4B2-FBC7-4EC5-B7D8-984398036302}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LegExists' , 'Orientation' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMeteredRoundabout_vtables_dispatch_ = 1
ISIAPIOutputMeteredRoundabout_vtables_ = [
	(( 'Metered_displayed_red' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Metered_displayed_blank' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Metered_effective_red' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Metered_effective_blank' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Blank_time_ratio' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Controlling_queue_detection_probability' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementPed_vtables_dispatch_ = 1
ISIAPIOutputMovementPed_vtables_ = [
	(( 'Type' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Stage' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Demand_flow_total' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_mov' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_mean' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_mean' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Stops_total' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_total' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_average' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_average' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Green_periods' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'OutputMovementPed_GreenPeriods' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16393, 10, None, "IID('{48C726FD-2FE1-44AA-8265-A5CE3B84B7D5}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_rate' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation_user_spec' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Crossing_dist' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Crossing_dist_user_spec' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Outputset' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16393, 10, None, "IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementPed_GreenPeriod_vtables_dispatch_ = 1
ISIAPIOutputMovementPed_GreenPeriod_vtables_ = [
	(( 'Start_phase' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'End_phase' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Greenperiod' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Start_loss' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'End_gain' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Eff_start_time' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Eff_end_time' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Lost_time' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Reqd_time' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Eff_green' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Adjusted_lost_time' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Adjusted_flow_ratio' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Reqd_green_time_ratio' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Satn_flow' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Flow_ratio' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Critical_mov' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Tmin' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Tmax' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Displayed_start_time' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Displayed_end_time' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Min_max_flag' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'No_arrival' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Min_walk_time' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Clearance1_time' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Clearance2_time' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Adjusted_lost_time_noact' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Tmin_noact' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Clearance1_time_option' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Clearance2_time_option' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Clearance_time_total' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Ped_minimum_time' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Ped_minimum_time_user_spec' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Ped_maximum_time' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Ped_negative_end_gain' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Start_intergrn_noact' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Start_intergrn' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Eff_min_walk_time_noact' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Eff_min_walk_time' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Walk_extension_time' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Total_walk_time' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Prob_ped_arrival' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Prob_ped_arrival_option' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Ped_maximum_time_option' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Unadj_reqd_time' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementPed_GreenPeriods_vtables_dispatch_ = 1
ISIAPIOutputMovementPed_GreenPeriods_vtables_ = [
	(( 'Item' , 'Greenperiod' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{D572C46E-740A-4488-BD94-1D2C1111C61F}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GreenPeriodExists' , 'Greenperiod' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementPeds_vtables_dispatch_ = 1
ISIAPIOutputMovementPeds_vtables_ = [
	(( 'Item' , 'Type' , 'Origin' , 'Stage' , 'pRetVal' , 
			 ), 0, (0, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{C0173099-4351-4B91-8AD7-82B5C047FAC2}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementExists' , 'Type' , 'Origin' , 'Stage' , 'pRetVal' , 
			 ), 1610743809, (1610743809, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementPersonOD_vtables_dispatch_ = 1
ISIAPIOutputMovementPersonOD_vtables_ = [
	(( 'Origin' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Destination' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Demand_flow_total' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_total' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Stops_total' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_total' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_average' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_average' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'OutputMovementPersonODMCs' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16393, 10, None, "IID('{607669B1-C03B-4159-B296-B084B2451BD2}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Outputset' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16393, 10, None, "IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementPersonODMC_vtables_dispatch_ = 1
ISIAPIOutputMovementPersonODMC_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Calc_exists' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Demand_flow_total' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_total' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Stops_total' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_total' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_average' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_average' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'OutputMovementPersonOD' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16393, 10, None, "IID('{D26606A5-98D6-468D-9B07-D9B3FD9B0321}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementPersonODMCs_vtables_dispatch_ = 1
ISIAPIOutputMovementPersonODMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{3B5F488E-D133-4697-85E3-05ACAA1915E9}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementClassExists' , 'mcClass' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementPersonODs_vtables_dispatch_ = 1
ISIAPIOutputMovementPersonODs_vtables_ = [
	(( 'Item' , 'Origin' , 'Destination' , 'pRetVal' , ), 0, (0, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{D26606A5-98D6-468D-9B07-D9B3FD9B0321}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementExists' , 'Origin' , 'Destination' , 'pRetVal' , ), 1610743809, (1610743809, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementVehicleOD_vtables_dispatch_ = 1
ISIAPIOutputMovementVehicleOD_vtables_ = [
	(( 'Origin' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Destination' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Flow_total' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Flow_LV' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_pct' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Flow_total_capconstr' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Flow_LV_capconstr' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_capconstr' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_pct_capconstr' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_mov' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'X1_flag' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Practical_spare_capacity' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total_veh' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total_persons' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Delay_stopline_average' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Delay_geometric' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_mean' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_percentile' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_mean' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_percentile' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_cycav_mean' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_cycav_percentile' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_mean' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_percentile' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_avg' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_percentile' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Stops_total' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_total' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_average' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_average' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Running_speed' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Cruise_speed' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_total' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_total' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_total' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_total' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Nox_total' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_rate' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_rate' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_rate' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_rate' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_rate' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Nox_rate' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Green_periods' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Approach_negotiation_speed' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Exit_negotiation_speed' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Exit_cruise_speed' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Has_highangle_slip' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Has_lowangle_slip' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Has_signals_control' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Has_stop_control' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Has_giveway_control' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Has_continuous_control' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Effective_control' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'OutputMovementVehicleODMCs' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (16393, 10, None, "IID('{0059BCEB-1475-43CB-A08D-E392F389F5DB}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstlane' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_stopline_total' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_stopline_average' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_stopline_total' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_stopline_average' , 'pRetVal' , ), 1610743878, (1610743878, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'Idling_time_average' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_flag' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_data_type' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'Queue_greenstart_mean' , 'pRetVal' , ), 1610743883, (1610743883, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'Queue_greenstart_percentile' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_greenstart_mean' , 'pRetVal' , ), 1610743885, (1610743885, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_greenstart_percentile' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adj_worstlane' , 'pRetVal' , ), 1610743887, (1610743887, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adj_flag_worstlane' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'Perc_arriving_during_green' , 'pRetVal' , ), 1610743889, (1610743889, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_ratio' , 'pRetVal' , ), 1610743890, (1610743890, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'Equivalent_AT' , 'pRetVal' , ), 1610743891, (1610743891, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'Avg_num_of_cycles_to_depart' , 'pRetVal' , ), 1610743892, (1610743892, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'Unblocked_time_ratio' , 'pRetVal' , ), 1610743893, (1610743893, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_cycle_time' , 'pRetVal' , ), 1610743894, (1610743894, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_blocked_time' , 'pRetVal' , ), 1610743895, (1610743895, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_unblocked_time' , 'pRetVal' , ), 1610743896, (1610743896, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_delay' , 'pRetVal' , ), 1610743897, (1610743897, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyFlag' , 'pRetVal' , ), 1610743898, (1610743898, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'CongestionCoefficient' , 'pRetVal' , ), 1610743899, (1610743899, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeIndex' , 'pRetVal' , ), 1610743900, (1610743900, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743901, (1610743901, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743902, (1610743902, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedProgram' , 'pRetVal' , ), 1610743903, (1610743903, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'Outputset' , 'pRetVal' , ), 1610743904, (1610743904, (), [ (16393, 10, None, "IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')") , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementVehicleODMC_vtables_dispatch_ = 1
ISIAPIOutputMovementVehicleODMC_vtables_ = [
	(( 'Origin' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Destination' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MC_class' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Flow' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Flow_capconstr' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_mov' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'X1_flag' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Practical_spare_capacity' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total_veh' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total_persons' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Delay_stopline_average' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Delay_geometric' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_mean' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_percentile' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_mean' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_percentile' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_cycav_mean' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_cycav_percentile' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_mean' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_percentile' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_avg' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_percentile' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Stops_total' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_total' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_average' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_average' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Running_speed' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Cruise_speed' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_total' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_total' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_total' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_total' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Nox_total' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_rate' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_rate' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_rate' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_rate' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_rate' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Nox_rate' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Green_periods' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Approach_negotiation_speed' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Exit_negotiation_speed' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Exit_cruise_speed' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Has_highangle_slip' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Has_lowangle_slip' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Has_signals_control' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Has_stop_control' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Has_giveway_control' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Has_continuous_control' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Effective_control' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'OutputMovementVehicleODMC_GreenPeriods' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16393, 10, None, "IID('{09DD6321-DDCF-4DA8-9DC6-099B915C5177}')") , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'OutputMovementVehicleOD' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16393, 10, None, "IID('{28749A62-EAF4-4575-BAB2-196A61EA612C}')") , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Calc_exists' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_stopline_total' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_stopline_average' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_stopline_total' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_stopline_average' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Negotiation_distance' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'Perc_arriving_during_green' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'Green_time_ratio' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'Platoon_ratio' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'Equivalent_AT' , 'pRetVal' , ), 1610743878, (1610743878, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'Signal_coordination' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Non_actuated' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_flag' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'Practical_degree_of_saturation' , 'pRetVal' , ), 1610743883, (1610743883, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'Queue_greenstart_mean' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'Queue_greenstart_percentile' , 'pRetVal' , ), 1610743885, (1610743885, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_greenstart_mean' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_greenstart_percentile' , 'pRetVal' , ), 1610743887, (1610743887, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'Avg_num_of_cycles_to_depart' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'Initial_demand_vol' , 'pRetVal' , ), 1610743889, (1610743889, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'Residual_demand_vol' , 'pRetVal' , ), 1610743890, (1610743890, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'Residual_demand_vol_clear_time' , 'pRetVal' , ), 1610743891, (1610743891, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'Oversatn_duration' , 'pRetVal' , ), 1610743892, (1610743892, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'Unblocked_time_ratio' , 'pRetVal' , ), 1610743893, (1610743893, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_cycle_time' , 'pRetVal' , ), 1610743894, (1610743894, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_blocked_time' , 'pRetVal' , ), 1610743895, (1610743895, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'Gap_accept_unblocked_time' , 'pRetVal' , ), 1610743896, (1610743896, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_delay' , 'pRetVal' , ), 1610743897, (1610743897, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyFlag' , 'pRetVal' , ), 1610743898, (1610743898, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'CongestionCoefficient' , 'pRetVal' , ), 1610743899, (1610743899, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeIndex' , 'pRetVal' , ), 1610743900, (1610743900, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743901, (1610743901, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743902, (1610743902, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedProgram' , 'pRetVal' , ), 1610743903, (1610743903, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'Flow_capconstr_no_initial' , 'pRetVal' , ), 1610743904, (1610743904, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementVehicleODMC_GreenPeriod_vtables_dispatch_ = 1
ISIAPIOutputMovementVehicleODMC_GreenPeriod_vtables_ = [
	(( 'Greenperiod' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Start_phase' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'End_phase' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Opposed' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Priority' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Undetected' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Start_loss' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'End_gain' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Eff_start_time' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Eff_end_time' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Lost_time' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Reqd_time' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Eff_green' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Adjusted_lost_time' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Adjusted_flow_ratio' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Reqd_green_time_ratio' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Satn_flow' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Flow_ratio' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Critical_mov' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Queue_move_up_speed' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Timing_data_type' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Tmin' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Tmax' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Displayed_start_time' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Displayed_end_time' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Min_max_flag' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'No_arrival' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Coord_mov_runs' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Displayed_green_time' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Satn_flow_flag' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Unadj_reqd_time' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Adjusted_lost_time_noact' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Min_green_noact' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Start_intergrn_noact' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Start_intergrn' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Prob_veh_arrival' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Prob_veh_arrival_flag' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Tmin_noact' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Red_arrow_drop_off_applied' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementVehicleODMC_GreenPeriods_vtables_dispatch_ = 1
ISIAPIOutputMovementVehicleODMC_GreenPeriods_vtables_ = [
	(( 'Item' , 'Greenperiod' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{D1B3E73C-50AF-4E33-83C7-DD0500022669}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GreenPeriodExists' , 'Greenperiod' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementVehicleODMCs_vtables_dispatch_ = 1
ISIAPIOutputMovementVehicleODMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{986170AC-21B5-40BE-B9FF-F0A3C2CDB6D1}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementClassExists' , 'mcClass' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMovementVehicleODs_vtables_dispatch_ = 1
ISIAPIOutputMovementVehicleODs_vtables_ = [
	(( 'Item' , 'Origin' , 'Destination' , 'pRetVal' , ), 0, (0, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{28749A62-EAF4-4575-BAB2-196A61EA612C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MovementExists' , 'Origin' , 'Destination' , 'pRetVal' , ), 1610743809, (1610743809, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMultiSequenceAnalyses_vtables_dispatch_ = 1
ISIAPIOutputMultiSequenceAnalyses_vtables_ = [
	(( 'Item' , 'index' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{6637A5AE-862D-4DB2-A89C-6368E9239E45}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputMultiSequenceAnalysis_vtables_dispatch_ = 1
ISIAPIOutputMultiSequenceAnalysis_vtables_ = [
	(( 'Seq_position' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_effective' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Practical_spare_capacity' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_percentile' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_percentile' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_total' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_total' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_total' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_total' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Nox_total' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Outputset' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16393, 10, None, "IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputNetwork_vtables_dispatch_ = 1
ISIAPIOutputNetwork_vtables_ = [
	(( 'Network' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GeneratedTime' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'IterationsCount' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'OutputNetworkVehicle' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{F5FAAD8A-BEAF-4C23-8ED9-4B22D4A45051}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'OutputNetworkPedestrian' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{A690DFE7-BEC8-47B7-A8A0-1176FE2EB02B}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'OutputNetworkPerson' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{DD7EC03C-ADB7-402E-973A-CC61673F18E3}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GeneratedByVersion' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'NetworkCycleTime' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'NetworkSummaryType' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'route' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16393, 10, None, "IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Analysis_method_flag' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Analysis_method' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Analysis_status' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Selected_future_year' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Largest_movement_flow_scale' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Selected_parameter_scale' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Single_ccg' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_option' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'OutputNetworkGraphTuples' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16393, 10, None, "IID('{CCE4D1AD-5F36-4DDD-94AB-6EF78A022E9B}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'OutputRouteMovementBasedVehicle' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16393, 10, None, "IID('{7FE4BECE-3C4E-4607-8CCA-C099AEE0F8B9}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'OutputRouteMovementBasedPerson' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16393, 10, None, "IID('{3C6C4EF3-04CC-4AD7-A16B-6643D85352C8}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputNetworkGraphTuple_vtables_dispatch_ = 1
ISIAPIOutputNetworkGraphTuple_vtables_ = [
	(( 'X_value' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_total' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_total_person' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Demand_flow_total' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_effective' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Practical_spare_capacity' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_percentile' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_percentile' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_total' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_total' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Nox_total' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_total' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_total' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Unsettled' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Demand_flow_total_ped' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Demand_flow_total_person' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Perc_heavy_veh' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn_ped' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total_veh' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total_ped' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total_person' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_veh' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_ped' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstlane' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov_ped' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov_person' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Delay_geometric_average' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Delay_stopline_average' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service_veh' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service_ped' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Total_stops_veh' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Total_stops_ped' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Total_stops_person' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate_veh' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate_ped' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Prop_queued_veh' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Prop_queued_ped' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Prop_queued_person' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index_veh' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index_ped' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_total_veh' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_total_ped' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_total_person' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_av_veh' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_av_ped' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Travel_dist_av_person' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total_veh' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total_ped' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total_person' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_av_veh' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_av_ped' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_av_person' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed_ped' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed_person' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total_veh' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total_ped' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputNetworkGraphTuples_vtables_dispatch_ = 1
ISIAPIOutputNetworkGraphTuples_vtables_ = [
	(( 'Item' , 'index' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{7B8EEE90-6CE2-465A-9022-FF17F8CC2BB4}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputNetworkPedestrian_vtables_dispatch_ = 1
ISIAPIOutputNetworkPedestrian_vtables_ = [
	(( 'ArrivalFlowTotal' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DemandFlowTotal' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DelayControlTotal' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DelayControlAverage' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DelayControlAverageWorstMovement' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'StopsTotal' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'StopRate' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ProportionQueued' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndex' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TravelDistanceTotal' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TravelDistanceAverage' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeTotal' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeAverage' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TravelSpeed' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'OperatingCostTotal' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputNetworkPerson_vtables_dispatch_ = 1
ISIAPIOutputNetworkPerson_vtables_ = [
	(( 'ArrivalFlowTotal' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DemandFlowTotal' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DelayControlTotal' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DelayControlAverage' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DelayControlAverageWorstMovement' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'StopsTotal' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'StopRate' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ProportionQueued' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndex' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TravelDistanceTotal' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TravelDistanceAverage' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeTotal' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeAverage' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TravelSpeed' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'OperatingCostTotal' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TravelDelay' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TravelDelayAverage' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputNetworkVehicle_vtables_dispatch_ = 1
ISIAPIOutputNetworkVehicle_vtables_ = [
	(( 'ArrivalFlowTotal' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ArrivalFlow_HV_pct' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DemandFlowTotal' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DemandFlow_HV_pct' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DegreeSaturation' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DelayControlTotal' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DelayControlAverage' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'DelayControlAverageWorstLane' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DelayControlAverageWorstMovement' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DelayGeometricAverage' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DelayStoplineAverage' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'StopsTotal' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'StopRate' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ProportionQueued' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndex' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TravelDistanceTotal' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeTotal' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'OperatingCostTotal' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'FuelConsumptionTotal' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CarbonDioxideTotal' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'HydrocarbonsTotal' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CarbonMonoxideTotal' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'NoxTotal' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CongestionCoefficient' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'TravelDistanceAverage' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeAverage' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'TravelSpeed' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DesiredTripTime' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'TravelDelay' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'IdlingTimeAvg' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RunningTimeAvg' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeIndex' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'QueueStorageRatioMaximum' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'QueueStorageRatioAverage' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'LevelOfService' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'OperatingCost_rate' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeAverage_rate' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'IdlingTimeAvgerage_rate' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'IdlingTimeAvgerage_pct' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'RunningTimeAvgerage_rate' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'RunningTimeAvgerage_pct' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'DesiredTripTime_rate' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'TravelDelay_rate' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'TravelDelay_pct' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'StopRate_rate' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'FuelConsumption_rate' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'CarbonDioxide_rate' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_rate' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'CarbonMonoxide_rate' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Nox_rate' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'FuelEconomy' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Min_dx_percent' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Max_dx_percent' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'TravelDelayAverage' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'TravelDelayAverage_rate' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Max_dx_percent_prev' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Max_dx_percent_prev2' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_effective' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Practical_spare_capacity' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'NwModel_vari_index' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyFlag' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputPhase_vtables_dispatch_ = 1
ISIAPIOutputPhase_vtables_ = [
	(( 'Position' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Phase_time' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Displayed_green_time' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Change_time' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Green_start' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Green_end' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Start_intergreen' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Terminating_intergreen' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Phase_split_percent' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Has_dummy' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_lost_time' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_reqd_time' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_eff_green' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Critical_dummy_mov_flag' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'IsReferencePhase' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Offset_change_time' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_adj_lost_time' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_adj_flow_ratio' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_reqd_green_time_ratio' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_tmin' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_tmax' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_min_max_flag' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Yellow_time' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'All_red_time' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Phase_frequency' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Phase_frequency_option' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputPhaseMovTimingPath_vtables_dispatch_ = 1
ISIAPIOutputPhaseMovTimingPath_vtables_ = [
	(( 'Position' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Outputset' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OutputPhaseMovTimingPathMovements' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{136F8B85-9B4F-40DF-8014-2D01E74B6BD4}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputPhaseMovTimingPathMovement_vtables_dispatch_ = 1
ISIAPIOutputPhaseMovTimingPathMovement_vtables_ = [
	(( 'Position' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Mov_type' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Destination' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MC_class' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Ped_type' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Ped_stage' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Greenperiod' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_phase_original_position' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Green_time' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Start_phase' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'End_phase' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'MovementDisplayID' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SiteDisplayID' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Critical_mov' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Eff_green' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Reqd_time' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'MaxGreenPeriod' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'OutputPhaseMovTimingPath' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16393, 10, None, "IID('{9454248A-D758-4959-98F8-AF6162DF5ACD}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputPhaseMovTimingPathMovements_vtables_dispatch_ = 1
ISIAPIOutputPhaseMovTimingPathMovements_vtables_ = [
	(( 'Item' , 'index' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{68493C00-16A9-4DDA-891E-386354D4D43C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputPhaseMovTimingPaths_vtables_dispatch_ = 1
ISIAPIOutputPhaseMovTimingPaths_vtables_ = [
	(( 'Item' , 'index' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{9454248A-D758-4959-98F8-AF6162DF5ACD}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputPhases_vtables_dispatch_ = 1
ISIAPIOutputPhases_vtables_ = [
	(( 'Item' , 'index' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{C186E5B6-87B7-4CBA-8D26-7190FC0709F1}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputRouteMovementBasedPerson_vtables_dispatch_ = 1
ISIAPIOutputRouteMovementBasedPerson_vtables_ = [
	(( 'TravelSpeed' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TravelDistanceAverage' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeAverage' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TravelDistanceTotal' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeTotal' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'TravelDelayAverage' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RouteStopRate' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RouteStopRate_rate' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputRouteMovementBasedVehicle_vtables_dispatch_ = 1
ISIAPIOutputRouteMovementBasedVehicle_vtables_ = [
	(( 'TravelSpeed' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TravelDistanceAverage' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeAverage' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeAverage_rate' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TravelDistanceTotal' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeTotal' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TravelDelayAverage' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TravelDelayAverage_rate' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RouteStopRate' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RouteStopRate_rate' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'LevelOfService' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeIndex' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CongestionCoefficient' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyFlag' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputSequence_vtables_dispatch_ = 1
ISIAPIOutputSequence_vtables_ = [
	(( 'Cycle_time_option' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_minimum' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_minimum_flag' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_practical' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Max_green_percent' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Adjusted_lost_time_total' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Adjusted_flow_ratio_total' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Reqd_green_time_ratio_total' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Reqd_movement_time_total' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Phases' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16393, 10, None, "IID('{3D49DB13-5D95-4180-BFDE-49B38D78781F}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_maximum' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_maximum_flag' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Warning_flag' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Cmaxsl_flag' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Largeyu_flag' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Critical_in_network' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_option_flag' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Seq_position' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputSitePedestrian_vtables_dispatch_ = 1
ISIAPIOutputSitePedestrian_vtables_ = [
	(( 'Demand_flow_total' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service_worstmov' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_mean' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_mean' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Stops_total' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_total' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_average' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_average' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_rate' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputSitePerson_vtables_dispatch_ = 1
ISIAPIOutputSitePerson_vtables_ = [
	(( 'Demand_flow_total' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Arrival_flow_total' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Stops_total' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_total' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_average' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_average' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_rate' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_total' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_total' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_total' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_total' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Nox_total' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputSiteRoute_vtables_dispatch_ = 1
ISIAPIOutputSiteRoute_vtables_ = [
	(( 'RouteName' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RouteSignalOffsetPriority' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Route_id' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Coord_mov_phasetime' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Coord_mov_effgreen' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Coord_mov_eff_start_time' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Coord_mov_displayed_start_time' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Coord_mov_displayed_green_time' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Outputset' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16393, 10, None, "IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputSiteRoutes_vtables_dispatch_ = 1
ISIAPIOutputSiteRoutes_vtables_ = [
	(( 'Item' , 'RouteName' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{E60C8BBE-4044-4AF0-900F-0840C61D77F7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E60C8BBE-4044-4AF0-900F-0840C61D77F7}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'RouteName' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputSiteVehicle_vtables_dispatch_ = 1
ISIAPIOutputSiteVehicle_vtables_ = [
	(( 'Flow_total' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Flow_LV' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_pct' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Flow_total_capconstr' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Flow_LV_capconstr' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_capconstr' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Flow_HV_pct_capconstr' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_effective' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_lane_total' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_mov_total' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Deg_satn' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Practical_spare_capacity' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstmov' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_average_worstlane' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Delay_control_total' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Delay_stopline_average' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Delay_geometric_average' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service_av_int_delay' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service_worstmov' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Level_of_service_worstlane' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_mean' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Queue_cycav_percentile' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_mean' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Queue_maxback_percentile' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_cycav_mean' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_cycav_percentile' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_mean' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_maxback_percentile' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_avg' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Queue_storage_ratio_percentile' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Stop_rate' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Stops_total' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Proportion_queued' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Performance_index' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_total' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Travel_distance_average' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_average' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Travel_speed' , 'pRetVal' , ), 1610743849, (1610743849, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_total' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_total' , 'pRetVal' , ), 1610743851, (1610743851, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_total' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_total' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_total' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Nox_total' , 'pRetVal' , ), 1610743855, (1610743855, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Operating_cost_rate' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Fuel_consumption_rate' , 'pRetVal' , ), 1610743857, (1610743857, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_dioxide_rate' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Hydrocarbons_rate' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Carbon_monoxide_rate' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Nox_rate' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Idling_time_average' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Analysis_method' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiency' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Queue_greenstart_mean' , 'pRetVal' , ), 1610743865, (1610743865, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Queue_greenstart_percentile' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_greenstart_mean' , 'pRetVal' , ), 1610743867, (1610743867, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Queue_dist_greenstart_percentile' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adj_worstlane' , 'pRetVal' , ), 1610743869, (1610743869, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Capacity_adj_flag_worstlane' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Avg_num_of_cycles_to_depart' , 'pRetVal' , ), 1610743871, (1610743871, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Model_timing_vari_index' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Max_timit_dx_percent' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Max_timit_dx_percent_prev' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'Max_timit_dx_percent_prev2' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'TimIterationsCount' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'Max_TimIterations' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'Model_flowcap_vari_index' , 'pRetVal' , ), 1610743878, (1610743878, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'Max_subit_dx_percent' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Max_subit_dx_percent_prev' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'Max_subit_dx_percent_prev2' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'SubIterationsCount' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'Max_SubIterations' , 'pRetVal' , ), 1610743883, (1610743883, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'Max_subit_capacity_diff' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'Max_subit_capacity_percent' , 'pRetVal' , ), 1610743885, (1610743885, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743887, (1610743887, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedProgram' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'TravelTimeIndex' , 'pRetVal' , ), 1610743889, (1610743889, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'CongestionCoefficient' , 'pRetVal' , ), 1610743890, (1610743890, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'SpeedEfficiencyFlag' , 'pRetVal' , ), 1610743891, (1610743891, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'Travel_time_total_at_desired_speed' , 'pRetVal' , ), 1610743892, (1610743892, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
]

ISIAPIOutputset_vtables_dispatch_ = 1
ISIAPIOutputset_vtables_ = [
	(( 'Generated' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'OutputSiteVehicle' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{EB43DD42-CCFE-4728-A81E-0246C4344B2F}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OutputSitePedestrian' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{5E3241AA-696A-4DAF-BDCA-C6C9AA13E0EB}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'OutputSitePerson' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{53819F2B-01AB-464E-B46A-1DF4F967E8B7}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'OutputLegs' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{7A84E80F-58FD-4C53-94B3-29713CCED51C}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'OutputMovementVehicleODs' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{F7CF3309-E6B6-4637-93F1-DC805C88F46A}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'OutputMovementPeds' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{3C02979B-5CC8-41CC-86DC-1884428878F1}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'OutputMeteredRoundabout' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{B11203CA-CABF-43DF-9156-6898CA85836F}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'OutputSequence' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16393, 10, None, "IID('{8832ED63-ACD1-45C0-B218-786FDF3B3E5C}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'OutputAnalysis' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16393, 10, None, "IID('{91779742-CF41-42AD-963E-22F788CA96F4}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'OutputGraphTuples' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16393, 10, None, "IID('{3E26EBE1-0955-49EB-8E9F-8CC3B645361B}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Site' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'networkSite' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16393, 10, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'GeneratedByVersion' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Analysis_method' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TWSC_calib_adjusted' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'NwSiteOffset' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'NwSite_SignalPlatoonMode' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'OutputLegPersons' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16393, 10, None, "IID('{D31B97D0-0C54-45B5-9529-1DFF92F8B457}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'OutputMovementPersonODs' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16393, 10, None, "IID('{C1ADE01E-D8D6-44AD-8FB2-18158BD070F1}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'OutputSiteRoutes' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16393, 10, None, "IID('{A30A36F9-FA16-4D54-9338-1357D2FF0D24}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Analysis_method_flag' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'OutputPhaseMovTimingPaths' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16393, 10, None, "IID('{5D48995D-44C9-40DE-A5EC-9460D1F8417C}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'HasSIDRUNUnsettledMsg' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'HasSIDRUNAWSCMsg' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'OutputMultiSequenceAnalyses' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16393, 10, None, "IID('{CD988BB1-BF23-45C3-B098-74FABCE0BDF2}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

ISIAPIPhase_vtables_dispatch_ = 1
ISIAPIPhase_vtables_ = [
	(( 'Phase_id' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Is_variable' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Is_variable' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'IsReferencePhase' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'IsReferencePhase' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Phase_time' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Phase_time' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Yellow_time' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Yellow_time' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'All_red_time' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'All_red_time' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Has_dummy' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Has_dummy' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_minimum_green_time_user' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_minimum_green_time_user' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_minimum_green_time' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_minimum_green_time' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_maximum_green_time_user' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_maximum_green_time_user' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_maximum_green_time' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Dummy_maximum_green_time' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_time' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Minimum_time' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Phasemovement_vehicles' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16393, 10, None, "IID('{843F1163-A090-4AA1-9AB4-8CF90C0A8BFF}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Phasemovement_peds' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16393, 10, None, "IID('{8F802394-B3B4-4D06-8EA2-A0247C600A86}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Sequence' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16393, 10, None, "IID('{B528481B-1627-4D64-9F55-5D7E943539A6}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Phase_frequency_user' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Phase_frequency_user' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Phase_frequency' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Phase_frequency' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

ISIAPIPhasemovement_ped_vtables_dispatch_ = 1
ISIAPIPhasemovement_ped_vtables_ = [
	(( 'Movement_ped_origin' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Movement_ped_type' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Movement_ped_stage' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Running' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Running' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Terminates' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Terminates' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Undetected' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Undetected' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Phase' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16393, 10, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

ISIAPIPhasemovement_peds_vtables_dispatch_ = 1
ISIAPIPhasemovement_peds_vtables_ = [
	(( 'Item' , 'Type' , 'Origin' , 'Stage' , 'pRetVal' , 
			 ), 0, (0, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{77A6AC80-AF80-4EED-9493-561C3B928907}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PhasemovementPedExists' , 'Type' , 'Origin' , 'Stage' , 'pRetVal' , 
			 ), 1610743809, (1610743809, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIPhasemovement_vehicle_vtables_dispatch_ = 1
ISIAPIPhasemovement_vehicle_vtables_ = [
	(( 'Movement_vehicle_origin' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Movement_vehicle_destination' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MC_class' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Running' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Running' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Terminates' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Terminates' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Undetected' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Undetected' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Phase' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16393, 10, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Is_red_arrow_drop_off_enabled' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Is_red_arrow_drop_off_enabled' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Red_arrow_drop_off' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Red_arrow_drop_off' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

ISIAPIPhasemovement_vehicles_vtables_dispatch_ = 1
ISIAPIPhasemovement_vehicles_vtables_ = [
	(( 'Item' , 'Origin' , 'Destination' , 'mcClass' , 'pRetVal' , 
			 ), 0, (0, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{96854CD8-BA75-4EB1-8320-7DCC929C2503}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PhasemovementVehicleExists' , 'Origin' , 'Destination' , 'mcClass' , 'pRetVal' , 
			 ), 1610743809, (1610743809, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPIPhases_vtables_dispatch_ = 1
ISIAPIPhases_vtables_ = [
	(( 'Item' , 'phasename' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PhaseExists' , 'phasename' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetPhaseByID' , 'Phase_id' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISIAPIProject_vtables_dispatch_ = 1
ISIAPIProject_vtables_ = [
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SiteFolders' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16393, 10, None, "IID('{9712E108-061B-4BB9-AC11-8ADECF24EA13}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NetworkFolders' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{12AD1FBE-8A7B-4CB9-9DD5-F233FC8FC13C}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UpdateModifiedInfo' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ImportSitesFromProject' , 'projectFilePath' , 'siteNames' , 'pRetVal' , ), 1610743813, (1610743813, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ImportNetworksFromProject' , 'projectFilePath' , 'networkNames' , 'pRetVal' , ), 1610743814, (1610743814, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AddSiteFolder' , 'Name' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RemoveSiteFolder' , 'siteFolder' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (9, 1, None, "IID('{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'MoveSiteFolderTo' , 'siteFolder' , 'newPosition' , 'pRetVal' , ), 1610743817, (1610743817, (), [ 
			 (9, 1, None, "IID('{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'AddNetworkFolder' , 'Name' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'RemoveNetworkFolder' , 'NetworkFolder' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (9, 1, None, "IID('{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'MoveNetworkFolderTo' , 'NetworkFolder' , 'newPosition' , 'pRetVal' , ), 1610743820, (1610743820, (), [ 
			 (9, 1, None, "IID('{18533800-8D94-4C98-8BF7-59DC4E51C2DF}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ISIAPIRoute_vtables_dispatch_ = 1
ISIAPIRoute_vtables_ = [
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'RouteID' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RouteID' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'LOSMethod' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'LOSMethod' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RouteSummaryOption' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'RouteSummaryOption' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInOutputNetworkByRoutes' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInOutputNetworkByRoutes' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInSignalOffsetCal' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInSignalOffsetCal' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SignalOffsetPriority' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SignalOffsetPriority' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SignalOffsetMethod' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SignalOffsetMethod' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SignalOffsetCalMCClass' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SignalOffsetCalMCClass' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Created_date' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Created_by' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Created_by_company' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Created_version' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Modified_date' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Modified_by' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Modified_by_company' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Modified_version' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'RouteNwSites' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16393, 10, None, "IID('{8FF9FA61-FA15-4F9C-95E4-3F02656F6F14}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Network' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16393, 10, None, "IID('{C5A62A3D-7D9C-4544-8547-499D4C770332}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'OutputRoute' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16393, 10, None, "IID('{5E551751-0DA8-4E10-931A-D474F6FFBB27}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'AddRouteNwSite' , 'networkSite' , 'Origin' , 'Destination' , 'pRetVal' , 
			 ), 1610743841, (1610743841, (), [ (9, 1, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{58C442E7-0E64-47B5-AFFA-99BABCE5435E}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'CheckIsValidForSignalOffsetCalc' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UpdateModifiedInfo' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Process' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RemoveRouteNwSite' , 'routeNwSite' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (9, 1, None, "IID('{58C442E7-0E64-47B5-AFFA-99BABCE5435E}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInProjectSummary' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInProjectSummary' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Is_time_distance_reverse_included' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Is_time_distance_reverse_included' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Time_distance_direction' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Time_distance_direction' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'RouteMCs' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16393, 10, None, "IID('{BBE52DD6-5D32-4984-A42B-E5F24F27EF13}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'RemoveOutputData' , 'pRetVal' , ), 1610743853, (1610743853, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'ShowSecondaryPlatoons' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'ShowSecondaryPlatoons' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
]

ISIAPIRouteMC_vtables_dispatch_ = 1
ISIAPIRouteMC_vtables_ = [
	(( 'MC_class' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeedMethod' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DesiredSpeed' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LowerLimitOfSpeedEfficiency' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LowerLimitOfSpeedEfficiency' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'route' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISIAPIRouteMCs_vtables_dispatch_ = 1
ISIAPIRouteMCs_vtables_ = [
	(( 'Item' , 'mcClass' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{74F4BB54-522D-4628-B31B-1A74786A6487}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISIAPIRouteNwSite_vtables_dispatch_ = 1
ISIAPIRouteNwSite_vtables_ = [
	(( 'SiteName' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Destination' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'route' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'networkSite' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{4888B50C-984E-4865-B2CE-4FA9B66C2622}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ISIAPIRouteNwSites_vtables_dispatch_ = 1
ISIAPIRouteNwSites_vtables_ = [
	(( 'Item' , 'SiteName' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{58C442E7-0E64-47B5-AFFA-99BABCE5435E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{58C442E7-0E64-47B5-AFFA-99BABCE5435E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RouteNwSiteExists' , 'SiteName' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPIRoutes_vtables_dispatch_ = 1
ISIAPIRoutes_vtables_ = [
	(( 'Item' , 'RouteName' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RouteExists' , 'RouteName' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPISensitivity_vtables_dispatch_ = 1
ISIAPISensitivity_vtables_ = [
	(( 'Groupno' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Selected_parameter' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Selected_parameter' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Lower' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Lower' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Upper' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Upper' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Increment' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Increment' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Is_constant_factor_applied' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Is_constant_factor_applied' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Constant_factor' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Constant_factor' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ISIAPISequence_vtables_dispatch_ = 1
ISIAPISequence_vtables_ = [
	(( 'Sequence_id' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Is_selected' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Is_selected' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_option' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Cycle_time_option' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Practical_max_cycle_time' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Practical_max_cycle_time' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Practical_cycle_rounding' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Practical_cycle_rounding' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower_user' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower_user' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_lower' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_upper' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_upper' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_increment' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_increment' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_perf_measure' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_perf_measure' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_optim_method' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_cycle_time_optim_method' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_lower' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_lower' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_upper' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_upper' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_increment' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_percent_increment' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_perf_measure' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_perf_measure' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_optim_method' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Optimum_max_green_optim_method' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Variable_phasing_perf_measure' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Variable_phasing_perf_measure' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Usergiven_cycle_time' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Usergiven_cycle_time' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Green_split_priority_option' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Green_split_priority_option' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_max_green_major_mov' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_max_green_major_mov' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_max_green_minor_mov' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_max_green_minor_mov' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_gap_major_mov' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_gap_major_mov' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_gap_minor_mov' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Actuated_gap_minor_mov' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Eff_det_zone_len_major_mov' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Eff_det_zone_len_major_mov' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Eff_det_zone_len_minor_mov' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Eff_det_zone_len_minor_mov' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Site' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Phases' , 'pRetVal' , ), 1610743861, (1610743861, (), [ (16393, 10, None, "IID('{98B4AB9E-189E-4149-BFE9-0DD10CA8BBEF}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'AddPhase' , 'Name' , 'pRetVal' , ), 1610743863, (1610743863, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'RemovePhase' , 'Phase' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (9, 1, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'InsertPhase' , 'Position' , 'Name' , 'pRetVal' , ), 1610743865, (1610743865, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , ], 1 , 1 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'ClonePhase' , 'Phase' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (9, 1, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , 
			 (16393, 10, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'MovePhaseTo' , 'Phase' , 'newPosition' , 'pRetVal' , ), 1610743867, (1610743867, (), [ 
			 (9, 1, None, "IID('{E772441A-2D95-4E27-B1D0-88BB8B995EAD}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Lane_blockage_effect_option' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Lane_blockage_effect_option' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Is_timing_optimised_for_selected_result' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Is_timing_optimised_for_selected_result' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
]

ISIAPISequences_vtables_dispatch_ = 1
ISIAPISequences_vtables_ = [
	(( 'Item' , 'Name' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{B528481B-1627-4D64-9F55-5D7E943539A6}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{B528481B-1627-4D64-9F55-5D7E943539A6}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SequenceExists' , 'Name' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetSequenceByID' , 'Sequence_id' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{B528481B-1627-4D64-9F55-5D7E943539A6}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISIAPISite_vtables_dispatch_ = 1
ISIAPISite_vtables_ = [
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Intersectionid' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Intersectionid' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Site_id' , 'pRetVal' , ), 1610743813, (1610743813, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'MovementClasses' , 'pRetVal' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{39B087B7-EB2C-4B47-8923-F8DD4238C771}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Legs' , 'pRetVal' , ), 1610743815, (1610743815, (), [ (16393, 10, None, "IID('{D7F45026-862A-432F-BC67-E0557FED8203}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'MovementVehicleODs' , 'pRetVal' , ), 1610743816, (1610743816, (), [ (16393, 10, None, "IID('{87B16289-A709-4781-ADA1-92C6D1F3EB3D}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'MovementPeds' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (16393, 10, None, "IID('{DE5491F4-C24E-4505-A74A-DC4E93712375}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Sequences' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (16393, 10, None, "IID('{838EB6A8-198A-4409-B1A5-0267857AD7F1}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ModelSetting' , 'pRetVal' , ), 1610743819, (1610743819, (), [ (16393, 10, None, "IID('{DB0EFBA0-673A-4E4B-B359-ED0CAFA0643F}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Analysis' , 'pRetVal' , ), 1610743820, (1610743820, (), [ (16393, 10, None, "IID('{C3D8FE89-6620-45E7-898A-F4108FA95E6F}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'GapAcceptanceTurnOnRed' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (16393, 10, None, "IID('{8860D705-1B2F-4F1E-B59A-6C4992A3FE9A}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TwoWaySignControlAdjMajorNumLanes' , 'pRetVal' , ), 1610743822, (1610743822, (), [ (16393, 10, None, "IID('{546F1C93-6CF2-44A4-B963-E18FBA6A7A61}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TwoWaySignControlAdjGeometryControls' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (16393, 10, None, "IID('{89002DC5-ADA3-4304-B64C-1A38C0D522A3}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Outputset' , 'pRetVal' , ), 1610743824, (1610743824, (), [ (16393, 10, None, "IID('{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Project' , 'pRetVal' , ), 1610743825, (1610743825, (), [ (16393, 10, None, "IID('{5817180B-2283-40FB-8068-C2F2D656EF04}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ProcessingError' , 'pRetVal' , ), 1610743826, (1610743826, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ProcessingWarnings' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'HasWarnings' , 'pRetVal' , ), 1610743828, (1610743828, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'pRetVal' , ), 1610743829, (1610743829, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'DiagnosticStatus' , 'pRetVal' , ), 1610743830, (1610743830, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'DiagnosticMsgs' , 'pRetVal' , ), 1610743831, (1610743831, (), [ (16393, 10, None, "IID('{CBFD7927-0588-4CF2-BEB4-052B1F31A027}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Sitetype' , 'pRetVal' , ), 1610743832, (1610743832, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Sitecontroltype' , 'pRetVal' , ), 1610743833, (1610743833, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'DriveOnLeft' , 'pRetVal' , ), 1610743834, (1610743834, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Units' , 'pRetVal' , ), 1610743835, (1610743835, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Hcm' , 'pRetVal' , ), 1610743836, (1610743836, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ModelSignature' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ModelName' , 'pRetVal' , ), 1610743838, (1610743838, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Freeway_orientation' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Created_date' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Created_by' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Created_by_company' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Created_version' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Modified_date' , 'pRetVal' , ), 1610743844, (1610743844, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Modified_by' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Modified_by_company' , 'pRetVal' , ), 1610743846, (1610743846, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Modified_version' , 'pRetVal' , ), 1610743847, (1610743847, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pRetVal' , ), 1610743848, (1610743848, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Unittimeforvolumes' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Unittimeforvolumes' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Peakflowperiod' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Peakflowperiod' , 'pRetVal' , ), 1610743854, (1610743854, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Signal_analysis_method' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Signal_analysis_method' , 'pRetVal' , ), 1610743856, (1610743856, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'CostUnit' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'CostUnit' , 'pRetVal' , ), 1610743858, (1610743858, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Rou_stopline_setback_dist' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Rou_stopline_setback_dist' , 'pRetVal' , ), 1610743860, (1610743860, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Rou_metered_start_loss' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Rou_metered_start_loss' , 'pRetVal' , ), 1610743862, (1610743862, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Rou_metered_end_gain' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Rou_metered_end_gain' , 'pRetVal' , ), 1610743864, (1610743864, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Rou_controlling_detector_setback_dist' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Rou_controlling_detector_setback_dist' , 'pRetVal' , ), 1610743866, (1610743866, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Rou_metered_leg_orientation' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Rou_metered_leg_orientation' , 'pRetVal' , ), 1610743868, (1610743868, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Rou_controlling_leg_orientation' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Rou_controlling_leg_orientation' , 'pRetVal' , ), 1610743870, (1610743870, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Process' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'ResetMovementVehicleODMCExists' , 'pRetVal' , ), 1610743873, (1610743873, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'ResetLaneMovements' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'ResetSitePrioritiesData' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'UpdateModifiedInfo' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'AddLeg' , 'Orientation' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{24A8E5D9-0016-45F2-9941-12E58EE54A05}')") , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'AddLegWithLanes' , 'Orientation' , 'LegGeometry' , 'pRetVal' , ), 1610743878, (1610743878, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{24A8E5D9-0016-45F2-9941-12E58EE54A05}')") , ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'RemoveLeg' , 'Orientation' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'Rotate' , 'step' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometryData' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'AddSequence' , 'Name' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{B528481B-1627-4D64-9F55-5D7E943539A6}')") , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'RemoveSequence' , 'Sequence' , 'pRetVal' , ), 1610743883, (1610743883, (), [ (9, 1, None, "IID('{B528481B-1627-4D64-9F55-5D7E943539A6}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'CreateLayoutPngData' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (24593, 10, None, None) , ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'CreateLayoutPngFile' , 'filename' , 'pRetVal' , ), 1610743885, (1610743885, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'CloneSequence' , 'Sequence' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (9, 1, None, "IID('{B528481B-1627-4D64-9F55-5D7E943539A6}')") , 
			 (16393, 10, None, "IID('{B528481B-1627-4D64-9F55-5D7E943539A6}')") , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'MoveSequenceTo' , 'Sequence' , 'newPosition' , 'pRetVal' , ), 1610743887, (1610743887, (), [ 
			 (9, 1, None, "IID('{B528481B-1627-4D64-9F55-5D7E943539A6}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'Category' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'Category' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInProjectSummary' , 'pRetVal' , ), 1610743890, (1610743890, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'IsIncludedInProjectSummary' , 'pRetVal' , ), 1610743890, (1610743890, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'siteFolder' , 'pRetVal' , ), 1610743892, (1610743892, (), [ (16393, 10, None, "IID('{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')") , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'Is_multi_sequence_enabled' , 'pRetVal' , ), 1610743893, (1610743893, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'Is_multi_sequence_enabled' , 'pRetVal' , ), 1610743893, (1610743893, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'RemoveOutputData' , 'pRetVal' , ), 1610743895, (1610743895, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'Sitesubtype' , 'pRetVal' , ), 1610743896, (1610743896, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'Sitesubtype' , 'pRetVal' , ), 1610743896, (1610743896, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
]

ISIAPISiteFolder_vtables_dispatch_ = 1
ISIAPISiteFolder_vtables_ = [
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Sites' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{8938DB91-E714-4703-8C7D-18B0DD89A19C}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Project' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{5817180B-2283-40FB-8068-C2F2D656EF04}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AddSite' , 'Sitetype' , 'softwareSetup' , 'pRetVal' , ), 1610743813, (1610743813, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AddSiteWithGeometry' , 'Sitetype' , 'softwareSetup' , 'majorRoadOrientation' , 'pRetVal' , 
			 ), 1610743814, (1610743814, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AddSite_2' , 'Sitetype' , 'softwareSetupSignature' , 'pRetVal' , ), 1610743815, (1610743815, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AddSiteWithGeometry_2' , 'Sitetype' , 'softwareSetupSignature' , 'majorRoadOrientation' , 'pRetVal' , 
			 ), 1610743816, (1610743816, (), [ (3, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RemoveSite' , 'Site' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (9, 1, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'CloneSite' , 'Site' , 'pRetVal' , ), 1610743818, (1610743818, (), [ (9, 1, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , 
			 (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MoveSiteTo' , 'Site' , 'newPosition' , 'pRetVal' , ), 1610743819, (1610743819, (), [ 
			 (9, 1, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'MoveSitesToFolder' , 'siteNames' , 'destFolder' , 'pRetVal' , ), 1610743820, (1610743820, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')") , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ISIAPISiteFolders_vtables_dispatch_ = 1
ISIAPISiteFolders_vtables_ = [
	(( 'Item' , 'Name' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SiteFolderExists' , 'Name' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISIAPISites_vtables_dispatch_ = 1
ISIAPISites_vtables_ = [
	(( 'Item' , 'SiteName' , 'pRetVal' , ), 0, (0, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item_2' , 'index' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SiteExists' , 'SiteName' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetSiteByID' , 'Site_id' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{4BD64E91-A354-4A38-AA9E-E581F8D302CC}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISIAPITwoWaySignControlAdjGeometryControl_vtables_dispatch_ = 1
ISIAPITwoWaySignControlAdjGeometryControl_vtables_ = [
	(( 'Type' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap_adj' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap_adj' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway_adj' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway_adj' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISIAPITwoWaySignControlAdjGeometryControls_vtables_dispatch_ = 1
ISIAPITwoWaySignControlAdjGeometryControls_vtables_ = [
	(( 'Item' , 'geoControlType' , 'pRetVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{06229DBD-9E71-4D04-A6DA-B7B0524A7302}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'geoControlType' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISIAPITwoWaySignControlAdjMajorNumLane_vtables_dispatch_ = 1
ISIAPITwoWaySignControlAdjMajorNumLane_vtables_ = [
	(( 'Major_num_lane' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Movement_type' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap_adj' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Critical_gap_adj' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway_adj' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Followup_headway_adj' , 'pRetVal' , ), 1610743812, (1610743812, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ISIAPITwoWaySignControlAdjMajorNumLanes_vtables_dispatch_ = 1
ISIAPITwoWaySignControlAdjMajorNumLanes_vtables_ = [
	(( 'Item' , 'majorRoadNumOfLane' , 'movType' , 'pRetVal' , ), 0, (0, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{77FFB02C-F596-4F32-907B-D5CF292B0686}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Exists' , 'majorRoadNumOfLane' , 'movType' , 'pRetVal' , ), 1610743809, (1610743809, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

_AuthorizationDecisionItem_vtables_dispatch_ = 1
_AuthorizationDecisionItem_vtables_ = [
]

_Object_vtables_dispatch_ = 1
_Object_vtables_ = [
	(( 'ToString' , 'pRetVal' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Equals' , 'obj' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (12, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetHashCode' , 'pRetVal' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetType' , 'pRetVal' , ), 1610743811, (1610743811, (), [ (16397, 10, None, "IID('{BCA8B44D-AAD6-3A86-8AB7-03349F4F2DA2}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

_SIOptionCustomData_vtables_dispatch_ = 1
_SIOptionCustomData_vtables_ = [
]

RecordMap = {
}

CLSIDToClassMap = {
	'{7FB3D82F-C33F-4919-AF8B-5AE805445CA5}' : ISIAPI,
	'{C3D8FE89-6620-45E7-898A-F4108FA95E6F}' : ISIAPIAnalysis,
	'{CC6E10F5-9A73-41A2-BCA8-235D7FB0091A}' : ISIAPIDiagnosticMsg,
	'{CBFD7927-0588-4CF2-BEB4-052B1F31A027}' : ISIAPIDiagnosticMsgs,
	'{8860D705-1B2F-4F1E-B59A-6C4992A3FE9A}' : ISIAPIGapAcceptanceSpecificApp,
	'{E741707B-9A4C-414A-A4F0-482E5F098534}' : ISIAPIIsland,
	'{6B55FEF0-D591-4E75-B2BA-81E22B796325}' : ISIAPIIslands,
	'{5F156412-3EAE-40A0-99B2-06D8E48D87D1}' : ISIAPILaneApproach,
	'{5C8E5D1E-E796-4190-8965-8BBD365D0D7F}' : ISIAPILaneApproachMovement,
	'{92115A53-7558-433A-AC10-E109B19E83ED}' : ISIAPILaneApproachMovementMC,
	'{E94C2A89-6DE0-4AE6-82E9-48DD3B752E1A}' : ISIAPILaneApproachMovementMCs,
	'{881029ED-4A7E-4469-A782-F48BF5E0F373}' : ISIAPILaneApproachMovements,
	'{148779D1-5A0D-48B1-9CBB-7002DAB05D95}' : ISIAPILaneApproachs,
	'{FE1B8A3D-ECC2-4B36-876E-FDB052503918}' : ISIAPILaneExit,
	'{9702C419-60FE-48C2-8412-23B83BF5C78C}' : ISIAPILaneExitMergeParam,
	'{99F74111-A47C-45B1-94DE-16E6F4194A60}' : ISIAPILaneExits,
	'{6DC82697-7A67-4BB3-8DA8-3F51C1D71135}' : ISIAPILaneMovement,
	'{D1EA4B6C-DC27-44B5-B0BE-233F53D81B6C}' : ISIAPILaneMovementMC,
	'{D8D650BB-D92A-4A21-9F34-F76F1C225497}' : ISIAPILaneMovementMCs,
	'{C1711C63-BCCC-41F6-94CC-80BFBF951D74}' : ISIAPILaneMovements,
	'{6BE9B7D6-A12E-4CB5-A938-08260963BE84}' : ISIAPILaneSegment,
	'{52442B71-F816-4AA6-9A01-9F66957C3925}' : ISIAPILaneSegmentMC,
	'{4962E57C-6B9E-4331-94DB-F141DA807485}' : ISIAPILaneSegmentMCs,
	'{24A8E5D9-0016-45F2-9941-12E58EE54A05}' : ISIAPILeg,
	'{D7F45026-862A-432F-BC67-E0557FED8203}' : ISIAPILegs,
	'{25BFA806-8BFC-4ADF-9A0B-9DA47FE86246}' : ISIAPILeg_roundabout,
	'{13F6A490-E35F-4AF3-9FCE-843062E81CCD}' : ISIAPILeg_rou_hcm,
	'{BD507F2C-6D0F-4256-8E40-79299F021130}' : ISIAPILeg_rou_hcm6_extended,
	'{DB0EFBA0-673A-4E4B-B359-ED0CAFA0643F}' : ISIAPIModelSetting,
	'{69AB3019-BCEB-413C-90C3-09A8DA0144DD}' : ISIAPIMovementClass,
	'{39B087B7-EB2C-4B47-8923-F8DD4238C771}' : ISIAPIMovementClasses,
	'{94958D62-C2A0-40CD-A631-894BD1A1BC00}' : ISIAPIMovementClassFuelEmission,
	'{BF9EA147-CE73-49C5-A6DB-7FAA6DFC663E}' : ISIAPIMovementClassFuelEmissions,
	'{86D55C22-E6CE-4FF9-89A9-F53001A61501}' : ISIAPIMovementClassMergeParam,
	'{0099AEAC-F9B6-4DCE-9C0E-1434E9D603D7}' : ISIAPIMovement_ped,
	'{DE5491F4-C24E-4505-A74A-DC4E93712375}' : ISIAPIMovement_peds,
	'{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}' : ISIAPIMovement_vehicle_od,
	'{87B16289-A709-4781-ADA1-92C6D1F3EB3D}' : ISIAPIMovement_vehicle_ods,
	'{55D25294-3468-41D8-96A1-B5B6E06AFF99}' : ISIAPIMovement_vehicle_od_mc,
	'{69A455C4-0A3C-4A69-8A20-DFC672995EDC}' : ISIAPIMovement_vehicle_od_mcs,
	'{C5A62A3D-7D9C-4544-8547-499D4C770332}' : ISIAPINetwork,
	'{6635581E-7C13-461E-9917-85B7CA3F7B07}' : ISIAPINetworkCCG,
	'{110BF49A-6953-499B-9648-8C1EFDA2B4CC}' : ISIAPINetworkCCGPhase,
	'{A2B9F260-C553-40A5-99CB-16F98407645F}' : ISIAPINetworkCCGPhases,
	'{AFE37B56-E6C5-4F98-8853-6FFF575C25BC}' : ISIAPINetworkCCGs,
	'{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}' : ISIAPINetworkCCGSequence,
	'{833D5364-D498-47D7-BE84-44624D8D16B5}' : ISIAPINetworkCCGSequences,
	'{B8795F7C-B342-4E4D-9F88-398D704B4453}' : ISIAPINetworkDemandSensitivity,
	'{18533800-8D94-4C98-8BF7-59DC4E51C2DF}' : ISIAPINetworkFolder,
	'{12AD1FBE-8A7B-4CB9-9DD5-F233FC8FC13C}' : ISIAPINetworkFolders,
	'{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}' : ISIAPINetworkLegConnection,
	'{F29A35EA-9B6B-46B7-839B-EC921C94A479}' : ISIAPINetworkLegConnections,
	'{213E3AC6-7026-49A5-A65E-B5E2CE167E8D}' : ISIAPINetworkMC,
	'{EA51880D-3150-4EF5-B203-17CC4EAC2214}' : ISIAPINetworkMCs,
	'{98CE5F37-494C-484F-B8F5-50993C839B3B}' : ISIAPINetworks,
	'{4888B50C-984E-4865-B2CE-4FA9B66C2622}' : ISIAPINetworkSite,
	'{8B19120E-37DE-43E9-AB2F-9F1743650053}' : ISIAPINetworkSites,
	'{1602B72A-4010-4F67-B45D-5C8A493BC687}' : ISIAPIOpposingmovement_ped,
	'{580C5233-F043-4662-8C1D-2E0C31C568B9}' : ISIAPIOpposingmovement_peds,
	'{CDC74ADC-2CF3-49D5-8DC5-3821AC96AA91}' : ISIAPIOpposingmovement_vehicle,
	'{677C1F98-D3D5-40B3-A5E5-5AEBD3A33CCC}' : ISIAPIOpposingmovement_vehicles,
	'{91779742-CF41-42AD-963E-22F788CA96F4}' : ISIAPIOutputAnalysis,
	'{7F03E897-A19D-41C6-A6EA-FECCF36A3358}' : ISIAPIOutputCirculatingLane,
	'{FA80BAB6-860C-4FA9-841D-3ECB6EA78605}' : ISIAPIOutputCirculatingLaneMC,
	'{E3D1A42E-AA21-4472-B566-8EAE73EAB615}' : ISIAPIOutputCirculatingLaneMCs,
	'{0FC1F22D-8C53-40A4-B9AB-B8B9D664B8EE}' : ISIAPIOutputCirculatingLanes,
	'{E69891AB-798F-4534-9C25-8BCD74AF811A}' : ISIAPIOutputGraphTuple,
	'{3E26EBE1-0955-49EB-8E9F-8CC3B645361B}' : ISIAPIOutputGraphTuples,
	'{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}' : ISIAPIOutputLane,
	'{00351D05-37F3-4949-BC7C-186B4F6231E7}' : ISIAPIOutputLaneExit,
	'{91DFAD2B-DD5C-40FE-B5DB-B4C40175952C}' : ISIAPIOutputLaneExits,
	'{2A8E738C-3173-41EB-A45C-AEDD77B5D649}' : ISIAPIOutputLaneGreenPeriod,
	'{472D3454-925A-442D-8498-E4A01EF86C20}' : ISIAPIOutputLaneGreenPeriods,
	'{96DB0ABD-FA20-4F9D-B2C8-4441009B4B88}' : ISIAPIOutputLaneMC,
	'{A04D1E92-C344-4E0E-850A-1B97D38BD7B8}' : ISIAPIOutputLaneMCs,
	'{BD4E1996-A933-4CEA-A1FD-9B0C7B81E9F3}' : ISIAPIOutputLaneOD,
	'{BD6E29F3-4E14-4A9C-AA40-65954AB6BE78}' : ISIAPIOutputLaneODMC,
	'{8B1F140D-9817-413B-9AE1-7BF9777B4EB8}' : ISIAPIOutputLaneODMCs,
	'{83C46DBA-91A4-4A1F-9EC4-7ECEB223C6DA}' : ISIAPIOutputLaneODs,
	'{376D0161-59D0-4F0E-911E-A7DD6774983E}' : ISIAPIOutputLanes,
	'{4D03B4B2-FBC7-4EC5-B7D8-984398036302}' : ISIAPIOutputLeg,
	'{2E9D2343-958B-4C06-9CD9-C004A4B481ED}' : ISIAPIOutputLegMC,
	'{C2BFE7C1-8AED-441A-AA66-B016245FC854}' : ISIAPIOutputLegMCs,
	'{F402DAA3-8B5C-47C7-BAB5-F124A4A16AC7}' : ISIAPIOutputLegPerson,
	'{D31B97D0-0C54-45B5-9529-1DFF92F8B457}' : ISIAPIOutputLegPersons,
	'{7A84E80F-58FD-4C53-94B3-29713CCED51C}' : ISIAPIOutputLegs,
	'{B11203CA-CABF-43DF-9156-6898CA85836F}' : ISIAPIOutputMeteredRoundabout,
	'{C0173099-4351-4B91-8AD7-82B5C047FAC2}' : ISIAPIOutputMovementPed,
	'{3C02979B-5CC8-41CC-86DC-1884428878F1}' : ISIAPIOutputMovementPeds,
	'{D572C46E-740A-4488-BD94-1D2C1111C61F}' : ISIAPIOutputMovementPed_GreenPeriod,
	'{48C726FD-2FE1-44AA-8265-A5CE3B84B7D5}' : ISIAPIOutputMovementPed_GreenPeriods,
	'{D26606A5-98D6-468D-9B07-D9B3FD9B0321}' : ISIAPIOutputMovementPersonOD,
	'{3B5F488E-D133-4697-85E3-05ACAA1915E9}' : ISIAPIOutputMovementPersonODMC,
	'{607669B1-C03B-4159-B296-B084B2451BD2}' : ISIAPIOutputMovementPersonODMCs,
	'{C1ADE01E-D8D6-44AD-8FB2-18158BD070F1}' : ISIAPIOutputMovementPersonODs,
	'{28749A62-EAF4-4575-BAB2-196A61EA612C}' : ISIAPIOutputMovementVehicleOD,
	'{986170AC-21B5-40BE-B9FF-F0A3C2CDB6D1}' : ISIAPIOutputMovementVehicleODMC,
	'{0059BCEB-1475-43CB-A08D-E392F389F5DB}' : ISIAPIOutputMovementVehicleODMCs,
	'{D1B3E73C-50AF-4E33-83C7-DD0500022669}' : ISIAPIOutputMovementVehicleODMC_GreenPeriod,
	'{09DD6321-DDCF-4DA8-9DC6-099B915C5177}' : ISIAPIOutputMovementVehicleODMC_GreenPeriods,
	'{F7CF3309-E6B6-4637-93F1-DC805C88F46A}' : ISIAPIOutputMovementVehicleODs,
	'{CD988BB1-BF23-45C3-B098-74FABCE0BDF2}' : ISIAPIOutputMultiSequenceAnalyses,
	'{6637A5AE-862D-4DB2-A89C-6368E9239E45}' : ISIAPIOutputMultiSequenceAnalysis,
	'{5E551751-0DA8-4E10-931A-D474F6FFBB27}' : ISIAPIOutputNetwork,
	'{7B8EEE90-6CE2-465A-9022-FF17F8CC2BB4}' : ISIAPIOutputNetworkGraphTuple,
	'{CCE4D1AD-5F36-4DDD-94AB-6EF78A022E9B}' : ISIAPIOutputNetworkGraphTuples,
	'{A690DFE7-BEC8-47B7-A8A0-1176FE2EB02B}' : ISIAPIOutputNetworkPedestrian,
	'{DD7EC03C-ADB7-402E-973A-CC61673F18E3}' : ISIAPIOutputNetworkPerson,
	'{F5FAAD8A-BEAF-4C23-8ED9-4B22D4A45051}' : ISIAPIOutputNetworkVehicle,
	'{C186E5B6-87B7-4CBA-8D26-7190FC0709F1}' : ISIAPIOutputPhase,
	'{9454248A-D758-4959-98F8-AF6162DF5ACD}' : ISIAPIOutputPhaseMovTimingPath,
	'{68493C00-16A9-4DDA-891E-386354D4D43C}' : ISIAPIOutputPhaseMovTimingPathMovement,
	'{136F8B85-9B4F-40DF-8014-2D01E74B6BD4}' : ISIAPIOutputPhaseMovTimingPathMovements,
	'{5D48995D-44C9-40DE-A5EC-9460D1F8417C}' : ISIAPIOutputPhaseMovTimingPaths,
	'{3D49DB13-5D95-4180-BFDE-49B38D78781F}' : ISIAPIOutputPhases,
	'{3C6C4EF3-04CC-4AD7-A16B-6643D85352C8}' : ISIAPIOutputRouteMovementBasedPerson,
	'{7FE4BECE-3C4E-4607-8CCA-C099AEE0F8B9}' : ISIAPIOutputRouteMovementBasedVehicle,
	'{8832ED63-ACD1-45C0-B218-786FDF3B3E5C}' : ISIAPIOutputSequence,
	'{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}' : ISIAPIOutputset,
	'{5E3241AA-696A-4DAF-BDCA-C6C9AA13E0EB}' : ISIAPIOutputSitePedestrian,
	'{53819F2B-01AB-464E-B46A-1DF4F967E8B7}' : ISIAPIOutputSitePerson,
	'{E60C8BBE-4044-4AF0-900F-0840C61D77F7}' : ISIAPIOutputSiteRoute,
	'{A30A36F9-FA16-4D54-9338-1357D2FF0D24}' : ISIAPIOutputSiteRoutes,
	'{EB43DD42-CCFE-4728-A81E-0246C4344B2F}' : ISIAPIOutputSiteVehicle,
	'{E772441A-2D95-4E27-B1D0-88BB8B995EAD}' : ISIAPIPhase,
	'{77A6AC80-AF80-4EED-9493-561C3B928907}' : ISIAPIPhasemovement_ped,
	'{8F802394-B3B4-4D06-8EA2-A0247C600A86}' : ISIAPIPhasemovement_peds,
	'{96854CD8-BA75-4EB1-8320-7DCC929C2503}' : ISIAPIPhasemovement_vehicle,
	'{843F1163-A090-4AA1-9AB4-8CF90C0A8BFF}' : ISIAPIPhasemovement_vehicles,
	'{98B4AB9E-189E-4149-BFE9-0DD10CA8BBEF}' : ISIAPIPhases,
	'{5817180B-2283-40FB-8068-C2F2D656EF04}' : ISIAPIProject,
	'{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}' : ISIAPIRoute,
	'{74F4BB54-522D-4628-B31B-1A74786A6487}' : ISIAPIRouteMC,
	'{BBE52DD6-5D32-4984-A42B-E5F24F27EF13}' : ISIAPIRouteMCs,
	'{58C442E7-0E64-47B5-AFFA-99BABCE5435E}' : ISIAPIRouteNwSite,
	'{8FF9FA61-FA15-4F9C-95E4-3F02656F6F14}' : ISIAPIRouteNwSites,
	'{DE44AC02-4804-4587-87BB-AC8E0ED05EEB}' : ISIAPIRoutes,
	'{D025138A-4F4C-4613-8FA7-D1FD5550A50C}' : ISIAPISensitivity,
	'{B528481B-1627-4D64-9F55-5D7E943539A6}' : ISIAPISequence,
	'{838EB6A8-198A-4409-B1A5-0267857AD7F1}' : ISIAPISequences,
	'{4BD64E91-A354-4A38-AA9E-E581F8D302CC}' : ISIAPISite,
	'{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}' : ISIAPISiteFolder,
	'{9712E108-061B-4BB9-AC11-8ADECF24EA13}' : ISIAPISiteFolders,
	'{8938DB91-E714-4703-8C7D-18B0DD89A19C}' : ISIAPISites,
	'{06229DBD-9E71-4D04-A6DA-B7B0524A7302}' : ISIAPITwoWaySignControlAdjGeometryControl,
	'{89002DC5-ADA3-4304-B64C-1A38C0D522A3}' : ISIAPITwoWaySignControlAdjGeometryControls,
	'{77FFB02C-F596-4F32-907B-D5CF292B0686}' : ISIAPITwoWaySignControlAdjMajorNumLane,
	'{546F1C93-6CF2-44A4-B963-E18FBA6A7A61}' : ISIAPITwoWaySignControlAdjMajorNumLanes,
	'{65074F7F-63C0-304E-AF0A-D51741CB4A8D}' : _Object,
	'{805D7A98-D4AF-3F0F-967F-E5CF45312D2C}' : IDisposable,
	'{D92122F2-74F7-4A2B-953E-B75CF1B2738D}' : SIAPI,
	'{3988FB26-C8F8-4AA9-8FCB-B803193F4D50}' : SIAPIAnalysis,
	'{6BD716CD-F4A3-4CAF-A052-24F92F02130D}' : SIAPIDiagnosticMsg,
	'{496B0ABE-CDEE-11D3-88E8-00902754C43A}' : IEnumerable,
	'{98563BD9-ED3E-4ECA-ABAD-FCC3D86B1021}' : SIAPIDiagnosticMsgs,
	'{8FAEAC43-040F-48C1-9FF0-D8883FFFFE11}' : SIAPIGapAcceptanceSpecificApp,
	'{EA335953-2755-4056-860C-5355FA753978}' : SIAPIIsland,
	'{F797F2BF-20A2-4353-9E76-14B778448B3B}' : SIAPIIslands,
	'{C64B58F7-7E6C-4D01-B73F-74EE785691D5}' : SIAPILaneApproach,
	'{A5CA350D-1764-431A-B3DE-4E66AEC098CE}' : SIAPILaneApproachMovement,
	'{A8FE0EAC-41F7-4B6D-A03E-BD4296549E04}' : SIAPILaneApproachMovementMC,
	'{D0F9DE87-E61E-43C9-AB12-A81DCCF2BE76}' : SIAPILaneApproachMovementMCs,
	'{3C6FB29C-52F6-426B-AE37-987D1910CF22}' : SIAPILaneApproachMovements,
	'{78A0E9B9-165B-4790-8B63-0003CEE1381F}' : SIAPILaneApproachs,
	'{F142FCA8-DBFF-4477-BA9B-4B6F416B3642}' : SIAPILaneExit,
	'{4E294323-0877-4866-8E42-50BDE4F0FC69}' : SIAPILaneExitMergeParam,
	'{6B84632B-C622-4C79-BCDB-16DBC5FE472E}' : SIAPILaneExits,
	'{62BB3A21-AE88-44DE-83A4-68663A3C1A09}' : SIAPILaneMovement,
	'{61E72EEE-F3BA-4B3D-8733-017C4F399459}' : SIAPILaneMovementMC,
	'{1C1577BA-CBAC-4781-9A9F-40C6A2AD215D}' : SIAPILaneMovementMCs,
	'{6C29D3CD-B050-411A-9B2B-F7A008C9342E}' : SIAPILaneMovements,
	'{8A1FCFC4-08FB-4CB6-A9BC-E58D495ACAB6}' : SIAPILaneSegment,
	'{34AA399B-6B65-46DE-8F64-9A59ACECCF8E}' : SIAPILaneSegmentMC,
	'{CDB7B33D-887D-4EAE-9596-1207BFC72BB5}' : SIAPILaneSegmentMCs,
	'{D8B9A97D-F4E1-4E42-81D2-C370A157DC13}' : SIAPILeg,
	'{CB79F519-887E-4349-B499-5FFF86EB475D}' : SIAPILegs,
	'{B9DD66CB-2900-4C0D-A7F9-A0BDF06656E9}' : SIAPILeg_roundabout,
	'{3824A747-9BC3-4304-B6C1-0969796A33EA}' : SIAPILeg_rou_hcm,
	'{FDA1F3A6-FA03-4937-99CB-AA207DD504F9}' : SIAPILeg_rou_hcm6_extended,
	'{4F6A34D7-8E26-4D62-819E-6A100FB00AC9}' : SIAPIModelSetting,
	'{22DCD1A6-1C92-478E-ABAB-FA0AFBE2F235}' : SIAPIMovementClass,
	'{ECE0790E-AA84-41A3-A0E2-74E3E2E4E2C5}' : SIAPIMovementClasses,
	'{7C2A53C7-B12F-4C83-A409-1BDD05DADB5C}' : SIAPIMovementClassFuelEmission,
	'{7D7AAA7B-6F56-44C2-A439-22A50FA85997}' : SIAPIMovementClassFuelEmissions,
	'{E567F5BB-9F02-452E-8633-568913739EBC}' : SIAPIMovementClassMergeParam,
	'{695474FC-BF40-4A63-B1D3-0E9D5974BB68}' : SIAPIMovement_ped,
	'{2680FEE3-C577-402C-BEC4-ED25E864B1C4}' : SIAPIMovement_peds,
	'{BDA8A10E-42F8-4CDB-961D-7B85BB245C66}' : SIAPIMovement_vehicle_od,
	'{954FF861-147D-46C1-BBBD-3B1FC1EEE70C}' : SIAPIMovement_vehicle_ods,
	'{23B2A7F0-0A7C-4DD8-BB86-8613CA079749}' : SIAPIMovement_vehicle_od_mc,
	'{8447273B-5B6D-438B-A672-27CE30624350}' : SIAPIMovement_vehicle_od_mcs,
	'{2756D52B-FF46-4C94-8B37-0443810347CB}' : SIAPINetwork,
	'{6D2F736E-A370-4F0A-ADBB-415015499B40}' : SIAPINetworkCCG,
	'{1D63D43D-AE3E-4580-A807-1D8F60277E86}' : SIAPINetworkCCGPhase,
	'{7A5CF9F9-A024-451D-8C83-60F453170DC4}' : SIAPINetworkCCGPhases,
	'{F42C1BFD-FE64-49F5-9EA9-97A29C94E9A8}' : SIAPINetworkCCGs,
	'{0C3B93A9-7DEE-4339-9CF8-1E5F7F64653C}' : SIAPINetworkCCGSequence,
	'{10A357EA-76F6-4197-B4DC-BA4E0B877F70}' : SIAPINetworkCCGSequences,
	'{75BDF116-4417-40F7-9D85-0E70C279A0E0}' : SIAPINetworkDemandSensitivity,
	'{EABC402D-EA39-45D4-B70C-57ABA79EE4AE}' : SIAPINetworkFolder,
	'{14AB4741-60D5-4E2C-A7D9-391036F4ADA2}' : SIAPINetworkFolders,
	'{16F09299-E4AE-446A-961B-8EE1ABB10071}' : SIAPINetworkLegConnection,
	'{01B7EA08-A88F-45BE-903F-FB14E5182042}' : SIAPINetworkLegConnections,
	'{2574B151-F7F0-4022-9BA1-A341BC5D729C}' : SIAPINetworkMC,
	'{CEE4DFD4-600F-4DAC-BA31-BE8B7F1DF783}' : SIAPINetworkMCs,
	'{19F0570A-094B-4C3E-A770-FFCA0601ADDA}' : SIAPINetworks,
	'{37361C6E-E0EE-4D90-AA13-88732732B094}' : SIAPINetworkSite,
	'{380DA3D4-9F8D-4C74-935B-707EA324270C}' : SIAPINetworkSites,
	'{5AC30B47-D990-41E3-A4E7-A6EB907B1552}' : SIAPIOpposingmovement_ped,
	'{D9E4FBC3-03B6-41E7-A725-5D0300B1D687}' : SIAPIOpposingmovement_peds,
	'{99EEB0D9-CD36-4CC6-B8D7-924CE09C963D}' : SIAPIOpposingmovement_vehicle,
	'{EAEECED7-036B-4734-BCA8-8EF70D134D28}' : SIAPIOpposingmovement_vehicles,
	'{2B3CCFD8-4A9C-4A0E-B589-3D1F3A6FFEA1}' : SIAPIOutputAnalysis,
	'{207A9ACF-CDFD-415C-8D9F-07019F6CF7AB}' : SIAPIOutputCirculatingLane,
	'{AC1E9E02-F9EB-4AE2-91B7-8E0656BB3918}' : SIAPIOutputCirculatingLaneMC,
	'{FF4EC6A5-5840-4E3D-84E1-86F02CC3F788}' : SIAPIOutputCirculatingLaneMCs,
	'{B191000C-58A2-414D-AE1C-4EFC68B3827A}' : SIAPIOutputCirculatingLanes,
	'{F7AAE6AF-D859-4522-A447-CD18941AE963}' : SIAPIOutputGraphTuple,
	'{8177D1E3-5454-4BB5-AE18-D7147D4C8A35}' : SIAPIOutputGraphTuples,
	'{F51F3BC3-A54E-4748-9886-5D4F3C30D4F0}' : SIAPIOutputLane,
	'{BF2C2275-C235-40CF-A2AB-54A9C372C1D9}' : SIAPIOutputLaneExit,
	'{DEBB105B-76D0-4FD5-A113-447035DC51FC}' : SIAPIOutputLaneExits,
	'{1E733D74-F977-426E-93F7-2A8BF1454878}' : SIAPIOutputLaneGreenPeriod,
	'{2FF0DB72-0FE3-4A4D-B5CF-904BB39595AA}' : SIAPIOutputLaneGreenPeriods,
	'{AD35D08C-C0AF-4D8F-9B88-751892BB25E3}' : SIAPIOutputLaneMC,
	'{1FBBD5AB-E682-4C06-BEFC-6EDB64D3666A}' : SIAPIOutputLaneMCs,
	'{B378D9C3-4E9D-4819-8762-BD68819E5CB2}' : SIAPIOutputLaneOD,
	'{4F4B3FF2-23D4-4461-AACB-6E2F84E31DC0}' : SIAPIOutputLaneODMC,
	'{BA8AE905-D5B8-4CAB-B5F4-FCA3F78E9E63}' : SIAPIOutputLaneODMCs,
	'{AF3C822E-8BAC-4DA0-819B-9312B69AD052}' : SIAPIOutputLaneODs,
	'{0D940366-6119-4660-8B95-80796E0695DB}' : SIAPIOutputLanes,
	'{E9A07B34-F024-4B0D-8F6E-54F6E743AC2C}' : SIAPIOutputLeg,
	'{F3741C26-DB83-4B1A-B27C-3A77398B820D}' : SIAPIOutputLegMC,
	'{A8384538-2E01-41E9-B927-A1B92997CBAE}' : SIAPIOutputLegMCs,
	'{437CCE51-F160-474A-9E8C-2F4563AB7972}' : SIAPIOutputLegPerson,
	'{6894003C-85BB-4C7D-AF06-4DA6296A53CD}' : SIAPIOutputLegPersons,
	'{CC917735-7108-44B2-AB13-4CA33F9BF15E}' : SIAPIOutputLegs,
	'{8E03F3A5-D77C-4D28-834D-5CEC97CB8B93}' : SIAPIOutputMeteredRoundabout,
	'{B3EBCA38-6BD7-47EE-860F-3CBAA18B0A8E}' : SIAPIOutputMovementPed,
	'{1365E5D6-A5D4-4F25-9103-C306C6367EDB}' : SIAPIOutputMovementPeds,
	'{84D7F6CD-F5FA-4A63-AAD3-A0836A53E19D}' : SIAPIOutputMovementPed_GreenPeriod,
	'{9A430652-1CDD-473B-B7B7-30803DDFA31B}' : SIAPIOutputMovementPed_GreenPeriods,
	'{A72FF5DE-CE06-4986-AE4E-6A0264AC85FE}' : SIAPIOutputMovementPersonOD,
	'{32E2E2DA-8053-4562-9511-995FAED66C61}' : SIAPIOutputMovementPersonODMC,
	'{701F5599-2068-4533-BBE9-1BEAE64344EB}' : SIAPIOutputMovementPersonODMCs,
	'{7448B67E-5F38-4E37-BF4C-A475561C7EFF}' : SIAPIOutputMovementPersonODs,
	'{62FF9ABF-31EF-46B7-A288-2B9074A70F87}' : SIAPIOutputMovementVehicleOD,
	'{DE724601-782C-4198-A2CD-745C397898D4}' : SIAPIOutputMovementVehicleODMC,
	'{D8D3C9FE-9684-4EA9-AC7D-3E1533984744}' : SIAPIOutputMovementVehicleODMCs,
	'{A3C07D6F-05EB-4636-96F4-2F2E21B76559}' : SIAPIOutputMovementVehicleODMC_GreenPeriod,
	'{3B2A414F-F47E-46DA-A129-8FA0E569A68E}' : SIAPIOutputMovementVehicleODMC_GreenPeriods,
	'{1D7046CE-4C37-4EE0-957D-F78BD3FE40E0}' : SIAPIOutputMovementVehicleODs,
	'{41E3DF9C-C236-47ED-A1C3-30A9F5C14C9A}' : SIAPIOutputMultiSequenceAnalyses,
	'{BD186FED-F0F8-49DA-B585-FBE8ED785FE5}' : SIAPIOutputMultiSequenceAnalysis,
	'{2AACA59E-CEC2-4BF8-B07B-C12BD329A7E9}' : SIAPIOutputNetwork,
	'{761871EA-EF42-4D9E-AD88-1363E5E9CCD9}' : SIAPIOutputNetworkGraphTuple,
	'{C4474735-1E00-4BA4-A903-A89A9D95381D}' : SIAPIOutputNetworkGraphTuples,
	'{BBEAE5FC-9424-4977-9EE8-1177608D1825}' : SIAPIOutputNetworkPedestrian,
	'{6183EA81-DA0E-44B6-B40D-F1DAF0933E78}' : SIAPIOutputNetworkPerson,
	'{82306492-4410-44E4-BBEE-D4223CB0DA23}' : SIAPIOutputNetworkVehicle,
	'{B640710A-977F-4313-BED9-C576EF0C58F1}' : SIAPIOutputPhase,
	'{84CB4043-3761-4F41-93D0-A36BD048C9F9}' : SIAPIOutputPhaseMovTimingPath,
	'{1B8CC9B3-532D-453B-AF77-5CB719ECCA69}' : SIAPIOutputPhaseMovTimingPathMovement,
	'{1C744150-30B7-468A-AC2E-262F67C49910}' : SIAPIOutputPhaseMovTimingPathMovements,
	'{50CFC083-8D6F-423C-8C80-B976A18F15AE}' : SIAPIOutputPhaseMovTimingPaths,
	'{6180E4A3-7220-40A9-B67E-1A1E2980081F}' : SIAPIOutputPhases,
	'{F9033992-8196-424F-9725-D4E387E2110D}' : SIAPIOutputRouteMovementBasedPerson,
	'{FDC3E673-E1B9-4AC2-9503-BCE42A55CD58}' : SIAPIOutputRouteMovementBasedVehicle,
	'{606A4EB4-6E73-4DB2-8E4A-610842F7F05B}' : SIAPIOutputSequence,
	'{5CCD43AB-186C-4353-BA54-9F5C7081FC75}' : SIAPIOutputset,
	'{270364E1-ECE5-4E2E-A7D4-1337FC506CE9}' : SIAPIOutputSitePedestrian,
	'{272D58B6-297A-4958-B030-4C7B65DE12B9}' : SIAPIOutputSitePerson,
	'{2E78F5C0-56C2-4BF1-B1D1-1A62D5A8420D}' : SIAPIOutputSiteRoute,
	'{5507EC83-9958-413B-BF33-40958E76EF71}' : SIAPIOutputSiteRoutes,
	'{5AE191CE-B05A-4EC0-93A2-7C18E4C68F62}' : SIAPIOutputSiteVehicle,
	'{601FC223-4405-429B-A762-BC05946EDE1E}' : SIAPIPhase,
	'{AE225517-D441-49D9-926F-18E976A6A05C}' : SIAPIPhasemovement_ped,
	'{66368ABF-3FE9-46B0-83AB-E291B28BD09D}' : SIAPIPhasemovement_peds,
	'{B18833B0-DFF8-4104-8CF7-CC6E72B2A0CC}' : SIAPIPhasemovement_vehicle,
	'{3E7EF29A-8A66-4DDE-B091-F3D882406164}' : SIAPIPhasemovement_vehicles,
	'{B17972E8-D253-40CB-8820-68BBE891708A}' : SIAPIPhases,
	'{AA3D5162-1291-44E3-B6DB-168A66FA698F}' : SIAPIProject,
	'{F41B79F2-95A5-485C-B977-48171C90931E}' : SIAPIRoute,
	'{E1AE119F-DBA4-4CFC-B95A-58A0F45607D0}' : SIAPIRouteMC,
	'{6968C090-DAA4-4E9B-A7CB-2BDE998AF328}' : SIAPIRouteMCs,
	'{DE246637-0712-4778-9FE3-1A6E50F0DF60}' : SIAPIRouteNwSite,
	'{3F421D2F-DDB0-4089-AFE4-8BED7C14BFA8}' : SIAPIRouteNwSites,
	'{14C9EB51-3E0F-407C-BD50-FB301D141A8A}' : SIAPIRoutes,
	'{562BD1F6-FCD9-4F3E-8F07-F2AA2274B12A}' : SIAPISensitivity,
	'{93907DC0-76DC-4B13-BE89-09CC209EC779}' : SIAPISequence,
	'{EC6DC582-D6C0-4DAA-B2A6-8A1E7C9E6ED2}' : SIAPISequences,
	'{1D0A3CAF-D0CF-4AC2-BCD6-FD377579759B}' : SIAPISite,
	'{51678BC8-2907-4D52-AB68-95CFCA3C029C}' : SIAPISiteFolder,
	'{B1DB958A-0F80-4845-B4FD-FED3BEDAFE13}' : SIAPISiteFolders,
	'{2322E0C4-40D9-46EF-9ACA-52AF8BA62A2D}' : SIAPISites,
	'{F2A4712E-4165-42F8-9336-30DA604C4279}' : SIAPITwoWaySignControlAdjGeometryControl,
	'{CD5FBEDB-CBE3-4A86-A2E8-BF71E507C463}' : SIAPITwoWaySignControlAdjGeometryControls,
	'{17E1A63D-976D-4A05-9151-8491AD5D8712}' : SIAPITwoWaySignControlAdjMajorNumLane,
	'{A5050181-1C6A-4BF4-A8C5-4A712A954A90}' : SIAPITwoWaySignControlAdjMajorNumLanes,
	'{C3A9F3D6-00FB-3F9D-81C4-0D629824F518}' : _AuthorizationDecisionItem,
	'{CB77544E-8929-37BB-B618-3978421B885A}' : AuthorizationDecisionItem,
	'{8977B4BE-3893-3D2D-8BCA-3B4120278FE3}' : _SIOptionCustomData,
	'{035BB123-A169-3E54-84A2-35F3A2E4521B}' : SIOptionCustomData,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{7FB3D82F-C33F-4919-AF8B-5AE805445CA5}' : 'ISIAPI',
	'{C3D8FE89-6620-45E7-898A-F4108FA95E6F}' : 'ISIAPIAnalysis',
	'{CC6E10F5-9A73-41A2-BCA8-235D7FB0091A}' : 'ISIAPIDiagnosticMsg',
	'{CBFD7927-0588-4CF2-BEB4-052B1F31A027}' : 'ISIAPIDiagnosticMsgs',
	'{8860D705-1B2F-4F1E-B59A-6C4992A3FE9A}' : 'ISIAPIGapAcceptanceSpecificApp',
	'{E741707B-9A4C-414A-A4F0-482E5F098534}' : 'ISIAPIIsland',
	'{6B55FEF0-D591-4E75-B2BA-81E22B796325}' : 'ISIAPIIslands',
	'{5F156412-3EAE-40A0-99B2-06D8E48D87D1}' : 'ISIAPILaneApproach',
	'{5C8E5D1E-E796-4190-8965-8BBD365D0D7F}' : 'ISIAPILaneApproachMovement',
	'{92115A53-7558-433A-AC10-E109B19E83ED}' : 'ISIAPILaneApproachMovementMC',
	'{E94C2A89-6DE0-4AE6-82E9-48DD3B752E1A}' : 'ISIAPILaneApproachMovementMCs',
	'{881029ED-4A7E-4469-A782-F48BF5E0F373}' : 'ISIAPILaneApproachMovements',
	'{148779D1-5A0D-48B1-9CBB-7002DAB05D95}' : 'ISIAPILaneApproachs',
	'{FE1B8A3D-ECC2-4B36-876E-FDB052503918}' : 'ISIAPILaneExit',
	'{9702C419-60FE-48C2-8412-23B83BF5C78C}' : 'ISIAPILaneExitMergeParam',
	'{99F74111-A47C-45B1-94DE-16E6F4194A60}' : 'ISIAPILaneExits',
	'{6DC82697-7A67-4BB3-8DA8-3F51C1D71135}' : 'ISIAPILaneMovement',
	'{D1EA4B6C-DC27-44B5-B0BE-233F53D81B6C}' : 'ISIAPILaneMovementMC',
	'{D8D650BB-D92A-4A21-9F34-F76F1C225497}' : 'ISIAPILaneMovementMCs',
	'{C1711C63-BCCC-41F6-94CC-80BFBF951D74}' : 'ISIAPILaneMovements',
	'{6BE9B7D6-A12E-4CB5-A938-08260963BE84}' : 'ISIAPILaneSegment',
	'{52442B71-F816-4AA6-9A01-9F66957C3925}' : 'ISIAPILaneSegmentMC',
	'{4962E57C-6B9E-4331-94DB-F141DA807485}' : 'ISIAPILaneSegmentMCs',
	'{24A8E5D9-0016-45F2-9941-12E58EE54A05}' : 'ISIAPILeg',
	'{D7F45026-862A-432F-BC67-E0557FED8203}' : 'ISIAPILegs',
	'{25BFA806-8BFC-4ADF-9A0B-9DA47FE86246}' : 'ISIAPILeg_roundabout',
	'{13F6A490-E35F-4AF3-9FCE-843062E81CCD}' : 'ISIAPILeg_rou_hcm',
	'{BD507F2C-6D0F-4256-8E40-79299F021130}' : 'ISIAPILeg_rou_hcm6_extended',
	'{DB0EFBA0-673A-4E4B-B359-ED0CAFA0643F}' : 'ISIAPIModelSetting',
	'{69AB3019-BCEB-413C-90C3-09A8DA0144DD}' : 'ISIAPIMovementClass',
	'{39B087B7-EB2C-4B47-8923-F8DD4238C771}' : 'ISIAPIMovementClasses',
	'{94958D62-C2A0-40CD-A631-894BD1A1BC00}' : 'ISIAPIMovementClassFuelEmission',
	'{BF9EA147-CE73-49C5-A6DB-7FAA6DFC663E}' : 'ISIAPIMovementClassFuelEmissions',
	'{86D55C22-E6CE-4FF9-89A9-F53001A61501}' : 'ISIAPIMovementClassMergeParam',
	'{0099AEAC-F9B6-4DCE-9C0E-1434E9D603D7}' : 'ISIAPIMovement_ped',
	'{DE5491F4-C24E-4505-A74A-DC4E93712375}' : 'ISIAPIMovement_peds',
	'{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}' : 'ISIAPIMovement_vehicle_od',
	'{87B16289-A709-4781-ADA1-92C6D1F3EB3D}' : 'ISIAPIMovement_vehicle_ods',
	'{55D25294-3468-41D8-96A1-B5B6E06AFF99}' : 'ISIAPIMovement_vehicle_od_mc',
	'{69A455C4-0A3C-4A69-8A20-DFC672995EDC}' : 'ISIAPIMovement_vehicle_od_mcs',
	'{C5A62A3D-7D9C-4544-8547-499D4C770332}' : 'ISIAPINetwork',
	'{6635581E-7C13-461E-9917-85B7CA3F7B07}' : 'ISIAPINetworkCCG',
	'{110BF49A-6953-499B-9648-8C1EFDA2B4CC}' : 'ISIAPINetworkCCGPhase',
	'{A2B9F260-C553-40A5-99CB-16F98407645F}' : 'ISIAPINetworkCCGPhases',
	'{AFE37B56-E6C5-4F98-8853-6FFF575C25BC}' : 'ISIAPINetworkCCGs',
	'{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}' : 'ISIAPINetworkCCGSequence',
	'{833D5364-D498-47D7-BE84-44624D8D16B5}' : 'ISIAPINetworkCCGSequences',
	'{B8795F7C-B342-4E4D-9F88-398D704B4453}' : 'ISIAPINetworkDemandSensitivity',
	'{18533800-8D94-4C98-8BF7-59DC4E51C2DF}' : 'ISIAPINetworkFolder',
	'{12AD1FBE-8A7B-4CB9-9DD5-F233FC8FC13C}' : 'ISIAPINetworkFolders',
	'{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}' : 'ISIAPINetworkLegConnection',
	'{F29A35EA-9B6B-46B7-839B-EC921C94A479}' : 'ISIAPINetworkLegConnections',
	'{213E3AC6-7026-49A5-A65E-B5E2CE167E8D}' : 'ISIAPINetworkMC',
	'{EA51880D-3150-4EF5-B203-17CC4EAC2214}' : 'ISIAPINetworkMCs',
	'{98CE5F37-494C-484F-B8F5-50993C839B3B}' : 'ISIAPINetworks',
	'{4888B50C-984E-4865-B2CE-4FA9B66C2622}' : 'ISIAPINetworkSite',
	'{8B19120E-37DE-43E9-AB2F-9F1743650053}' : 'ISIAPINetworkSites',
	'{1602B72A-4010-4F67-B45D-5C8A493BC687}' : 'ISIAPIOpposingmovement_ped',
	'{580C5233-F043-4662-8C1D-2E0C31C568B9}' : 'ISIAPIOpposingmovement_peds',
	'{CDC74ADC-2CF3-49D5-8DC5-3821AC96AA91}' : 'ISIAPIOpposingmovement_vehicle',
	'{677C1F98-D3D5-40B3-A5E5-5AEBD3A33CCC}' : 'ISIAPIOpposingmovement_vehicles',
	'{91779742-CF41-42AD-963E-22F788CA96F4}' : 'ISIAPIOutputAnalysis',
	'{7F03E897-A19D-41C6-A6EA-FECCF36A3358}' : 'ISIAPIOutputCirculatingLane',
	'{FA80BAB6-860C-4FA9-841D-3ECB6EA78605}' : 'ISIAPIOutputCirculatingLaneMC',
	'{E3D1A42E-AA21-4472-B566-8EAE73EAB615}' : 'ISIAPIOutputCirculatingLaneMCs',
	'{0FC1F22D-8C53-40A4-B9AB-B8B9D664B8EE}' : 'ISIAPIOutputCirculatingLanes',
	'{E69891AB-798F-4534-9C25-8BCD74AF811A}' : 'ISIAPIOutputGraphTuple',
	'{3E26EBE1-0955-49EB-8E9F-8CC3B645361B}' : 'ISIAPIOutputGraphTuples',
	'{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}' : 'ISIAPIOutputLane',
	'{00351D05-37F3-4949-BC7C-186B4F6231E7}' : 'ISIAPIOutputLaneExit',
	'{91DFAD2B-DD5C-40FE-B5DB-B4C40175952C}' : 'ISIAPIOutputLaneExits',
	'{2A8E738C-3173-41EB-A45C-AEDD77B5D649}' : 'ISIAPIOutputLaneGreenPeriod',
	'{472D3454-925A-442D-8498-E4A01EF86C20}' : 'ISIAPIOutputLaneGreenPeriods',
	'{96DB0ABD-FA20-4F9D-B2C8-4441009B4B88}' : 'ISIAPIOutputLaneMC',
	'{A04D1E92-C344-4E0E-850A-1B97D38BD7B8}' : 'ISIAPIOutputLaneMCs',
	'{BD4E1996-A933-4CEA-A1FD-9B0C7B81E9F3}' : 'ISIAPIOutputLaneOD',
	'{BD6E29F3-4E14-4A9C-AA40-65954AB6BE78}' : 'ISIAPIOutputLaneODMC',
	'{8B1F140D-9817-413B-9AE1-7BF9777B4EB8}' : 'ISIAPIOutputLaneODMCs',
	'{83C46DBA-91A4-4A1F-9EC4-7ECEB223C6DA}' : 'ISIAPIOutputLaneODs',
	'{376D0161-59D0-4F0E-911E-A7DD6774983E}' : 'ISIAPIOutputLanes',
	'{4D03B4B2-FBC7-4EC5-B7D8-984398036302}' : 'ISIAPIOutputLeg',
	'{2E9D2343-958B-4C06-9CD9-C004A4B481ED}' : 'ISIAPIOutputLegMC',
	'{C2BFE7C1-8AED-441A-AA66-B016245FC854}' : 'ISIAPIOutputLegMCs',
	'{F402DAA3-8B5C-47C7-BAB5-F124A4A16AC7}' : 'ISIAPIOutputLegPerson',
	'{D31B97D0-0C54-45B5-9529-1DFF92F8B457}' : 'ISIAPIOutputLegPersons',
	'{7A84E80F-58FD-4C53-94B3-29713CCED51C}' : 'ISIAPIOutputLegs',
	'{B11203CA-CABF-43DF-9156-6898CA85836F}' : 'ISIAPIOutputMeteredRoundabout',
	'{C0173099-4351-4B91-8AD7-82B5C047FAC2}' : 'ISIAPIOutputMovementPed',
	'{3C02979B-5CC8-41CC-86DC-1884428878F1}' : 'ISIAPIOutputMovementPeds',
	'{D572C46E-740A-4488-BD94-1D2C1111C61F}' : 'ISIAPIOutputMovementPed_GreenPeriod',
	'{48C726FD-2FE1-44AA-8265-A5CE3B84B7D5}' : 'ISIAPIOutputMovementPed_GreenPeriods',
	'{D26606A5-98D6-468D-9B07-D9B3FD9B0321}' : 'ISIAPIOutputMovementPersonOD',
	'{3B5F488E-D133-4697-85E3-05ACAA1915E9}' : 'ISIAPIOutputMovementPersonODMC',
	'{607669B1-C03B-4159-B296-B084B2451BD2}' : 'ISIAPIOutputMovementPersonODMCs',
	'{C1ADE01E-D8D6-44AD-8FB2-18158BD070F1}' : 'ISIAPIOutputMovementPersonODs',
	'{28749A62-EAF4-4575-BAB2-196A61EA612C}' : 'ISIAPIOutputMovementVehicleOD',
	'{986170AC-21B5-40BE-B9FF-F0A3C2CDB6D1}' : 'ISIAPIOutputMovementVehicleODMC',
	'{0059BCEB-1475-43CB-A08D-E392F389F5DB}' : 'ISIAPIOutputMovementVehicleODMCs',
	'{D1B3E73C-50AF-4E33-83C7-DD0500022669}' : 'ISIAPIOutputMovementVehicleODMC_GreenPeriod',
	'{09DD6321-DDCF-4DA8-9DC6-099B915C5177}' : 'ISIAPIOutputMovementVehicleODMC_GreenPeriods',
	'{F7CF3309-E6B6-4637-93F1-DC805C88F46A}' : 'ISIAPIOutputMovementVehicleODs',
	'{CD988BB1-BF23-45C3-B098-74FABCE0BDF2}' : 'ISIAPIOutputMultiSequenceAnalyses',
	'{6637A5AE-862D-4DB2-A89C-6368E9239E45}' : 'ISIAPIOutputMultiSequenceAnalysis',
	'{5E551751-0DA8-4E10-931A-D474F6FFBB27}' : 'ISIAPIOutputNetwork',
	'{7B8EEE90-6CE2-465A-9022-FF17F8CC2BB4}' : 'ISIAPIOutputNetworkGraphTuple',
	'{CCE4D1AD-5F36-4DDD-94AB-6EF78A022E9B}' : 'ISIAPIOutputNetworkGraphTuples',
	'{A690DFE7-BEC8-47B7-A8A0-1176FE2EB02B}' : 'ISIAPIOutputNetworkPedestrian',
	'{DD7EC03C-ADB7-402E-973A-CC61673F18E3}' : 'ISIAPIOutputNetworkPerson',
	'{F5FAAD8A-BEAF-4C23-8ED9-4B22D4A45051}' : 'ISIAPIOutputNetworkVehicle',
	'{C186E5B6-87B7-4CBA-8D26-7190FC0709F1}' : 'ISIAPIOutputPhase',
	'{9454248A-D758-4959-98F8-AF6162DF5ACD}' : 'ISIAPIOutputPhaseMovTimingPath',
	'{68493C00-16A9-4DDA-891E-386354D4D43C}' : 'ISIAPIOutputPhaseMovTimingPathMovement',
	'{136F8B85-9B4F-40DF-8014-2D01E74B6BD4}' : 'ISIAPIOutputPhaseMovTimingPathMovements',
	'{5D48995D-44C9-40DE-A5EC-9460D1F8417C}' : 'ISIAPIOutputPhaseMovTimingPaths',
	'{3D49DB13-5D95-4180-BFDE-49B38D78781F}' : 'ISIAPIOutputPhases',
	'{3C6C4EF3-04CC-4AD7-A16B-6643D85352C8}' : 'ISIAPIOutputRouteMovementBasedPerson',
	'{7FE4BECE-3C4E-4607-8CCA-C099AEE0F8B9}' : 'ISIAPIOutputRouteMovementBasedVehicle',
	'{8832ED63-ACD1-45C0-B218-786FDF3B3E5C}' : 'ISIAPIOutputSequence',
	'{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}' : 'ISIAPIOutputset',
	'{5E3241AA-696A-4DAF-BDCA-C6C9AA13E0EB}' : 'ISIAPIOutputSitePedestrian',
	'{53819F2B-01AB-464E-B46A-1DF4F967E8B7}' : 'ISIAPIOutputSitePerson',
	'{E60C8BBE-4044-4AF0-900F-0840C61D77F7}' : 'ISIAPIOutputSiteRoute',
	'{A30A36F9-FA16-4D54-9338-1357D2FF0D24}' : 'ISIAPIOutputSiteRoutes',
	'{EB43DD42-CCFE-4728-A81E-0246C4344B2F}' : 'ISIAPIOutputSiteVehicle',
	'{E772441A-2D95-4E27-B1D0-88BB8B995EAD}' : 'ISIAPIPhase',
	'{77A6AC80-AF80-4EED-9493-561C3B928907}' : 'ISIAPIPhasemovement_ped',
	'{8F802394-B3B4-4D06-8EA2-A0247C600A86}' : 'ISIAPIPhasemovement_peds',
	'{96854CD8-BA75-4EB1-8320-7DCC929C2503}' : 'ISIAPIPhasemovement_vehicle',
	'{843F1163-A090-4AA1-9AB4-8CF90C0A8BFF}' : 'ISIAPIPhasemovement_vehicles',
	'{98B4AB9E-189E-4149-BFE9-0DD10CA8BBEF}' : 'ISIAPIPhases',
	'{5817180B-2283-40FB-8068-C2F2D656EF04}' : 'ISIAPIProject',
	'{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}' : 'ISIAPIRoute',
	'{74F4BB54-522D-4628-B31B-1A74786A6487}' : 'ISIAPIRouteMC',
	'{BBE52DD6-5D32-4984-A42B-E5F24F27EF13}' : 'ISIAPIRouteMCs',
	'{58C442E7-0E64-47B5-AFFA-99BABCE5435E}' : 'ISIAPIRouteNwSite',
	'{8FF9FA61-FA15-4F9C-95E4-3F02656F6F14}' : 'ISIAPIRouteNwSites',
	'{DE44AC02-4804-4587-87BB-AC8E0ED05EEB}' : 'ISIAPIRoutes',
	'{D025138A-4F4C-4613-8FA7-D1FD5550A50C}' : 'ISIAPISensitivity',
	'{B528481B-1627-4D64-9F55-5D7E943539A6}' : 'ISIAPISequence',
	'{838EB6A8-198A-4409-B1A5-0267857AD7F1}' : 'ISIAPISequences',
	'{4BD64E91-A354-4A38-AA9E-E581F8D302CC}' : 'ISIAPISite',
	'{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}' : 'ISIAPISiteFolder',
	'{9712E108-061B-4BB9-AC11-8ADECF24EA13}' : 'ISIAPISiteFolders',
	'{8938DB91-E714-4703-8C7D-18B0DD89A19C}' : 'ISIAPISites',
	'{06229DBD-9E71-4D04-A6DA-B7B0524A7302}' : 'ISIAPITwoWaySignControlAdjGeometryControl',
	'{89002DC5-ADA3-4304-B64C-1A38C0D522A3}' : 'ISIAPITwoWaySignControlAdjGeometryControls',
	'{77FFB02C-F596-4F32-907B-D5CF292B0686}' : 'ISIAPITwoWaySignControlAdjMajorNumLane',
	'{546F1C93-6CF2-44A4-B963-E18FBA6A7A61}' : 'ISIAPITwoWaySignControlAdjMajorNumLanes',
	'{65074F7F-63C0-304E-AF0A-D51741CB4A8D}' : '_Object',
	'{805D7A98-D4AF-3F0F-967F-E5CF45312D2C}' : 'IDisposable',
	'{496B0ABE-CDEE-11D3-88E8-00902754C43A}' : 'IEnumerable',
	'{C3A9F3D6-00FB-3F9D-81C4-0D629824F518}' : '_AuthorizationDecisionItem',
	'{8977B4BE-3893-3D2D-8BCA-3B4120278FE3}' : '_SIOptionCustomData',
}


NamesToIIDMap = {
	'ISIAPI' : '{7FB3D82F-C33F-4919-AF8B-5AE805445CA5}',
	'ISIAPIAnalysis' : '{C3D8FE89-6620-45E7-898A-F4108FA95E6F}',
	'ISIAPIDiagnosticMsg' : '{CC6E10F5-9A73-41A2-BCA8-235D7FB0091A}',
	'ISIAPIDiagnosticMsgs' : '{CBFD7927-0588-4CF2-BEB4-052B1F31A027}',
	'ISIAPIGapAcceptanceSpecificApp' : '{8860D705-1B2F-4F1E-B59A-6C4992A3FE9A}',
	'ISIAPIIsland' : '{E741707B-9A4C-414A-A4F0-482E5F098534}',
	'ISIAPIIslands' : '{6B55FEF0-D591-4E75-B2BA-81E22B796325}',
	'ISIAPILaneApproach' : '{5F156412-3EAE-40A0-99B2-06D8E48D87D1}',
	'ISIAPILaneApproachMovement' : '{5C8E5D1E-E796-4190-8965-8BBD365D0D7F}',
	'ISIAPILaneApproachMovementMC' : '{92115A53-7558-433A-AC10-E109B19E83ED}',
	'ISIAPILaneApproachMovementMCs' : '{E94C2A89-6DE0-4AE6-82E9-48DD3B752E1A}',
	'ISIAPILaneApproachMovements' : '{881029ED-4A7E-4469-A782-F48BF5E0F373}',
	'ISIAPILaneApproachs' : '{148779D1-5A0D-48B1-9CBB-7002DAB05D95}',
	'ISIAPILaneExit' : '{FE1B8A3D-ECC2-4B36-876E-FDB052503918}',
	'ISIAPILaneExitMergeParam' : '{9702C419-60FE-48C2-8412-23B83BF5C78C}',
	'ISIAPILaneExits' : '{99F74111-A47C-45B1-94DE-16E6F4194A60}',
	'ISIAPILaneMovement' : '{6DC82697-7A67-4BB3-8DA8-3F51C1D71135}',
	'ISIAPILaneMovementMC' : '{D1EA4B6C-DC27-44B5-B0BE-233F53D81B6C}',
	'ISIAPILaneMovementMCs' : '{D8D650BB-D92A-4A21-9F34-F76F1C225497}',
	'ISIAPILaneMovements' : '{C1711C63-BCCC-41F6-94CC-80BFBF951D74}',
	'ISIAPILaneSegment' : '{6BE9B7D6-A12E-4CB5-A938-08260963BE84}',
	'ISIAPILaneSegmentMC' : '{52442B71-F816-4AA6-9A01-9F66957C3925}',
	'ISIAPILaneSegmentMCs' : '{4962E57C-6B9E-4331-94DB-F141DA807485}',
	'ISIAPILeg' : '{24A8E5D9-0016-45F2-9941-12E58EE54A05}',
	'ISIAPILegs' : '{D7F45026-862A-432F-BC67-E0557FED8203}',
	'ISIAPILeg_roundabout' : '{25BFA806-8BFC-4ADF-9A0B-9DA47FE86246}',
	'ISIAPILeg_rou_hcm' : '{13F6A490-E35F-4AF3-9FCE-843062E81CCD}',
	'ISIAPILeg_rou_hcm6_extended' : '{BD507F2C-6D0F-4256-8E40-79299F021130}',
	'ISIAPIModelSetting' : '{DB0EFBA0-673A-4E4B-B359-ED0CAFA0643F}',
	'ISIAPIMovementClass' : '{69AB3019-BCEB-413C-90C3-09A8DA0144DD}',
	'ISIAPIMovementClasses' : '{39B087B7-EB2C-4B47-8923-F8DD4238C771}',
	'ISIAPIMovementClassFuelEmission' : '{94958D62-C2A0-40CD-A631-894BD1A1BC00}',
	'ISIAPIMovementClassFuelEmissions' : '{BF9EA147-CE73-49C5-A6DB-7FAA6DFC663E}',
	'ISIAPIMovementClassMergeParam' : '{86D55C22-E6CE-4FF9-89A9-F53001A61501}',
	'ISIAPIMovement_ped' : '{0099AEAC-F9B6-4DCE-9C0E-1434E9D603D7}',
	'ISIAPIMovement_peds' : '{DE5491F4-C24E-4505-A74A-DC4E93712375}',
	'ISIAPIMovement_vehicle_od' : '{A45E3EE2-1580-47CA-9686-4EA527D3C0E3}',
	'ISIAPIMovement_vehicle_ods' : '{87B16289-A709-4781-ADA1-92C6D1F3EB3D}',
	'ISIAPIMovement_vehicle_od_mc' : '{55D25294-3468-41D8-96A1-B5B6E06AFF99}',
	'ISIAPIMovement_vehicle_od_mcs' : '{69A455C4-0A3C-4A69-8A20-DFC672995EDC}',
	'ISIAPINetwork' : '{C5A62A3D-7D9C-4544-8547-499D4C770332}',
	'ISIAPINetworkCCG' : '{6635581E-7C13-461E-9917-85B7CA3F7B07}',
	'ISIAPINetworkCCGPhase' : '{110BF49A-6953-499B-9648-8C1EFDA2B4CC}',
	'ISIAPINetworkCCGPhases' : '{A2B9F260-C553-40A5-99CB-16F98407645F}',
	'ISIAPINetworkCCGs' : '{AFE37B56-E6C5-4F98-8853-6FFF575C25BC}',
	'ISIAPINetworkCCGSequence' : '{8868F8C2-1348-42AB-9FEF-6E327C85BDBA}',
	'ISIAPINetworkCCGSequences' : '{833D5364-D498-47D7-BE84-44624D8D16B5}',
	'ISIAPINetworkDemandSensitivity' : '{B8795F7C-B342-4E4D-9F88-398D704B4453}',
	'ISIAPINetworkFolder' : '{18533800-8D94-4C98-8BF7-59DC4E51C2DF}',
	'ISIAPINetworkFolders' : '{12AD1FBE-8A7B-4CB9-9DD5-F233FC8FC13C}',
	'ISIAPINetworkLegConnection' : '{24CE5DAB-7C7A-43CD-8C7D-1808801BCD8A}',
	'ISIAPINetworkLegConnections' : '{F29A35EA-9B6B-46B7-839B-EC921C94A479}',
	'ISIAPINetworkMC' : '{213E3AC6-7026-49A5-A65E-B5E2CE167E8D}',
	'ISIAPINetworkMCs' : '{EA51880D-3150-4EF5-B203-17CC4EAC2214}',
	'ISIAPINetworks' : '{98CE5F37-494C-484F-B8F5-50993C839B3B}',
	'ISIAPINetworkSite' : '{4888B50C-984E-4865-B2CE-4FA9B66C2622}',
	'ISIAPINetworkSites' : '{8B19120E-37DE-43E9-AB2F-9F1743650053}',
	'ISIAPIOpposingmovement_ped' : '{1602B72A-4010-4F67-B45D-5C8A493BC687}',
	'ISIAPIOpposingmovement_peds' : '{580C5233-F043-4662-8C1D-2E0C31C568B9}',
	'ISIAPIOpposingmovement_vehicle' : '{CDC74ADC-2CF3-49D5-8DC5-3821AC96AA91}',
	'ISIAPIOpposingmovement_vehicles' : '{677C1F98-D3D5-40B3-A5E5-5AEBD3A33CCC}',
	'ISIAPIOutputAnalysis' : '{91779742-CF41-42AD-963E-22F788CA96F4}',
	'ISIAPIOutputCirculatingLane' : '{7F03E897-A19D-41C6-A6EA-FECCF36A3358}',
	'ISIAPIOutputCirculatingLaneMC' : '{FA80BAB6-860C-4FA9-841D-3ECB6EA78605}',
	'ISIAPIOutputCirculatingLaneMCs' : '{E3D1A42E-AA21-4472-B566-8EAE73EAB615}',
	'ISIAPIOutputCirculatingLanes' : '{0FC1F22D-8C53-40A4-B9AB-B8B9D664B8EE}',
	'ISIAPIOutputGraphTuple' : '{E69891AB-798F-4534-9C25-8BCD74AF811A}',
	'ISIAPIOutputGraphTuples' : '{3E26EBE1-0955-49EB-8E9F-8CC3B645361B}',
	'ISIAPIOutputLane' : '{3CBEC765-0D30-4CFD-8630-4C83C4B1874D}',
	'ISIAPIOutputLaneExit' : '{00351D05-37F3-4949-BC7C-186B4F6231E7}',
	'ISIAPIOutputLaneExits' : '{91DFAD2B-DD5C-40FE-B5DB-B4C40175952C}',
	'ISIAPIOutputLaneGreenPeriod' : '{2A8E738C-3173-41EB-A45C-AEDD77B5D649}',
	'ISIAPIOutputLaneGreenPeriods' : '{472D3454-925A-442D-8498-E4A01EF86C20}',
	'ISIAPIOutputLaneMC' : '{96DB0ABD-FA20-4F9D-B2C8-4441009B4B88}',
	'ISIAPIOutputLaneMCs' : '{A04D1E92-C344-4E0E-850A-1B97D38BD7B8}',
	'ISIAPIOutputLaneOD' : '{BD4E1996-A933-4CEA-A1FD-9B0C7B81E9F3}',
	'ISIAPIOutputLaneODMC' : '{BD6E29F3-4E14-4A9C-AA40-65954AB6BE78}',
	'ISIAPIOutputLaneODMCs' : '{8B1F140D-9817-413B-9AE1-7BF9777B4EB8}',
	'ISIAPIOutputLaneODs' : '{83C46DBA-91A4-4A1F-9EC4-7ECEB223C6DA}',
	'ISIAPIOutputLanes' : '{376D0161-59D0-4F0E-911E-A7DD6774983E}',
	'ISIAPIOutputLeg' : '{4D03B4B2-FBC7-4EC5-B7D8-984398036302}',
	'ISIAPIOutputLegMC' : '{2E9D2343-958B-4C06-9CD9-C004A4B481ED}',
	'ISIAPIOutputLegMCs' : '{C2BFE7C1-8AED-441A-AA66-B016245FC854}',
	'ISIAPIOutputLegPerson' : '{F402DAA3-8B5C-47C7-BAB5-F124A4A16AC7}',
	'ISIAPIOutputLegPersons' : '{D31B97D0-0C54-45B5-9529-1DFF92F8B457}',
	'ISIAPIOutputLegs' : '{7A84E80F-58FD-4C53-94B3-29713CCED51C}',
	'ISIAPIOutputMeteredRoundabout' : '{B11203CA-CABF-43DF-9156-6898CA85836F}',
	'ISIAPIOutputMovementPed' : '{C0173099-4351-4B91-8AD7-82B5C047FAC2}',
	'ISIAPIOutputMovementPeds' : '{3C02979B-5CC8-41CC-86DC-1884428878F1}',
	'ISIAPIOutputMovementPed_GreenPeriod' : '{D572C46E-740A-4488-BD94-1D2C1111C61F}',
	'ISIAPIOutputMovementPed_GreenPeriods' : '{48C726FD-2FE1-44AA-8265-A5CE3B84B7D5}',
	'ISIAPIOutputMovementPersonOD' : '{D26606A5-98D6-468D-9B07-D9B3FD9B0321}',
	'ISIAPIOutputMovementPersonODMC' : '{3B5F488E-D133-4697-85E3-05ACAA1915E9}',
	'ISIAPIOutputMovementPersonODMCs' : '{607669B1-C03B-4159-B296-B084B2451BD2}',
	'ISIAPIOutputMovementPersonODs' : '{C1ADE01E-D8D6-44AD-8FB2-18158BD070F1}',
	'ISIAPIOutputMovementVehicleOD' : '{28749A62-EAF4-4575-BAB2-196A61EA612C}',
	'ISIAPIOutputMovementVehicleODMC' : '{986170AC-21B5-40BE-B9FF-F0A3C2CDB6D1}',
	'ISIAPIOutputMovementVehicleODMCs' : '{0059BCEB-1475-43CB-A08D-E392F389F5DB}',
	'ISIAPIOutputMovementVehicleODMC_GreenPeriod' : '{D1B3E73C-50AF-4E33-83C7-DD0500022669}',
	'ISIAPIOutputMovementVehicleODMC_GreenPeriods' : '{09DD6321-DDCF-4DA8-9DC6-099B915C5177}',
	'ISIAPIOutputMovementVehicleODs' : '{F7CF3309-E6B6-4637-93F1-DC805C88F46A}',
	'ISIAPIOutputMultiSequenceAnalyses' : '{CD988BB1-BF23-45C3-B098-74FABCE0BDF2}',
	'ISIAPIOutputMultiSequenceAnalysis' : '{6637A5AE-862D-4DB2-A89C-6368E9239E45}',
	'ISIAPIOutputNetwork' : '{5E551751-0DA8-4E10-931A-D474F6FFBB27}',
	'ISIAPIOutputNetworkGraphTuple' : '{7B8EEE90-6CE2-465A-9022-FF17F8CC2BB4}',
	'ISIAPIOutputNetworkGraphTuples' : '{CCE4D1AD-5F36-4DDD-94AB-6EF78A022E9B}',
	'ISIAPIOutputNetworkPedestrian' : '{A690DFE7-BEC8-47B7-A8A0-1176FE2EB02B}',
	'ISIAPIOutputNetworkPerson' : '{DD7EC03C-ADB7-402E-973A-CC61673F18E3}',
	'ISIAPIOutputNetworkVehicle' : '{F5FAAD8A-BEAF-4C23-8ED9-4B22D4A45051}',
	'ISIAPIOutputPhase' : '{C186E5B6-87B7-4CBA-8D26-7190FC0709F1}',
	'ISIAPIOutputPhaseMovTimingPath' : '{9454248A-D758-4959-98F8-AF6162DF5ACD}',
	'ISIAPIOutputPhaseMovTimingPathMovement' : '{68493C00-16A9-4DDA-891E-386354D4D43C}',
	'ISIAPIOutputPhaseMovTimingPathMovements' : '{136F8B85-9B4F-40DF-8014-2D01E74B6BD4}',
	'ISIAPIOutputPhaseMovTimingPaths' : '{5D48995D-44C9-40DE-A5EC-9460D1F8417C}',
	'ISIAPIOutputPhases' : '{3D49DB13-5D95-4180-BFDE-49B38D78781F}',
	'ISIAPIOutputRouteMovementBasedPerson' : '{3C6C4EF3-04CC-4AD7-A16B-6643D85352C8}',
	'ISIAPIOutputRouteMovementBasedVehicle' : '{7FE4BECE-3C4E-4607-8CCA-C099AEE0F8B9}',
	'ISIAPIOutputSequence' : '{8832ED63-ACD1-45C0-B218-786FDF3B3E5C}',
	'ISIAPIOutputset' : '{4F204C5E-93A0-4090-B6EF-F370FD3E5E54}',
	'ISIAPIOutputSitePedestrian' : '{5E3241AA-696A-4DAF-BDCA-C6C9AA13E0EB}',
	'ISIAPIOutputSitePerson' : '{53819F2B-01AB-464E-B46A-1DF4F967E8B7}',
	'ISIAPIOutputSiteRoute' : '{E60C8BBE-4044-4AF0-900F-0840C61D77F7}',
	'ISIAPIOutputSiteRoutes' : '{A30A36F9-FA16-4D54-9338-1357D2FF0D24}',
	'ISIAPIOutputSiteVehicle' : '{EB43DD42-CCFE-4728-A81E-0246C4344B2F}',
	'ISIAPIPhase' : '{E772441A-2D95-4E27-B1D0-88BB8B995EAD}',
	'ISIAPIPhasemovement_ped' : '{77A6AC80-AF80-4EED-9493-561C3B928907}',
	'ISIAPIPhasemovement_peds' : '{8F802394-B3B4-4D06-8EA2-A0247C600A86}',
	'ISIAPIPhasemovement_vehicle' : '{96854CD8-BA75-4EB1-8320-7DCC929C2503}',
	'ISIAPIPhasemovement_vehicles' : '{843F1163-A090-4AA1-9AB4-8CF90C0A8BFF}',
	'ISIAPIPhases' : '{98B4AB9E-189E-4149-BFE9-0DD10CA8BBEF}',
	'ISIAPIProject' : '{5817180B-2283-40FB-8068-C2F2D656EF04}',
	'ISIAPIRoute' : '{48B4C497-EDE8-4B3E-8E5D-5DDA34867D00}',
	'ISIAPIRouteMC' : '{74F4BB54-522D-4628-B31B-1A74786A6487}',
	'ISIAPIRouteMCs' : '{BBE52DD6-5D32-4984-A42B-E5F24F27EF13}',
	'ISIAPIRouteNwSite' : '{58C442E7-0E64-47B5-AFFA-99BABCE5435E}',
	'ISIAPIRouteNwSites' : '{8FF9FA61-FA15-4F9C-95E4-3F02656F6F14}',
	'ISIAPIRoutes' : '{DE44AC02-4804-4587-87BB-AC8E0ED05EEB}',
	'ISIAPISensitivity' : '{D025138A-4F4C-4613-8FA7-D1FD5550A50C}',
	'ISIAPISequence' : '{B528481B-1627-4D64-9F55-5D7E943539A6}',
	'ISIAPISequences' : '{838EB6A8-198A-4409-B1A5-0267857AD7F1}',
	'ISIAPISite' : '{4BD64E91-A354-4A38-AA9E-E581F8D302CC}',
	'ISIAPISiteFolder' : '{AC330FFE-2598-4EEA-8CAA-46F34FEE401E}',
	'ISIAPISiteFolders' : '{9712E108-061B-4BB9-AC11-8ADECF24EA13}',
	'ISIAPISites' : '{8938DB91-E714-4703-8C7D-18B0DD89A19C}',
	'ISIAPITwoWaySignControlAdjGeometryControl' : '{06229DBD-9E71-4D04-A6DA-B7B0524A7302}',
	'ISIAPITwoWaySignControlAdjGeometryControls' : '{89002DC5-ADA3-4304-B64C-1A38C0D522A3}',
	'ISIAPITwoWaySignControlAdjMajorNumLane' : '{77FFB02C-F596-4F32-907B-D5CF292B0686}',
	'ISIAPITwoWaySignControlAdjMajorNumLanes' : '{546F1C93-6CF2-44A4-B963-E18FBA6A7A61}',
	'_Object' : '{65074F7F-63C0-304E-AF0A-D51741CB4A8D}',
	'IDisposable' : '{805D7A98-D4AF-3F0F-967F-E5CF45312D2C}',
	'IEnumerable' : '{496B0ABE-CDEE-11D3-88E8-00902754C43A}',
	'_AuthorizationDecisionItem' : '{C3A9F3D6-00FB-3F9D-81C4-0D629824F518}',
	'_SIOptionCustomData' : '{8977B4BE-3893-3D2D-8BCA-3B4120278FE3}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

