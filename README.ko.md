<div align="center">

# ⚡ HappyCoding Everyday

### 위험도에 맞춰 엄격성을 자동으로 조정하는 Codex 코딩 워크플로입니다.

목표를 한 번만 설명하면 HappyCoding이 작은 수정, 제한된 협업, 고위험 전달 중 가장 가볍고 안전한 경로를 선택합니다.

**🌐 Language / 语言 / 言語 / 언어 / Idioma**

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md)

[![Status: Alpha](https://img.shields.io/badge/status-alpha-f59e0b)](#프로젝트-상태)
[![CI](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/actions/workflows/validate.yml/badge.svg)](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/actions/workflows/validate.yml)
[![Codex Skill](https://img.shields.io/badge/Codex-agent%20skill-111827)](skills/jensenmo-happy-coding-everyday/SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-22c55e.svg)](LICENSE)

[빠른 시작](#빠른-시작) · [실행 레인](#세-가지-실행-레인) · [설계 원칙](#설계-원칙) · [문서](docs/README.md)

</div>

> 영문 [README.md](README.md)가 기준 문서입니다. 이 한국어 문서는 초안이며 원어민 검토가 필요합니다. 내용이 다르면 영문을 우선합니다.

## HappyCoding이란?

HappyCoding Everyday는 Codex를 위한 하나의 자동 코딩 워크플로 진입점입니다. 일반 요청을 작은 계약으로 정리하고, 필요한 만큼만 엄격한 실행 레인을 선택한 뒤, 작업을 수행하고 최종 변경 이후의 최신 검증 증거로 마무리합니다. 사용자가 매번 모드, 테스트, 에이전트 구성을 직접 지정할 필요가 없습니다.

## 빠른 시작

```bash
codex plugin marketplace add caredhieacid/jensenmo-happy_coding_everyday
```

Codex에서 **Plugins**를 열고 **JensenMo HappyCoding** 아래의 **HappyCoding Everyday**를 설치합니다. 새 작업에서 평소처럼 요청하세요.

```text
로그인 회귀를 수정하고, 관련 없는 미커밋 변경을 보존한 뒤, 최신 검증 결과를 보여 주세요.
```

명시적으로 호출할 수도 있습니다.

```text
$jensenmo-happy-coding-everyday 코드를 변경하기 전에 이 API 계약을 감사해 주세요.
```

## 세 가지 실행 레인

| 레인 | 사용 조건 | 기본 동작 |
| --- | --- | --- |
| **Everyday** | 하나의 제한된 결과, 낮은 결합도, 하나의 인수 경로 | 조사, 최소 변경, 집중 검증 |
| **Collaboration** | 독립적으로 나눌 수 있는 작업 또는 넓은 읽기 범위 | 읽기는 병렬화하고 공유 쓰기는 한 경로로 통제 |
| **Delivery** | 보안, 마이그레이션, 프로덕션, 장기 조정 또는 단계적 실제 경로 검증 | 지속 계약, 단계 게이트, 독립 리뷰, 롤백 |

PR, 여러 파일, 프런트엔드와 백엔드라는 표현만으로 Delivery로 올라가지 않습니다. 위험, 독립성, 소유권, 검증 비용을 기준으로 판단합니다.

## 설계 원칙

- **의도는 한 번만**: 사용자에게 워크플로 선택을 떠넘기지 않습니다.
- **필요한 만큼만 엄격하게**: Everyday에서 시작하고 증거가 있을 때만 상향합니다.
- **의식보다 증거**: 명령 실행이 아니라 요청된 동작을 증명합니다.
- **읽기는 병렬, 쓰기는 통제**: 컨텍스트를 지키면서 충돌을 피합니다.
- **최신 검증**: 최종 변경 후 관련 검증을 다시 실행합니다.
- **읽기 전용 존중**: 감사, 설명, 진단은 수정 권한이 아닙니다.

자세한 내용은 [설계 철학](docs/design-philosophy.md)과 [아키텍처](docs/architecture.md)를 참고하세요.

## Skill 직접 설치

```bash
git clone https://github.com/caredhieacid/jensenmo-happy_coding_everyday.git
cd jensenmo-happy_coding_everyday
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd)/skills/jensenmo-happy-coding-everyday" \
  "$HOME/.agents/skills/jensenmo-happy-coding-everyday"
```

대상 경로가 이미 있다면 삭제하거나 교체하기 전에 먼저 확인하세요. `$HOME/.agents/skills`는 현재 Codex의 사용자 범위 skill 위치입니다.

## 검증과 릴리스

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_repository.py
```

각 PR은 결정적 plugin 미리보기 패키지를 만듭니다. plugin 버전과 일치하는 `v*` 태그는 ZIP과 SHA-256 체크섬을 포함한 GitHub Release를 자동으로 생성합니다. 시나리오 파일만 존재한다고 행동 테스트가 통과한 것은 아니며, 새 에이전트 컨텍스트에서 관찰 가능한 불변 조건을 확인해야 합니다.

## 프로젝트 상태

현재 상태는 **Alpha**입니다. 핵심 라우팅, plugin 패키지, 구조 검증, 초기 압력 시나리오는 준비되어 있지만 실제 코딩 작업을 통해 임계값을 계속 조정하고 있습니다.

[문서](docs/README.md) · [기여](CONTRIBUTING.md) · [보안](SECURITY.md) · [지원](SUPPORT.md) · [행동 강령](CODE_OF_CONDUCT.md)

## 라이선스

[MIT](LICENSE) © 2026 Jensen Mo
