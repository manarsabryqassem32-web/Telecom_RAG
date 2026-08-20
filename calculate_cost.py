"""
calculate_cost.py

Utility to estimate the USD cost of a single RAG request to the
Telecom RAG API, based on the prompt_tokens / completion_tokens
returned by POST /api/v1/query.

Pricing source: https://ai.google.dev/gemini-api/docs/pricing
(Gemini 2.5 Flash, Standard / paid tier, verified August 2026)
    Input:  $0.30 per 1,000,000 tokens
    Output: $2.50 per 1,000,000 tokens

Usage:
    python calculate_cost.py --prompt-tokens 850 --completion-tokens 140

Or import and call calculate_cost(prompt_tokens, completion_tokens) directly.
"""

import argparse

# Gemini 2.5 Flash standard pricing, per 1,000,000 tokens (USD)
INPUT_PRICE_PER_MILLION = 0.30
OUTPUT_PRICE_PER_MILLION = 2.50


def calculate_cost(prompt_tokens: int, completion_tokens: int) -> dict:
    input_cost = (prompt_tokens / 1_000_000) * INPUT_PRICE_PER_MILLION
    output_cost = (completion_tokens / 1_000_000) * OUTPUT_PRICE_PER_MILLION
    total_cost = input_cost + output_cost

    return {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
        "input_cost_usd": round(input_cost, 8),
        "output_cost_usd": round(output_cost, 8),
        "total_cost_usd": round(total_cost, 8),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estimate Gemini 2.5 Flash request cost.")
    parser.add_argument("--prompt-tokens", type=int, required=True, help="prompt_tokens from the API response")
    parser.add_argument("--completion-tokens", type=int, required=True, help="completion_tokens from the API response")
    args = parser.parse_args()

    result = calculate_cost(args.prompt_tokens, args.completion_tokens)

    print("=== Gemini 2.5 Flash Cost Estimate ===")
    print(f"Prompt tokens:     {result['prompt_tokens']}")
    print(f"Completion tokens: {result['completion_tokens']}")
    print(f"Total tokens:      {result['total_tokens']}")
    print(f"Input cost:        ${result['input_cost_usd']:.8f}")
    print(f"Output cost:       ${result['output_cost_usd']:.8f}")
    print(f"Total cost:        ${result['total_cost_usd']:.8f}")
