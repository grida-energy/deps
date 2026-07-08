# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [deps/preset/bess/model.v1.proto](#deps_preset_bess_model-v1-proto)
    - [Bess](#deps-preset-bess-v1-Bess)
    - [BessCommand](#deps-preset-bess-v1-BessCommand)
    - [Rpc](#deps-preset-bess-v1-Rpc)
    - [Rpc.CommandRequest](#deps-preset-bess-v1-Rpc-CommandRequest)
    - [Rpc.CommandResponse](#deps-preset-bess-v1-Rpc-CommandResponse)
    - [Rpc.MeasureResponse](#deps-preset-bess-v1-Rpc-MeasureResponse)
  
- [deps/preset/station-cast/model.v1.proto](#deps_preset_station-cast_model-v1-proto)
    - [CastSet](#deps-preset-station_cast-v1-CastSet)
    - [Rpc](#deps-preset-station_cast-v1-Rpc)
    - [Rpc.CastMeasure](#deps-preset-station_cast-v1-Rpc-CastMeasure)
    - [StationCastPreset](#deps-preset-station_cast-v1-StationCastPreset)
    - [StationCastPreset.GroupEntry](#deps-preset-station_cast-v1-StationCastPreset-GroupEntry)
  
- [deps/preset/dbserver/model.v1.proto](#deps_preset_dbserver_model-v1-proto)
    - [Answer](#deps-preset-dbserver-v1-Answer)
    - [Answer.Log](#deps-preset-dbserver-v1-Answer-Log)
    - [Answer.Measure](#deps-preset-dbserver-v1-Answer-Measure)
    - [Answer.MeasureInfo](#deps-preset-dbserver-v1-Answer-MeasureInfo)
    - [Answer.MeasureMeta](#deps-preset-dbserver-v1-Answer-MeasureMeta)
    - [Query](#deps-preset-dbserver-v1-Query)
    - [Query.MeasureInfo](#deps-preset-dbserver-v1-Query-MeasureInfo)
    - [Rpc](#deps-preset-dbserver-v1-Rpc)
    - [Rpc.PullLogRequest](#deps-preset-dbserver-v1-Rpc-PullLogRequest)
    - [Rpc.PullLogResponse](#deps-preset-dbserver-v1-Rpc-PullLogResponse)
    - [Rpc.PullMeasureRequest](#deps-preset-dbserver-v1-Rpc-PullMeasureRequest)
    - [Rpc.PullMeasureResponse](#deps-preset-dbserver-v1-Rpc-PullMeasureResponse)
    - [Rpc.QueryRequest](#deps-preset-dbserver-v1-Rpc-QueryRequest)
    - [Rpc.QueryResponse](#deps-preset-dbserver-v1-Rpc-QueryResponse)
  
- [deps/preset/upms/model.v1.proto](#deps_preset_upms_model-v1-proto)
    - [PmsCommand](#deps-preset-upms-v1-PmsCommand)
    - [Rpc](#deps-preset-upms-v1-Rpc)
    - [Rpc.CommandRequest](#deps-preset-upms-v1-Rpc-CommandRequest)
    - [Rpc.CommandResponse](#deps-preset-upms-v1-Rpc-CommandResponse)
    - [Rpc.MeasureResponse](#deps-preset-upms-v1-Rpc-MeasureResponse)
  
- [deps/vnd/rpc.v1.proto](#deps_vnd_rpc-v1-proto)
    - [Rpc](#deps-vnd-v1-Rpc)
    - [Rpc.AlarmResponse](#deps-vnd-v1-Rpc-AlarmResponse)
    - [Rpc.ParamReadWriteRequest](#deps-vnd-v1-Rpc-ParamReadWriteRequest)
    - [Rpc.ParamReadWriteResponse](#deps-vnd-v1-Rpc-ParamReadWriteResponse)
    - [Rpc.ParamRequest](#deps-vnd-v1-Rpc-ParamRequest)
    - [Rpc.ParamResponse](#deps-vnd-v1-Rpc-ParamResponse)
  
- [deps/vnd/parameter.v1.proto](#deps_vnd_parameter-v1-proto)
    - [ParamBlock](#deps-vnd-v1-ParamBlock)
    - [ParamIdRange](#deps-vnd-v1-ParamIdRange)
    - [ParamInfo](#deps-vnd-v1-ParamInfo)
    - [ParamInfo.MinMax](#deps-vnd-v1-ParamInfo-MinMax)
    - [ParamInfo.OneOfPick](#deps-vnd-v1-ParamInfo-OneOfPick)
    - [ParamInfo.OneOfPick.OptionsEntry](#deps-vnd-v1-ParamInfo-OneOfPick-OptionsEntry)
    - [ParamMeta](#deps-vnd-v1-ParamMeta)
    - [ParamMeta.ParamInfosEntry](#deps-vnd-v1-ParamMeta-ParamInfosEntry)
  
    - [ParamInfo.ParamKind](#deps-vnd-v1-ParamInfo-ParamKind)
  
- [deps/vnd/alarm.v1.proto](#deps_vnd_alarm-v1-proto)
    - [AlarmData](#deps-vnd-v1-AlarmData)
    - [AlarmMeta](#deps-vnd-v1-AlarmMeta)
    - [AlarmMeta.FaultEntry](#deps-vnd-v1-AlarmMeta-FaultEntry)
    - [AlarmMeta.StatusEntry](#deps-vnd-v1-AlarmMeta-StatusEntry)
    - [AlarmMeta.WarningEntry](#deps-vnd-v1-AlarmMeta-WarningEntry)
  
    - [AlarmType](#deps-vnd-v1-AlarmType)
  
- [deps/model/ems/model.v1.proto](#deps_model_ems_model-v1-proto)
- [deps/model/pcs/model.v1.proto](#deps_model_pcs_model-v1-proto)
    - [DcDcConverter](#deps-model-pcs-v1-DcDcConverter)
    - [DcDcConverter.Command](#deps-model-pcs-v1-DcDcConverter-Command)
    - [DcDcConverter.Fault](#deps-model-pcs-v1-DcDcConverter-Fault)
    - [DcDcConverter.Status](#deps-model-pcs-v1-DcDcConverter-Status)
    - [DcDcConverter.Warning](#deps-model-pcs-v1-DcDcConverter-Warning)
    - [DcPart](#deps-model-pcs-v1-DcPart)
    - [Rpc](#deps-model-pcs-v1-Rpc)
    - [Rpc.DcDc](#deps-model-pcs-v1-Rpc-DcDc)
    - [Rpc.DcDc.CommandRequest](#deps-model-pcs-v1-Rpc-DcDc-CommandRequest)
    - [Rpc.DcDc.CommandResponse](#deps-model-pcs-v1-Rpc-DcDc-CommandResponse)
    - [Rpc.DcDc.MeasureResponse](#deps-model-pcs-v1-Rpc-DcDc-MeasureResponse)
    - [Rpc.Grid](#deps-model-pcs-v1-Rpc-Grid)
    - [Rpc.Grid.MeasureResponse](#deps-model-pcs-v1-Rpc-Grid-MeasureResponse)
    - [Rpc.Pcs](#deps-model-pcs-v1-Rpc-Pcs)
    - [Rpc.Pcs.CommandRequest](#deps-model-pcs-v1-Rpc-Pcs-CommandRequest)
    - [Rpc.Pcs.CommandResponse](#deps-model-pcs-v1-Rpc-Pcs-CommandResponse)
    - [Rpc.Pcs.MeasureResponse](#deps-model-pcs-v1-Rpc-Pcs-MeasureResponse)
    - [TemperaturePart](#deps-model-pcs-v1-TemperaturePart)
    - [ThreePhase](#deps-model-pcs-v1-ThreePhase)
    - [ThreePhaseGridPart](#deps-model-pcs-v1-ThreePhaseGridPart)
    - [ThreePhaseLine](#deps-model-pcs-v1-ThreePhaseLine)
    - [ThreePhaseNSum](#deps-model-pcs-v1-ThreePhaseNSum)
    - [ThreePhasePcsPart](#deps-model-pcs-v1-ThreePhasePcsPart)
    - [ThreePhasePcsPart.Command](#deps-model-pcs-v1-ThreePhasePcsPart-Command)
    - [ThreePhasePcsPart.Fault](#deps-model-pcs-v1-ThreePhasePcsPart-Fault)
    - [ThreePhasePcsPart.Status](#deps-model-pcs-v1-ThreePhasePcsPart-Status)
    - [ThreePhasePcsPart.Warning](#deps-model-pcs-v1-ThreePhasePcsPart-Warning)
  
    - [DcDcConverter.St](#deps-model-pcs-v1-DcDcConverter-St)
    - [ThreePhasePcsPart.DirPwr](#deps-model-pcs-v1-ThreePhasePcsPart-DirPwr)
    - [ThreePhasePcsPart.St](#deps-model-pcs-v1-ThreePhasePcsPart-St)
  
- [deps/model/net/model.v1.proto](#deps_model_net_model-v1-proto)
    - [AcLine](#deps-model-net-v1-AcLine)
    - [AcLineSum](#deps-model-net-v1-AcLineSum)
    - [AcLineThreePhase](#deps-model-net-v1-AcLineThreePhase)
    - [Energy](#deps-model-net-v1-Energy)
    - [Harmonics](#deps-model-net-v1-Harmonics)
    - [HarmonicsThreePhase](#deps-model-net-v1-HarmonicsThreePhase)
    - [Line](#deps-model-net-v1-Line)
    - [LineToLine](#deps-model-net-v1-LineToLine)
    - [MeterThreePhase](#deps-model-net-v1-MeterThreePhase)
    - [Phasor](#deps-model-net-v1-Phasor)
    - [Rpc](#deps-model-net-v1-Rpc)
    - [Rpc.MeterThreePhase](#deps-model-net-v1-Rpc-MeterThreePhase)
    - [Rpc.MeterThreePhase.MeasureResponse](#deps-model-net-v1-Rpc-MeterThreePhase-MeasureResponse)
  
- [deps/model/esd/model.v1.proto](#deps_model_esd_model-v1-proto)
    - [EsdBank](#deps-model-esd-v1-EsdBank)
    - [EsdBank.CellCount](#deps-model-esd-v1-EsdBank-CellCount)
    - [EsdBank.Command](#deps-model-esd-v1-EsdBank-Command)
    - [EsdBank.Fault](#deps-model-esd-v1-EsdBank-Fault)
    - [EsdBank.ModuleCount](#deps-model-esd-v1-EsdBank-ModuleCount)
    - [EsdBank.Status](#deps-model-esd-v1-EsdBank-Status)
    - [EsdBank.StringCount](#deps-model-esd-v1-EsdBank-StringCount)
    - [EsdBank.Warning](#deps-model-esd-v1-EsdBank-Warning)
    - [EsdCell](#deps-model-esd-v1-EsdCell)
    - [EsdCell.St](#deps-model-esd-v1-EsdCell-St)
    - [EsdModule](#deps-model-esd-v1-EsdModule)
    - [EsdModule.CellCount](#deps-model-esd-v1-EsdModule-CellCount)
    - [EsdString](#deps-model-esd-v1-EsdString)
    - [EsdString.CellCount](#deps-model-esd-v1-EsdString-CellCount)
    - [EsdString.Command](#deps-model-esd-v1-EsdString-Command)
    - [EsdString.Fault](#deps-model-esd-v1-EsdString-Fault)
    - [EsdString.ModuleCount](#deps-model-esd-v1-EsdString-ModuleCount)
    - [EsdString.StCon](#deps-model-esd-v1-EsdString-StCon)
    - [EsdString.Status](#deps-model-esd-v1-EsdString-Status)
    - [EsdString.Warning](#deps-model-esd-v1-EsdString-Warning)
    - [Rpc](#deps-model-esd-v1-Rpc)
    - [Rpc.Bank](#deps-model-esd-v1-Rpc-Bank)
    - [Rpc.Bank.CommandRequest](#deps-model-esd-v1-Rpc-Bank-CommandRequest)
    - [Rpc.Bank.CommandResponse](#deps-model-esd-v1-Rpc-Bank-CommandResponse)
    - [Rpc.Bank.MeasureResponse](#deps-model-esd-v1-Rpc-Bank-MeasureResponse)
  
    - [EsdBank.St](#deps-model-esd-v1-EsdBank-St)
    - [EsdBank.StCha](#deps-model-esd-v1-EsdBank-StCha)
    - [EsdString.Command.SetCon](#deps-model-esd-v1-EsdString-Command-SetCon)
    - [EsdString.Command.SetEna](#deps-model-esd-v1-EsdString-Command-SetEna)
    - [EsdString.ConFail](#deps-model-esd-v1-EsdString-ConFail)
  
- [deps/model/esd/extra.v1.proto](#deps_model_esd_extra-v1-proto)
    - [ChaLimit](#deps-model-esd-v1-ChaLimit)
    - [Conn](#deps-model-esd-v1-Conn)
  
    - [Conn.ConnCmd](#deps-model-esd-v1-Conn-ConnCmd)
  
- [deps/model/tsdb/model.v1.proto](#deps_model_tsdb_model-v1-proto)
    - [AlarmExtra](#deps-model-tsdb-v1-AlarmExtra)
    - [CommandExtra](#deps-model-tsdb-v1-CommandExtra)
    - [EventExtra](#deps-model-tsdb-v1-EventExtra)
    - [LogConstraint](#deps-model-tsdb-v1-LogConstraint)
    - [LogItem](#deps-model-tsdb-v1-LogItem)
    - [LogMatch](#deps-model-tsdb-v1-LogMatch)
    - [MeasureConstraint](#deps-model-tsdb-v1-MeasureConstraint)
    - [MeasureId](#deps-model-tsdb-v1-MeasureId)
  
    - [AlarmKind](#deps-model-tsdb-v1-AlarmKind)
    - [AlarmStatus](#deps-model-tsdb-v1-AlarmStatus)
    - [LogKind](#deps-model-tsdb-v1-LogKind)
    - [Order](#deps-model-tsdb-v1-Order)
  
- [deps/model/cast/model.v1.proto](#deps_model_cast_model-v1-proto)
    - [CastHeader](#deps-model-cast-v1-CastHeader)
    - [EnergyCast](#deps-model-cast-v1-EnergyCast)
    - [GridOperation](#deps-model-cast-v1-GridOperation)
    - [GridOutputControl](#deps-model-cast-v1-GridOutputControl)
    - [H2StationMeasure](#deps-model-cast-v1-H2StationMeasure)
    - [StationCast](#deps-model-cast-v1-StationCast)
    - [WeatherCast](#deps-model-cast-v1-WeatherCast)
    - [WindData](#deps-model-cast-v1-WindData)
  
- [deps/model/source/model.v1.proto](#deps_model_source_model-v1-proto)
    - [PvLine](#deps-model-source-v1-PvLine)
    - [PvString](#deps-model-source-v1-PvString)
  
- [deps/model/pms/model.v1.proto](#deps_model_pms_model-v1-proto)
    - [ChainFn](#deps-model-pms-v1-ChainFn)
    - [ChartFn](#deps-model-pms-v1-ChartFn)
    - [LookupComplete](#deps-model-pms-v1-LookupComplete)
    - [LookupInput](#deps-model-pms-v1-LookupInput)
    - [LookupItem](#deps-model-pms-v1-LookupItem)
    - [LookupItemAnchor](#deps-model-pms-v1-LookupItemAnchor)
    - [LookupItemAxisRange](#deps-model-pms-v1-LookupItemAxisRange)
    - [LookupOutput](#deps-model-pms-v1-LookupOutput)
    - [LookupRule](#deps-model-pms-v1-LookupRule)
    - [LookupRule.Command](#deps-model-pms-v1-LookupRule-Command)
    - [LookupRule.Command.AddRule](#deps-model-pms-v1-LookupRule-Command-AddRule)
    - [LookupRule.Command.ClearRules](#deps-model-pms-v1-LookupRule-Command-ClearRules)
    - [LookupRule.Command.DeleteRule](#deps-model-pms-v1-LookupRule-Command-DeleteRule)
    - [LookupRule.Command.EnaRule](#deps-model-pms-v1-LookupRule-Command-EnaRule)
    - [LookupRule.Command.OverwriteRules](#deps-model-pms-v1-LookupRule-Command-OverwriteRules)
    - [LookupRule.Fault](#deps-model-pms-v1-LookupRule-Fault)
    - [LookupRule.Status](#deps-model-pms-v1-LookupRule-Status)
    - [LookupRule.Warning](#deps-model-pms-v1-LookupRule-Warning)
    - [LookupSequence](#deps-model-pms-v1-LookupSequence)
    - [LookupSequenceState](#deps-model-pms-v1-LookupSequenceState)
    - [MinMax](#deps-model-pms-v1-MinMax)
    - [Point2D](#deps-model-pms-v1-Point2D)
  
    - [LookupInputType](#deps-model-pms-v1-LookupInputType)
    - [LookupOutputType](#deps-model-pms-v1-LookupOutputType)
    - [LookupRule.St](#deps-model-pms-v1-LookupRule-St)
    - [OutputBlendMode](#deps-model-pms-v1-OutputBlendMode)
  
- [deps/model/system/model.v1.proto](#deps_model_system_model-v1-proto)
    - [SystemHead](#deps-model-system-v1-SystemHead)
  
- [deps/model/nameplate/model.v1.proto](#deps_model_nameplate_model-v1-proto)
    - [Id](#deps-model-nameplate-v1-Id)
    - [NetworkConfig](#deps-model-nameplate-v1-NetworkConfig)
    - [NetworkConfig.IpsEntry](#deps-model-nameplate-v1-NetworkConfig-IpsEntry)
  
- [deps/model/rms/model.v1.proto](#deps_model_rms_model-v1-proto)
    - [DeleteNode](#deps-model-rms-v1-DeleteNode)
    - [LocalRms](#deps-model-rms-v1-LocalRms)
    - [LocalRms.Command](#deps-model-rms-v1-LocalRms-Command)
    - [MeasureRequest](#deps-model-rms-v1-MeasureRequest)
    - [NodeItem](#deps-model-rms-v1-NodeItem)
    - [NodeItem.ArgsEntry](#deps-model-rms-v1-NodeItem-ArgsEntry)
    - [Rpc](#deps-model-rms-v1-Rpc)
    - [Rpc.CommandRequest](#deps-model-rms-v1-Rpc-CommandRequest)
    - [Rpc.CommandResponse](#deps-model-rms-v1-Rpc-CommandResponse)
    - [Rpc.MeasureResponse](#deps-model-rms-v1-Rpc-MeasureResponse)
  
- [deps/rpc/header.v1.proto](#deps_rpc_header-v1-proto)
    - [Request](#deps-rpc-v1-Request)
    - [Response](#deps-rpc-v1-Response)
    - [Response.Error](#deps-rpc-v1-Response-Error)
  
    - [Response.ErrorCode](#deps-rpc-v1-Response-ErrorCode)
  
- [Scalar Value Types](#scalar-value-types)



<a name="deps_preset_bess_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/preset/bess/model.v1.proto



<a name="deps-preset-bess-v1-Bess"></a>

### Bess
배터리 &#43; 인버터로 구성된 단순 BESS 모델


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bank | [deps.model.esd.v1.EsdBank](#deps-model-esd-v1-EsdBank) |  | BESS 시스템 명령 message Command { oneof cmd { // 전체 시스템 정지 bool estop = 3; } } 배터리 모델 |
| pcs | [deps.model.pcs.v1.ThreePhasePcsPart](#deps-model-pcs-v1-ThreePhasePcsPart) |  | PCS 모델 |
| off_grid | [deps.model.pcs.v1.ThreePhaseGridPart](#deps-model-pcs-v1-ThreePhaseGridPart) |  | Off Grid (부하 연결 부) |
| on_grid | [deps.model.pcs.v1.ThreePhaseGridPart](#deps-model-pcs-v1-ThreePhaseGridPart) |  | On Grid (계통 연결 부) |
| dcdc | [deps.model.pcs.v1.DcDcConverter](#deps-model-pcs-v1-DcDcConverter) |  | DcDc 모델 (옵션) |
| pv | [deps.model.source.v1.PvLine](#deps-model-source-v1-PvLine) |  | PV 연결 부 (옵션) |






<a name="deps-preset-bess-v1-BessCommand"></a>

### BessCommand
BESS 명령


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bank | [deps.model.esd.v1.EsdBank.Command](#deps-model-esd-v1-EsdBank-Command) |  | 배터리 명령 |
| pcs | [deps.model.pcs.v1.ThreePhasePcsPart.Command](#deps-model-pcs-v1-ThreePhasePcsPart-Command) |  | PCS 명령 |
| dcdc | [deps.model.pcs.v1.DcDcConverter.Command](#deps-model-pcs-v1-DcDcConverter-Command) |  | DcDc 명령 |






<a name="deps-preset-bess-v1-Rpc"></a>

### Rpc
RPC 메시지






<a name="deps-preset-bess-v1-Rpc-CommandRequest"></a>

### Rpc.CommandRequest
BESS RPC 요청


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  | 요청 헤더 |
| payload | [BessCommand](#deps-preset-bess-v1-BessCommand) | repeated | BESS 명령 |






<a name="deps-preset-bess-v1-Rpc-CommandResponse"></a>

### Rpc.CommandResponse
BESS RPC 응답


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  | 응답 헤더 |
| payload | [uint32](#uint32) |  |  |






<a name="deps-preset-bess-v1-Rpc-MeasureResponse"></a>

### Rpc.MeasureResponse
BESS 계측 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | 타임 스탬프 |
| payload | [Bess](#deps-preset-bess-v1-Bess) |  | BESS 데이터 |





 

 

 

 



<a name="deps_preset_station-cast_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/preset/station-cast/model.v1.proto



<a name="deps-preset-station_cast-v1-CastSet"></a>

### CastSet
그룹별 수소 발전단지 데이터


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cst_stn | [deps.model.cast.v1.StationCast](#deps-model-cast-v1-StationCast) |  | 발전소 예측 정보 |
| h2 | [deps.model.cast.v1.H2StationMeasure](#deps-model-cast-v1-H2StationMeasure) |  | 수소 발전 단지 계측 값 |
| forecast | [deps.model.cast.v1.WeatherCast](#deps-model-cast-v1-WeatherCast) |  | 기상 예측 정보 |






<a name="deps-preset-station_cast-v1-Rpc"></a>

### Rpc







<a name="deps-preset-station_cast-v1-Rpc-CastMeasure"></a>

### Rpc.CastMeasure



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| data | [StationCastPreset](#deps-preset-station_cast-v1-StationCastPreset) |  |  |






<a name="deps-preset-station_cast-v1-StationCastPreset"></a>

### StationCastPreset



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group | [StationCastPreset.GroupEntry](#deps-preset-station_cast-v1-StationCastPreset-GroupEntry) | repeated | 그룹별 수소 발전단지 데이터 |
| ops_grid | [deps.model.cast.v1.GridOperation](#deps-model-cast-v1-GridOperation) |  | 계통 운영 정보 |
| ctl_grid | [deps.model.cast.v1.GridOutputControl](#deps-model-cast-v1-GridOutputControl) |  | 예측 출력 제어 데이터 |
| cst_dmnd | [deps.model.cast.v1.EnergyCast](#deps-model-cast-v1-EnergyCast) |  | 일간 수요 예측 데이터 |
| cst_re | [deps.model.cast.v1.EnergyCast](#deps-model-cast-v1-EnergyCast) |  | 일간 신재생 예측 발전 데이터 |






<a name="deps-preset-station_cast-v1-StationCastPreset-GroupEntry"></a>

### StationCastPreset.GroupEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [CastSet](#deps-preset-station_cast-v1-CastSet) |  |  |





 

 

 

 



<a name="deps_preset_dbserver_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/preset/dbserver/model.v1.proto



<a name="deps-preset-dbserver-v1-Answer"></a>

### Answer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| measure_info | [Answer.MeasureInfo](#deps-preset-dbserver-v1-Answer-MeasureInfo) |  | .deps.model.nameplate.v2.Nameplate nameplate = 1; |
| measure | [Answer.Measure](#deps-preset-dbserver-v1-Answer-Measure) |  |  |
| log | [Answer.Log](#deps-preset-dbserver-v1-Answer-Log) |  |  |






<a name="deps-preset-dbserver-v1-Answer-Log"></a>

### Answer.Log



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | [deps.model.tsdb.v1.LogItem](#deps-model-tsdb-v1-LogItem) | repeated |  |






<a name="deps-preset-dbserver-v1-Answer-Measure"></a>

### Answer.Measure



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | [google.protobuf.ListValue](#google-protobuf-ListValue) | repeated |  |






<a name="deps-preset-dbserver-v1-Answer-MeasureInfo"></a>

### Answer.MeasureInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | [Answer.MeasureMeta](#deps-preset-dbserver-v1-Answer-MeasureMeta) | repeated |  |






<a name="deps-preset-dbserver-v1-Answer-MeasureMeta"></a>

### Answer.MeasureMeta



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| nodetype | [deps.model.nameplate.v2.Wknt](#deps-model-nameplate-v2-Wknt) |  |  |
| extra_kind | [string](#string) |  |  |






<a name="deps-preset-dbserver-v1-Query"></a>

### Query



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| measure_info | [Query.MeasureInfo](#deps-preset-dbserver-v1-Query-MeasureInfo) |  | .deps.model.nameplate.v2.NameplateFilter nameplate = 1; |
| measure | [deps.model.tsdb.v1.MeasureConstraint](#deps-model-tsdb-v1-MeasureConstraint) |  |  |
| log | [deps.model.tsdb.v1.LogConstraint](#deps-model-tsdb-v1-LogConstraint) |  |  |






<a name="deps-preset-dbserver-v1-Query-MeasureInfo"></a>

### Query.MeasureInfo







<a name="deps-preset-dbserver-v1-Rpc"></a>

### Rpc







<a name="deps-preset-dbserver-v1-Rpc-PullLogRequest"></a>

### Rpc.PullLogRequest
topic: rpc/tsdb/log


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| payload | [deps.model.tsdb.v1.LogConstraint](#deps-model-tsdb-v1-LogConstraint) |  |  |






<a name="deps-preset-dbserver-v1-Rpc-PullLogResponse"></a>

### Rpc.PullLogResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| payload | [deps.model.tsdb.v1.LogItem](#deps-model-tsdb-v1-LogItem) | repeated |  |






<a name="deps-preset-dbserver-v1-Rpc-PullMeasureRequest"></a>

### Rpc.PullMeasureRequest
topic: rpc/tsdb/measure


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| payload | [deps.model.tsdb.v1.MeasureConstraint](#deps-model-tsdb-v1-MeasureConstraint) |  |  |






<a name="deps-preset-dbserver-v1-Rpc-PullMeasureResponse"></a>

### Rpc.PullMeasureResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| payload | [google.protobuf.ListValue](#google-protobuf-ListValue) | repeated |  |






<a name="deps-preset-dbserver-v1-Rpc-QueryRequest"></a>

### Rpc.QueryRequest
topic: rpc/query


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| payload | [Query](#deps-preset-dbserver-v1-Query) | repeated |  |






<a name="deps-preset-dbserver-v1-Rpc-QueryResponse"></a>

### Rpc.QueryResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| payload | [Answer](#deps-preset-dbserver-v1-Answer) | repeated |  |





 

 

 

 



<a name="deps_preset_upms_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/preset/upms/model.v1.proto



<a name="deps-preset-upms-v1-PmsCommand"></a>

### PmsCommand



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lookup | [deps.model.pms.v1.LookupRule.Command](#deps-model-pms-v1-LookupRule-Command) |  |  |






<a name="deps-preset-upms-v1-Rpc"></a>

### Rpc







<a name="deps-preset-upms-v1-Rpc-CommandRequest"></a>

### Rpc.CommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| payload | [PmsCommand](#deps-preset-upms-v1-PmsCommand) | repeated |  |






<a name="deps-preset-upms-v1-Rpc-CommandResponse"></a>

### Rpc.CommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| payload | [uint32](#uint32) |  |  |






<a name="deps-preset-upms-v1-Rpc-MeasureResponse"></a>

### Rpc.MeasureResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| lookup | [deps.model.pms.v1.LookupRule](#deps-model-pms-v1-LookupRule) |  |  |
| input | [deps.model.pms.v1.LookupInput](#deps-model-pms-v1-LookupInput) |  |  |
| output | [deps.model.pms.v1.LookupOutput](#deps-model-pms-v1-LookupOutput) |  |  |





 

 

 

 



<a name="deps_vnd_rpc-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/vnd/rpc.v1.proto



<a name="deps-vnd-v1-Rpc"></a>

### Rpc







<a name="deps-vnd-v1-Rpc-AlarmResponse"></a>

### Rpc.AlarmResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| payload | [AlarmData](#deps-vnd-v1-AlarmData) |  |  |






<a name="deps-vnd-v1-Rpc-ParamReadWriteRequest"></a>

### Rpc.ParamReadWriteRequest
&#34;writes&#34; performs first then &#34;reads&#34;


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reads | [ParamIdRange](#deps-vnd-v1-ParamIdRange) | repeated |  |
| writes | [ParamBlock](#deps-vnd-v1-ParamBlock) |  |  |






<a name="deps-vnd-v1-Rpc-ParamReadWriteResponse"></a>

### Rpc.ParamReadWriteResponse
error codes would be specified in deps.rpc.Response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reads | [ParamBlock](#deps-vnd-v1-ParamBlock) |  | returns successfully read values if possible |
| writes | [ParamIdRange](#deps-vnd-v1-ParamIdRange) | repeated | returns successfully writen ids if possible |






<a name="deps-vnd-v1-Rpc-ParamRequest"></a>

### Rpc.ParamRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| payload | [Rpc.ParamReadWriteRequest](#deps-vnd-v1-Rpc-ParamReadWriteRequest) |  |  |






<a name="deps-vnd-v1-Rpc-ParamResponse"></a>

### Rpc.ParamResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| payload | [Rpc.ParamReadWriteResponse](#deps-vnd-v1-Rpc-ParamReadWriteResponse) |  |  |





 

 

 

 



<a name="deps_vnd_parameter-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/vnd/parameter.v1.proto



<a name="deps-vnd-v1-ParamBlock"></a>

### ParamBlock



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ranges | [ParamIdRange](#deps-vnd-v1-ParamIdRange) | repeated |  |
| values | [google.protobuf.Value](#google-protobuf-Value) | repeated |  |






<a name="deps-vnd-v1-ParamIdRange"></a>

### ParamIdRange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [uint32](#uint32) |  |  |
| length | [uint32](#uint32) |  |  |






<a name="deps-vnd-v1-ParamInfo"></a>

### ParamInfo
제조사 고유 파라미터 메타 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| param_name | [string](#string) |  |  |
| description | [string](#string) |  |  |
| unit | [string](#string) |  |  |
| min_max | [ParamInfo.MinMax](#deps-vnd-v1-ParamInfo-MinMax) |  |  |
| pick | [ParamInfo.OneOfPick](#deps-vnd-v1-ParamInfo-OneOfPick) |  |  |
| schema | [google.protobuf.FileDescriptorSet](#google-protobuf-FileDescriptorSet) |  |  |
| accepts | [ParamInfo.ParamKind](#deps-vnd-v1-ParamInfo-ParamKind) | repeated |  |






<a name="deps-vnd-v1-ParamInfo-MinMax"></a>

### ParamInfo.MinMax



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min | [double](#double) |  |  |
| max | [double](#double) |  |  |
| exclusive_min | [bool](#bool) |  |  |
| exclusive_max | [bool](#bool) |  |  |






<a name="deps-vnd-v1-ParamInfo-OneOfPick"></a>

### ParamInfo.OneOfPick



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| options | [ParamInfo.OneOfPick.OptionsEntry](#deps-vnd-v1-ParamInfo-OneOfPick-OptionsEntry) | repeated |  |






<a name="deps-vnd-v1-ParamInfo-OneOfPick-OptionsEntry"></a>

### ParamInfo.OneOfPick.OptionsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [double](#double) |  |  |






<a name="deps-vnd-v1-ParamMeta"></a>

### ParamMeta



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| param_infos | [ParamMeta.ParamInfosEntry](#deps-vnd-v1-ParamMeta-ParamInfosEntry) | repeated |  |






<a name="deps-vnd-v1-ParamMeta-ParamInfosEntry"></a>

### ParamMeta.ParamInfosEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [ParamInfo](#deps-vnd-v1-ParamInfo) |  |  |





 


<a name="deps-vnd-v1-ParamInfo-ParamKind"></a>

### ParamInfo.ParamKind


| Name | Number | Description |
| ---- | ------ | ----------- |
| PARAM_KIND_NA | 0 |  |
| PARAM_KIND_NULL | 1 |  |
| PARAM_KIND_NUMBER | 2 |  |
| PARAM_KIND_STRING | 3 |  |
| PARAM_KIND_BOOL | 4 |  |
| PARAM_KIND_STRUCT | 5 |  |
| PARAM_KIND_LIST | 6 |  |


 

 

 



<a name="deps_vnd_alarm-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/vnd/alarm.v1.proto



<a name="deps-vnd-v1-AlarmData"></a>

### AlarmData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| status | [bool](#bool) | repeated |  |
| warning | [bool](#bool) | repeated |  |
| fault | [bool](#bool) | repeated |  |






<a name="deps-vnd-v1-AlarmMeta"></a>

### AlarmMeta



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| status | [AlarmMeta.StatusEntry](#deps-vnd-v1-AlarmMeta-StatusEntry) | repeated |  |
| warning | [AlarmMeta.WarningEntry](#deps-vnd-v1-AlarmMeta-WarningEntry) | repeated |  |
| fault | [AlarmMeta.FaultEntry](#deps-vnd-v1-AlarmMeta-FaultEntry) | repeated |  |






<a name="deps-vnd-v1-AlarmMeta-FaultEntry"></a>

### AlarmMeta.FaultEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [string](#string) |  |  |






<a name="deps-vnd-v1-AlarmMeta-StatusEntry"></a>

### AlarmMeta.StatusEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [string](#string) |  |  |






<a name="deps-vnd-v1-AlarmMeta-WarningEntry"></a>

### AlarmMeta.WarningEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [string](#string) |  |  |





 


<a name="deps-vnd-v1-AlarmType"></a>

### AlarmType
TODO: remove later

| Name | Number | Description |
| ---- | ------ | ----------- |
| ALARM_TYPE_UNSPECIFIED | 0 |  |
| ALARM_TYPE_STATUS | 1 |  |
| ALARM_TYPE_WARNING | 2 |  |
| ALARM_TYPE_FAULT | 3 |  |


 

 

 



<a name="deps_model_ems_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/ems/model.v1.proto


 

 

 

 



<a name="deps_model_pcs_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/pcs/model.v1.proto



<a name="deps-model-pcs-v1-DcDcConverter"></a>

### DcDcConverter
DC-DC 컨버터


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| st | [DcDcConverter.St](#deps-model-pcs-v1-DcDcConverter-St) |  | 상태 |
| status | [DcDcConverter.Status](#deps-model-pcs-v1-DcDcConverter-Status) |  | 상태 알람 |
| fault | [DcDcConverter.Fault](#deps-model-pcs-v1-DcDcConverter-Fault) |  | 고장 알람 |
| warning | [DcDcConverter.Warning](#deps-model-pcs-v1-DcDcConverter-Warning) |  | 경고 알람 |
| input | [deps.model.net.v1.Line](#deps-model-net-v1-Line) |  |  |
| output | [deps.model.net.v1.Line](#deps-model-net-v1-Line) |  |  |






<a name="deps-model-pcs-v1-DcDcConverter-Command"></a>

### DcDcConverter.Command



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| conn | [bool](#bool) |  | run/stop |
| reset | [bool](#bool) |  |  |






<a name="deps-model-pcs-v1-DcDcConverter-Fault"></a>

### DcDcConverter.Fault



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  |  |






<a name="deps-model-pcs-v1-DcDcConverter-Status"></a>

### DcDcConverter.Status



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  |  |






<a name="deps-model-pcs-v1-DcDcConverter-Warning"></a>

### DcDcConverter.Warning



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  |  |






<a name="deps-model-pcs-v1-DcPart"></a>

### DcPart
DC측 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dca | [float](#float) |  | DC 전류 |
| dcv | [float](#float) |  | DC 전압 |
| dcw | [float](#float) |  | DC 전력 |






<a name="deps-model-pcs-v1-Rpc"></a>

### Rpc







<a name="deps-model-pcs-v1-Rpc-DcDc"></a>

### Rpc.DcDc







<a name="deps-model-pcs-v1-Rpc-DcDc-CommandRequest"></a>

### Rpc.DcDc.CommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| payload | [DcDcConverter.Command](#deps-model-pcs-v1-DcDcConverter-Command) | repeated |  |






<a name="deps-model-pcs-v1-Rpc-DcDc-CommandResponse"></a>

### Rpc.DcDc.CommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| payload | [uint32](#uint32) |  |  |






<a name="deps-model-pcs-v1-Rpc-DcDc-MeasureResponse"></a>

### Rpc.DcDc.MeasureResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| payload | [DcDcConverter](#deps-model-pcs-v1-DcDcConverter) |  |  |






<a name="deps-model-pcs-v1-Rpc-Grid"></a>

### Rpc.Grid







<a name="deps-model-pcs-v1-Rpc-Grid-MeasureResponse"></a>

### Rpc.Grid.MeasureResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| payload | [ThreePhaseGridPart](#deps-model-pcs-v1-ThreePhaseGridPart) |  |  |






<a name="deps-model-pcs-v1-Rpc-Pcs"></a>

### Rpc.Pcs







<a name="deps-model-pcs-v1-Rpc-Pcs-CommandRequest"></a>

### Rpc.Pcs.CommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| payload | [ThreePhasePcsPart.Command](#deps-model-pcs-v1-ThreePhasePcsPart-Command) | repeated |  |






<a name="deps-model-pcs-v1-Rpc-Pcs-CommandResponse"></a>

### Rpc.Pcs.CommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| payload | [uint32](#uint32) |  |  |






<a name="deps-model-pcs-v1-Rpc-Pcs-MeasureResponse"></a>

### Rpc.Pcs.MeasureResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| payload | [ThreePhasePcsPart](#deps-model-pcs-v1-ThreePhasePcsPart) |  |  |






<a name="deps-model-pcs-v1-TemperaturePart"></a>

### TemperaturePart
온도 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tmp_cab | [float](#float) |  | 캐비넷 온도 |
| tmp_snk | [float](#float) |  | 히트싱크 온도 |
| tmp_trns | [float](#float) |  | 변압기 온도 |
| tmp_ot | [float](#float) | repeated | 기타 제조사 측정 온도 - 의미는 제조사에 따라 다름 |






<a name="deps-model-pcs-v1-ThreePhase"></a>

### ThreePhase
3상 상 (전압) 값


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ph_a | [float](#float) |  | a phase |
| ph_b | [float](#float) |  | b phase |
| ph_c | [float](#float) |  | c phase |






<a name="deps-model-pcs-v1-ThreePhaseGridPart"></a>

### ThreePhaseGridPart
3상 계통 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sum | [deps.model.net.v1.AcLineSum](#deps-model-net-v1-AcLineSum) |  | 3상 합 |
| a | [deps.model.net.v1.AcLine](#deps-model-net-v1-AcLine) |  | A 상 |
| b | [deps.model.net.v1.AcLine](#deps-model-net-v1-AcLine) |  | B 상 |
| c | [deps.model.net.v1.AcLine](#deps-model-net-v1-AcLine) |  | C 상 |






<a name="deps-model-pcs-v1-ThreePhaseLine"></a>

### ThreePhaseLine
3상 선간 (전압) 값


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ph_ab | [float](#float) |  | ab phase |
| ph_bc | [float](#float) |  | bc phase |
| ph_ca | [float](#float) |  | ca phase |






<a name="deps-model-pcs-v1-ThreePhaseNSum"></a>

### ThreePhaseNSum
3상 상 (전압) 값 및 합


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ph_a | [float](#float) |  |  |
| ph_b | [float](#float) |  |  |
| ph_c | [float](#float) |  |  |
| sum | [float](#float) |  |  |






<a name="deps-model-pcs-v1-ThreePhasePcsPart"></a>

### ThreePhasePcsPart
3상 PCS 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| st | [ThreePhasePcsPart.St](#deps-model-pcs-v1-ThreePhasePcsPart-St) |  | 상태 |
| status | [ThreePhasePcsPart.Status](#deps-model-pcs-v1-ThreePhasePcsPart-Status) |  | 상태 알람 |
| fault | [ThreePhasePcsPart.Fault](#deps-model-pcs-v1-ThreePhasePcsPart-Fault) |  | 고장 알람 |
| warning | [ThreePhasePcsPart.Warning](#deps-model-pcs-v1-ThreePhasePcsPart-Warning) |  | 경고 알람 |
| dir_pwr | [ThreePhasePcsPart.DirPwr](#deps-model-pcs-v1-ThreePhasePcsPart-DirPwr) |  | 전력 흐름 방향 |
| ph_v | [ThreePhase](#deps-model-pcs-v1-ThreePhase) |  | 상 전압 |
| pp_v | [ThreePhaseLine](#deps-model-pcs-v1-ThreePhaseLine) |  | 선간 전압 |
| a | [ThreePhaseNSum](#deps-model-pcs-v1-ThreePhaseNSum) |  | 전류 |
| w | [float](#float) |  | 유효전력 |
| hz | [float](#float) |  | 주파수 |
| va | [float](#float) |  | 피상전력 |
| var | [float](#float) |  | 무효전력 |
| pf | [float](#float) |  | 역률 - (방향 TBD) |
| dc | [DcPart](#deps-model-pcs-v1-DcPart) |  | DC측 정보 |
| tmp | [TemperaturePart](#deps-model-pcs-v1-TemperaturePart) |  | 온도 정보 |
| cmds | [ThreePhasePcsPart.Command](#deps-model-pcs-v1-ThreePhasePcsPart-Command) | repeated |  |
| wh | [deps.model.net.v1.Energy](#deps-model-net-v1-Energy) |  |  |






<a name="deps-model-pcs-v1-ThreePhasePcsPart-Command"></a>

### ThreePhasePcsPart.Command
명령


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| conn | [bool](#bool) |  |  |
| reset | [bool](#bool) |  |  |
| estop | [bool](#bool) |  |  |
| block | [bool](#bool) |  |  |
| a | [float](#float) |  | 전류 지령치 |
| v | [float](#float) |  | 전압 지령치 - UPS 등 |
| w | [float](#float) |  | 유효 전력 지령치 |
| dcv | [float](#float) |  | DC 전압 지령치 - DC 시뮬레이터 등 |
| dca | [float](#float) |  | DC 전류 지령치 |
| p_pct | [float](#float) |  | 유효 전력 백분율 지령치 |
| q_pct | [float](#float) |  | 무효 전력 백분율 지령치 |
| pf | [float](#float) |  | 역률 지령치 |
| hz | [float](#float) |  | 주파수 지령치

float var = 14; |






<a name="deps-model-pcs-v1-ThreePhasePcsPart-Fault"></a>

### ThreePhasePcsPart.Fault
고장 상태


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  | 기타 |
| AC_OVER_VOLT | [bool](#bool) |  | 과전압 |
| AC_UNDER_VOLT | [bool](#bool) |  | 저전압 |
| OVER_FREQUENCY | [bool](#bool) |  | 과주파수 |
| UNDER_FREQUENCY | [bool](#bool) |  | 저주파수 |
| OVER_CURRENT | [bool](#bool) |  | 과전류 |
| GROUND_FAULT | [bool](#bool) |  | 지락 |
| DC_OVER_VOLT | [bool](#bool) |  | DC 과전압 |
| OVER_TEMP | [bool](#bool) |  | 과열 |
| UNDER_TEMP | [bool](#bool) |  | 저온 |
| AC_UNBALANCE_VOLT | [bool](#bool) |  | 불균형 전압 |
| AC_UNBALANCE_CURRENT | [bool](#bool) |  | 불균형 전류 |
| HW_TEST_FAILURE | [bool](#bool) |  | 하드웨어 테스트 실패 |
| CB_TRIP | [bool](#bool) |  | 차단기 트립

bool STARTUP_FAIL = 15; |






<a name="deps-model-pcs-v1-ThreePhasePcsPart-Status"></a>

### ThreePhasePcsPart.Status



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  | 기타 |
| AC_DISCONNECT | [bool](#bool) |  | AC측 비연결 상태 |
| DC_DISCONNECT | [bool](#bool) |  | DC측 비연결 상태 |
| GRID_DISCONNECT | [bool](#bool) |  | 계통 비연결 상태 |
| MANUAL_SHUTDOWN | [bool](#bool) |  | 수동 정지 |
| OPEN_DOOR | [bool](#bool) |  | 캐비넷 문 열림 |
| THROTTLED | [bool](#bool) |  | 출력 제한 상태 |
| MPPT | [bool](#bool) |  | MPPT 중 |
| UNDER_COOL | [bool](#bool) |  | 저온 |
| SPD | [bool](#bool) |  | 서지 보호 장치 동작 |






<a name="deps-model-pcs-v1-ThreePhasePcsPart-Warning"></a>

### ThreePhasePcsPart.Warning



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  | 기타 |
| AC_OVER_VOLT | [bool](#bool) |  | 과전압 |
| AC_UNDER_VOLT | [bool](#bool) |  | 저전압 |
| OVER_FREQUENCY | [bool](#bool) |  | 과주파수 |
| UNDER_FREQUENCY | [bool](#bool) |  | 저주파수 |
| OVER_LOAD | [bool](#bool) |  | 과부하 |
| DC_OVER_VOLT | [bool](#bool) |  | DC 과전압 |
| OVER_TEMP | [bool](#bool) |  | 과열 |
| UNDER_TEMP | [bool](#bool) |  | 저온 |
| AC_UNBALANCE_VOLT | [bool](#bool) |  | 불균형 전압 |
| AC_UNBALANCE_CURRENT | [bool](#bool) |  | 불균형 전류 |





 


<a name="deps-model-pcs-v1-DcDcConverter-St"></a>

### DcDcConverter.St


| Name | Number | Description |
| ---- | ------ | ----------- |
| ST_NA | 0 |  |
| ST_OFF | 1 | 정지 |
| ST_SLEEPING | 2 | 슬립 |
| ST_STARTING | 3 | 시작 중 |
| ST_SHUTTING_DOWN | 6 | 정지 중 |
| ST_FAULT | 7 | 고장 |
| ST_STANDBY | 8 | 대기 |
| ST_OPERATION | 9 | 동작 중 |



<a name="deps-model-pcs-v1-ThreePhasePcsPart-DirPwr"></a>

### ThreePhasePcsPart.DirPwr
전력 흐름 방향

| Name | Number | Description |
| ---- | ------ | ----------- |
| DIR_PWR_NA | 0 |  |
| DIR_PWR_STOP | 1 | 정지 |
| DIR_PWR_DC_TO_AC | 2 | DC =&gt; AC |
| DIR_PWR_AC_TO_DC | 3 | AC =&gt; DC |



<a name="deps-model-pcs-v1-ThreePhasePcsPart-St"></a>

### ThreePhasePcsPart.St
PCS 상태

| Name | Number | Description |
| ---- | ------ | ----------- |
| ST_NA | 0 | 기타 |
| ST_OFF | 1 | 정지 |
| ST_SLEEPING | 2 | 슬립 |
| ST_STARTING | 3 | 시작 중 |
| ST_SHUTTING_DOWN | 6 | 정지 중 |
| ST_FAULT | 7 | 고장 |
| ST_STANDBY | 8 | 대기 |
| ST_OPERATION | 9 | 동작 중 |
| ST_BYPASS | 10 | 바이패스 (스위칭 없이 부하를 계통에 연결) |


 

 

 



<a name="deps_model_net_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/net/model.v1.proto



<a name="deps-model-net-v1-AcLine"></a>

### AcLine



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v | [float](#float) |  |  |
| a | [float](#float) |  |  |
| hz | [float](#float) |  |  |
| w | [float](#float) |  |  |
| va | [float](#float) |  |  |
| var | [float](#float) |  |  |
| pf | [float](#float) |  |  |
| wh | [Energy](#deps-model-net-v1-Energy) |  |  |






<a name="deps-model-net-v1-AcLineSum"></a>

### AcLineSum



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| a | [float](#float) |  |  |
| hz | [float](#float) |  |  |
| w | [float](#float) |  |  |
| va | [float](#float) |  |  |
| var | [float](#float) |  |  |
| pf | [float](#float) |  |  |
| wh | [Energy](#deps-model-net-v1-Energy) |  |  |






<a name="deps-model-net-v1-AcLineThreePhase"></a>

### AcLineThreePhase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sum | [AcLineSum](#deps-model-net-v1-AcLineSum) |  | 3상 합 |
| a | [AcLine](#deps-model-net-v1-AcLine) |  | A 상 |
| b | [AcLine](#deps-model-net-v1-AcLine) |  | B 상 |
| c | [AcLine](#deps-model-net-v1-AcLine) |  | C 상 |
| pp_v | [LineToLine](#deps-model-net-v1-LineToLine) |  |  |






<a name="deps-model-net-v1-Energy"></a>

### Energy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| exported | [double](#double) |  |  |
| imported | [double](#double) |  |  |






<a name="deps-model-net-v1-Harmonics"></a>

### Harmonics



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v_series | [float](#float) | repeated | 0 = DC, 1 = fundamental, 2 = 2nd harmonic, ... |
| a_series | [float](#float) | repeated |  |
| thd_v | [float](#float) |  |  |
| thd_a | [float](#float) |  |  |
| tdd_a | [float](#float) |  |  |
| phs_v | [Phasor](#deps-model-net-v1-Phasor) |  | Fundamental 페이저 |
| phs_a | [Phasor](#deps-model-net-v1-Phasor) |  |  |






<a name="deps-model-net-v1-HarmonicsThreePhase"></a>

### HarmonicsThreePhase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| a | [Harmonics](#deps-model-net-v1-Harmonics) |  |  |
| b | [Harmonics](#deps-model-net-v1-Harmonics) |  |  |
| c | [Harmonics](#deps-model-net-v1-Harmonics) |  |  |






<a name="deps-model-net-v1-Line"></a>

### Line



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v | [float](#float) |  |  |
| a | [float](#float) |  |  |
| w | [float](#float) |  |  |
| wh | [Energy](#deps-model-net-v1-Energy) |  |  |






<a name="deps-model-net-v1-LineToLine"></a>

### LineToLine



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ab | [float](#float) |  |  |
| bc | [float](#float) |  |  |
| ca | [float](#float) |  |  |






<a name="deps-model-net-v1-MeterThreePhase"></a>

### MeterThreePhase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| main | [AcLineThreePhase](#deps-model-net-v1-AcLineThreePhase) |  |  |
| harmonics | [HarmonicsThreePhase](#deps-model-net-v1-HarmonicsThreePhase) |  |  |






<a name="deps-model-net-v1-Phasor"></a>

### Phasor



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [float](#float) |  |  |
| y | [float](#float) |  |  |






<a name="deps-model-net-v1-Rpc"></a>

### Rpc







<a name="deps-model-net-v1-Rpc-MeterThreePhase"></a>

### Rpc.MeterThreePhase







<a name="deps-model-net-v1-Rpc-MeterThreePhase-MeasureResponse"></a>

### Rpc.MeterThreePhase.MeasureResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| payload | [MeterThreePhase](#deps-model-net-v1-MeterThreePhase) |  |  |





 

 

 

 



<a name="deps_model_esd_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/esd/model.v1.proto



<a name="deps-model-esd-v1-EsdBank"></a>

### EsdBank
배터리 총 합 (병렬 String으로 구성)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| st | [EsdBank.St](#deps-model-esd-v1-EsdBank-St) |  | 상태 |
| st_cha | [EsdBank.StCha](#deps-model-esd-v1-EsdBank-StCha) |  | 충전 상태 |
| cnt_mod | [EsdBank.ModuleCount](#deps-model-esd-v1-EsdBank-ModuleCount) |  | Module 요약 |
| cnt_str | [EsdBank.StringCount](#deps-model-esd-v1-EsdBank-StringCount) |  | String 요약 |
| cnt_cell | [EsdBank.CellCount](#deps-model-esd-v1-EsdBank-CellCount) |  | Cell 요약 |
| soc | [float](#float) |  | SoC |
| dod | [float](#float) |  | DoD |
| soh | [float](#float) |  | SoH |
| n_cyc | [uint32](#uint32) |  | 충방전 사이클 수 |
| hb | [uint32](#uint32) |  | HeartBeat |
| v | [float](#float) |  | 전압 |
| a | [float](#float) |  | 전류 |
| a_cha_max | [float](#float) |  | 최대 충전 전류 |
| a_discha_max | [float](#float) |  | 최대 방전 전류 |
| w | [float](#float) |  | 전력 |
| status | [EsdBank.Status](#deps-model-esd-v1-EsdBank-Status) |  | 상태 알람 |
| warning | [EsdBank.Warning](#deps-model-esd-v1-EsdBank-Warning) |  | 경고 알람 |
| fault | [EsdBank.Fault](#deps-model-esd-v1-EsdBank-Fault) |  | 고장 알람 |
| strs | [EsdString](#deps-model-esd-v1-EsdString) | repeated | String (Rack) 정보 |






<a name="deps-model-esd-v1-EsdBank-CellCount"></a>

### EsdBank.CellCount
Bank Cell 요약


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v_max | [float](#float) |  | 최대 Cell 전압 |
| v_max_str | [uint32](#uint32) |  | 최대 Cell 전압의 String 위치 (1-base, 0 = N/A) |
| v_max_mod | [uint32](#uint32) |  | 최대 Cell 전압의 Module 위치 (1-base, 0 = N/A) |
| v_min | [float](#float) |  | 최소 Cell 전압 |
| v_min_str | [uint32](#uint32) |  | 최소 Cell 전압의 String 위치 (1-base, 0 = N/A) |
| v_min_mod | [uint32](#uint32) |  | 최소 Cell 전압의 Module 위치 (1-base, 0 = N/A) |
| v_avg | [float](#float) |  | 평균 Cell 전압 |
| n_bal | [uint32](#uint32) |  | Cell Balance 갯수 |






<a name="deps-model-esd-v1-EsdBank-Command"></a>

### EsdBank.Command
명령


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| conn | [bool](#bool) |  | 동작 설정 |
| reset | [bool](#bool) |  |  |






<a name="deps-model-esd-v1-EsdBank-Fault"></a>

### EsdBank.Fault
고장 알람


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  | 기타 고장 |
| OVER_TEMP | [bool](#bool) |  | 과열 상태 |
| UNDER_TEMP | [bool](#bool) |  | 저온 상태 |
| OVER_CHARGE_CURRENT | [bool](#bool) |  | 과충전 전류 |
| OVER_DISCHARGE_CURRENT | [bool](#bool) |  | 과방전 전류 |
| OVER_VOLT | [bool](#bool) |  | 과잉 전압 |
| UNDER_VOLT | [bool](#bool) |  | 부족 전압 |
| UNDER_SOC_MIN | [bool](#bool) |  | 부족 SOC |
| OVER_SOC_MAX | [bool](#bool) |  | 과잉 SOC |
| VOLTAGE_IMBALANCE | [bool](#bool) |  | 전압 불균형 |
| TEMPERATURE_IMBALANCE | [bool](#bool) |  | 온도 불균형 |
| CURRENT_IMBALANCE | [bool](#bool) |  | 전류 불균형 |
| CONFIGURATION | [bool](#bool) |  | 설정 오류 |
| COMMUNICATION_ERROR | [bool](#bool) |  | 통신 오류 |
| CONTACTOR_ERROR | [bool](#bool) |  | 컨택터 오류 |
| FAN_ERROR | [bool](#bool) |  | 팬 오류 |
| GROUND_FAULT | [bool](#bool) |  | 접지 오류 |






<a name="deps-model-esd-v1-EsdBank-ModuleCount"></a>

### EsdBank.ModuleCount
Bank Module 요약


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tmp_max | [float](#float) |  | 최고 온도 |
| tmp_max_str | [uint32](#uint32) |  | 최고 온도의 String 위치 (1-base, 0 = N/A) |
| tmp_max_mod | [uint32](#uint32) |  | 최고 온도의 Module 위치 (1-base, 0 = N/A) |
| tmp_min | [float](#float) |  | 최소 온도 |
| tmp_min_str | [uint32](#uint32) |  | 최소 온도의 String 위치 (1-base, 0 = N/A) |
| tmp_min_mod | [uint32](#uint32) |  | 최소 온도의 Module 위치 (1-base, 0 = N/A) |
| tmp_avg | [float](#float) |  | 평균 온도 |






<a name="deps-model-esd-v1-EsdBank-Status"></a>

### EsdBank.Status
상태 알람


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  | 기타 상태 |
| OPEN_DOOR | [bool](#bool) |  | 케비넷 문 열림 |






<a name="deps-model-esd-v1-EsdBank-StringCount"></a>

### EsdBank.StringCount
Bank String 요약


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v_max | [float](#float) |  | 최대 String 전압 |
| v_max_str | [uint32](#uint32) |  | 최대 String 전압의 String 위치 (1-base, 0 = N/A) |
| v_min | [float](#float) |  | 최소 String 전압 |
| v_min_str | [uint32](#uint32) |  | 최소 String 전압의 String 위치 (1-base, 0 = N/A) |
| v_avg | [float](#float) |  | 평균 String 전압 |
| a_max | [float](#float) |  | 최대 String 전류 |
| a_max_str | [uint32](#uint32) |  | 최대 String 전류의 String 위치 (1-base, 0 = N/A) |
| a_min | [float](#float) |  | 최소 String 전류 |
| a_min_str | [uint32](#uint32) |  | 최소 String 전류의 String 위치 (1-base, 0 = N/A) |
| a_avg | [float](#float) |  | 평균 String 전류 |
| n_conn | [uint32](#uint32) |  | 연결된 String 갯수 |






<a name="deps-model-esd-v1-EsdBank-Warning"></a>

### EsdBank.Warning
TODO: CELL_OV, CELL_UV 필요할 수도
경고 알람


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  | 기타 경고 |
| OVER_TEMP | [bool](#bool) |  | 과열 상태 |
| UNDER_TEMP | [bool](#bool) |  | 저온 상태 |
| OVER_CHARGE_CURRENT | [bool](#bool) |  | 과충전 전류 |
| OVER_DISCHARGE_CURRENT | [bool](#bool) |  | 과방전 전류 |
| OVER_VOLT | [bool](#bool) |  | 과잉 전압 |
| UNDER_VOLT | [bool](#bool) |  | 부족 전압 |
| UNDER_SOC_MIN | [bool](#bool) |  | 부족 SOC |
| OVER_SOC_MAX | [bool](#bool) |  | 과잉 SOC |
| VOLTAGE_IMBALANCE | [bool](#bool) |  | 전압 불균형 |
| TEMPERATURE_IMBALANCE | [bool](#bool) |  | 온도 불균형 |
| CURRENT_IMBALANCE | [bool](#bool) |  | 전류 불균형 |
| CONFIGURATION | [bool](#bool) |  | 구성 오류 |






<a name="deps-model-esd-v1-EsdCell"></a>

### EsdCell
Cell 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v | [float](#float) |  | 전압 |
| tmp | [float](#float) |  | 온도 |
| st | [EsdCell.St](#deps-model-esd-v1-EsdCell-St) |  | 상태 알람 |






<a name="deps-model-esd-v1-EsdCell-St"></a>

### EsdCell.St
Cell 상태 알람


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| is_balancing | [bool](#bool) |  | Cell 밸런싱 여부 |






<a name="deps-model-esd-v1-EsdModule"></a>

### EsdModule
Module


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| str_idx | [uint32](#uint32) |  | Module의 String 인덱스 (1-base, 0 = N/A) |
| mod_idx | [uint32](#uint32) |  | Module 인덱스 (1-base, 0 = N/A) |
| n_cell | [uint32](#uint32) |  | Cell 갯수 |
| soc | [float](#float) |  | SoC |
| dod | [float](#float) |  | DoD |
| soh | [float](#float) |  | SoH |
| n_cyc | [uint32](#uint32) |  | 충방전 사이클 수 |
| v | [float](#float) |  | 전압 |
| cnt_cell | [EsdModule.CellCount](#deps-model-esd-v1-EsdModule-CellCount) |  | Cell 요약 |
| sn | [string](#string) |  | 시리얼 넘버 |
| cells | [EsdCell](#deps-model-esd-v1-EsdCell) | repeated | Cell 정보 |






<a name="deps-model-esd-v1-EsdModule-CellCount"></a>

### EsdModule.CellCount
Cell 요약


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v_max | [float](#float) |  | 최대 Cell 전압 |
| v_max_cell | [uint32](#uint32) |  | 최대 Cell 전압의 Module 위치 |
| v_min | [float](#float) |  | 최소 Cell 전압 |
| v_min_cell | [uint32](#uint32) |  | 최소 Cell 전압의 Module 위치 |
| v_avg | [float](#float) |  | 평균 Cell 전압 |
| tmp_max | [float](#float) |  | 최고 온도 |
| tmp_max_cell | [uint32](#uint32) |  | 최고 온도의 Cell 위치 |
| tmp_min | [float](#float) |  | 최저 온도 |
| tmp_min_cell | [uint32](#uint32) |  | 최저 온도의 Cell 위치 |
| tmp_avg | [float](#float) |  | 평균 온도 |
| n_bal | [uint32](#uint32) |  | Cell Balance 갯수 |






<a name="deps-model-esd-v1-EsdString"></a>

### EsdString
배터리 String (Rack)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| con_fail | [EsdString.ConFail](#deps-model-esd-v1-EsdString-ConFail) |  | 컨택터 실패 여부 |
| soc | [float](#float) |  | SoC |
| dod | [float](#float) |  | DoD |
| n_cyc | [uint32](#uint32) |  | 충방전 사이클 수 |
| soh | [float](#float) |  | SoH |
| a | [float](#float) |  | 전류 |
| v | [float](#float) |  | 전압 |
| cnt_cell | [EsdString.CellCount](#deps-model-esd-v1-EsdString-CellCount) |  | Cell 요약 |
| cnt_mod | [EsdString.ModuleCount](#deps-model-esd-v1-EsdString-ModuleCount) |  | Module 요약 |
| st_con | [EsdString.StCon](#deps-model-esd-v1-EsdString-StCon) |  | 컨택터 상태 |
| status | [EsdString.Status](#deps-model-esd-v1-EsdString-Status) |  | 상태 알람 |
| warning | [EsdString.Warning](#deps-model-esd-v1-EsdString-Warning) |  | 경고 알람 |
| fault | [EsdString.Fault](#deps-model-esd-v1-EsdString-Fault) |  | 고장 알람 |
| mods | [EsdModule](#deps-model-esd-v1-EsdModule) | repeated | 활성화 설정 Command.SetEna set_ena = 15; // 동작 설정 Command.SetCon set_con = 16; 모듈 정보 |






<a name="deps-model-esd-v1-EsdString-CellCount"></a>

### EsdString.CellCount
Cell 요약


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v_max | [float](#float) |  | 최대 Cell 전압 |
| v_max_mod | [uint32](#uint32) |  | 최대 Cell 전압의 Module 위치 |
| v_min | [float](#float) |  | 최소 Cell 전압 |
| v_min_mod | [uint32](#uint32) |  | 최소 Cell 전압의 Module 위치 |
| v_avg | [float](#float) |  | 평균 Cell 전압 |
| n_cell_bal | [uint32](#uint32) |  | Cell Balance 갯수 |






<a name="deps-model-esd-v1-EsdString-Command"></a>

### EsdString.Command
명령


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| set_con | [EsdString.Command.SetCon](#deps-model-esd-v1-EsdString-Command-SetCon) |  | 동작 설정 |
| set_ena | [EsdString.Command.SetEna](#deps-model-esd-v1-EsdString-Command-SetEna) |  | 활성화 설정 |






<a name="deps-model-esd-v1-EsdString-Fault"></a>

### EsdString.Fault
TODO: CURRENT_IMBALANCE 필요할지 체크
고장 알람


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  | 기타 고장 |
| OVER_TEMP | [bool](#bool) |  | 과열 |
| UNDER_TEMP | [bool](#bool) |  | 저온 |
| OVER_CHARGE_CURRENT | [bool](#bool) |  | 과충전 전류 |
| OVER_DISCHARGE_CURRENT | [bool](#bool) |  | 과방전 전류 |
| OVER_VOLT | [bool](#bool) |  | 과전압 |
| UNDER_VOLT | [bool](#bool) |  | 저전압 |
| UNDER_SOC_MIN | [bool](#bool) |  | 부족 SoC |
| OVER_SOC_MAX | [bool](#bool) |  | 과잉 SoC |
| VOLTAGE_IMBALANCE | [bool](#bool) |  | 전압 불균형 |
| TEMPERATURE_IMBALANCE | [bool](#bool) |  | 온도 불균형 |
| COMMUNICATION_ERROR | [bool](#bool) |  | 통신 오류 |
| CONFIGURATION | [bool](#bool) |  | 설정 오류 |
| CONTACTOR_ERROR | [bool](#bool) |  | 컨택터 오류 |
| FAN_ERROR | [bool](#bool) |  | 팬 오류 |
| GROUND_FAULT | [bool](#bool) |  | 접지 오류 |






<a name="deps-model-esd-v1-EsdString-ModuleCount"></a>

### EsdString.ModuleCount
Module 요약


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tmp_max | [float](#float) |  | 최고 온도 |
| tmp_max_mod | [uint32](#uint32) |  | 최고 온도의 Module 위치 |
| tmp_min | [float](#float) |  | 최소 온도 |
| tmp_min_mod | [uint32](#uint32) |  | 최소 온도의 Module 위치 |
| tmp_avg | [float](#float) |  | 평균 온도 |






<a name="deps-model-esd-v1-EsdString-StCon"></a>

### EsdString.StCon
TODO: 필요 여부 재확인
컨택터 상태


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| conn | [bool](#bool) | repeated |  |






<a name="deps-model-esd-v1-EsdString-Status"></a>

### EsdString.Status
상태 알람


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  | 기타 알람 |
| OPEN_DOOR | [bool](#bool) |  | 캐비넷 문 열림 |
| STRING_ENABLED | [bool](#bool) |  | String 활성화 |
| CONTACTOR_STATUS | [bool](#bool) |  | 컨택터 상태 (?) |






<a name="deps-model-esd-v1-EsdString-Warning"></a>

### EsdString.Warning
경고 알람


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| OTHER | [bool](#bool) |  | 기타 알람 |
| OVER_TEMP | [bool](#bool) |  | 과열 |
| UNDER_TEMP | [bool](#bool) |  | 저온 |
| OVER_CHARGE_CURRENT | [bool](#bool) |  | 과충전 전류 |
| OVER_DISCHARGE_CURRENT | [bool](#bool) |  | 과방전 전류 |
| OVER_VOLT | [bool](#bool) |  | 과전압 |
| UNDER_VOLT | [bool](#bool) |  | 저전압 |
| UNDER_SOC_MIN | [bool](#bool) |  | 부족 SoC |
| OVER_SOC_MAX | [bool](#bool) |  | 과잉 SoC |
| VOLTAGE_IMBALANCE | [bool](#bool) |  | 전압 불균형 |
| TEMPERATURE_IMBALANCE | [bool](#bool) |  | 온도 불균형 |






<a name="deps-model-esd-v1-Rpc"></a>

### Rpc







<a name="deps-model-esd-v1-Rpc-Bank"></a>

### Rpc.Bank







<a name="deps-model-esd-v1-Rpc-Bank-CommandRequest"></a>

### Rpc.Bank.CommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| payload | [EsdBank.Command](#deps-model-esd-v1-EsdBank-Command) | repeated |  |






<a name="deps-model-esd-v1-Rpc-Bank-CommandResponse"></a>

### Rpc.Bank.CommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| payload | [uint32](#uint32) |  |  |






<a name="deps-model-esd-v1-Rpc-Bank-MeasureResponse"></a>

### Rpc.Bank.MeasureResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| payload | [EsdBank](#deps-model-esd-v1-EsdBank) |  |  |





 


<a name="deps-model-esd-v1-EsdBank-St"></a>

### EsdBank.St
시스템 상태

| Name | Number | Description |
| ---- | ------ | ----------- |
| ST_NA | 0 |  |
| ST_DISCONNECTED | 1 | 연결 해제 됨 |
| ST_INITIALIZING | 2 | 초기화 중 |
| ST_CONNECTED | 3 | 연결 됨 |
| ST_FAULT | 99 | 대기 중 ST_STANDBY = 4; SoC 보호 상태 ST_SOC_PROTECTION = 5; 일시 중지 상태 ST_SUSPENDING = 6; 고장 상태 |



<a name="deps-model-esd-v1-EsdBank-StCha"></a>

### EsdBank.StCha
배터리 충전 상태

| Name | Number | Description |
| ---- | ------ | ----------- |
| ST_CHA_NA | 0 |  |
| ST_CHA_STOP | 1 | 정지 |
| ST_CHA_EMPTY | 2 | 완전 방전됨 (정지) |
| ST_CHA_DISCHARGING | 3 | 방전 중 |
| ST_CHA_CHARGING | 4 | 충전 중 |
| ST_CHA_FULL | 5 | 완전 충전됨 (정지) |
| ST_CHA_HOLDING | 6 | 유지 중 (현재 SoC 유지) |
| ST_CHA_TESTING | 7 | 테스트 상태 |



<a name="deps-model-esd-v1-EsdString-Command-SetCon"></a>

### EsdString.Command.SetCon
동작 설정

| Name | Number | Description |
| ---- | ------ | ----------- |
| SET_CON_NA | 0 |  |
| SET_CON_CONNECT_STRING | 1 | 연결 |
| SET_CON_DISCONNECT_STRING | 2 | 연결 해제 |



<a name="deps-model-esd-v1-EsdString-Command-SetEna"></a>

### EsdString.Command.SetEna
활성화 설정

| Name | Number | Description |
| ---- | ------ | ----------- |
| SET_ENA_NA | 0 |  |
| SET_ENA_ENABLE_STRING | 1 | 활성화 |
| SET_ENA_DISABLE_STRING | 2 | 비활성화 |



<a name="deps-model-esd-v1-EsdString-ConFail"></a>

### EsdString.ConFail
연결 실패 여부

| Name | Number | Description |
| ---- | ------ | ----------- |
| CON_FAIL_NA | 0 |  |
| CON_FAIL_NO_FAILURE | 1 | 고장 없음 |
| CON_FAIL_BUTTON_PUSHED | 2 | 비상 정지 |
| CON_FAIL_STR_GROUND_FAULT | 3 | 접지 오류 |
| CON_FAIL_OUTSIDE_VOLTAGE_RANGE | 4 | 허용 전압 범위 초과 |
| CON_FAIL_STRING_NOT_ENABLED | 5 | 비활성화 |
| CON_FAIL_FUSE_OPEN | 6 | 퓨즈 개방 |
| CON_FAIL_CONTACTOR_FAILURE | 7 | 컨택터 동작 실패 |
| CON_FAIL_PRECHARGE_FAILURE | 8 | 초기충전 실패 |
| CON_FAIL_STRING_FAULT | 9 | String 고장 |


 

 

 



<a name="deps_model_esd_extra-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/esd/extra.v1.proto



<a name="deps-model-esd-v1-ChaLimit"></a>

### ChaLimit
충방전 제한 SoC 범위


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| soc_max | [float](#float) |  | 최대 SoC |
| soc_min | [float](#float) |  | 최소 SoC |






<a name="deps-model-esd-v1-Conn"></a>

### Conn
시스템 연결 상태


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| conn | [Conn.ConnCmd](#deps-model-esd-v1-Conn-ConnCmd) |  |  |





 


<a name="deps-model-esd-v1-Conn-ConnCmd"></a>

### Conn.ConnCmd


| Name | Number | Description |
| ---- | ------ | ----------- |
| DISCONNECT | 0 | 연결 해제 |
| CONNECT | 1 | 연결 |


 

 

 



<a name="deps_model_tsdb_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/tsdb/model.v1.proto



<a name="deps-model-tsdb-v1-AlarmExtra"></a>

### AlarmExtra



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| kind | [AlarmKind](#deps-model-tsdb-v1-AlarmKind) |  |  |
| status | [AlarmStatus](#deps-model-tsdb-v1-AlarmStatus) |  |  |






<a name="deps-model-tsdb-v1-CommandExtra"></a>

### CommandExtra



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target | [string](#string) |  |  |
| parameters | [google.protobuf.Struct](#google-protobuf-Struct) |  |  |






<a name="deps-model-tsdb-v1-EventExtra"></a>

### EventExtra



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tags | [google.protobuf.Struct](#google-protobuf-Struct) |  |  |






<a name="deps-model-tsdb-v1-LogConstraint"></a>

### LogConstraint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| end | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| matches | [LogMatch](#deps-model-tsdb-v1-LogMatch) | repeated |  |
| limit | [uint32](#uint32) |  |  |
| order | [Order](#deps-model-tsdb-v1-Order) |  |  |






<a name="deps-model-tsdb-v1-LogItem"></a>

### LogItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| source | [string](#string) |  |  |
| name | [string](#string) |  |  |
| event | [EventExtra](#deps-model-tsdb-v1-EventExtra) |  |  |
| alarm | [AlarmExtra](#deps-model-tsdb-v1-AlarmExtra) |  |  |
| command | [CommandExtra](#deps-model-tsdb-v1-CommandExtra) |  |  |






<a name="deps-model-tsdb-v1-LogMatch"></a>

### LogMatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| log_kind | [LogKind](#deps-model-tsdb-v1-LogKind) |  |  |
| source_like | [string](#string) |  |  |
| name_like | [string](#string) |  |  |
| alarm_kind | [AlarmKind](#deps-model-tsdb-v1-AlarmKind) |  |  |
| target_like | [string](#string) |  |  |
| alarm_status | [AlarmStatus](#deps-model-tsdb-v1-AlarmStatus) |  |  |






<a name="deps-model-tsdb-v1-MeasureConstraint"></a>

### MeasureConstraint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| end | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| measures | [MeasureId](#deps-model-tsdb-v1-MeasureId) | repeated |  |
| limit | [uint32](#uint32) |  |  |
| order | [Order](#deps-model-tsdb-v1-Order) |  |  |






<a name="deps-model-tsdb-v1-MeasureId"></a>

### MeasureId



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| source | [string](#string) |  |  |
| paths | [string](#string) | repeated |  |





 


<a name="deps-model-tsdb-v1-AlarmKind"></a>

### AlarmKind


| Name | Number | Description |
| ---- | ------ | ----------- |
| ALARM_KIND_STATUS | 0 |  |
| ALARM_KIND_WARNING | 1 |  |
| ALARM_KIND_FAULT | 2 |  |



<a name="deps-model-tsdb-v1-AlarmStatus"></a>

### AlarmStatus


| Name | Number | Description |
| ---- | ------ | ----------- |
| ALARM_STATUS_CLEAR | 0 |  |
| ALARM_STATUS_TRIGGER | 1 |  |



<a name="deps-model-tsdb-v1-LogKind"></a>

### LogKind


| Name | Number | Description |
| ---- | ------ | ----------- |
| LOG_KIND_EVENT | 0 |  |
| LOG_KIND_ALARM | 1 |  |
| LOG_KIND_COMMAND | 2 |  |



<a name="deps-model-tsdb-v1-Order"></a>

### Order


| Name | Number | Description |
| ---- | ------ | ----------- |
| ORDER_ASC | 0 |  |
| ORDER_DESC | 1 |  |


 

 

 



<a name="deps_model_cast_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/cast/model.v1.proto



<a name="deps-model-cast-v1-CastHeader"></a>

### CastHeader
예측 정보 헤더


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| caststamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | 예측 시간 (예측 생성 시간) |
| pointstamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | 예측 기준 시점 (예측 대상 시점) |
| leadtime | [google.protobuf.Duration](#google-protobuf-Duration) |  | 예측 선행 시간 |
| kind | [uint32](#uint32) |  | 예측 생산 생산 구분 |






<a name="deps-model-cast-v1-EnergyCast"></a>

### EnergyCast
수요/발전 예측 데이터


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [CastHeader](#deps-model-cast-v1-CastHeader) |  | 예측 정보 헤더 |
| w_cap | [double](#double) | optional | 설비 용량 |
| w | [double](#double) | repeated | 수요/발전 예측량 (배열) |
| w_tot | [double](#double) |  | 최종 수요/발전 예측량 |
| w_min | [double](#double) |  | 수요/발전 예측 최소값 |
| w_max | [double](#double) |  | 수요/발전 예측 최대값 |






<a name="deps-model-cast-v1-GridOperation"></a>

### GridOperation
계통 운영 데이터


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | 계측 시각 |
| w_dmnd | [double](#double) |  | 현재 수요 |
| w_pv | [double](#double) |  | 태양광 합계 |
| w_wind | [double](#double) |  | 풍력 합계 |
| w_re_tot | [double](#double) |  | 신재생 합계 |
| w_cap_sup | [double](#double) |  | 공급 능력 |






<a name="deps-model-cast-v1-GridOutputControl"></a>

### GridOutputControl
예측 출력 제어 데이터


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [CastHeader](#deps-model-cast-v1-CastHeader) |  | .google.protobuf.Timestamp timestamp = 1; 예측 정보 헤더 |
| w_p_m2_ctl | [double](#double) |  | 출력 제어량 |
| w_p_m2_min | [double](#double) |  | 최소 출력량 |






<a name="deps-model-cast-v1-H2StationMeasure"></a>

### H2StationMeasure
수소 발전 단지 계측 값


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | 계측 시각 |
| kg_cap | [double](#double) |  | 설비 용량 |
| kg | [double](#double) |  | 생산량 |






<a name="deps-model-cast-v1-StationCast"></a>

### StationCast
발전소 예측 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [CastHeader](#deps-model-cast-v1-CastHeader) |  | 예측 정보 헤더 |
| w_cap | [double](#double) |  | 설비 용량 |
| wh | [double](#double) |  | 생산량 |






<a name="deps-model-cast-v1-WeatherCast"></a>

### WeatherCast
기상 예측 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [CastHeader](#deps-model-cast-v1-CastHeader) |  | 예측 정보 헤더 |
| tmp | [double](#double) | repeated | 기온 (°C) |
| rh | [double](#double) | repeated | 습도 (%) |
| irr | [double](#double) | repeated | 일사량 (W/m²) |
| wind | [WindData](#deps-model-cast-v1-WindData) | repeated | 풍속/풍향 |






<a name="deps-model-cast-v1-WindData"></a>

### WindData
풍속 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mps_spd | [double](#double) |  | 풍속 (m/s) |
| deg_dir | [double](#double) |  | 풍향 (deg) |





 

 

 

 



<a name="deps_model_source_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/source/model.v1.proto



<a name="deps-model-source-v1-PvLine"></a>

### PvLine



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| strings | [PvString](#deps-model-source-v1-PvString) | repeated |  |






<a name="deps-model-source-v1-PvString"></a>

### PvString



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v | [float](#float) |  |  |
| a | [float](#float) |  |  |
| w | [float](#float) |  |  |





 

 

 

 



<a name="deps_model_pms_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/pms/model.v1.proto



<a name="deps-model-pms-v1-ChainFn"></a>

### ChainFn



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| charts | [ChartFn](#deps-model-pms-v1-ChartFn) | repeated |  |






<a name="deps-model-pms-v1-ChartFn"></a>

### ChartFn



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| points | [Point2D](#deps-model-pms-v1-Point2D) | repeated |  |






<a name="deps-model-pms-v1-LookupComplete"></a>

### LookupComplete



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ranges | [Point2D](#deps-model-pms-v1-Point2D) | repeated |  |
| win_tms | [double](#double) |  |  |






<a name="deps-model-pms-v1-LookupInput"></a>

### LookupInput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| soc | [double](#double) | optional |  |
| tmp | [double](#double) | optional |  |
| price | [double](#double) | optional |  |
| w_src | [double](#double) | optional |  |
| w_cut | [double](#double) | optional |  |






<a name="deps-model-pms-v1-LookupItem"></a>

### LookupItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| anchor | [LookupItemAnchor](#deps-model-pms-v1-LookupItemAnchor) |  |  |
| axis_range | [LookupItemAxisRange](#deps-model-pms-v1-LookupItemAxisRange) | repeated |  |
| in_type | [LookupInputType](#deps-model-pms-v1-LookupInputType) |  |  |
| out_type | [LookupOutputType](#deps-model-pms-v1-LookupOutputType) |  |  |
| chain_fn | [ChainFn](#deps-model-pms-v1-ChainFn) |  |  |
| blend_mode | [OutputBlendMode](#deps-model-pms-v1-OutputBlendMode) |  |  |
| win_tms | [double](#double) |  |  |
| rmp_tms | [double](#double) |  |  |
| complete | [LookupComplete](#deps-model-pms-v1-LookupComplete) |  |  |






<a name="deps-model-pms-v1-LookupItemAnchor"></a>

### LookupItemAnchor



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#double) | optional |  |
| y | [double](#double) | optional |  |






<a name="deps-model-pms-v1-LookupItemAxisRange"></a>

### LookupItemAxisRange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [MinMax](#deps-model-pms-v1-MinMax) |  |  |
| y | [MinMax](#deps-model-pms-v1-MinMax) |  |  |






<a name="deps-model-pms-v1-LookupOutput"></a>

### LookupOutput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| w_cmd | [double](#double) | optional |  |
| w_max_pos | [double](#double) | optional |  |
| w_max_neg | [double](#double) | optional |  |
| va_abs | [double](#double) | optional |  |






<a name="deps-model-pms-v1-LookupRule"></a>

### LookupRule



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ena | [bool](#bool) |  |  |
| rules | [LookupSequence](#deps-model-pms-v1-LookupSequence) | repeated |  |
| forced | [LookupSequence](#deps-model-pms-v1-LookupSequence) | repeated |  |






<a name="deps-model-pms-v1-LookupRule-Command"></a>

### LookupRule.Command
enum Ena {
  ENA_NA = 0;
  ENA_DISABLE = 1;
  ENA_ENABLE = 2;
}


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ena | [bool](#bool) |  |  |
| ena_rule | [LookupRule.Command.EnaRule](#deps-model-pms-v1-LookupRule-Command-EnaRule) |  |  |
| add | [LookupRule.Command.AddRule](#deps-model-pms-v1-LookupRule-Command-AddRule) |  |  |
| delete | [LookupRule.Command.DeleteRule](#deps-model-pms-v1-LookupRule-Command-DeleteRule) |  |  |
| clear | [LookupRule.Command.ClearRules](#deps-model-pms-v1-LookupRule-Command-ClearRules) |  |  |
| overwrite | [LookupRule.Command.OverwriteRules](#deps-model-pms-v1-LookupRule-Command-OverwriteRules) |  |  |






<a name="deps-model-pms-v1-LookupRule-Command-AddRule"></a>

### LookupRule.Command.AddRule



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| items | [LookupItem](#deps-model-pms-v1-LookupItem) | repeated |  |
| upsert | [bool](#bool) |  |  |






<a name="deps-model-pms-v1-LookupRule-Command-ClearRules"></a>

### LookupRule.Command.ClearRules







<a name="deps-model-pms-v1-LookupRule-Command-DeleteRule"></a>

### LookupRule.Command.DeleteRule



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |






<a name="deps-model-pms-v1-LookupRule-Command-EnaRule"></a>

### LookupRule.Command.EnaRule



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| ena | [bool](#bool) |  |  |






<a name="deps-model-pms-v1-LookupRule-Command-OverwriteRules"></a>

### LookupRule.Command.OverwriteRules



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rules | [LookupSequence](#deps-model-pms-v1-LookupSequence) | repeated |  |






<a name="deps-model-pms-v1-LookupRule-Fault"></a>

### LookupRule.Fault



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| other | [bool](#bool) |  |  |






<a name="deps-model-pms-v1-LookupRule-Status"></a>

### LookupRule.Status



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| other | [bool](#bool) |  |  |






<a name="deps-model-pms-v1-LookupRule-Warning"></a>

### LookupRule.Warning



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| other | [bool](#bool) |  |  |






<a name="deps-model-pms-v1-LookupSequence"></a>

### LookupSequence



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ena | [bool](#bool) |  |  |
| name | [string](#string) |  |  |
| sequence | [LookupItem](#deps-model-pms-v1-LookupItem) | repeated |  |
| state | [LookupSequenceState](#deps-model-pms-v1-LookupSequenceState) |  |  |






<a name="deps-model-pms-v1-LookupSequenceState"></a>

### LookupSequenceState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| io_snapshot | [LookupItemAnchor](#deps-model-pms-v1-LookupItemAnchor) | repeated |  |
| completed | [bool](#bool) | repeated |  |
| stamp_complete_check | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| stamp_sequence_enter | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| stamp_chain_enter | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| error | [string](#string) |  |  |






<a name="deps-model-pms-v1-MinMax"></a>

### MinMax



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min | [double](#double) | optional |  |
| max | [double](#double) | optional |  |






<a name="deps-model-pms-v1-Point2D"></a>

### Point2D



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [double](#double) |  |  |
| y | [double](#double) |  |  |





 


<a name="deps-model-pms-v1-LookupInputType"></a>

### LookupInputType


| Name | Number | Description |
| ---- | ------ | ----------- |
| LOOKUP_INPUT_TYPE_NA | 0 |  |
| LOOKUP_INPUT_TYPE_TIME_SEC | 1 |  |
| LOOKUP_INPUT_TYPE_TIME_MIN | 2 |  |
| LOOKUP_INPUT_TYPE_TIME_HOUR | 3 |  |
| LOOKUP_INPUT_TYPE_TIME_SEC_SINCE_SEQUENCE | 4 |  |
| LOOKUP_INPUT_TYPE_TIME_SEC_SINCE_CHAIN | 5 |  |
| LOOKUP_INPUT_TYPE_SOC | 6 |  |
| LOOKUP_INPUT_TYPE_SOC_PU | 7 |  |
| LOOKUP_INPUT_TYPE_TMP | 8 |  |
| LOOKUP_INPUT_TYPE_PRICE | 9 |  |
| LOOKUP_INPUT_TYPE_W_SRC | 10 |  |
| LOOKUP_INPUT_TYPE_W_CUT | 11 |  |



<a name="deps-model-pms-v1-LookupOutputType"></a>

### LookupOutputType


| Name | Number | Description |
| ---- | ------ | ----------- |
| LOOKUP_OUTPUT_TYPE_NA | 0 |  |
| LOOKUP_OUTPUT_TYPE_W_CMD | 1 |  |
| LOOKUP_OUTPUT_TYPE_W_ABS | 2 |  |
| LOOKUP_OUTPUT_TYPE_W_MAX_POS | 3 |  |
| LOOKUP_OUTPUT_TYPE_W_MAX_NEG | 4 |  |
| LOOKUP_OUTPUT_TYPE_VA_CMD | 5 |  |



<a name="deps-model-pms-v1-LookupRule-St"></a>

### LookupRule.St


| Name | Number | Description |
| ---- | ------ | ----------- |
| ST_NA | 0 |  |



<a name="deps-model-pms-v1-OutputBlendMode"></a>

### OutputBlendMode


| Name | Number | Description |
| ---- | ------ | ----------- |
| OUTPUT_BLEND_MODE_OVERRIDE | 0 |  |
| OUTPUT_BLEND_MODE_CLAMP_ZERO | 1 |  |
| OUTPUT_BLEND_MODE_ADDITION | 2 |  |
| OUTPUT_BLEND_MODE_SUBTRACT | 3 |  |
| OUTPUT_BLEND_MODE_MULTIPLY | 4 |  |
| OUTPUT_BLEND_MODE_MUL_MASK_ZPOS | 5 |  |
| OUTPUT_BLEND_MODE_OVERRIDE_SOME | 6 |  |
| OUTPUT_BLEND_MODE_FILTER_NONZERO_ADDITION | 7 | value != 0: add value to output value == 0: output is cleared (None) |


 

 

 



<a name="deps_model_system_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/system/model.v1.proto



<a name="deps-model-system-v1-SystemHead"></a>

### SystemHead



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |





 

 

 

 



<a name="deps_model_nameplate_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/nameplate/model.v1.proto



<a name="deps-model-nameplate-v1-Id"></a>

### Id



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vendor | [string](#string) |  |  |
| model | [string](#string) |  |  |
| serial | [string](#string) |  |  |
| sw_version | [string](#string) |  |  |
| hw_version | [string](#string) |  |  |






<a name="deps-model-nameplate-v1-NetworkConfig"></a>

### NetworkConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ips | [NetworkConfig.IpsEntry](#deps-model-nameplate-v1-NetworkConfig-IpsEntry) | repeated |  |






<a name="deps-model-nameplate-v1-NetworkConfig-IpsEntry"></a>

### NetworkConfig.IpsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |





 

 

 

 



<a name="deps_model_rms_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/rms/model.v1.proto



<a name="deps-model-rms-v1-DeleteNode"></a>

### DeleteNode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_id | [string](#string) |  |  |






<a name="deps-model-rms-v1-LocalRms"></a>

### LocalRms
Resource Management System


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| nodes | [NodeItem](#deps-model-rms-v1-NodeItem) | repeated |  |






<a name="deps-model-rms-v1-LocalRms-Command"></a>

### LocalRms.Command



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| create_node | [NodeItem](#deps-model-rms-v1-NodeItem) |  |  |
| delete_node | [DeleteNode](#deps-model-rms-v1-DeleteNode) |  |  |
| measure_request | [MeasureRequest](#deps-model-rms-v1-MeasureRequest) |  |  |






<a name="deps-model-rms-v1-MeasureRequest"></a>

### MeasureRequest







<a name="deps-model-rms-v1-NodeItem"></a>

### NodeItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_id | [string](#string) |  |  |
| kind | [string](#string) |  |  |
| path_prefix | [string](#string) | optional |  |
| args | [NodeItem.ArgsEntry](#deps-model-rms-v1-NodeItem-ArgsEntry) | repeated |  |






<a name="deps-model-rms-v1-NodeItem-ArgsEntry"></a>

### NodeItem.ArgsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [google.protobuf.Value](#google-protobuf-Value) |  |  |






<a name="deps-model-rms-v1-Rpc"></a>

### Rpc







<a name="deps-model-rms-v1-Rpc-CommandRequest"></a>

### Rpc.CommandRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| payload | [LocalRms.Command](#deps-model-rms-v1-LocalRms-Command) | repeated |  |






<a name="deps-model-rms-v1-Rpc-CommandResponse"></a>

### Rpc.CommandResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| payload | [uint32](#uint32) |  |  |






<a name="deps-model-rms-v1-Rpc-MeasureResponse"></a>

### Rpc.MeasureResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| payload | [LocalRms](#deps-model-rms-v1-LocalRms) |  |  |





 

 

 

 



<a name="deps_rpc_header-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/rpc/header.v1.proto



<a name="deps-rpc-v1-Request"></a>

### Request
요청 헤더
함수 콜 형태의 모든 요청은 Request 메시지를 포함하여 전송한다.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  | 요청 고유의 코드 |
| resp_topic | [string](#string) |  | 응답을 전달할 임시 토픽 |






<a name="deps-rpc-v1-Response"></a>

### Response
응답 헤더
요청의 결과를 전달할 때 어떤 요청에 대한 응답인지와 응답의 상태 Response
메시지에 포함하여 전송한다.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  | 요청 메시지의 UUID |
| error | [Response.Error](#deps-rpc-v1-Response-Error) |  | 요청을 성공적으로 처리하였을 경우 NULL |






<a name="deps-rpc-v1-Response-Error"></a>

### Response.Error



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | [Response.ErrorCode](#deps-rpc-v1-Response-ErrorCode) |  | 에러 코드 |
| detail | [string](#string) |  | 에러 상세 이유 |





 


<a name="deps-rpc-v1-Response-ErrorCode"></a>

### Response.ErrorCode


| Name | Number | Description |
| ---- | ------ | ----------- |
| ERROR_CODE_SUCCESS | 0 | 요청의 모든 항목이 성공함 |
| ERROR_CODE_NOT_IMPLEMENTED | 1 | 요청 일부 혹은 모두가 구현되지 않음 (임시적) |
| ERROR_CODE_NOT_SUPPORTED_MESSAGE | 2 | 요청 메시지가 현재 장비에서 지원되지 않음 (영구적) |
| ERROR_CODE_INVALID_PARAMETER | 3 | 요청 메시지 내부의 값이 잘못됨 |
| ERROR_CODE_NOT_APPLICABLE | 4 | 요청의 내용을 적용할 수 없음 (현재 장치의 상태에 따라 임시적으로 해당 요청을 수행할수 없는 경우 등) |
| ERROR_CODE_INTERNAL_ERROR | 5 | 내부 오류로 요청을 수행할 수 없음 |


 

 

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

