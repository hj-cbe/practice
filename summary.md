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

## H₂ + D₂ → 2HD 반응 계산

`ReactionBarrierTask`를 사용해 B3LYP/6-31G(d) 수준에서 NEB, 전이상태 최적화, 반응물·생성물·전이상태 열화학을 계산했다. 계산은 Slurm에서 1코어로 실행했다.

| Quantity | Value |
|---|---:|
| Activation ΔG‡ | `-0.007431446733239255 Eh` (`-4.663303231102579 kcal/mol`) |
| Reaction ΔG | `-0.003724393541037152 Eh` (`-2.3370922321394754 kcal/mol`) |
| Electronic barrier | `0.00010330695764837472 Eh` (`0.064826094660986 kcal/mol`) |

프로파일 그림은 로컬 결과 디렉터리 `h2_d2_reaction_work/reactionbarrier/profile/results/figure.png`에 생성됐다.

주의: MAESTRO의 현재 입력 형식은 동위원소를 구분하지 않으므로 D를 H로 근사했다. 따라서 위 ΔG에는 H/D 동위원소 질량 효과가 포함되지 않는다. 특히 음의 ΔG‡는 이 근사 구조와 열화학 처리에 따른 값이며, 실제 H₂+D₂ 동위원소 교환의 물리적 장벽으로 해석하면 안 된다.

재현 스크립트: [`h2_d2_reaction.py`](h2_d2_reaction.py)
