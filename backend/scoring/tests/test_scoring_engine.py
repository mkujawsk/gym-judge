from scoring.services.scoring_engine import calculate_score


def test_calculate_score_simple_case() -> None:
    d_scores = [5.8, 6.2]  # D -> 6.0
    e_scores = [8.5, 8.8, 9.0, 8.9, 9.2]  # po odrzuceniu min/max -> 8.9
    neutral_deductions = 0.3              # ND

    result = calculate_score(d_scores, e_scores, neutral_deductions)

    assert result.d_final == 6.0
    assert result.e_final == 8.9
    assert result.final_score == 14.6