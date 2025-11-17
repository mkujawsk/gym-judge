from typing import List

class ScoreResult:
    def __init__(self, d_final: float, e_final: float, final_score: float) -> None:
        self.d_final = d_final
        self.e_final = e_final
        self.final_score = final_score
        
    
def calculate_score(
    d_scores: List[float],
    e_scores: List[float],
    neutral_deducations: float,
) -> ScoreResult:
    d_final_raw = sum(d_scores) / len(d_scores)

    sorted_e = sorted(e_scores)
    trimmed = sorted_e[1:-1]
    e_final_raw = sum(trimmed) / len(trimmed)
    
    final_raw = d_final_raw + e_final_raw - neutral_deducations
    
    return ScoreResult(
        d_final = d_final_raw,
        e_final = e_final_raw,
        final_score = final_raw
    )