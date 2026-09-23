# H₂ + D₂ DFT 계산 요약

## 계산 조건

- 작업: H₂ + D₂ 전체의 단일점 전자에너지
- 엔진: PySCF
- 방법: DFT, B3LYP/6-31G(d)
- 전하: 0
- 스핀: 0 (singlet)
- 실행 모드: Slurm, 32 cores
- SCF 수렴: 5 iterations

## 결과

| Quantity | Value |
|---|---:|
| Total QM energy | `-2.3506039492115742 Eh` |
| Total QM energy | `-1475.0262478999246 kcal/mol` |

## 참고

D₂는 전자구조가 H₂와 동일하므로 전자에너지 계산 입력에서는 D 원자를 H 원자로 표현했다. 따라서 이 결과는 분리된 H₂와 D₂ 구조의 전자에너지이며, 동위원소 질량 효과를 포함한 진동·열화학 결과는 아니다.

재현 스크립트: [`h2_d2_energy.py`](h2_d2_energy.py)
