# DEPS (Distributed Energy Protocol System)

[데이터 모델 링크](api/md/deps-protos.md)

## 공통 모델

### 1. 개요

본 문서는 ESS 시스템 등 **분산** 에너지 관리 시스템에서 상호 운용성을 증대하기 위한 방법을 정의한다. 상호 운용성을 증대하기 위한 방법은 크게 **공통 데이터 모델의 정의**와 이런 공통 데이터 **모델을 상호 교환하기 위한 프로토콜**의 두가지로 구성된다.

#### 1.1. 취지

공통으로 사용할수 있는 데이터 모델의 **조각**들을 사전에 정의하고, 이러한 조각들을 조합하여 각 제조사의 장치를 표현하는 데이터 모델을 정의할수 있도록 지원한다. 공통된 데이터 모델로 각 장치들을 모델링하면 분산 에너지 관리 시스템 내에서 구성 요소 사이에서 공통으로 **미리 알려진 데이터의 구조**로 데이터를 교환 할 수 있으므로 제조사 마다 파편화된 데이터 구조에 대응하지 않고 동일한 데이터 모델을 기반으로 상호운용성을 증가 시킬 수 있다.

#### 1.2. 데이터 모델 정의

- 데이터 모델은 프로그래밍 언어에 중립적인 [Protocol Buffers](https://protobuf.dev)를 사용해서 모델링 한다. (거의 대부분의 프로그래밍 언어에 대응하는 Protocol Buffers 컴파일러가 존재함)

[프로토콜 버퍼에서 데이터 정의 예시]

```protobuf
message Person {
  string name = 1;
  int32 id = 2;
  string email = 3;
}
```

|언어|Protobuf 지원 여부|
|-|-|
|C++| 공식 지원|
|C#| 공식 지원|
|Dart| 공식 지원|
|Go| 공식 지원|
|Java| 공식 지원|
|Kotlin| 공식 지원|
|Python| 공식 지원|
|Ruby| 공식 지원|
|Objective-C| 공식 지원|
|PHP| 공식 지원|
|C| 비공식 지원|
|Rust| 비공식 지원|
|Javascript| 비공식 지원|
|Typescript| 비공식 지원|

- Protocol Buffers는 필드 이름에 필드 번호를 강제하기 때문에 새로운 필드를 추가하거나 기존 필드를 삭제하여도 호환성에는 큰 문제가 발생하지 않는다. (새로 추가된 필드를 보지 못하거나, 삭제된 필드를 무시하는 방식)

- 모델에서 각 필드의 이름은 sunspec을 참고하였지만 Modbus와 Protocol Buffers 에서 데이터를 정의하는 방법의 차이등으로 인해서 실제 데이터 모델의 구조에는 큰 차이가 발생한다.

##### 1.2.1. Protocol Bufffers 제약 및 sunspec 모델과의 차이점

- 16비트 정수 타입은 uint32/int32 사용한다. (16비트 이하의 정수 타입이 존재하지 않음)
- 정의된 비트 필드는 message로 표현한다.

```protobuf
  message Evt1 {
    bool COMMUNICATION_ERROR = 1;
    bool OVER_TEMP_ALARM = 2;
    bool OVER_TEMP_WARNING = 3;
    ...
  }
```

- ~~정의되지 않은 비트 필드는 uint32 등 사용한다.~~ (TBD)
- 숫자 타입은 SF 없이 float/double 값을 사용한다.
- write 모델의 경우 연관 필드들의 묶음인 [Command](#32-명령-command) 단위로 쓰기가 수행한다.

#### ! 유의 사항

숫자 값들은 float/double을 사용하기 때문에 기본적으로 단위 (k,M,G)는 사용하지 않는다. (예 전력은 kW 단위를 사용하지 않고 W 단위를 사용한다)

#### 1.3. 데이터 전송 프로토콜

공통 데이터 모델의 상호 교환은 [MQTT](https://mqtt.org)프로토콜을 사용한다.

- - -

### 2. 이름 규칙

- Protocol Buffers 이름 규칙에 따라 필드의 이름은 snake_case를 사용한다.

```protobuf
  float v = 20;
  float v_max = 21;
  float v_min = 22;
...
  float a = 30;
  float a_cha_max = 31;
  float a_discha_max = 32;
```

- 단위 및 필드 의미를 나타내는 부분이 앞에 온다.*
- 값의 성격을 규정하거나 제한하는 부분이 뒤에 온다. (min,max)

```txt
*) 예외 - 계층적 위치를 나타내는 속성은 접두어로 함
tot - 전체 누적값 의미, cell - cell 전압, mod 배터리 보듈
```

- 혼란을 방지하고 의미를 명확히 드러내기위해, 필요한 경우 필드이름 경로에서 중복을 허용한다.

```txt
// tmp 부분이 중복되지만 계층화시 가시성을 위해 허용
pcs.tmp.tmp_cab
// ph (phase) 부분이 중복되지만 전류를 의미하는 a와 3상에서 a,b,c 상을 의미하는 a와의 모호성을 방지하기 위해 허용
pcs.ph_v.ph_a
```

- ~~이름 경로의 중복은 허용하지만 데이터의 중복은 가능한 피한다. (계산 가능한 데이터를 별도의 필드로 넣는 등...)~~ (TBD)

#### **[필드 이름 약어 설명]**

|단축어|설명|
|-|-|
|idx|index|
|tot|total(누적 값)|
|evt|event|
|vnd|vender|
|min/max/avg|-|
|cyc|cycle|
|req|request|
|rsp|response|
|st|status|
|ctl|control|
|ctrl|controller|
|rem|remote|
|rst|reset|
|rsv|reserve|
|typ|type|
|warr|warranty|
|op|operation|
|rtg|rating-capacity|
|rte|rate|
|dt|date|
|str|배터리 스트링 (랙) - 배터리 모듈의 그룹|
|mod|배터리 모듈 - 배터리 셀의 그룹|
|tms|time/duration|
|win|window|
|rvrt|revert|
|lim|limit|
|pct|percent|
|aval|available|
|cab|cabinet|
|snK|heat sink|
|trns|transformer|
|ot|other|

- - -

#### 2.1 열거형

- Protocol Buffers에서 열거형 필드는 동일 이름공간 (열거형이 정의된 이름공간)에서 다른 열거형 타입의 필드와 이름 충돌이 발생할 수 있다. 따라서 통상의 Protocol Buffers의 관례와 같이 열거형 필드의 이름 앞에는 열거형 타입의 이름을 접두어로 하여 필드 이름을 정의한다.
  - 일부 Protocol Buffers 컴파일러는 위 접두어를 생략하는 형태로 컴파일하기 때문에 해당 언어에서는 접두어를 붙이는 것이 사용의 편의성을 저해시키지 않는다. (Rust, Go, C#)
- 열거형의 필드 이름은 SCREAMING_SNAKE_CASE 를 사용하여 정의한다.
- Protocol Buffers에서의 제약상 열거형은 반드시 0번 필드로 시작하여야 한다. 만약 0번 필드에 대응되는 의미가 없을 경우에는 더미로 0번 필드의 값을 만들도록 한다.

```protobuf
enum SomeState {
  SOME_STATE_NA = 0;
  SOME_STATE_STOP = 1;
  ...
}
```

### 3. 모델의 구성

- 여러개의 필드(기본 타입)로 하나의 모델(블럭)을 구성한다.

```protobuf
message ThreePhase {
  float ph_a = 1;
  float ph_b = 2;
  float ph_c = 3;
}
```

- 하나의 모델은 다른 모델을 포함할 수 있다.

```protobuf
message Pcs... {
  ThreePhase ph_v = 6;
  ThreePhaseLine pp_v = 7;
  ThreePhaseNSum a = 8;

  float w = 9;
  float hz = 10;
}
```

- 각 모델은 리비전 정보를 포함한 특정 네임스페이스 하위에 정의한다.

```protobuf
package deps.model.esd.v1;
message EsdBank {...}

---------------------------
package deps.model.pcs.v1;
message ThreePhasePcsPart {...}
```

- 디바이스(PCS, 배터리 등)는 하나의 프리셋 모델로 구성하여 사용한다.

```protobuf
package deps.preset.bess.v1;

message Bess {
  .deps.model.esd.v1.EsdBank battery = 1;
  .deps.model.pcs.v1.ThreePhasePcsPart pcs = 2;
  .deps.model.pcs.v1.ThreePhaseGridPart off_grid = 3;
  .deps.model.pcs.v1.ThreePhaseGridPart on_grid = 4;
}

message BessMeasure {
  .google.protobuf.Timestamp timestamp = 1;
  Bess data = 2;
}
```

#### 이름 공간 계층 구성 예시

|이름|설명|
|-|-|
|deps.model|공통 데이터의 **조각**을 정의|
|deps.model.eds| 배터리/에너지 저장 장치를 위한 모델들|
|deps.model.pcs| 에너지 변환 장치를 위한 모델들|
|deps.preset| MQTT Topic으로 교환되는 **상위 데이터** 묶음|
|deps.preset.bess| bess 장치를 위한 공통 모델|
|deps.rpc| MQTT 프로토콜로 윈격 호출을 위한 데이터 정의|
|deps.vnd| 제조사 고유의 데이터를 위한 데이터 정의|

#### 3.1. 기본 데이터 템플릿

일반적으로 하나의 장치는 아래의 데이터들로 모델링을 한다.

|데이터|설명|
|-|-|
|State| 장치 상태 - 열거형으로 정의되는 현재 동작 상태|
|Alarm* - Fault| 고장 알람 - 정상 운전이 불가한 알람 모음|
|Alarm* - Warning| 경고 알람 - 운전 가능하지만 조치가 필요한 알람 모음|
|Alarm* - Status| 상태 알람 - 현재 장치의 상태 정보 모음|
|Measure| 계측 값들 - 장치의 계측 값들|
|Command**| 명령 - 장치에서 수행 가능한 명령들의 모음|

*) 알람은 공통 모델에 정확히 매치되지 않는 제조사 고유 값에 대한 Fallback으로 Other 값을 기본으로 넣어두는것을 권장함

**) 명령은 On/Off 및 출력 지령치와 같이 장치의 운전 중간에 수시로 변경이 필요한 것들을 공통 모델로 추출함. 초기 장치 설치 시에 한번만 설정이 필요한 값은 (CT Calibration 등) 제조사별 고유값([Parameter](#4-제조사별-고유-값-vender-parameter-vender-alarm))으로 접근하는것을 기본으로 함

일반적으로 Protocol Buffers에서는 상태(State) 및 알람(Fault, Waring, Status)과 수행 가능한 명령(Command)을 정의하고 이후에 계측 값을 기술한다.

```protobuf
message Device {
  enum St {
    ST_NA = 0;
    ST_OFF = 1;
    ST_SLEEPING = 2;
    ST_STARTING = 3;
  }
  // Fault와 Warning의 OTHER는 Status 와 조합으로 상태를 표시하기도 함
  // 예) Warning.OTHER와 Status.THROTLED를 같이 표시하여 Warning의 상세 이유를 표시하는 등
  message Fault {
    bool OTHER = 1;
    bool AC_OVER_VOLT = 2;
    bool AC_UNDER_VOLT = 3;
    bool OVER_FREQUENCY = 4;
  }
  message Warning {
    bool OTHER = 1;
    ..
  }
  message Status { bool OTHER = 1;
    ..
  }
  message Command {
    oneof ref {
      float a = 1;
      float v = 2;
      float w = 3;
    }
  }
  ... measure fields ...
}
```

#### 3.1. 알람 플래그 (Fault, Warning, Status)

- 일반적으로 Fault, Warning, Status 3개로 구분된 알람으로 구성한다.
- 각 알람의 필드는 boolean 으로 구성하여 알람 발생/해제 여부만을 표시한다.
- 공통 모델에 포함되지 않는 제조사 고유의 알람은 OTHER로 표시하고 상세한 알람 발생 여부는 [Vender-Alarm](#4-제조사별-고유-값-vender-parameter-vender-alarm)으로 전달한다.

#### 3.2 명령 (Command)

- Command는 장치에 보내질 수 있는 명령의 구조를 정의한다.
- 일반적으로 다양한 명령이 전달될 수 있도록 oneof로 명령을 묶어 그룹화한다.
- 공통 모델에서는 포괄적인 명령을 모두 정의하며, 만약 공통 모델을 구현하는 장치에서 해당 명령의 수행을 지원하지 않을 경우 [ERROR_CODE_NOT_SUPPORTED_MESSAGE](api/md/deps-protos.md#deps-rpc-v1-Response-ErrorCode)로 응답한다.

### 4. 제조사별 고유 값 (Vender-Parameter, Vender-Alarm)

공통 모델에 포함되지 않은 제조사별 고유 상태(파라미터 및 알람)를 표현하기 위해 다음의 구조를 통해 동적으로 고유 상태를 표현한다.

#### 4.1. 숫자 번호와 파라미터 값 혹은 알람 값을 매칭

개념적 예시

```json
// 제조사별 고유 값 정의
{
  1: {
    "param_name": "특정 전압 값",
    "description": "제조사 고유한 특정 측정 전압",
    "unit": "V",
  }
  2: ..
}
```

#### 4.2. 번호의 의미 및 이름은 Meta 모델(ParamMeta, AlarmMeta)을 통해 동적 조회한다

```json
// 읽기 요청 (1번, 5번 파라미터 읽기)
=> [1, 5]

// 읽기 응답 (1번 파라미터 = 100, 5번 파라미터 = 25)
<= [100, 25]
```

#### 4.1. 파라미터

제조사별 고유값은 파라미터 형태로 조회하거나 써넣는 방법을 사용한다.

- 제조사별 고유값 별로 파라미터 번호가 할당되어야 하고, 해당 파라미터 번호로 값을 읽기/쓰기를 명시적으로 요청해야한다.
- 요청/응답을 통해 제조사별 고유값을 읽어온다.

[ParamInfo](api/md/deps-protos.md#deps-vnd-v1-ParamInfo),
[ParamMeta](api/md/deps-protos.md#deps-vnd-v1-ParamMeta)

```protobuf
message ParamInfo {
  message MinMax {
    float min = 1;
    float max = 2;
  }
  message Enum { map<int32, string> collections = 1; }

  string param_name = 1;
  string description = 2;
  string unit = 3;
  oneof constraint {
    MinMax min_max = 4;
    Enum pick = 5;
  }
}

message ParamMeta { map<uint32, ParamInfo> param_infos = 1; }
```

#### 4.2. 알람

- 알람은 현재 발생한 모든 알람을 한번에 읽어 오는 형태로 조회한다.
- 알람 발생 여부는 알람 번호의 위치에 있는 repeated 필드(bool)로 조회한다.

[AlarmMeta](api/md/deps-protos.md#deps-vnd-v1-AlarmMeta),
[AlarmData](api/md/deps-protos.md#deps-vnd-v1-AlarmData)

```protobuf
message AlarmMeta {
  map<uint32, string> status = 1;
  map<uint32, string> warning = 2;
  map<uint32, string> fault = 3;
}

message AlarmData {
  repeated bool status = 1;
  repeated bool warning = 2;
  repeated bool fault = 3;
}
```

- - -

### 5. MQTT 연동

#### 5.1. 토픽

- MQTT 서버에 참여하는 클라이언트는 특정 토픽 접두어를 사용해야하며 그 접두어는 다음과 같이 구성된다.

```markdown
/scope/type/id
```

|항목|의미|
|-|-|
|scope|장치가 속한 그룹|
|type|자칭 타입 - 해당 토픽에서 오고 가는 데이터의 형식을 결정|
|id|장치 고유 ID|

[실험 연구실에 위치한 BESS 장치에 부여된 토픽 접두어 예시]

```markdown
/test-lab/bess/001
```

- 장치에 고유한 토픽 접두어가 부여되면 (일반적으로 관리자가 부여), 해당 장치는 해당 접두어에 특정 접미어가 합처진 토픽에 대해 발행/구독을 하여 데이터를 주고 받는다.

##### 5.1.1 토픽 접미어

[**공통 데이터**]

|접미어|의미 (장치 관점)|retained|
|-|-|-|
|measure|주기적으로 자신의 계측값을 발행한다|no|
|command*|명령처리 **요청**을 구독하고 처리한다|no|
|event|발생한 이벤트를 발행한다|no|

[**제조사 고유 데이터 (선택적 구현)**]

|접미어|의미 (장치 관점)|retained|
|-|-|-|
|vnd/param*|제조사 고유의 읽기/쓰기 데이터 **요청**을 구독하고 처리한다|no|
|vnd/param-meta|제조사 고유의 읽기/쓰기 데이터에 대한 [인덱스-설명] 메타 데이터|yes|
|vnd/alarm*|제조사 고유의 알람 데이터 **요청**을 구독하고 처리한다|no|
|vnd/alarm-meta|제조사 고유의 알라 데이터에 대한 [인덱스-이름] 메타 데이터|yes|

\* 장치에서 구독하는 토픽은 요청(Request) 형태로 전달되며, 경우에 따라 처리 결과를 특정 토픽으로 발행해야할 필요가 있음 ([MQTT RPC](#52-mqtt-rpc))

#### 5.2. MQTT RPC

장치에서 특정 명령 등 행위를 요청하고 그 결과를 받아야할 필요가 있을 때, MQTT를 이용하여 다음과 같이 RPC 호출처럼 처리할 수 있다.

##### 5.2.1. RPC 요청에 다음의 Header 데이터를 요청 데이터와 함께 전송한다. 응답이 필요하지 않을 경우 Header 데이터를 제외하고 (null) 요청 데이터만 전송한다

```protobuf
message Request {
  string uuid = 1;
  string resp_topic = 2;
}
```

|필드|의미|
|-|-|
|uuid|요청 고유 ID로 응답 토픽에 발행되는 응답에 대해 필터링을 위해 사용된다.|
|resp_topic|응답을 주고 받는 토픽이다. 요청하는 측에서는 본 토픽을 구독 후 요청을 발행한 뒤 응답이 오기르 대기한다. 처리 측에서는 요청을 처리하면 본 토픽에 대해 결과를 발행한다.|

##### 5.2.2. RPC 요청 처리 측에서는 자신의 요청 처리 토픽 (command, param, alarm 등)으로 요청을 받고 요청을 처리한다. 요청에 Header 데이터가 존재했다면 해당 Header 정보에 대해 응답 Header와 함께 결과를 발행한다

```protobuf
message Response {
  enum ErrorCode {
    SUCCESS = 0;
    NOT_SUPPORTED_MESSAGE = 1;
    NOT_APPLICABLE = 2;
  }
  string uuid = 1;
  ErrorCode error_code = 2;
  string error_msg = 3;
}
```

[ErrorCode](api/md/deps-protos.md#deps-rpc-v1-Response-ErrorCode)

|ErrorCode|의미|
|-|-|
|SUCCESS|요청 처리에 성공|
|NOT_SUPPORTED_MESSAGE|요청이 지원되지 않거나 잘못된 형식의 요청임|
|NOT_APPLICABLE|요청 형식을 올바르나, 요청이 유효하지 않은 값을 포함함|
|...|...|

|Field|의미|
|-|-|
|uuid|요청 측에서 보내온 uuid의 복사값|
|error_code|요청 처리 실패의 이유 - 성공일 경우 (null)|
|error_msg|요청 처리 실패의 상세 이유 - 성공일 경우 빈 문자열 ("")|

### 6. 장치 타입

|타입|설명|
|-|-|
|bess| bess 장치 - 배터리 + PCS로 구성된 장치. 계통에서 충방전을 수행한다. 선택적으로 부하에 직접 전력을 공급하는 기능을 포함한다.|
