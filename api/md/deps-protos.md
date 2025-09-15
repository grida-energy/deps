# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [deps/preset/bess/model.v1.proto](#deps_preset_bess_model-v1-proto)
    - [Bess](#deps-preset-bess-v1-Bess)
    - [BessCommand](#deps-preset-bess-v1-BessCommand)
    - [BessMeasure](#deps-preset-bess-v1-BessMeasure)
    - [HybridBess](#deps-preset-bess-v1-HybridBess)
    - [HybridBessMeasure](#deps-preset-bess-v1-HybridBessMeasure)
    - [Rpc](#deps-preset-bess-v1-Rpc)
    - [Rpc.BessRequest](#deps-preset-bess-v1-Rpc-BessRequest)
    - [Rpc.BessResponse](#deps-preset-bess-v1-Rpc-BessResponse)
  
- [deps/preset/upms/model.v1.proto](#deps_preset_upms_model-v1-proto)
    - [PmsCommand](#deps-preset-upms-v1-PmsCommand)
    - [PmsMeasure](#deps-preset-upms-v1-PmsMeasure)
    - [Rpc](#deps-preset-upms-v1-Rpc)
    - [Rpc.PmsRequest](#deps-preset-upms-v1-Rpc-PmsRequest)
    - [Rpc.PmsResponse](#deps-preset-upms-v1-Rpc-PmsResponse)
  
- [deps/vnd/rpc.v1.proto](#deps_vnd_rpc-v1-proto)
    - [Rpc](#deps-vnd-v1-Rpc)
    - [Rpc.AlarmEvent](#deps-vnd-v1-Rpc-AlarmEvent)
    - [Rpc.ParamReadWriteRequest](#deps-vnd-v1-Rpc-ParamReadWriteRequest)
    - [Rpc.ParamReadWriteResponse](#deps-vnd-v1-Rpc-ParamReadWriteResponse)
    - [Rpc.ParamRequest](#deps-vnd-v1-Rpc-ParamRequest)
    - [Rpc.ParamResponse](#deps-vnd-v1-Rpc-ParamResponse)
  
- [deps/vnd/parameter.v1.proto](#deps_vnd_parameter-v1-proto)
    - [ParamBlock](#deps-vnd-v1-ParamBlock)
    - [ParamIdRange](#deps-vnd-v1-ParamIdRange)
    - [ParamInfo](#deps-vnd-v1-ParamInfo)
    - [ParamInfo.Enum](#deps-vnd-v1-ParamInfo-Enum)
    - [ParamInfo.Enum.CollectionsEntry](#deps-vnd-v1-ParamInfo-Enum-CollectionsEntry)
    - [ParamInfo.MinMax](#deps-vnd-v1-ParamInfo-MinMax)
    - [ParamMeta](#deps-vnd-v1-ParamMeta)
    - [ParamMeta.ParamInfosEntry](#deps-vnd-v1-ParamMeta-ParamInfosEntry)
  
- [deps/vnd/alarm.v1.proto](#deps_vnd_alarm-v1-proto)
    - [AlarmData](#deps-vnd-v1-AlarmData)
    - [AlarmMeta](#deps-vnd-v1-AlarmMeta)
    - [AlarmMeta.FaultEntry](#deps-vnd-v1-AlarmMeta-FaultEntry)
    - [AlarmMeta.StatusEntry](#deps-vnd-v1-AlarmMeta-StatusEntry)
    - [AlarmMeta.WarningEntry](#deps-vnd-v1-AlarmMeta-WarningEntry)
  
    - [AlarmType](#deps-vnd-v1-AlarmType)
  
- [deps/model/pcs/model.v1.proto](#deps_model_pcs_model-v1-proto)
    - [DcDcConverter](#deps-model-pcs-v1-DcDcConverter)
    - [DcDcConverter.Command](#deps-model-pcs-v1-DcDcConverter-Command)
    - [DcDcConverter.Fault](#deps-model-pcs-v1-DcDcConverter-Fault)
    - [DcDcConverter.Status](#deps-model-pcs-v1-DcDcConverter-Status)
    - [DcDcConverter.Warning](#deps-model-pcs-v1-DcDcConverter-Warning)
    - [DcPart](#deps-model-pcs-v1-DcPart)
    - [TemperaturePart](#deps-model-pcs-v1-TemperaturePart)
    - [ThreePhase](#deps-model-pcs-v1-ThreePhase)
    - [ThreePhaseGridPart](#deps-model-pcs-v1-ThreePhaseGridPart)
    - [ThreePhaseLine](#deps-model-pcs-v1-ThreePhaseLine)
    - [ThreePhaseNSum](#deps-model-pcs-v1-ThreePhaseNSum)
    - [ThreePhasePcsPart](#deps-model-pcs-v1-ThreePhasePcsPart)
    - [ThreePhasePcsPart.Command](#deps-model-pcs-v1-ThreePhasePcsPart-Command)
    - [ThreePhasePcsPart.Command.Reference](#deps-model-pcs-v1-ThreePhasePcsPart-Command-Reference)
    - [ThreePhasePcsPart.Fault](#deps-model-pcs-v1-ThreePhasePcsPart-Fault)
    - [ThreePhasePcsPart.Status](#deps-model-pcs-v1-ThreePhasePcsPart-Status)
    - [ThreePhasePcsPart.Warning](#deps-model-pcs-v1-ThreePhasePcsPart-Warning)
  
    - [DcDcConverter.St](#deps-model-pcs-v1-DcDcConverter-St)
    - [ThreePhasePcsPart.Command.Action](#deps-model-pcs-v1-ThreePhasePcsPart-Command-Action)
    - [ThreePhasePcsPart.DirPwr](#deps-model-pcs-v1-ThreePhasePcsPart-DirPwr)
    - [ThreePhasePcsPart.St](#deps-model-pcs-v1-ThreePhasePcsPart-St)
  
- [deps/model/net/model.v1.proto](#deps_model_net_model-v1-proto)
    - [AcLine](#deps-model-net-v1-AcLine)
    - [AcLineSum](#deps-model-net-v1-AcLineSum)
    - [Energy](#deps-model-net-v1-Energy)
  
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
    - [EsdSummary](#deps-model-esd-v1-EsdSummary)
    - [EsdSummary.CellCount](#deps-model-esd-v1-EsdSummary-CellCount)
    - [EsdSummary.Command](#deps-model-esd-v1-EsdSummary-Command)
    - [EsdSummary.Evt1](#deps-model-esd-v1-EsdSummary-Evt1)
  
    - [EsdBank.Command.SetOp](#deps-model-esd-v1-EsdBank-Command-SetOp)
    - [EsdBank.St](#deps-model-esd-v1-EsdBank-St)
    - [EsdBank.StCha](#deps-model-esd-v1-EsdBank-StCha)
    - [EsdString.Command.SetCon](#deps-model-esd-v1-EsdString-Command-SetCon)
    - [EsdString.Command.SetEna](#deps-model-esd-v1-EsdString-Command-SetEna)
    - [EsdString.ConFail](#deps-model-esd-v1-EsdString-ConFail)
    - [EsdSummary.ChaSt](#deps-model-esd-v1-EsdSummary-ChaSt)
    - [EsdSummary.SetOp](#deps-model-esd-v1-EsdSummary-SetOp)
    - [EsdSummary.State](#deps-model-esd-v1-EsdSummary-State)
  
- [deps/model/esd/extra.v1.proto](#deps_model_esd_extra-v1-proto)
    - [ChaLimit](#deps-model-esd-v1-ChaLimit)
    - [Conn](#deps-model-esd-v1-Conn)
  
    - [Conn.Conn](#deps-model-esd-v1-Conn-Conn)
  
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
| battery | [deps.model.esd.v1.EsdBank](#deps-model-esd-v1-EsdBank) |  | 배터리 모델 |
| pcs | [deps.model.pcs.v1.ThreePhasePcsPart](#deps-model-pcs-v1-ThreePhasePcsPart) |  | PCS 모델 |
| off_grid | [deps.model.pcs.v1.ThreePhaseGridPart](#deps-model-pcs-v1-ThreePhaseGridPart) |  | Off Grid (부하 연결 부) |
| on_grid | [deps.model.pcs.v1.ThreePhaseGridPart](#deps-model-pcs-v1-ThreePhaseGridPart) |  | On Grid (계통 연결 부) |






<a name="deps-preset-bess-v1-BessCommand"></a>

### BessCommand
BESS 명령


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| battery | [deps.model.esd.v1.EsdBank.Command](#deps-model-esd-v1-EsdBank-Command) |  | 배터리 명령 |
| pcs | [deps.model.pcs.v1.ThreePhasePcsPart.Command](#deps-model-pcs-v1-ThreePhasePcsPart-Command) |  | PCS 명령 |






<a name="deps-preset-bess-v1-BessMeasure"></a>

### BessMeasure
BESS 계측 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | 타임 스탬프 |
| data | [Bess](#deps-preset-bess-v1-Bess) |  | BESS 데이터 |






<a name="deps-preset-bess-v1-HybridBess"></a>

### HybridBess
PV 입력이 존재하는 BESS (모델에 대한 정제 필요)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| battery | [deps.model.esd.v1.EsdBank](#deps-model-esd-v1-EsdBank) |  | 배터리 모델 |
| pcs | [deps.model.pcs.v1.ThreePhasePcsPart](#deps-model-pcs-v1-ThreePhasePcsPart) |  | PCS 모델 |
| off_grid | [deps.model.pcs.v1.ThreePhaseGridPart](#deps-model-pcs-v1-ThreePhaseGridPart) |  | Off Grid (부하 연결 부) |
| on_grid | [deps.model.pcs.v1.ThreePhaseGridPart](#deps-model-pcs-v1-ThreePhaseGridPart) |  | On Grid (계통 연결 부) |
| pv | [deps.model.source.v1.PvLine](#deps-model-source-v1-PvLine) |  | PV 연결 부 |






<a name="deps-preset-bess-v1-HybridBessMeasure"></a>

### HybridBessMeasure
하이브리드 BESS 계측 정보


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | 타임 스탬프 |
| data | [HybridBess](#deps-preset-bess-v1-HybridBess) |  | 하이브리드 BESS 데이터 |






<a name="deps-preset-bess-v1-Rpc"></a>

### Rpc
RPC 메시지






<a name="deps-preset-bess-v1-Rpc-BessRequest"></a>

### Rpc.BessRequest
BESS RPC 요청


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| head | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  | 요청 헤더 |
| data | [BessCommand](#deps-preset-bess-v1-BessCommand) |  | BESS 명령 |






<a name="deps-preset-bess-v1-Rpc-BessResponse"></a>

### Rpc.BessResponse
BESS RPC 응답


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| head | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  | 응답 헤더 |





 

 

 

 



<a name="deps_preset_upms_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/preset/upms/model.v1.proto



<a name="deps-preset-upms-v1-PmsCommand"></a>

### PmsCommand



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lookup | [deps.model.pms.v1.LookupRule.Command](#deps-model-pms-v1-LookupRule-Command) |  |  |






<a name="deps-preset-upms-v1-PmsMeasure"></a>

### PmsMeasure



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lookup | [deps.model.pms.v1.LookupRule](#deps-model-pms-v1-LookupRule) |  |  |
| input | [deps.model.pms.v1.LookupInput](#deps-model-pms-v1-LookupInput) |  |  |
| output | [deps.model.pms.v1.LookupOutput](#deps-model-pms-v1-LookupOutput) |  |  |






<a name="deps-preset-upms-v1-Rpc"></a>

### Rpc







<a name="deps-preset-upms-v1-Rpc-PmsRequest"></a>

### Rpc.PmsRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| payload | [PmsCommand](#deps-preset-upms-v1-PmsCommand) | repeated |  |






<a name="deps-preset-upms-v1-Rpc-PmsResponse"></a>

### Rpc.PmsResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| n | [uint32](#uint32) |  |  |





 

 

 

 



<a name="deps_vnd_rpc-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/vnd/rpc.v1.proto



<a name="deps-vnd-v1-Rpc"></a>

### Rpc







<a name="deps-vnd-v1-Rpc-AlarmEvent"></a>

### Rpc.AlarmEvent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  |  |
| alarm_data | [AlarmData](#deps-vnd-v1-AlarmData) |  |  |






<a name="deps-vnd-v1-Rpc-ParamReadWriteRequest"></a>

### Rpc.ParamReadWriteRequest



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
| head | [deps.rpc.v1.Request](#deps-rpc-v1-Request) |  |  |
| data | [Rpc.ParamReadWriteRequest](#deps-vnd-v1-Rpc-ParamReadWriteRequest) |  | repeated ParamOps data = 3; |






<a name="deps-vnd-v1-Rpc-ParamResponse"></a>

### Rpc.ParamResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| head | [deps.rpc.v1.Response](#deps-rpc-v1-Response) |  |  |
| data | [Rpc.ParamReadWriteResponse](#deps-vnd-v1-Rpc-ParamReadWriteResponse) |  | repeated ParamResult data = 4; |





 

 

 

 



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
| pick | [ParamInfo.Enum](#deps-vnd-v1-ParamInfo-Enum) |  |  |






<a name="deps-vnd-v1-ParamInfo-Enum"></a>

### ParamInfo.Enum



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| collections | [ParamInfo.Enum.CollectionsEntry](#deps-vnd-v1-ParamInfo-Enum-CollectionsEntry) | repeated |  |






<a name="deps-vnd-v1-ParamInfo-Enum-CollectionsEntry"></a>

### ParamInfo.Enum.CollectionsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [int32](#int32) |  |  |
| value | [string](#string) |  |  |






<a name="deps-vnd-v1-ParamInfo-MinMax"></a>

### ParamInfo.MinMax



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min | [float](#float) |  |  |
| max | [float](#float) |  |  |






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


 

 

 



<a name="deps_model_pcs_model-v1-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## deps/model/pcs/model.v1.proto



<a name="deps-model-pcs-v1-DcDcConverter"></a>

### DcDcConverter
DC-DC 컨버터






<a name="deps-model-pcs-v1-DcDcConverter-Command"></a>

### DcDcConverter.Command



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| enable | [bool](#bool) |  |  |






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






<a name="deps-model-pcs-v1-ThreePhasePcsPart-Command"></a>

### ThreePhasePcsPart.Command
명령


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| action | [ThreePhasePcsPart.Command.Action](#deps-model-pcs-v1-ThreePhasePcsPart-Command-Action) |  |  |
| ref | [ThreePhasePcsPart.Command.Reference](#deps-model-pcs-v1-ThreePhasePcsPart-Command-Reference) |  |  |






<a name="deps-model-pcs-v1-ThreePhasePcsPart-Command-Reference"></a>

### ThreePhasePcsPart.Command.Reference
지령치 - 장치에 따라 일부만 적용할 수 있음


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| a | [float](#float) |  | 전류 지령치 |
| v | [float](#float) |  | 전압 지령치 - UPS 등 |
| w | [float](#float) |  | 유효 전력 지령치 |
| dcv | [float](#float) |  | DC 전압 지령치 - DC 시뮬레이터 등 |
| dca | [float](#float) |  | DC 전류 지령치 |
| p_pct | [float](#float) |  | 유효 전력 백분율 지령치 |
| q_pct | [float](#float) |  | 무효 전력 백분율 지령치 |
| pf | [float](#float) |  | 역률 지령치 |
| hz | [float](#float) |  | 주파수 지령치 |






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
| CB_TRIP | [bool](#bool) |  | 차단기 트립 |






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



<a name="deps-model-pcs-v1-ThreePhasePcsPart-Command-Action"></a>

### ThreePhasePcsPart.Command.Action
동작

| Name | Number | Description |
| ---- | ------ | ----------- |
| ACTION_NA | 0 |  |
| ACTION_CONNECT | 1 | 운전 시작 |
| ACTION_DISCONNECT | 2 | 운전 정지 |
| ACTION_RESET_ALARM | 3 | 알람 리셋 |



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
| ST_OFF | 1 | 기타 |
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
| hz | [float](#float) |  | maby needs to be |
| w | [float](#float) |  |  |
| va | [float](#float) |  |  |
| var | [float](#float) |  |  |
| pf | [float](#float) |  |  |






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






<a name="deps-model-net-v1-Energy"></a>

### Energy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| exported | [double](#double) |  |  |
| imported | [double](#double) |  |  |





 

 

 

 



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
| set_op | [EsdBank.Command.SetOp](#deps-model-esd-v1-EsdBank-Command-SetOp) |  | 동작 설정 |
| strs | [EsdString](#deps-model-esd-v1-EsdString) | repeated | String (Rack) 정보 |






<a name="deps-model-esd-v1-EsdBank-CellCount"></a>

### EsdBank.CellCount
Bank Cell 요약


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v_max | [float](#float) |  | 최대 Cell 전압 |
| v_max_str | [uint32](#uint32) |  | 최대 Cell 전압의 String 위치 |
| v_max_mod | [uint32](#uint32) |  | 최대 Cell 전압의 Module 위치 |
| v_min | [float](#float) |  | 최소 Cell 전압 |
| v_min_str | [uint32](#uint32) |  | 최소 Cell 전압의 String 위치 |
| v_min_mod | [uint32](#uint32) |  | 최소 Cell 전압의 Module 위치 |
| v_avg | [float](#float) |  | 평균 Cell 전압 |
| n_bal | [uint32](#uint32) |  | Cell Balance 갯수 |






<a name="deps-model-esd-v1-EsdBank-Command"></a>

### EsdBank.Command
명령


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| set_op | [EsdBank.Command.SetOp](#deps-model-esd-v1-EsdBank-Command-SetOp) |  | 동작 설정 |






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
| tmp_max_str | [uint32](#uint32) |  | 최고 온도의 String 위치 |
| tmp_max_mod | [uint32](#uint32) |  | 최고 온도의 Module 위치 |
| tmp_min | [float](#float) |  | 최소 온도 |
| tmp_min_str | [uint32](#uint32) |  | 최소 온도의 String 위치 |
| tmp_min_mod | [uint32](#uint32) |  | 최소 온도의 Module 위치 |
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
| v_max_str | [uint32](#uint32) |  | 최대 String 전압의 String 위치 |
| v_min | [float](#float) |  | 최소 String 전압 |
| v_min_str | [uint32](#uint32) |  | 최소 String 전압의 String 위치 |
| v_avg | [float](#float) |  | 평균 String 전압 |
| a_max | [float](#float) |  | 최대 String 전류 |
| a_max_str | [uint32](#uint32) |  | 최대 String 전류의 String 위치 |
| a_min | [float](#float) |  | 최소 String 전류 |
| a_min_str | [uint32](#uint32) |  | 최소 String 전류의 String 위치 |
| a_avg | [float](#float) |  | 평균 String 전류 |
| n_conn | [uint32](#uint32) |  | 연결된 String 갯수 |






<a name="deps-model-esd-v1-EsdBank-Warning"></a>

### EsdBank.Warning
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
| set_ena | [EsdString.Command.SetEna](#deps-model-esd-v1-EsdString-Command-SetEna) |  | 활성화 설정 |
| set_con | [EsdString.Command.SetCon](#deps-model-esd-v1-EsdString-Command-SetCon) |  | 동작 설정 |
| mods | [EsdModule](#deps-model-esd-v1-EsdModule) | repeated | 모듈 정보 |






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
컨택터 상태


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| CONTACTOR_0 | [bool](#bool) |  |  |
| CONTACTOR_1 | [bool](#bool) |  |  |
| CONTACTOR_2 | [bool](#bool) |  |  |
| CONTACTOR_3 | [bool](#bool) |  |  |
| CONTACTOR_4 | [bool](#bool) |  |  |
| CONTACTOR_5 | [bool](#bool) |  |  |
| CONTACTOR_6 | [bool](#bool) |  |  |
| CONTACTOR_7 | [bool](#bool) |  |  |
| CONTACTOR_8 | [bool](#bool) |  |  |
| CONTACTOR_9 | [bool](#bool) |  |  |
| CONTACTOR_10 | [bool](#bool) |  |  |
| CONTACTOR_11 | [bool](#bool) |  |  |
| CONTACTOR_12 | [bool](#bool) |  |  |
| CONTACTOR_13 | [bool](#bool) |  |  |
| CONTACTOR_14 | [bool](#bool) |  |  |
| CONTACTOR_15 | [bool](#bool) |  |  |
| CONTACTOR_16 | [bool](#bool) |  |  |
| CONTACTOR_17 | [bool](#bool) |  |  |
| CONTACTOR_18 | [bool](#bool) |  |  |
| CONTACTOR_19 | [bool](#bool) |  |  |
| CONTACTOR_20 | [bool](#bool) |  |  |
| CONTACTOR_21 | [bool](#bool) |  |  |
| CONTACTOR_22 | [bool](#bool) |  |  |
| CONTACTOR_23 | [bool](#bool) |  |  |
| CONTACTOR_24 | [bool](#bool) |  |  |
| CONTACTOR_25 | [bool](#bool) |  |  |
| CONTACTOR_26 | [bool](#bool) |  |  |
| CONTACTOR_27 | [bool](#bool) |  |  |
| CONTACTOR_28 | [bool](#bool) |  |  |
| CONTACTOR_29 | [bool](#bool) |  |  |
| CONTACTOR_30 | [bool](#bool) |  |  |






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






<a name="deps-model-esd-v1-EsdSummary"></a>

### EsdSummary
폐지됨 - 더 이상 사용되지 않음


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| soc | [float](#float) |  |  |
| dod | [float](#float) |  |  |
| soh | [float](#float) |  |  |
| n_cyc | [uint32](#uint32) |  |  |
| cha_st | [EsdSummary.ChaSt](#deps-model-esd-v1-EsdSummary-ChaSt) |  |  |
| hb | [uint32](#uint32) |  |  |
| state | [EsdSummary.State](#deps-model-esd-v1-EsdSummary-State) |  |  |
| state_vnd | [uint32](#uint32) |  |  |
| evt1 | [EsdSummary.Evt1](#deps-model-esd-v1-EsdSummary-Evt1) |  |  |
| v | [float](#float) |  |  |
| v_max | [float](#float) |  |  |
| v_min | [float](#float) |  |  |
| cnt_cell | [EsdSummary.CellCount](#deps-model-esd-v1-EsdSummary-CellCount) |  |  |
| a | [float](#float) |  |  |
| a_cha_max | [float](#float) |  |  |
| a_discha_max | [float](#float) |  |  |
| w | [float](#float) |  |  |
| set_op | [EsdSummary.SetOp](#deps-model-esd-v1-EsdSummary-SetOp) |  |  |
| bank | [EsdBank](#deps-model-esd-v1-EsdBank) |  |  |






<a name="deps-model-esd-v1-EsdSummary-CellCount"></a>

### EsdSummary.CellCount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| v_max | [float](#float) |  |  |
| v_max_str | [uint32](#uint32) |  |  |
| v_max_mod | [uint32](#uint32) |  |  |
| v_min | [float](#float) |  |  |
| v_min_str | [uint32](#uint32) |  |  |
| v_min_mod | [uint32](#uint32) |  |  |
| v_avg | [float](#float) |  |  |






<a name="deps-model-esd-v1-EsdSummary-Command"></a>

### EsdSummary.Command



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| set_op | [EsdSummary.SetOp](#deps-model-esd-v1-EsdSummary-SetOp) |  |  |






<a name="deps-model-esd-v1-EsdSummary-Evt1"></a>

### EsdSummary.Evt1



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| COMMUNICATION_ERROR | [bool](#bool) |  |  |
| OVER_TEMP_ALARM | [bool](#bool) |  |  |
| OVER_TEMP_WARNING | [bool](#bool) |  |  |
| UNDER_TEMP_ALARM | [bool](#bool) |  |  |
| UNDER_TEMP_WARNING | [bool](#bool) |  |  |
| OVER_CHARGE_CURRENT_ALARM | [bool](#bool) |  |  |
| OVER_CHARGE_CURRENT_WARNING | [bool](#bool) |  |  |
| OVER_DISCHARGE_CURRENT_ALARM | [bool](#bool) |  |  |
| OVER_DISCHARGE_CURRENT_WARNING | [bool](#bool) |  |  |
| OVER_VOLT_ALARM | [bool](#bool) |  |  |
| OVER_VOLT_WARNING | [bool](#bool) |  |  |
| UNDER_VOLT_ALARM | [bool](#bool) |  |  |
| UNDER_VOLT_WARNING | [bool](#bool) |  |  |
| UNDER_SOC_MIN_ALARM | [bool](#bool) |  |  |
| UNDER_SOC_MIN_WARNING | [bool](#bool) |  |  |
| OVER_SOC_MAX_ALARM | [bool](#bool) |  |  |
| OVER_SOC_MAX_WARNING | [bool](#bool) |  |  |
| VOLTAGE_IMBALANCE_WARNING | [bool](#bool) |  |  |
| TEMPERATURE_IMBALANCE_ALARM | [bool](#bool) |  |  |
| TEMPERATURE_IMBALANCE_WARNING | [bool](#bool) |  |  |
| CONTACTOR_ERROR | [bool](#bool) |  |  |
| FAN_ERROR | [bool](#bool) |  |  |
| GROUND_FAULT | [bool](#bool) |  |  |
| OPEN_DOOR_ERROR | [bool](#bool) |  |  |
| CURRENT_IMBALANCE_WARNING | [bool](#bool) |  |  |
| OTHER_ALARM | [bool](#bool) |  |  |
| OTHER_WARNING | [bool](#bool) |  |  |
| RESERVED_1 | [bool](#bool) |  |  |
| CONFIGURATION_ALARM | [bool](#bool) |  |  |
| CONFIGURATION_WARNING | [bool](#bool) |  |  |





 


<a name="deps-model-esd-v1-EsdBank-Command-SetOp"></a>

### EsdBank.Command.SetOp
동작 설정

| Name | Number | Description |
| ---- | ------ | ----------- |
| SET_OP_NA | 0 |  |
| SET_OP_CONNECT | 1 | 연결 |
| SET_OP_DISCONNECT | 2 | 연결 해제 |



<a name="deps-model-esd-v1-EsdBank-St"></a>

### EsdBank.St
시스템 상태

| Name | Number | Description |
| ---- | ------ | ----------- |
| ST_NA | 0 |  |
| ST_DISCONNECTED | 1 | 연결 해제 됨 |
| ST_INITIALIZING | 2 | 초기화 중 |
| ST_CONNECTED | 3 | 연결 됨 |
| ST_STANDBY | 4 | 대기 중 |
| ST_SOC_PROTECTION | 5 | SoC 보호 상태 |
| ST_SUSPENDING | 6 | 일시 중지 상태 |
| ST_FAULT | 99 | 고장 상태 |



<a name="deps-model-esd-v1-EsdBank-StCha"></a>

### EsdBank.StCha
배터리 충전 상태

| Name | Number | Description |
| ---- | ------ | ----------- |
| ST_CHA_NA | 0 |  |
| ST_CHA_OFF | 1 | 정지 |
| ST_CHA_EMPTY | 2 | 완전 방전됨 |
| ST_CHA_DISCHARGING | 3 | 방전 중 |
| ST_CHA_CHARGING | 4 | 충전 중 |
| ST_CHA_FULL | 5 | 완전 충전됨 |
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
| CON_FAIL_NO_FAILURE | 0 | 고장 없음 |
| CON_FAIL_BUTTON_PUSHED | 1 | 비상 정지 |
| CON_FAIL_STR_GROUND_FAULT | 2 | 접지 오류 |
| CON_FAIL_OUTSIDE_VOLTAGE_RANGE | 3 | 허용 전압 범위 초과 |
| CON_FAIL_STRING_NOT_ENABLED | 4 | 비활성화 |
| CON_FAIL_FUSE_OPEN | 5 | 퓨즈 개방 |
| CON_FAIL_CONTACTOR_FAILURE | 6 | 컨택터 동작 실패 |
| CON_FAIL_PRECHARGE_FAILURE | 7 | 초기충전 실패 |
| CON_FAIL_STRING_FAULT | 8 | String 고장 |



<a name="deps-model-esd-v1-EsdSummary-ChaSt"></a>

### EsdSummary.ChaSt


| Name | Number | Description |
| ---- | ------ | ----------- |
| CHA_ST_NA | 0 |  |
| CHA_ST_OFF | 1 |  |
| CHA_ST_EMPTY | 2 |  |
| CHA_ST_DISCHARGING | 3 |  |
| CHA_ST_CHARGING | 4 |  |
| CHA_ST_FULL | 5 |  |
| CHA_ST_HOLDING | 6 |  |
| CHA_ST_TESTING | 7 |  |



<a name="deps-model-esd-v1-EsdSummary-SetOp"></a>

### EsdSummary.SetOp


| Name | Number | Description |
| ---- | ------ | ----------- |
| SETOP_NA | 0 |  |
| SETOP_CONNECT | 1 |  |
| SETOP_DISCONNECT | 2 |  |



<a name="deps-model-esd-v1-EsdSummary-State"></a>

### EsdSummary.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| STATE_NA | 0 |  |
| STATE_DISCONNECTED | 1 |  |
| STATE_INITIALIZING | 2 |  |
| STATE_CONNECTED | 3 |  |
| STATE_STANDBY | 4 |  |
| STATE_SOC_PROTECTION | 5 |  |
| STATE_SUSPENDING | 6 |  |
| STATE_FAULT | 99 |  |


 

 

 



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
| conn | [Conn.Conn](#deps-model-esd-v1-Conn-Conn) |  |  |





 


<a name="deps-model-esd-v1-Conn-Conn"></a>

### Conn.Conn


| Name | Number | Description |
| ---- | ------ | ----------- |
| DISCONNECT | 0 | 연결 해제 |
| CONNECT | 1 | 연결 |


 

 

 



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

