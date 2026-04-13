# DEPS (Distributed Energy Protocol System) - v1

[데이터 모델 링크](api/md/deps-protos.md)

## 공통 모델

### 1. 개요

본 문서는 ESS 시스템 등 **분산** 에너지 관리 시스템에서 장치 간 상호 운용성을 증대하기 위한 방안을 정의한다. 상호 운용성을 증대하기 위한 방법은 크게 **공통 데이터 모델의 정의**와 이런 공통 데이터 **모델을 상호 교환하기 위한 프로토콜**의 두가지로 구성된다.

#### 1.1. 취지

에너지 관리 분야에서 각 분산 장치들은 제조사별로 데이터 모델이 파편화되어 있어 상호 운용시 장비의 조합이 변경되면 그 때마다 개발 비용이 발생할 수 밖에 없다. 이러한 문제는 파편화된 데이터 모델을 유형별로 그룹화하고 그 안의 데이터를 표준화한다면 상당부분 해소될 수 있다.

DEPS에서는 공통으로 사용할 수 있는 데이터 모델의 **조각**들을 사전에 정의하고, 이러한 조각들을 조합하여 각 제조사의 장치를 표현하는 데이터 모델을 정의할수 있도록 지원한다. 표준화된 공통 데이터 모델을 활용하면 시스템 내 구성 요소들이 **사전 정의된 데이터 구조**를 기반으로 정보를 교환할 수 있다. 이를 통해 제조사별로 파편화된 데이터 형식에 개별 대응해야 하는 비용을 절감하고, 시스템 전체의 상호 운용성을 극대화할 수 있다.

#### 1.2. 데이터 모델 정의

- 데이터 모델은 프로그래밍 언어에 중립적인 [Protocol Buffers](https://protobuf.dev)를 사용해서 모델링 한다. Protocol Buffers는 대부분의 프로그래밍 언어를 지원하므로 다양한 개발 환경에서 일관된 데이터 구조를 유지할 수 있다.

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
|C++|공식 지원|
|C#|공식 지원|
|Dart|공식 지원|
|Go|공식 지원|
|Java|공식 지원|
|Kotlin|공식 지원|
|Python|공식 지원|
|Ruby|공식 지원|
|Objective-C|공식 지원|
|PHP|공식 지원|
|C|비공식 지원|
|Rust|비공식 지원|
|Javascript|비공식 지원|
|Typescript|비공식 지원|

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

- 숫자 타입은 SF(Scale Factor) 없이 float/double 값을 사용한다.
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
|deps.model|공통 데이터의 **조각**을 정의 - 재사용성이 높은 작은 모델들로 구성|
|deps.model.eds|배터리 및 에너지 저장 장치를 위한 모델들|
|deps.model.pcs|에너지 변환 장치를 위한 모델들|
|deps.preset|공통 모델들을 조합한 장치 유형에 대응되는 맞춤형 모델 - MQTT Topic으로 교환되는 **상위 데이터** 묶음|
|deps.preset.bess|bess 장치를 위한 공통 모델|
|deps.rpc|MQTT 프로토콜로 윈격 호출을 위한 데이터 정의|
|deps.vnd|제조사 고유의 데이터를 위한 데이터 정의|

#### 3.1. 기본 데이터 템플릿

일반적으로 하나의 장치는 아래의 데이터들로 모델링을 한다.

|데이터|설명|
|-|-|
|State|장치 상태 - 열거형으로 정의되는 현재 동작 상태|
|Alarm* - Fault|고장 알람 - 정상 운전이 불가한 알람 모음|
|Alarm* - Warning|경고 알람 - 운전 가능하지만 조치가 필요한 알람 모음|
|Alarm* - Status|상태 알람 - 현재 장치의 상태 정보 모음|
|Measure|계측 값들 - 장치의 계측 값들|
|Command**|명령 - 장치에서 수행 가능한 명령들의 모음|

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

공통 모델에 포함되지 않은 제조사별 고유 상태를 표현하기 위해 다음의 구조를 통해 동적으로 고유 상태를 표현한다.
제조사별 고유 상태는 아래를 포함한다.

- Parameter: 읽거나 쓰기 가능한 제조사 고유의 항목 (예) 과전압, 저전압 보호 레벨 설정, 장치 시간 설정 등
- Alarm: 고장, 경고, 상태를 나타내는 Boolean 값의 집합

제조사 고유의 값은 각 항목에 대해 번호가 매겨지며 각 항목에 대해서는 해당 번호로 접근되어 읽기/쓰기가 수행된다.
제조사 고유의 값에 대해서는 사람이 인식 가능한 부가(Meta) 정보가 존재하며 이는 값에 대한 접근과 별도로 조회할 수 있다.

#### 4.1. 파라미터 값 혹은 알람 값에 대한 번호 부여 (Meta 정보)

개념적 예시

```json
// 제조사별 고유 값 정의
{
  1: { // 1번 파라미터는 전압 값에 대응
    "param_name": "특정 전압 값",
    "description": "제조사 고유한 특정 측정 전압",
    "unit": "V",
  }
  2: ..
}
```

#### 4.2. 파라미터의 정보는 번호를 통해 동적 조회한다

```json
// 읽기 요청 (1번, 5번 파라미터 읽기)
=> [1, 5]

// 읽기 응답 (1번 파라미터 = 100, 5번 파라미터 = 25)
<= [100, 25]
```

#### 4.1. 파라미터

제조사별 고유값은 파라미터 형태로 조회하거나 써넣는 방법을 사용한다.\
파라미터는 번호가 할당된 값의 리스트로 볼수 있으며 각 파라미터 번호에 대응되는 의미는 제조사에서 할당한다.

1) 제조사에서는 파라미터 리스트를 만들고 각 파라미터에 번호를 부여하여 ParamMeta 타입으로 */vnd/param-meta 토픽으로 전송한다. (장치 연결 시 최초 한번)
2) 클라이언트에서는 ParamMeta를 확인하고 원하는 파라미터의 번호를 파악한다.
3) 읽거나 쓰고자하는 파라미터의 번호와 값을 담아 ParamRequest 타입으로 */vnd/param 토픽으로 전송한다.
4) 응답*)을 확인하여 파라미터 값을 확인한다.

*) MQTT는 구독/발행 방식이므로 요청/응답 방식을 사용하기 위해 파라미터를 사용하는 클라이언트는 요청의 헤더에 응답을 위한 토픽 주소를 **명시**하여야하고, 파라미터 구현측에서는 요청에 명시된 **토픽 주소로 응답을 발행**하여야 한다.

각 파라미터 정보는 ParamInfo에 저장된다.\
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

파라미터 읽기 쓰기는 ParamReadWriteRequest를 통해 요청한다. 하나의 요청을 통해 읽기 및 쓰기 모두를 요청할 수 있으며, 파라미터 구현측에서는 쓰기가 먼저 수행된 다음 읽기가 수행하여야 한다.\
[ParamReadWriteRequest](api/md/deps-protos.md#deps-vnd-v1-Rpc-ParamReadWriteRequest)
[ParamReadWriteResponse](api/md/deps-protos.md#deps-vnd-v1-Rpc-ParamReadWriteResponse)

```protobuf
message ParamReadWriteRequest {
  repeated ParamIdRange reads = 1;
  ParamBlock writes = 2;
}
// error codes would be specified in deps.rpc.Response
message ParamReadWriteResponse {
  // returns successfully read values if possible
  ParamBlock reads = 1;
  // returns successfully writen ids if possible
  repeated ParamIdRange writes = 2;
}
```

##### 4.1.1 파라미터 요청/응답 예시 (JSON 인코딩)

|ParamMeta 예시|(deps.vnd.v1.ParamMeta)|
|-|-|
|**Topic**|.../vnd/param-meta|

```json
{
  "paramInfos": {
    ...,
    // 파라미터 번호는 연속일 필요가 없으며 임의의 번호를 부여 가능 (32bit 양의정수)
    // 제조사 부여 파라미터 번호 (필수)
    "103": {
      // 제조사 부여 파라미터 이름 (필수)
      "paramName": "soc.min",
      // 파라미터 설명 (선택)
      "description": "Minumum SoC to discharge",
      // 파라미터 값 단위 (선택)
      "unit": "%",
      // 입력 가능 타입 (선택: protobuf Value 타입 중 하나)
      "accepts": [
        "PARAM_KIND_NUMBER"
      ],
      // 최대 최소값 명시 (선택: protobuf oneof 필드)
      "minMax": {
        "max": 100.0
      }
    },
    "104": {
      "paramName": "soc.max",
      "description": "Maximum SoC to charge",
      "unit": "%",
      "accepts": [
        "PARAM_KIND_NUMBER"
      ],
      "minMax": {
        "max": 100.0
      }
    },
    ...
  }
}
```

|파라미터 읽기 요청 예시|(deps.vnd.v1.rpc.ParamRequest)|
|-|-|
|**Topic**|.../vnd/param|

```json
{
  // 헤더 (선택: 응답을 받을 필요가 있을 경우 명시)
  "header": {
    // 요청시 (응답으로) 구독하는 토픽을 헤더에 명시
    // 파라미터 구현 측은 반드시 헤더에 명시된 토픽으로 응답을 보내야함
    // 본 예제에서는 매 요청마다 고유의 토픽 주소를 생성하여 사용함 (요청 전 구독 후 응답 확인 후 구독 해제)
    "respTopic": "eebfe4b9-fe72-4c04-ad7a-af0a9a6be04b"
    // uuid 필드는 respTopic을 여러 요청에 걸처 동일하게 사용할 경우에 요청을 구분하기 위해 사용함 (예제에서는 생략)
  },
  "payload": {
    // 103번 파라미터 부터 2개 (103, 104)를 읽는 요청
    "reads": [
      {
        "start": 103,
        "length": 2
      },
    ]
  }
}
```

|파라미터 읽기 응답 예시|(deps.vnd.v1.rpc.ParamResponse)|
|-|-|
|**Topic**|eebfe4b9-fe72-4c04-ad7a-af0a9a6be04b|

```json
{
  // 응답에 에러가 있을 경우에만 헤더에 에러 정보를 넣음
  "header": {},
  "payload": {
    // 읽기 응답
    "reads": {
      // values 필드의 값과 순차적으로 대응되는 파라미터 번호
      "ranges": [
        {
          "start": 103,
          "length": 1
        },
        {
          "start": 104,
          "length": 1
        },
      ],
      // 읽은 값의 리스트
      "values": [
        // 103번 파라미터 값
        20.0,
        // 104번 파라미터의 값
        50.0,
      ]
    }
  }
}
```

|파라미터 쓰기/읽기 요청 예시|(deps.vnd.v1.rpc.ParamRequest)|
|-|-|
|**Topic**|.../vnd/param|

```json
{
  "header": {
    "respTopic": "75d59d95-0662-48cf-8cee-16e545158646"
  },
  "payload": {
    // 쓴 값이 정상적으로 쓰였는지 다시 읽기 위해 103번 명시
    // 쓰기와 읽기는 번호가 같을 필요는 없음
    // 파라미터 구현 시 항상 쓰기 다음에 읽기를 수행
    "reads": [
      {
        "start": 103,
        "length": 1
      }
    ],
    // 쓰기
    "writes": {
      // values 필드의 값과 순차적으로 매칭되는 파라미터 번호
      "ranges": [
        {
          "start": 103,
          "length": 1
        }
      ],
      // 103번 파라미터에 쓸 값 (protobuf Value 값)
      "values": [
        15.0
      ]
    }
  }
}
```

|파라미터 쓰기/읽기 응답 예시|(deps.vnd.v1.rpc.ParamResponse)|
|-|-|
|**Topic**|75d59d95-0662-48cf-8cee-16e545158646|

```json
{
  "header": {},
  "payload": {
    "reads": {
      "ranges": [
        {
          "start": 103,
          "length": 1
        }
      ],
      "values": [
        15.0
      ]
    },
    // 정상적으로 쓰여진 파라미터 번호
    // 연속된 쓰기 중 에러가 발생하면 성공한 파라미터의 번호들만 명시하고 헤더에 에러 메시지를 담아 응답
    "writes": [
      {
        "start": 103,
        "length": 1
      }
    ]
  }
}
```

|파라미터 에러 응답 예시|(deps.vnd.v1.rpc.ParamResponse|
|-|-|
|**Topic**|...|

```json
{
  "header": {
    "error": {
      // 에러 코드 (열거형)
      "code": "ERROR_CODE_INVALID_PARAMETER",
      // 상세 에러 내용
      "detail": "parameter value out of range"
    }
  }
}
```

#### 4.2. 알람

알람은 장치에서 발생할 수 있는 제조사 고유 장치 상태를 다음의 고장, 경고, 상태 3그룹의 비트 플래그로 표현한다.

- 고장: 장치가 정상 운전을 할 수 없는 상태 (예시 - Over Voltage 등)
- 경고: 장치가 현재 운전은 가능하지만 연속적인 운전을 위해서는 조치가 필요할수 있는 상태 (예시 - High Temperature 등)
- 상태: 고장/경고를 제외한 장치 내부의 상태를 표현하기 위해 사용 (예시 - Contactor On 등)

알람을 전송하는 순서는 다음과 같다.

1. 제조사에서 알람 3개 그룹에 알람 리스트를 만들고 번호*) 및 의미(문자열)을 부여한다. 해당 메타 데이터는 AlarmMeta 타입에 담아*/vnd/alarm-meta 토픽으로 전송한다. (장치 연결시 최초 한번)
1. 장치에서는 AlaramMeta에 정의된 순서에 맞추어 알람 데이터를 비트플래그로 형태로 AlarmData 타입에 채워넣는다 **). 이렇게 생성된 알람 데이터는 장치에서 알람이 발생한 시간 정보와 같이 AlarmResponse 타입으로 */vnd/alarm로 전송한다.
1. 알람 데이터 전송의 주기는 1) 주기적으로 전송하는 방법이나 2) 알람이 변경되었을때만 전송하는 방법 혹은 두가지 방법을 혼용할 수 있으며 제조사에서 선택하여 구현하되 알람이 변경되었음을 인지하면 즉각적으로 알람 데이터를 전송하도록 한다.

\*) 알람 데이터는 연속된 비트 플래그로 전송되므로 알람 번호는 가능하면 0번 부터 시작하도록하고 연속된 번호를 부여하여야 전송되는 데이터의 크기를 최소화 활수 있다.\
\**) 알람 데이터는 개별적인 상태가 아닌 AlarmMeta에 명시된 알람의 상태를 모두 포함하여 일괄적으로 전송한다.

[AlarmMeta](api/md/deps-protos.md#deps-vnd-v1-AlarmMeta),
[AlarmData](api/md/deps-protos.md#deps-vnd-v1-AlarmData)
[AlarmResponse](api/md/deps-protos.md#deps-vnd-v1-AlarmResponse)

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

message AlarmResponse {
  .google.protobuf.Timestamp timestamp = 1;
  AlarmData payload = 2;
}
```

##### 4.2.1 알람 패킷 예시 (JSON 인코딩)

|AlramMeta 예시|(deps.vnd.v1.AlarmMeta)|
|-|-|
|**Topic**|.../vnd/alarm-meta|

```json
{
  "status": {
    // 예약을 위해 번호를 비워둘수 있음
    // 단 알람 데이터는 리스트 형태이므로 알람 데이터 전송 시에는 비어있는 번호에도 더미 값 (false)를 채워서 전송해야함
    "4": "Charging",
    "5": "Discharging",
    "6": "Idle"
    ...
  },
  "warning": {
    "2": "OverTemperature",
    "3": "UnderTemperature",
    ...
  },
  "fault": {
    "0": "OverChargeCurrent",
    "1": "OverDischargeCurrent",
    // 알람 번호는 반드시 연속적으로 부여될 필요는 없음 (2~9번 비워둠)
    "10": "OverVoltage",
    "11": "UnderVoltage",
    ...
  }
}
```

|AlarmResponse 예시|(deps.vnd.v1.rpc.AlarmResponse)|
|-|-|
|**Topic**|.../vnd/alarm|

```json
{
  // 알람이 계측된 시간
  "timestamp": "2026-03-26T00:51:59.722451+00:00",
  "payload": {
    "status": [
      // 예약된거나 비워둔 번호들의 위치에도 더미 데이터 넣어야 함
      false,
      false,
      false,
      false,
      true, // Charging
      false, // Discharging
      false, // Idle
      ...
    ],
    "warning": [
      false,
      false,
      false, // OverTemperature
      false, // UnderTemperature
      ...
    ],
    "fault": [
      false, // OverChargeCurrent
      false, // OverDischargeCurrent
      false,
      false,
      false,
      false,
      false,
      false,
      false,
      false,
      false, // OverVoltage
      false, // UnderVoltage
      ...
    ]
  }
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

|접미어|의미 (장치 관점)|retained**|
|-|-|-|
|vnd/param*|제조사 고유의 읽기/쓰기 데이터 **요청**을 구독하고 처리한다|no|
|vnd/param-meta|제조사 고유의 읽기/쓰기 데이터에 대한 [인덱스-설명] 메타 데이터|yes|
|vnd/alarm*|제조사 고유의 알람 데이터 **요청**을 구독하고 처리한다|no|
|vnd/alarm-meta|제조사 고유의 알라 데이터에 대한 [인덱스-이름] 메타 데이터|yes|

\* 장치에서 구독하는 토픽은 요청(Request) 형태로 전달되며, 경우에 따라 처리 결과를 특정 토픽으로 발행해야할 필요가 있다. ([MQTT RPC](#52-mqtt-rpc))\
\** 제조사 고유의 정보는 retained 형태로 전송되므로 장치는 접속 시 MQTT LastWill 메시지에 vnd/xxx-meta 토픽을 ratained 메시지로 해제(clear)하여야 한다.

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
|bess|bess 장치 - 배터리 + PCS로 구성된 장치. 계통에서 충방전을 수행한다. 선택적으로 부하에 직접 전력을 공급하는 기능을 포함한다.|

## 비호환성 변경점

### 0.0.2 -> 1.0.0

- 일관성 있는 Request/Response 메시지 이름으로 변경
  - preset.bess.v1.BessMeasure -> preset.bess.v1.Rpc.MeasureResponse
  - preset.bess.v1.BessRequest -> preset.bess.v1.Rpc.CommandRequest
  - preset.bess.v1.BessResponse -> preset.bess.v1.Rpc.CommandResponse
  - vnd.v1.Rpc.AlarmEvent -> vnd.v1.Rpc.AlarmResponse
  - ...

- 일관성을 위한 일부 필드 이름 변경
  - preset.bess.v1.BessRequest.head -> preset.bess.v1.Rpc.CommandRequest.header
  - preset.bess.v1.BessRequest.data -> preset.bess.v1.Rpc.CommandRequest.payload
  - preset.bess.v1.Bess.battery -> preset.bess.v1.Bess.bank
  - ...

- Command
  - 여러 명령을 한번에 전송 할수 있도록 oneof와 repeated 필드 조합으로 변경

  - model.pcs.v1.ThreePhasePcsPart.Command.Action 및 Reference -> oneof 필드로 통합됨
  - preset.bess.v1.BessRequest.data -> preset.bess.v1.Rpc.CommandRequest.payload (repeated 필드로 변경)
