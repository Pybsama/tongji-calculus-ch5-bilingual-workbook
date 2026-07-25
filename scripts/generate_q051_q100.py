from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.source_lineage import CATEGORY_RELATIONS, METHOD_FAMILY_REFERENCES


OUTPUT = ROOT / "content" / "parts" / "part_b_q051_q100.json"

FAMILY = {
    "definite_integral_substitution": {
        "zh_knowledge": ["定积分换元法", "变量、微分与上下限同步变换", "换元后的端点方向"],
        "en_knowledge": ["substitution in definite integrals", "transforming the variable, differential, and limits together", "orientation of transformed limits"],
        "zh_pitfalls": ["换元后混用新变量与旧上下限", "换元函数非一一时不分段就直接改限", "漏掉微分中的常数或负号"],
        "en_pitfalls": ["mixing a new variable with old limits", "changing limits through a non-one-to-one map without splitting", "losing a constant or minus sign in the differential"],
        "zh_takeaway": "定积分换元必须让变量、微分和端点成为一个闭合系统；端点方向由换元自动决定。",
        "en_takeaway": "A definite-integral substitution must transform the variable, differential, and endpoints as one coherent system; the substitution determines orientation.",
        "zh_extension": "用原变量回代再代入原端点，可作为独立验算路线。",
        "en_extension": "Back-substitute before evaluating at the original endpoints as an independent verification route.",
    },
    "definite_integral_by_parts": {
        "zh_knowledge": ["定积分分部积分", "边界项", "因子选择与循环关系"],
        "en_knowledge": ["integration by parts for definite integrals", "boundary terms", "factor choice and reduction relations"],
        "zh_pitfalls": ["漏算或错算边界项", "把不定积分公式直接照搬而忽略端点", "分部后未检查新积分是否更简单"],
        "en_pitfalls": ["omitting or mis-evaluating the boundary term", "copying the indefinite formula without endpoints", "failing to check that the new integral is simpler"],
        "zh_takeaway": "分部积分的核心不是机械套式，而是用一个可控的边界项换取更简单的定积分。",
        "en_takeaway": "Integration by parts trades the original integral for a controlled boundary term and a simpler definite integral.",
        "zh_extension": "对最终闭式求导或作数值估计，检查边界项的符号与数量级。",
        "en_extension": "Differentiate a parameterized closed form or estimate numerically to check the sign and scale of boundary terms.",
    },
    "improper_integral_infinite_interval": {
        "zh_knowledge": ["无穷区间反常积分的定义", "截断极限", "收敛值与尾积分"],
        "en_knowledge": ["definition on an infinite interval", "truncation limits", "convergence values and tails"],
        "zh_pitfalls": ["把无穷大直接当作可代入端点", "双侧无穷积分未拆成两个独立极限", "对称主值冒充普通收敛"],
        "en_pitfalls": ["substituting infinity as if it were an endpoint", "failing to split a two-sided infinite interval into independent limits", "confusing a symmetric principal value with ordinary convergence"],
        "zh_takeaway": "无穷端点必须先截断再取极限；双侧积分要求左右两部分分别收敛。",
        "en_takeaway": "An infinite endpoint must be truncated before taking a limit, and a two-sided integral requires both one-sided pieces to converge independently.",
        "zh_extension": "改变截断方式并检查结果是否稳定，可揭示主值与普通反常积分的差异。",
        "en_extension": "Vary the truncation scheme to expose the difference between a principal value and an ordinary improper integral.",
    },
    "improper_integral_singular_endpoint": {
        "zh_knowledge": ["瑕点在端点的反常积分", "单侧极限", "幂函数与对数型端点行为"],
        "en_knowledge": ["endpoint-singular improper integrals", "one-sided limits", "power and logarithmic endpoint behavior"],
        "zh_pitfalls": ["直接把瑕点代入原函数", "忽略极限方向", "只看原函数形式而不计算截断极限"],
        "en_pitfalls": ["substituting the singular endpoint directly", "ignoring the direction of the limit", "judging from an antiderivative without evaluating the truncation limit"],
        "zh_takeaway": "端点瑕积分的值与收敛性都由单侧截断极限决定。",
        "en_takeaway": "Both the value and convergence of an endpoint-singular integral are determined by its one-sided truncation limit.",
        "zh_extension": "把被积函数与 $x^{-p}$ 或 $|\ln x|$ 比较，可快速判断附近的可积性。",
        "en_extension": "Comparison with $x^{-p}$ or $|\ln x|$ often reveals local integrability near the endpoint.",
    },
    "improper_integral_interior_singularity": {
        "zh_knowledge": ["区间内部瑕点", "左右反常积分独立收敛", "Cauchy 主值与普通积分的区别"],
        "en_knowledge": ["interior singularities", "independent convergence on both sides", "Cauchy principal value versus ordinary convergence"],
        "zh_pitfalls": ["跨越瑕点直接套 Newton-Leibniz 公式", "用正负无穷抵消", "把对称截断极限当成普通积分"],
        "en_pitfalls": ["applying Newton-Leibniz across a singularity", "canceling positive and negative infinities", "reporting a symmetric truncation limit as the ordinary integral"],
        "zh_takeaway": "内部瑕点必须把区间切开；任一侧发散，普通反常积分就发散。",
        "en_takeaway": "An interior singularity splits the interval; divergence on either side makes the ordinary improper integral divergent.",
        "zh_extension": "若对称主值存在，应单独标记为 $\\operatorname{PV}$，不能省略限定词。",
        "en_extension": "If a symmetric principal value exists, label it explicitly as $\\operatorname{PV}$ rather than omitting the qualifier.",
    },
    "improper_integral_convergence_tests": {
        "zh_knowledge": ["反常积分比较审敛法", "极限比较", "绝对收敛与条件收敛"],
        "en_knowledge": ["comparison tests for improper integrals", "limit comparison", "absolute and conditional convergence"],
        "zh_pitfalls": ["比较不等式方向用反", "极限比较常数取到 $0$ 或无穷仍直接套等价结论", "只证收敛而未检查绝对收敛"],
        "en_pitfalls": ["reversing the comparison inequality", "using the finite-positive limit conclusion when the ratio tends to zero or infinity", "proving convergence without checking absolute convergence"],
        "zh_takeaway": "审敛比较必须同时说明非负性、比较区间和已知基准积分。",
        "en_takeaway": "A convergence comparison must state nonnegativity, the tail or neighborhood being compared, and the benchmark integral.",
        "zh_extension": "尝试用同一基准函数分别构造上界与下界，理解充分条件与必要条件的方向。",
        "en_extension": "Use the same benchmark to build both upper and lower comparisons and clarify the direction of sufficient and necessary conditions.",
    },
    "gamma_function_enrichment": {
        "zh_knowledge": ["Gamma 函数的反常积分定义", "参数收敛范围", "递推与尺度换元"],
        "en_knowledge": ["improper-integral definition of the Gamma function", "parameter range for convergence", "recurrence and scaling substitution"],
        "zh_pitfalls": ["未检查 $0$ 附近的参数条件", "分部积分时未验证无穷边界项", "尺度换元后指数或幂次漏因子"],
        "en_pitfalls": ["omitting the parameter condition near zero", "failing to justify the boundary term at infinity", "losing a scale factor or power during substitution"],
        "zh_takeaway": "Gamma 函数把阶乘延拓为参数积分，但公式只在相应反常积分收敛时成立。",
        "en_takeaway": "The Gamma function extends factorial structure through a parameter integral, but each identity is valid only in its convergence range.",
        "zh_extension": "先用尺度换元提取参数，再用递推式把 Gamma 值降到 $\\Gamma(1)$ 或 $\\Gamma\\!\\left(\\frac12\\right)$。",
        "en_extension": "Extract scale parameters first, then use the recurrence to reduce to $\\Gamma(1)$ or $\\Gamma\\!\\left(\\frac12\\right)$.",
    },
}

OPEN_IDS = {
    "Q051", "Q052", "Q055", "Q056", "Q058",
    "Q071", "Q072", "Q073", "Q089", "Q093",
}

ORIGINAL_IDS = {
    "Q053", "Q054", "Q060", "Q061", "Q062", "Q065", "Q066",
    "Q067", "Q070", "Q075", "Q079", "Q080", "Q081", "Q085",
    "Q086", "Q092", "Q100",
}

TYPE_META = {
    "single_choice": (6, "S"),
    "multiple_choice": (9, "M"),
    "true_false": (7, "M"),
    "fill_blank": (7, "M"),
    "calculation": (14, "L"),
    "proof": (20, "XL"),
    "comprehensive": (24, "XL"),
    "error_diagnosis": (18, "XL"),
}

QUESTIONS: list[dict] = []


def add(
    qid: str,
    section: int,
    qtype: str,
    family: str,
    title_zh: str,
    title_en: str,
    prompt_zh: str,
    prompt_en: str,
    answer_zh: str,
    answer_en: str,
    analysis_zh: str,
    analysis_en: str,
    steps_zh: list[str],
    steps_en: list[str],
    verification_zh: str,
    verification_en: str,
    *,
    choices_zh: list[str] | None = None,
    choices_en: list[str] | None = None,
    space_override: str | None = None,
) -> None:
    number = int(qid[1:])
    if number <= 60:
        difficulty = "standard"
    elif number <= 82:
        difficulty = "advanced"
    elif number <= 96:
        difficulty = "hard"
    else:
        difficulty = "challenge"
    tier = "challenge" if difficulty == "challenge" else "synthesis"

    if qid in OPEN_IDS:
        category = "open_text_adaptation"
    elif qid in ORIGINAL_IDS:
        category = "original_synthesis"
    else:
        category = "classic_method_variant"

    references = sorted(METHOD_FAMILY_REFERENCES[family])
    if category != "open_text_adaptation":
        references = [references[0]]

    data = FAMILY[family]
    minutes, space = TYPE_META[qtype]
    if space_override is not None:
        space = space_override
    zh = {
        "title": title_zh,
        "prompt": prompt_zh,
        "answer": answer_zh,
        "solution": {
            "knowledge": data["zh_knowledge"],
            "analysis": analysis_zh,
            "steps": steps_zh,
            "pitfalls": data["zh_pitfalls"],
            "verification": verification_zh,
            "takeaway": data["zh_takeaway"],
            "extension": data["zh_extension"],
        },
    }
    en = {
        "title": title_en,
        "prompt": prompt_en,
        "answer": answer_en,
        "solution": {
            "knowledge": data["en_knowledge"],
            "analysis": analysis_en,
            "steps": steps_en,
            "pitfalls": data["en_pitfalls"],
            "verification": verification_en,
            "takeaway": data["en_takeaway"],
            "extension": data["en_extension"],
        },
    }
    if choices_zh is not None:
        zh["choices"] = choices_zh
        en["choices"] = choices_en

    QUESTIONS.append(
        {
            "id": qid,
            "section": section,
            "tier": tier,
            "difficulty": difficulty,
            "type": qtype,
            "tags": {
                "zh": data["zh_knowledge"],
                "en": data["en_knowledge"],
            },
            "minutes": minutes,
            "space": space,
            "classic_method": category != "original_synthesis",
            "source_lineage": {
                "category": category,
                "method_family": family,
                "relation": CATEGORY_RELATIONS[category],
                "references": references,
            },
            "zh": zh,
            "en": en,
        }
    )


add(
    "Q051", 3, "fill_blank", "definite_integral_substitution",
    "复合多项式换元", "A Composite-Polynomial Substitution",
    "计算 $\\displaystyle \\int_0^1x(1+x^2)^2\\,dx=\\underline{\\qquad}$。",
    "Evaluate $\\displaystyle \\int_0^1x(1+x^2)^2\\,dx=\\underline{\\qquad}$.",
    "$\\frac76$", "$\\frac76$",
    "内层 $1+x^2$ 的微分与因子 $x\\,dx$ 只差常数；换元后得到一个可直接积分的二次幂。",
    "The differential of the inner expression $1+x^2$ differs from the factor $x\\,dx$ only by a constant, leaving a directly integrable square.",
    [
        "令 $u=1+x^2$，则 $du=2x\\,dx$，即 $x\\,dx=\\frac12du$。",
        "当 $x=0$ 时 $u=1$；当 $x=1$ 时 $u=2$。",
        "原积分化为 $\\frac12\\int_1^2u^2\\,du$。",
        "因此结果为 $\\frac12\\left.\\frac{u^3}{3}\\right|_1^2=\\frac16(8-1)=\\frac76$。",
    ],
    [
        "Set $u=1+x^2$, so $du=2x\\,dx$ and $x\\,dx=\\frac12du$.",
        "When $x=0$, $u=1$; when $x=1$, $u=2$.",
        "The integral becomes $\\frac12\\int_1^2u^2\\,du$.",
        "Therefore the value is $\\frac12\\left.\\frac{u^3}{3}\\right|_1^2=\\frac16(8-1)=\\frac76$.",
    ],
    "展开得 $x(1+x^2)^2=x+2x^3+x^5$；逐项积分为 $\\frac12+2\\cdot\\frac14+\\frac16=\\frac76$，与换元结果一致。",
    "Expanding gives $x(1+x^2)^2=x+2x^3+x^5$; termwise integration gives $\\frac12+2\\cdot\\frac14+\\frac16=\\frac76$, confirming the substitution.",
)

add(
    "Q052", 3, "single_choice", "definite_integral_substitution",
    "指数复合函数的定积分", "A Definite Integral of an Exponential Composite",
    "积分 $\\displaystyle \\int_0^1 x e^{x^2}\\,dx$ 的值是哪一项？",
    "Which value equals $\\displaystyle \\int_0^1 x e^{x^2}\\,dx$?",
    "B", "B",
    "令 $u=x^2$ 时微分只差常数因子 $\\frac12$；新端点仍为 $0$ 与 $1$。",
    "With $u=x^2$, the differential contributes the factor $\\frac12$, and the new endpoints remain $0$ and $1$.",
    [
        "令 $u=x^2$，则 $du=2x\\,dx$，所以 $x\\,dx=\\frac12du$。",
        "端点变换为 $x=0\\Rightarrow u=0$，$x=1\\Rightarrow u=1$。",
        "于是积分等于 $\\frac12\\int_0^1e^u\\,du$。",
        "计算得 $\\frac12\\left(e-1\\right)$，故选择 B。",
    ],
    [
        "Let $u=x^2$, so $du=2x\\,dx$ and $x\\,dx=\\frac12du$.",
        "The endpoints become $x=0\\Rightarrow u=0$ and $x=1\\Rightarrow u=1$.",
        "Thus the integral is $\\frac12\\int_0^1e^u\\,du$.",
        "Its value is $\\frac12(e-1)$, so B is correct.",
    ],
    "因 $x e^{x^2}<e$ 且区间长度为 $1$，结果应小于 $e$；$\\frac{e-1}{2}$ 满足该估计。",
    "Since $x e^{x^2}<e$ on an interval of length $1$, the result must be below $e$; $\\frac{e-1}{2}$ satisfies this bound.",
    choices_zh=[
        "A. $e-1$",
        "B. $\\frac{e-1}{2}$",
        "C. $\\frac{e}{2}$",
        "D. $\\frac12$",
    ],
    choices_en=[
        "A. $e-1$",
        "B. $\\frac{e-1}{2}$",
        "C. $\\frac{e}{2}$",
        "D. $\\frac12$",
    ],
)

add(
    "Q053", 3, "multiple_choice", "definite_integral_substitution",
    "换元与端点一致性辨析", "Consistency of Substitution and Endpoints",
    "下列换元结果中，哪些完全正确？假设出现的 $f$ 连续。",
    "Which substitution results are fully correct? Assume every displayed $f$ is continuous.",
    "A、B、D。", "A, B, and D.",
    "逐项检查微分因子、端点及变量是否统一；等式数值偶然相同也不能替代合法的换元过程。",
    "For each choice, check the differential factor, endpoints, and variable consistency; accidental numerical equality cannot replace a valid substitution.",
    [
        "A 中令 $u=x^2$，$du=2x\\,dx$，端点 $0,1$ 不变，故 A 正确。",
        "B 中令 $u=\\ln x$，$du=\\frac{dx}{x}$，端点 $1,e$ 变为 $0,1$，故 B 正确。",
        "C 中令 $u=\\cos x$ 时 $du=-\\sin x\\,dx$；若保持端点 $1,0$，积分前必须有负号，所以 C 错误。",
        "D 中令 $u=\\frac{x}{a}$，则 $dx=a\\,du$；在 $a>0$ 下端点 $0,a$ 变为 $0,1$，故 D 正确。",
    ],
    [
        "In A, $u=x^2$ gives $du=2x\\,dx$ and leaves the endpoints $0,1$, so A is correct.",
        "In B, $u=\\ln x$ gives $du=\\frac{dx}{x}$ and sends $1,e$ to $0,1$, so B is correct.",
        "In C, $u=\\cos x$ gives $du=-\\sin x\\,dx$; retaining endpoints $1,0$ requires a leading minus sign, so C is false.",
        "In D, $u=\\frac{x}{a}$ gives $dx=a\\,du$; for $a>0$, endpoints $0,a$ become $0,1$, so D is correct.",
    ],
    "对 C 直接计算：左侧为 $1$，而写出的右侧 $\\int_1^0du=-1$，明确暴露负号错误。",
    "For C, direct evaluation gives $1$ on the left but $\\int_1^0du=-1$ on the displayed right, exposing the sign error.",
    choices_zh=[
        "A. $\\displaystyle \\int_0^1 2x f(x^2)\\,dx=\\int_0^1f(u)\\,du$",
        "B. $\\displaystyle \\int_1^e\\frac{f(\\ln x)}{x}\\,dx=\\int_0^1f(u)\\,du$",
        "C. 令 $u=\\cos x$，则 $\\displaystyle \\int_0^{\\frac\\pi2}\\sin x\\,dx=\\int_1^0du$",
        "D. 若 $a>0$，则 $\\displaystyle \\int_0^a f\\!\\left(\\frac{x}{a}\\right)\\,dx=a\\int_0^1f(u)\\,du$",
    ],
    choices_en=[
        "A. $\\displaystyle \\int_0^1 2x f(x^2)\\,dx=\\int_0^1f(u)\\,du$",
        "B. $\\displaystyle \\int_1^e\\frac{f(\\ln x)}{x}\\,dx=\\int_0^1f(u)\\,du$",
        "C. With $u=\\cos x$, $\\displaystyle \\int_0^{\\frac\\pi2}\\sin x\\,dx=\\int_1^0du$",
        "D. If $a>0$, $\\displaystyle \\int_0^a f\\!\\left(\\frac{x}{a}\\right)\\,dx=a\\int_0^1f(u)\\,du$",
    ],
    space_override="S",
)

add(
    "Q054", 3, "true_false", "definite_integral_substitution",
    "递减换元的端点方向", "Endpoint Orientation under a Decreasing Substitution",
    "判断：若换元 $u=\\varphi(x)$ 在 $[a,b]$ 上严格递减，则换元后总可以把较小的新端点写作下限、较大的新端点写作上限，而不添加负号。",
    "True or false: if $u=\\varphi(x)$ is strictly decreasing on $[a,b]$, one may always put the smaller transformed endpoint below the larger one without adding a minus sign.",
    "错误。交换上下限必须同时产生负号。", "False. Reversing the transformed limits introduces a minus sign.",
    "合法公式首先保留有向端点 $\\varphi(a)$ 到 $\\varphi(b)$；若人为改成从小到大，就必须补偿一个负号。",
    "The valid formula first keeps the oriented endpoints from $\\varphi(a)$ to $\\varphi(b)$; manually reordering them requires a compensating minus sign.",
    [
        "换元公式写成 $\\int_a^b f(\\varphi(x))\\varphi'(x)\\,dx=\\int_{\\varphi(a)}^{\\varphi(b)}f(u)\\,du$。",
        "严格递减意味着 $\\varphi(a)>\\varphi(b)$，所以右侧本来就是反向积分。",
        "若改写为从 $\\varphi(b)$ 到 $\\varphi(a)$，根据换限性质必须乘以 $-1$。",
        "例如 $u=1-x$ 把 $[0,1]$ 变为 $[1,0]$；遗漏负号会使常数函数积分由 $-1$ 错成 $1$。",
    ],
    [
        "The substitution formula is $\\int_a^b f(\\varphi(x))\\varphi'(x)\\,dx=\\int_{\\varphi(a)}^{\\varphi(b)}f(u)\\,du$.",
        "Strict decrease gives $\\varphi(a)>\\varphi(b)$, so the transformed integral is naturally reversed.",
        "Rewriting it from $\\varphi(b)$ to $\\varphi(a)$ requires multiplication by $-1$.",
        "For example, $u=1-x$ sends $[0,1]$ to $[1,0]$; omitting the sign changes the constant-function integral from $-1$ to $1$.",
    ],
    "取 $f(u)=1$、$\\varphi(x)=1-x$：左侧 $\\int_0^1(-1)\\,dx=-1$，而无负号的顺向新积分等于 $1$。",
    "Take $f(u)=1$ and $\\varphi(x)=1-x$: the left side is $\\int_0^1(-1)\\,dx=-1$, whereas the reordered integral without a minus sign is $1$.",
)

add(
    "Q055", 3, "calculation", "definite_integral_substitution",
    "奇次正弦幂的换元积分", "Substitution for an Odd Power of Sine",
    "计算 $\\displaystyle \\int_0^{\\frac\\pi2}\\sin^3x\\cos^2x\\,dx$。",
    "Evaluate $\\displaystyle \\int_0^{\\frac\\pi2}\\sin^3x\\cos^2x\\,dx$.",
    "$\\frac{2}{15}$", "$\\frac{2}{15}$",
    "保留一个 $\\sin x\\,dx$，把其余 $\\sin^2x$ 改写为 $1-\\cos^2x$，再令 $u=\\cos x$。",
    "Reserve one factor $\\sin x\\,dx$, rewrite the remaining $\\sin^2x$ as $1-\\cos^2x$, and set $u=\\cos x$.",
    [
        "写成 $\\sin^3x\\cos^2x=(1-\\cos^2x)\\cos^2x\\sin x$。",
        "令 $u=\\cos x$，则 $du=-\\sin x\\,dx$。",
        "端点由 $x=0,\\frac\\pi2$ 变为 $u=1,0$，故积分为 $\\int_0^1(u^2-u^4)\\,du$。",
        "计算得 $\\left.\\left(\\frac{u^3}{3}-\\frac{u^5}{5}\\right)\\right|_0^1=\\frac13-\\frac15=\\frac{2}{15}$。",
    ],
    [
        "Rewrite $\\sin^3x\\cos^2x=(1-\\cos^2x)\\cos^2x\\sin x$.",
        "Set $u=\\cos x$, so $du=-\\sin x\\,dx$.",
        "The endpoints $x=0,\\frac\\pi2$ become $u=1,0$, hence the integral is $\\int_0^1(u^2-u^4)\\,du$.",
        "Evaluation gives $\\left.\\left(\\frac{u^3}{3}-\\frac{u^5}{5}\\right)\\right|_0^1=\\frac13-\\frac15=\\frac{2}{15}$.",
    ],
    "被积函数非负且不超过 $1$，答案应在 $0$ 与 $\\frac\\pi2$ 之间；$\\frac{2}{15}$ 符合并可由 Beta 型数值核验。",
    "The integrand is nonnegative and at most $1$, so the value lies between $0$ and $\\frac\\pi2$; $\\frac{2}{15}$ satisfies this and agrees with numerical evaluation.",
)

add(
    "Q056", 3, "calculation", "definite_integral_substitution",
    "根式中的反向链式结构", "A Reverse-Chain Structure in a Radical",
    "计算 $\\displaystyle \\int_0^{\\frac{\\sqrt3}{2}}\\frac{x}{\\sqrt{1-x^2}}\\,dx$。",
    "Evaluate $\\displaystyle \\int_0^{\\frac{\\sqrt3}{2}}\\frac{x}{\\sqrt{1-x^2}}\\,dx$.",
    "$\\frac12$", "$\\frac12$",
    "根号内 $1-x^2$ 的微分是 $-2x\\,dx$；端点换元后从 $1$ 降到 $\\frac14$。",
    "The differential of $1-x^2$ is $-2x\\,dx$; the transformed endpoints decrease from $1$ to $\\frac14$.",
    [
        "令 $u=1-x^2$，则 $du=-2x\\,dx$。",
        "当 $x=0$ 时 $u=1$；当 $x=\\frac{\\sqrt3}{2}$ 时 $u=\\frac14$。",
        "积分化为 $-\\frac12\\int_1^{\\frac14}u^{-\\frac12}\\,du=\\frac12\\int_{\\frac14}^1u^{-\\frac12}\\,du$。",
        "结果为 $\\left.\\sqrt{u}\\right|_{\\frac14}^1=1-\\frac12=\\frac12$。",
    ],
    [
        "Set $u=1-x^2$, so $du=-2x\\,dx$.",
        "When $x=0$, $u=1$; when $x=\\frac{\\sqrt3}{2}$, $u=\\frac14$.",
        "The integral becomes $-\\frac12\\int_1^{\\frac14}u^{-\\frac12}\\,du=\\frac12\\int_{\\frac14}^1u^{-\\frac12}\\,du$.",
        "Thus the value is $\\left.\\sqrt{u}\\right|_{\\frac14}^1=1-\\frac12=\\frac12$.",
    ],
    "原函数为 $-\\sqrt{1-x^2}$；在两端作上限值减下限值同样得到 $-\\frac12-(-1)=\\frac12$。",
    "An antiderivative is $-\\sqrt{1-x^2}$; upper minus lower gives $-\\frac12-(-1)=\\frac12$ again.",
)

add(
    "Q057", 3, "fill_blank", "definite_integral_substitution",
    "指数分式的端点换元", "Endpoint Substitution in an Exponential Fraction",
    "计算 $\\displaystyle \\int_0^{\\ln2}\\frac{e^x}{1+e^x}\\,dx=\\underline{\\qquad}$。",
    "Evaluate $\\displaystyle \\int_0^{\\ln2}\\frac{e^x}{1+e^x}\\,dx=\\underline{\\qquad}$.",
    "$\\ln\\frac32$", "$\\ln\\frac32$",
    "令 $u=1+e^x$ 可同时吸收分子和微分；新端点是 $2$ 与 $3$。",
    "Setting $u=1+e^x$ absorbs both the numerator and differential; the new endpoints are $2$ and $3$.",
    [
        "令 $u=1+e^x$，则 $du=e^x\\,dx$。",
        "当 $x=0$ 时 $u=2$；当 $x=\\ln2$ 时 $u=3$。",
        "原积分变为 $\\int_2^3\\frac{1}{u}\\,du$。",
        "所以结果为 $\\ln3-\\ln2=\\ln\\frac32$。",
    ],
    [
        "Set $u=1+e^x$, so $du=e^x\\,dx$.",
        "When $x=0$, $u=2$; when $x=\\ln2$, $u=3$.",
        "The integral becomes $\\int_2^3\\frac{1}{u}\\,du$.",
        "Hence the value is $\\ln3-\\ln2=\\ln\\frac32$.",
    ],
    "被积函数介于 $\\frac12$ 与 $\\frac23$，区间长度为 $\\ln2$；$\\ln\\frac32$ 落在相应上下界之间。",
    "The integrand lies between $\\frac12$ and $\\frac23$ on an interval of length $\\ln2$; $\\ln\\frac32$ lies between the corresponding bounds.",
)

add(
    "Q058", 3, "single_choice", "definite_integral_by_parts",
    "分部积分公式的边界项", "The Boundary Term in Integration by Parts",
    "设 $u,v$ 在 $[a,b]$ 上连续可微。下列哪一项是正确的定积分分部公式？",
    "Let $u,v$ be continuously differentiable on $[a,b]$. Which formula for definite integration by parts is correct?",
    "C", "C",
    "由乘积微分 $d(uv)=u\\,dv+v\\,du$ 在 $[a,b]$ 上积分，并把 $\\int v\\,du$ 移到另一侧。",
    "Integrate the product differential $d(uv)=u\\,dv+v\\,du$ over $[a,b]$ and move $\\int v\\,du$ to the other side.",
    [
        "乘积法则给出 $(uv)'=u'v+uv'$。",
        "在 $[a,b]$ 上积分得 $[uv]_a^b=\\int_a^bu'v\\,dx+\\int_a^buv'\\,dx$。",
        "移项得到 $\\int_a^buv'\\,dx=[uv]_a^b-\\int_a^bu'v\\,dx$。",
        "这正是选项 C；其余选项漏掉边界项或符号错误。",
    ],
    [
        "The product rule gives $(uv)'=u'v+uv'$.",
        "Integrating over $[a,b]$ yields $[uv]_a^b=\\int_a^bu'v\\,dx+\\int_a^buv'\\,dx$.",
        "Rearrangement gives $\\int_a^buv'\\,dx=[uv]_a^b-\\int_a^bu'v\\,dx$.",
        "This is choice C; the others omit the boundary term or use an incorrect sign.",
    ],
    "取 $u=x$、$v=x$、$[a,b]=[0,1]$，C 两侧都等于 $\\frac12$。",
    "With $u=x$, $v=x$, and $[a,b]=[0,1]$, both sides of C equal $\\frac12$.",
    choices_zh=[
        "A. $\\displaystyle \\int_a^buv'\\,dx=uv-\\int_a^bu'v\\,dx$",
        "B. $\\displaystyle \\int_a^buv'\\,dx=[uv]_a^b+\\int_a^bu'v\\,dx$",
        "C. $\\displaystyle \\int_a^buv'\\,dx=[uv]_a^b-\\int_a^bu'v\\,dx$",
        "D. $\\displaystyle \\int_a^buv'\\,dx=\\int_a^bu'v\\,dx$",
    ],
    choices_en=[
        "A. $\\displaystyle \\int_a^buv'\\,dx=uv-\\int_a^bu'v\\,dx$",
        "B. $\\displaystyle \\int_a^buv'\\,dx=[uv]_a^b+\\int_a^bu'v\\,dx$",
        "C. $\\displaystyle \\int_a^buv'\\,dx=[uv]_a^b-\\int_a^bu'v\\,dx$",
        "D. $\\displaystyle \\int_a^buv'\\,dx=\\int_a^bu'v\\,dx$",
    ],
)

add(
    "Q059", 3, "calculation", "definite_integral_by_parts",
    "对数因子的分部积分", "Integration by Parts with a Logarithmic Factor",
    "计算 $\\displaystyle \\int_0^1x\\ln(1+x)\\,dx$。",
    "Evaluate $\\displaystyle \\int_0^1x\\ln(1+x)\\,dx$.",
    "$\\frac14$", "$\\frac14$",
    "令对数因子求导、代数因子积分；分部后出现的 $\\frac{x^2}{1+x}$ 可用多项式除法化简。",
    "Differentiate the logarithmic factor and integrate the algebraic factor; polynomial division simplifies the resulting $\\frac{x^2}{1+x}$.",
    [
        "取 $u=\\ln(1+x)$、$dv=x\\,dx$，则 $du=\\frac{dx}{1+x}$、$v=\\frac{x^2}{2}$。",
        "分部积分得 $\\int_0^1x\\ln(1+x)\\,dx=\\left.\\frac{x^2}{2}\\ln(1+x)\\right|_0^1-\\frac12\\int_0^1\\frac{x^2}{1+x}\\,dx$。",
        "边界项为 $\\frac12\\ln2$，且 $\\frac{x^2}{1+x}=x-1+\\frac{1}{1+x}$。",
        "所以 $\\int_0^1\\frac{x^2}{1+x}\\,dx=\\left.\\left(\\frac{x^2}{2}-x+\\ln(1+x)\\right)\\right|_0^1=\\ln2-\\frac12$。",
        "代回得到 $\\frac12\\ln2-\\frac12\\left(\\ln2-\\frac12\\right)=\\frac14$。",
    ],
    [
        "Choose $u=\\ln(1+x)$ and $dv=x\\,dx$, so $du=\\frac{dx}{1+x}$ and $v=\\frac{x^2}{2}$.",
        "Integration by parts gives $\\int_0^1x\\ln(1+x)\\,dx=\\left.\\frac{x^2}{2}\\ln(1+x)\\right|_0^1-\\frac12\\int_0^1\\frac{x^2}{1+x}\\,dx$.",
        "The boundary term is $\\frac12\\ln2$, and $\\frac{x^2}{1+x}=x-1+\\frac{1}{1+x}$.",
        "Hence $\\int_0^1\\frac{x^2}{1+x}\\,dx=\\left.\\left(\\frac{x^2}{2}-x+\\ln(1+x)\\right)\\right|_0^1=\\ln2-\\frac12$.",
        "Substitution back gives $\\frac12\\ln2-\\frac12\\left(\\ln2-\\frac12\\right)=\\frac14$.",
    ],
    "由 $0<\\ln(1+x)<x$（$0<x\\le1$）可得 $0<I<\\int_0^1x^2\\,dx=\\frac13$；结果 $\\frac14$ 落在该范围内。",
    "Since $0<\\ln(1+x)<x$ for $0<x\\le1$, one has $0<I<\\int_0^1x^2\\,dx=\\frac13$; the value $\\frac14$ has the correct sign and scale.",
)

add(
    "Q060", 3, "proof", "definite_integral_substitution",
    "定积分换元公式的链式证明", "A Chain-Rule Proof of Definite Substitution",
    "设 $f$ 在包含 $\\varphi([\\alpha,\\beta])$ 的区间上连续，$\\varphi$ 在 $[\\alpha,\\beta]$ 上连续可微。证明 $\\displaystyle \\int_\\alpha^\\beta f(\\varphi(t))\\varphi'(t)\\,dt=\\int_{\\varphi(\\alpha)}^{\\varphi(\\beta)}f(u)\\,du$，并说明无需假设 $\\varphi$ 单调。",
    "Let $f$ be continuous on an interval containing $\\varphi([\\alpha,\\beta])$, and let $\\varphi$ be continuously differentiable on $[\\alpha,\\beta]$. Prove $\\displaystyle \\int_\\alpha^\\beta f(\\varphi(t))\\varphi'(t)\\,dt=\\int_{\\varphi(\\alpha)}^{\\varphi(\\beta)}f(u)\\,du$, and explain why monotonicity of $\\varphi$ is unnecessary.",
    "证明见解析；结论由原函数与链式法则直接得到。", "See the proof; the result follows directly from an antiderivative and the chain rule.",
    "连续性保证 $f$ 有原函数；复合原函数 $F\\circ\\varphi$ 的导数正是左侧被积函数，因此只需在端点应用 Newton-Leibniz 公式。",
    "Continuity gives an antiderivative of $f$, and the derivative of the composite $F\\circ\\varphi$ is exactly the left integrand, so Newton-Leibniz at the endpoints suffices.",
    [
        "取 $f$ 的一个原函数 $F$，即 $F'(u)=f(u)$。",
        "由链式法则，$\\frac{d}{dt}F(\\varphi(t))=f(\\varphi(t))\\varphi'(t)$。",
        "Newton-Leibniz 公式给出左侧等于 $F(\\varphi(\\beta))-F(\\varphi(\\alpha))$。",
        "另一方面，$\\int_{\\varphi(\\alpha)}^{\\varphi(\\beta)}f(u)\\,du=F(\\varphi(\\beta))-F(\\varphi(\\alpha))$。",
        "证明只使用端点与链式法则；即使 $\\varphi$ 在区间内往返，等式仍成立，因此不需要单调性。",
    ],
    [
        "Choose an antiderivative $F$ of $f$, so $F'(u)=f(u)$.",
        "The chain rule gives $\\frac{d}{dt}F(\\varphi(t))=f(\\varphi(t))\\varphi'(t)$.",
        "Newton-Leibniz makes the left side $F(\\varphi(\\beta))-F(\\varphi(\\alpha))$.",
        "Meanwhile, $\\int_{\\varphi(\\alpha)}^{\\varphi(\\beta)}f(u)\\,du=F(\\varphi(\\beta))-F(\\varphi(\\alpha))$.",
        "Only endpoint values and the chain rule were used; the identity remains valid if $\\varphi$ reverses direction internally, so monotonicity is unnecessary.",
    ],
    "令 $f(u)=1$，两侧都等于 $\\varphi(\\beta)-\\varphi(\\alpha)$，可直接验证端点方向与符号。",
    "With $f(u)=1$, both sides equal $\\varphi(\\beta)-\\varphi(\\alpha)$, directly checking endpoint orientation and sign.",
)

add(
    "Q061", 3, "multiple_choice", "definite_integral_substitution",
    "含参数函数的换元恒等式", "Substitution Identities with a General Function",
    "设 $f$ 在相应区间连续，且 $a>0$。下列恒等式哪些成立？",
    "Let $f$ be continuous on the relevant intervals and let $a>0$. Which identities hold?",
    "A、C、D。", "A, C, and D.",
    "A、B 比较换元 $u=x^2$ 在半区间和对称区间上的差异；C 需先利用偶性，D 是线性尺度换元。",
    "A and B contrast $u=x^2$ on a half interval and a symmetric interval; C first uses evenness, and D is a linear scaling.",
    [
        "A 中 $u=x^2$、$du=2x\\,dx$，直接得到 $\\frac12\\int_0^1f(u)\\,du$。",
        "B 的被积函数 $x f(x^2)$ 为奇函数，所以左侧为 $0$；右侧一般不为 $0$，故 B 错误。",
        "C 中 $f(x^2)$ 为偶函数；先写成 $2\\int_0^1f(x^2)\\,dx$，再令 $u=x^2$，得到 $\\int_0^1\\frac{f(u)}{\\sqrt{u}}\\,du$。",
        "D 中令 $u=\\frac{x}{a}$，$dx=a\\,du$，端点 $0,a$ 变为 $0,1$，故成立。",
    ],
    [
        "In A, $u=x^2$ and $du=2x\\,dx$ give $\\frac12\\int_0^1f(u)\\,du$ directly.",
        "In B, $x f(x^2)$ is odd, so the left side is $0$ while the right side need not be $0$; B is false.",
        "In C, $f(x^2)$ is even; write $2\\int_0^1f(x^2)\\,dx$ and then set $u=x^2$ to obtain $\\int_0^1\\frac{f(u)}{\\sqrt{u}}\\,du$.",
        "In D, $u=\\frac{x}{a}$ gives $dx=a\\,du$ and maps $0,a$ to $0,1$, so D holds.",
    ],
    "取 $f\\equiv1$：B 左侧为 $0$、右侧为 $1$，排除 B；A、C、D 两侧分别都化为 $\\frac12$、$2$、$a$。",
    "For $f\\equiv1$, B gives $0$ on the left and $1$ on the right; A, C, and D give matching values $\\frac12$, $2$, and $a$.",
    choices_zh=[
        "A. $\\displaystyle \\int_0^1x f(x^2)\\,dx=\\frac12\\int_0^1f(u)\\,du$",
        "B. $\\displaystyle \\int_{-1}^1x f(x^2)\\,dx=\\int_0^1f(u)\\,du$",
        "C. $\\displaystyle \\int_{-1}^1f(x^2)\\,dx=\\int_0^1\\frac{f(u)}{\\sqrt{u}}\\,du$",
        "D. $\\displaystyle \\int_0^a f\\!\\left(\\frac{x}{a}\\right)\\,dx=a\\int_0^1f(u)\\,du$",
    ],
    choices_en=[
        "A. $\\displaystyle \\int_0^1x f(x^2)\\,dx=\\frac12\\int_0^1f(u)\\,du$",
        "B. $\\displaystyle \\int_{-1}^1x f(x^2)\\,dx=\\int_0^1f(u)\\,du$",
        "C. $\\displaystyle \\int_{-1}^1f(x^2)\\,dx=\\int_0^1\\frac{f(u)}{\\sqrt{u}}\\,du$",
        "D. $\\displaystyle \\int_0^a f\\!\\left(\\frac{x}{a}\\right)\\,dx=a\\int_0^1f(u)\\,du$",
    ],
    space_override="S",
)

add(
    "Q062", 3, "true_false", "definite_integral_substitution",
    "非单调映射也可使用换元公式", "A Nonmonotone Map Can Still Satisfy the Substitution Formula",
    "判断：若 $f$ 连续，则即使 $u=x^2$ 在 $[-1,1]$ 上不单调，仍可由定积分换元公式直接得到 $\\displaystyle \\int_{-1}^1x f(x^2)\\,dx=\\frac12\\int_1^1f(u)\\,du=0$。",
    "True or false: if $f$ is continuous, then even though $u=x^2$ is not monotone on $[-1,1]$, the definite-integral substitution formula still gives $\\displaystyle \\int_{-1}^1x f(x^2)\\,dx=\\frac12\\int_1^1f(u)\\,du=0$ directly.",
    "正确。", "True.",
    "这里的被积式恰含 $\\varphi'(x)=2x$：定积分换元公式由原函数和链式法则推出，并不要求 $\\varphi(x)=x^2$ 单调。",
    "The integrand contains exactly the factor $\\varphi'(x)=2x$. The definite-integral substitution theorem follows from an antiderivative and the chain rule, so monotonicity of $\\varphi(x)=x^2$ is unnecessary.",
    [
        "令 $F$ 为 $f$ 的一个原函数，则链式法则给出 $\\frac{d}{dx}F(x^2)=2x f(x^2)$。",
        "因此 $\\int_{-1}^1x f(x^2)\\,dx=\\frac12\\left[F(x^2)\\right]_{-1}^{1}$。",
        "两个端点都给出 $x^2=1$，所以结果为 $\\frac12(F(1)-F(1))=0$。",
        "这正等价于 $\\frac12\\int_1^1f(u)\\,du=0$，全过程没有使用 $x^2$ 的单调性。",
        "另验：$f(x^2)$ 为偶函数，故 $x f(x^2)$ 为奇函数，对称区间积分也为 $0$。",
    ],
    [
        "Let $F$ be an antiderivative of $f$. The chain rule gives $\\frac{d}{dx}F(x^2)=2x f(x^2)$.",
        "Hence $\\int_{-1}^1x f(x^2)\\,dx=\\frac12\\left[F(x^2)\\right]_{-1}^{1}$.",
        "Both endpoints give $x^2=1$, so the value is $\\frac12(F(1)-F(1))=0$.",
        "This is exactly $\\frac12\\int_1^1f(u)\\,du=0$, and no monotonicity of $x^2$ was used.",
        "As a check, $f(x^2)$ is even, so $x f(x^2)$ is odd and its symmetric-interval integral is $0$.",
    ],
    "取 $f(u)=e^u$，原函数为 $F(u)=e^u$，端点差为 $\\frac12(e-e)=0$；奇函数检验给出相同结论。",
    "For $f(u)=e^u$, take $F(u)=e^u$; the endpoint difference is $\\frac12(e-e)=0$, matching the oddness check.",
)

add(
    "Q063", 3, "calculation", "definite_integral_substitution",
    "换元后的有理拆分", "Rational Decomposition after Substitution",
    "计算 $\\displaystyle \\int_0^1\\frac{x^3}{(1+x^2)^2}\\,dx$。",
    "Evaluate $\\displaystyle \\int_0^1\\frac{x^3}{(1+x^2)^2}\\,dx$.",
    "$\\frac12\\ln2-\\frac14$", "$\\frac12\\ln2-\\frac14$",
    "令 $u=1+x^2$ 后，把 $x^2$ 写成 $u-1$，使所有原变量完全消失。",
    "After setting $u=1+x^2$, rewrite $x^2$ as $u-1$ so that no old variable remains.",
    [
        "令 $u=1+x^2$，则 $du=2x\\,dx$，且 $x^2=u-1$。",
        "端点 $x=0,1$ 变为 $u=1,2$。",
        "原积分化为 $\\frac12\\int_1^2\\frac{u-1}{u^2}\\,du=\\frac12\\int_1^2\\left(\\frac1u-\\frac1{u^2}\\right)du$。",
        "原函数为 $\\frac12\\left(\\ln u+\\frac1u\\right)$。",
        "代入端点得 $\\frac12\\left(\\ln2+\\frac12-1\\right)=\\frac12\\ln2-\\frac14$。",
    ],
    [
        "Set $u=1+x^2$, so $du=2x\\,dx$ and $x^2=u-1$.",
        "The endpoints $x=0,1$ become $u=1,2$.",
        "The integral becomes $\\frac12\\int_1^2\\frac{u-1}{u^2}\\,du=\\frac12\\int_1^2\\left(\\frac1u-\\frac1{u^2}\\right)du$.",
        "An antiderivative is $\\frac12\\left(\\ln u+\\frac1u\\right)$.",
        "Endpoint evaluation gives $\\frac12\\left(\\ln2+\\frac12-1\\right)=\\frac12\\ln2-\\frac14$.",
    ],
    "答案约为 $0.0966>0$；这与原被积函数非负且在 $[0,1]$ 上较小相符。",
    "The answer is approximately $0.0966>0$, consistent with the nonnegative and relatively small integrand on $[0,1]$.",
)

add(
    "Q064", 3, "calculation", "definite_integral_by_parts",
    "线性因子乘余弦", "A Linear Factor Times Cosine",
    "计算 $\\displaystyle \\int_0^{\\frac\\pi2}x\\cos x\\,dx$。",
    "Evaluate $\\displaystyle \\int_0^{\\frac\\pi2}x\\cos x\\,dx$.",
    "$\\frac\\pi2-1$", "$\\frac\\pi2-1$",
    "取 $u=x$、$dv=\\cos x\\,dx$；边界项在上端产生 $\\frac\\pi2$，剩余正弦积分产生 $1$。",
    "Choose $u=x$ and $dv=\\cos x\\,dx$; the upper boundary contributes $\\frac\\pi2$, and the remaining sine integral contributes $1$.",
    [
        "令 $u=x$、$dv=\\cos x\\,dx$，则 $du=dx$、$v=\\sin x$。",
        "分部积分得 $\\int_0^{\\frac\\pi2}x\\cos x\\,dx=\\left.x\\sin x\\right|_0^{\\frac\\pi2}-\\int_0^{\\frac\\pi2}\\sin x\\,dx$。",
        "边界项为 $\\frac\\pi2$。",
        "剩余积分为 $1$，所以结果是 $\\frac\\pi2-1$。",
    ],
    [
        "Let $u=x$ and $dv=\\cos x\\,dx$, so $du=dx$ and $v=\\sin x$.",
        "Integration by parts gives $\\int_0^{\\frac\\pi2}x\\cos x\\,dx=\\left.x\\sin x\\right|_0^{\\frac\\pi2}-\\int_0^{\\frac\\pi2}\\sin x\\,dx$.",
        "The boundary term is $\\frac\\pi2$.",
        "The remaining integral is $1$, so the value is $\\frac\\pi2-1$.",
    ],
    "被积函数非负，且 $\\frac\\pi2-1\\approx0.571>0$；对原函数 $x\\sin x+\\cos x$ 求导也恢复 $x\\cos x$。",
    "The integrand is nonnegative and $\\frac\\pi2-1\\approx0.571>0$; differentiating $x\\sin x+\\cos x$ also recovers $x\\cos x$.",
)

add(
    "Q065", 3, "proof", "definite_integral_substitution",
    "关于区间中点对称的加权积分", "A Weighted Integral with Midpoint Symmetry",
    "设 $a>0$，$f$ 在 $[0,a]$ 上连续并满足 $f(a-x)=f(x)$。证明 $\\displaystyle \\int_0^a x f(x)\\,dx=\\frac{a}{2}\\int_0^a f(x)\\,dx$。",
    "Let $a>0$ and let $f$ be continuous on $[0,a]$ with $f(a-x)=f(x)$. Prove $\\displaystyle \\int_0^a x f(x)\\,dx=\\frac{a}{2}\\int_0^a f(x)\\,dx$.",
    "证明见解析。", "See the proof.",
    "把加权积分记为 $I$，作反射换元 $u=a-x$；对称条件把变换后的函数恢复成 $f(u)$，再与原式相加。",
    "Call the weighted integral $I$ and reflect with $u=a-x$; symmetry restores $f(u)$, after which adding the two representations removes the weight.",
    [
        "记 $I=\\int_0^a x f(x)\\,dx$。",
        "令 $u=a-x$，则 $dx=-du$，端点 $0,a$ 变为 $a,0$。",
        "利用 $f(a-u)=f(u)$，得到 $I=\\int_0^a(a-u)f(u)\\,du$。",
        "将它与原表示 $I=\\int_0^a u f(u)\\,du$ 相加，得 $2I=a\\int_0^af(u)\\,du$。",
        "两边除以 $2$ 即得所证公式。",
    ],
    [
        "Let $I=\\int_0^a x f(x)\\,dx$.",
        "Set $u=a-x$, so $dx=-du$ and endpoints $0,a$ become $a,0$.",
        "Using $f(a-u)=f(u)$ gives $I=\\int_0^a(a-u)f(u)\\,du$.",
        "Add this to $I=\\int_0^a u f(u)\\,du$ to obtain $2I=a\\int_0^af(u)\\,du$.",
        "Division by $2$ proves the formula.",
    ],
    "取 $f\\equiv1$，左侧为 $\\frac{a^2}{2}$，右侧为 $\\frac a2\\cdot a=\\frac{a^2}{2}$。",
    "For $f\\equiv1$, the left side is $\\frac{a^2}{2}$ and the right side is $\\frac a2\\cdot a=\\frac{a^2}{2}$.",
)

add(
    "Q066", 3, "comprehensive", "definite_integral_substitution",
    "带参数半圆根式积分", "A Parameterized Semicircle-Radical Integral",
    "设 $a>0$。计算 $\\displaystyle I(a)=\\int_0^a x\\sqrt{a^2-x^2}\\,dx$，并说明答案随尺度 $a$ 的次数。",
    "Let $a>0$. Evaluate $\\displaystyle I(a)=\\int_0^a x\\sqrt{a^2-x^2}\\,dx$ and identify its scaling power in $a$.",
    "$I(a)=\\frac{a^3}{3}$，按三次尺度变化。", "$I(a)=\\frac{a^3}{3}$, scaling cubically in $a$.",
    "根式内的二次式与外部因子 $x\\,dx$ 配套；换元 $u=a^2-x^2$ 后端点从 $a^2$ 到 $0$。",
    "The quadratic inside the radical pairs with $x\\,dx$; the substitution $u=a^2-x^2$ sends the endpoints from $a^2$ to $0$.",
    [
        "令 $u=a^2-x^2$，则 $du=-2x\\,dx$。",
        "当 $x=0$ 时 $u=a^2$；当 $x=a$ 时 $u=0$。",
        "所以 $I(a)=-\\frac12\\int_{a^2}^0u^{\\frac12}\\,du=\\frac12\\int_0^{a^2}u^{\\frac12}\\,du$。",
        "计算得 $I(a)=\\frac12\\cdot\\frac23(a^2)^{\\frac32}$。",
        "因 $a>0$，$(a^2)^{\\frac32}=a^3$，故 $I(a)=\\frac{a^3}{3}$；这也显示三次尺度。",
    ],
    [
        "Set $u=a^2-x^2$, so $du=-2x\\,dx$.",
        "When $x=0$, $u=a^2$; when $x=a$, $u=0$.",
        "Thus $I(a)=-\\frac12\\int_{a^2}^0u^{\\frac12}\\,du=\\frac12\\int_0^{a^2}u^{\\frac12}\\,du$.",
        "Evaluation gives $I(a)=\\frac12\\cdot\\frac23(a^2)^{\\frac32}$.",
        "Since $a>0$, $(a^2)^{\\frac32}=a^3$, so $I(a)=\\frac{a^3}{3}$ and the scaling is cubic.",
    ],
    "另令 $x=at$ 可直接提出 $a\\cdot a\\cdot a=a^3$，得到 $I(a)=a^3\\int_0^1t\\sqrt{1-t^2}\\,dt=\\frac{a^3}{3}$。",
    "Alternatively, $x=at$ extracts $a\\cdot a\\cdot a=a^3$ and gives $I(a)=a^3\\int_0^1t\\sqrt{1-t^2}\\,dt=\\frac{a^3}{3}$.",
)

add(
    "Q067", 3, "error_diagnosis", "definite_integral_substitution",
    "诊断非一一换元", "Diagnosing a Non-injective Substitution",
    "某同学计算 $\\displaystyle J=\\int_{-1}^1|x|e^{x^2}\\,dx$，直接令 $u=x^2$，因新上下限都是 $1$ 而写出 $J=\\frac12\\int_1^1e^u\\,du=0$。指出错误并求出正确值。",
    "A student evaluates $\\displaystyle J=\\int_{-1}^1|x|e^{x^2}\\,dx$ by setting $u=x^2$ on the whole interval and writes $J=\\frac12\\int_1^1e^u\\,du=0$ because both transformed endpoints are $1$. Identify the error and find the correct value.",
    "$J=e-1$；错误在于把 $|x|\\,dx$ 全程写成 $\\frac12du$，忽略了负半轴上 $|x|=-x$。", "$J=e-1$; the error is treating $|x|\\,dx$ as $\\frac12du$ on both branches and ignoring that $|x|=-x$ on the negative half-axis.",
    "映射 $x^2$ 的两支具有相反方向，而绝对值又改变了微分因子的符号；应先用偶性化到 $[0,1]$，或在 $0$ 处分段换元。",
    "The two branches of $x^2$ have opposite orientations, while the absolute value changes the sign relation in the differential. Use evenness first or split at $0$.",
    [
        "$|x|e^{x^2}$ 是偶函数，所以 $J=2\\int_0^1xe^{x^2}\\,dx$。",
        "在 $[0,1]$ 上令 $u=x^2$，此时 $du=2x\\,dx$，端点由 $0,1$ 变为 $0,1$。",
        "于是 $J=2\\cdot\\frac12\\int_0^1e^u\\,du=\\left.e^u\\right|_0^1=e-1$。",
        "学生的全区间写法把负半轴上的 $|x|=-x$ 漏掉；在那里应有 $|x|\\,dx=-\\frac12du$。",
        "由于原被积函数处处非负且不恒为零，答案 $0$ 也立即违反符号检查。",
    ],
    [
        "$|x|e^{x^2}$ is even, so $J=2\\int_0^1xe^{x^2}\\,dx$.",
        "On $[0,1]$, set $u=x^2$. Then $du=2x\\,dx$, and endpoints $0,1$ remain $0,1$.",
        "Therefore $J=2\\cdot\\frac12\\int_0^1e^u\\,du=\\left.e^u\\right|_0^1=e-1$.",
        "The student's global step omits $|x|=-x$ on the negative half-axis, where $|x|\\,dx=-\\frac12du$.",
        "Since the original integrand is nonnegative and not identically zero, the claimed value $0$ also fails an immediate sign check.",
    ],
    "分段验算：左右两段各为 $\\frac12(e-1)$，相加得到 $e-1>0$。",
    "Splitting verifies that each half contributes $\\frac12(e-1)$, so the total is $e-1>0$.",
)

add(
    "Q068", 3, "calculation", "definite_integral_by_parts",
    "反正切函数的定积分", "A Definite Integral of Arctangent",
    "计算 $\\displaystyle \\int_0^1\\arctan x\\,dx$。",
    "Evaluate $\\displaystyle \\int_0^1\\arctan x\\,dx$.",
    "$\\frac\\pi4-\\frac12\\ln2$", "$\\frac\\pi4-\\frac12\\ln2$",
    "把 $1$ 作为易积分因子，令 $u=\\arctan x$；分部后出现 $\\frac{x}{1+x^2}$，可用对数换元。",
    "Use $1$ as the easily integrated factor and take $u=\\arctan x$; integration by parts produces $\\frac{x}{1+x^2}$, which is logarithmic.",
    [
        "取 $u=\\arctan x$、$dv=dx$，则 $du=\\frac{dx}{1+x^2}$、$v=x$。",
        "分部积分得 $\\int_0^1\\arctan x\\,dx=\\left.x\\arctan x\\right|_0^1-\\int_0^1\\frac{x}{1+x^2}\\,dx$。",
        "边界项为 $\\frac\\pi4$。",
        "令 $w=1+x^2$，剩余积分为 $\\frac12\\ln2$。",
        "故结果为 $\\frac\\pi4-\\frac12\\ln2$。",
    ],
    [
        "Choose $u=\\arctan x$ and $dv=dx$, so $du=\\frac{dx}{1+x^2}$ and $v=x$.",
        "Integration by parts gives $\\int_0^1\\arctan x\\,dx=\\left.x\\arctan x\\right|_0^1-\\int_0^1\\frac{x}{1+x^2}\\,dx$.",
        "The boundary term is $\\frac\\pi4$.",
        "With $w=1+x^2$, the remaining integral is $\\frac12\\ln2$.",
        "Hence the value is $\\frac\\pi4-\\frac12\\ln2$.",
    ],
    "因 $0\\le\\arctan x\\le\\frac\\pi4$，积分应介于 $0$ 与 $\\frac\\pi4$；所得值约 $0.439$，符合。",
    "Since $0\\le\\arctan x\\le\\frac\\pi4$, the integral lies between $0$ and $\\frac\\pi4$; the value is approximately $0.439$.",
)

add(
    "Q069", 3, "proof", "definite_integral_by_parts",
    "Wallis 积分递推", "The Wallis Integral Recurrence",
    "对整数 $n\\ge2$，设 $I_n=\\displaystyle \\int_0^{\\frac\\pi2}\\sin^n x\\,dx$。证明 $\\displaystyle I_n=\\frac{n-1}{n}I_{n-2}$，并给出初值 $I_0,I_1$。",
    "For an integer $n\\ge2$, let $I_n=\\displaystyle \\int_0^{\\frac\\pi2}\\sin^n x\\,dx$. Prove $\\displaystyle I_n=\\frac{n-1}{n}I_{n-2}$ and state $I_0,I_1$.",
    "$I_n=\\frac{n-1}{n}I_{n-2}$，$I_0=\\frac\\pi2$，$I_1=1$。", "$I_n=\\frac{n-1}{n}I_{n-2}$, $I_0=\\frac\\pi2$, and $I_1=1$.",
    "拆出一个 $\\sin x$ 作为 $dv$，让 $\\sin^{n-1}x$ 求导；用 $\\cos^2x=1-\\sin^2x$ 后会重新出现 $I_n$。",
    "Use one factor $\\sin x$ as $dv$ and differentiate $\\sin^{n-1}x$; after $\\cos^2x=1-\\sin^2x$, the integral $I_n$ reappears.",
    [
        "写成 $I_n=\\int_0^{\\frac\\pi2}\\sin^{n-1}x\\sin x\\,dx$。",
        "取 $u=\\sin^{n-1}x$、$dv=\\sin x\\,dx$，则 $du=(n-1)\\sin^{n-2}x\\cos x\\,dx$、$v=-\\cos x$。",
        "边界项 $[-\\sin^{n-1}x\\cos x]_0^{\\frac\\pi2}=0$。",
        "于是 $I_n=(n-1)\\int_0^{\\frac\\pi2}\\sin^{n-2}x\\cos^2x\\,dx$。",
        "代入 $\\cos^2x=1-\\sin^2x$，得 $I_n=(n-1)(I_{n-2}-I_n)$。",
        "整理为 $nI_n=(n-1)I_{n-2}$；直接积分得 $I_0=\\frac\\pi2$、$I_1=1$。",
    ],
    [
        "Write $I_n=\\int_0^{\\frac\\pi2}\\sin^{n-1}x\\sin x\\,dx$.",
        "Take $u=\\sin^{n-1}x$ and $dv=\\sin x\\,dx$, giving $du=(n-1)\\sin^{n-2}x\\cos x\\,dx$ and $v=-\\cos x$.",
        "The boundary term $[-\\sin^{n-1}x\\cos x]_0^{\\frac\\pi2}$ is $0$.",
        "Therefore $I_n=(n-1)\\int_0^{\\frac\\pi2}\\sin^{n-2}x\\cos^2x\\,dx$.",
        "Using $\\cos^2x=1-\\sin^2x$ gives $I_n=(n-1)(I_{n-2}-I_n)$.",
        "Thus $nI_n=(n-1)I_{n-2}$; direct integration gives $I_0=\\frac\\pi2$ and $I_1=1$.",
    ],
    "由递推 $I_2=\\frac12I_0=\\frac\\pi4$，与 $\\sin^2x$ 的降幂公式直接积分一致。",
    "The recurrence gives $I_2=\\frac12I_0=\\frac\\pi4$, agreeing with direct integration using the power-reduction identity.",
)

add(
    "Q070", 3, "proof", "definite_integral_by_parts",
    "分部积分的加权导数恒等式", "A Weighted-Derivative Identity from Integration by Parts",
    "设 $a>0$，$f$ 在 $[0,a]$ 上连续可微。证明 $\\displaystyle \\int_0^a x f'(x)\\,dx=a f(a)-\\int_0^a f(x)\\,dx$。",
    "Let $a>0$ and let $f$ be continuously differentiable on $[0,a]$. Prove $\\displaystyle \\int_0^a x f'(x)\\,dx=a f(a)-\\int_0^a f(x)\\,dx$.",
    "证明见解析。", "See the proof.",
    "把 $x$ 作为求导后简化的因子、$f'(x)\\,dx$ 作为可直接积分的因子；下端边界因乘有 $x$ 自动为零。",
    "Use $x$ as the factor simplified by differentiation and $f'(x)\\,dx$ as the directly integrable factor; the lower boundary vanishes because it is multiplied by $x$.",
    [
        "取 $u=x$、$dv=f'(x)\\,dx$，则 $du=dx$、$v=f(x)$。",
        "定积分分部公式给出 $\\int_0^a x f'(x)\\,dx=\\left.xf(x)\\right|_0^a-\\int_0^af(x)\\,dx$。",
        "上端边界为 $af(a)$。",
        "下端边界为 $0\\cdot f(0)=0$。",
        "代回即得 $\\int_0^a x f'(x)\\,dx=af(a)-\\int_0^af(x)\\,dx$。",
    ],
    [
        "Choose $u=x$ and $dv=f'(x)\\,dx$, so $du=dx$ and $v=f(x)$.",
        "Definite integration by parts yields $\\int_0^a x f'(x)\\,dx=\\left.xf(x)\\right|_0^a-\\int_0^af(x)\\,dx$.",
        "The upper boundary is $af(a)$.",
        "The lower boundary is $0\\cdot f(0)=0$.",
        "Substitution gives the desired identity.",
    ],
    "取 $f(x)=x^2$：左侧为 $\\int_0^a2x^2dx=\\frac{2a^3}{3}$，右侧为 $a^3-\\frac{a^3}{3}=\\frac{2a^3}{3}$。",
    "For $f(x)=x^2$, the left side is $\\int_0^a2x^2dx=\\frac{2a^3}{3}$ and the right side is $a^3-\\frac{a^3}{3}=\\frac{2a^3}{3}$.",
)

add(
    "Q071", 4, "true_false", "improper_integral_infinite_interval",
    "无穷区间的幂积分判别", "The Power Test on an Infinite Interval",
    "对实参数 $p$ 判断：反常积分 $\\displaystyle \\int_1^{+\\infty}\\frac{dx}{x^p}$ 当且仅当 $p>1$ 时收敛。",
    "For real $p$, determine whether the following statement is true: the improper integral $\\displaystyle \\int_1^{+\\infty}\\frac{dx}{x^p}$ converges if and only if $p>1$.",
    "正确。", "True.",
    "分别处理 $p=1$ 与 $p\\ne1$；收敛取决于截断原函数在 $R\\to+\\infty$ 时是否有有限极限。",
    "Handle $p=1$ and $p\\ne1$ separately; convergence depends on whether the truncated antiderivative has a finite limit as $R\\to+\\infty$.",
    [
        "按定义考察 $\\lim_{R\\to+\\infty}\\int_1^Rx^{-p}\\,dx$。",
        "若 $p\\ne1$，截断积分为 $\\frac{R^{1-p}-1}{1-p}$。",
        "当 $p>1$ 时 $R^{1-p}\\to0$，极限为 $\\frac{1}{p-1}$；当 $p<1$ 时该式发散到 $+\\infty$。",
        "若 $p=1$，截断积分为 $\\ln R\\to+\\infty$。",
        "因此恰在 $p>1$ 时收敛。",
    ],
    [
        "By definition, examine $\\lim_{R\\to+\\infty}\\int_1^Rx^{-p}\\,dx$.",
        "For $p\\ne1$, the truncated integral is $\\frac{R^{1-p}-1}{1-p}$.",
        "If $p>1$, then $R^{1-p}\\to0$ and the limit is $\\frac{1}{p-1}$; if $p<1$, it diverges to $+\\infty$.",
        "For $p=1$, the truncated integral is $\\ln R\\to+\\infty$.",
        "Thus convergence occurs exactly when $p>1$.",
    ],
    "取 $p=2$ 得值 $1$，取临界值 $p=1$ 得 $\\ln R$ 发散，分别核验收敛区间和边界。",
    "For $p=2$ the value is $1$, while the boundary case $p=1$ gives the divergent $\\ln R$, checking both the range and its threshold.",
)

add(
    "Q072", 4, "calculation", "improper_integral_infinite_interval",
    "最基本的无穷区间反常积分", "A Basic Improper Integral on an Infinite Interval",
    "计算 $\\displaystyle \\int_1^{+\\infty}\\frac{dx}{x^2}$。",
    "Evaluate $\\displaystyle \\int_1^{+\\infty}\\frac{dx}{x^2}$.",
    "$1$", "$1$",
    "用有限上限 $R$ 替代 $+\\infty$，计算后再令 $R\\to+\\infty$；不能把无穷大直接代入原函数。",
    "Replace $+\\infty$ by a finite upper limit $R$, evaluate, and then let $R\\to+\\infty$; infinity is not an endpoint value to substitute directly.",
    [
        "按定义写成 $\\lim_{R\\to+\\infty}\\int_1^Rx^{-2}\\,dx$。",
        "原函数为 $-x^{-1}$。",
        "截断积分等于 $\\left.-\\frac1x\\right|_1^R=1-\\frac1R$。",
        "令 $R\\to+\\infty$ 得极限 $1$，所以反常积分收敛且值为 $1$。",
    ],
    [
        "By definition, write $\\lim_{R\\to+\\infty}\\int_1^Rx^{-2}\\,dx$.",
        "An antiderivative is $-x^{-1}$.",
        "The truncated integral is $\\left.-\\frac1x\\right|_1^R=1-\\frac1R$.",
        "As $R\\to+\\infty$, the limit is $1$, so the improper integral converges to $1$.",
    ],
    "尾积分 $\\int_A^{+\\infty}x^{-2}dx=\\frac1A\\to0$，独立符合收敛积分尾部消失的必要性质。",
    "The tail $\\int_A^{+\\infty}x^{-2}dx=\\frac1A\\to0$, independently matching the vanishing-tail property of a convergent improper integral.",
)

add(
    "Q073", 4, "calculation", "improper_integral_singular_endpoint",
    "可积的端点幂奇性", "An Integrable Power Singularity at an Endpoint",
    "计算 $\\displaystyle \\int_0^1\\frac{dx}{\\sqrt{x}}$。",
    "Evaluate $\\displaystyle \\int_0^1\\frac{dx}{\\sqrt{x}}$.",
    "$2$", "$2$",
    "被积函数在 $x=0$ 无界，必须从右侧截断；幂指数 $-\\frac12>-1$ 预示其可积。",
    "The integrand is unbounded at $x=0$, so truncate from the right; the exponent $-\\frac12>-1$ indicates integrability.",
    [
        "按定义写成 $\\lim_{\\varepsilon\\to0^+}\\int_\\varepsilon^1x^{-\\frac12}\\,dx$。",
        "原函数为 $2\\sqrt{x}$。",
        "截断积分等于 $2-2\\sqrt\\varepsilon$。",
        "当 $\\varepsilon\\to0^+$ 时，$\\sqrt\\varepsilon\\to0$。",
        "因此反常积分收敛，值为 $2$。",
    ],
    [
        "By definition, write $\\lim_{\\varepsilon\\to0^+}\\int_\\varepsilon^1x^{-\\frac12}\\,dx$.",
        "An antiderivative is $2\\sqrt{x}$.",
        "The truncated integral equals $2-2\\sqrt\\varepsilon$.",
        "As $\\varepsilon\\to0^+$, $\\sqrt\\varepsilon\\to0$.",
        "Therefore the improper integral converges to $2$.",
    ],
    "虽然被积函数无界，但截断面积 $2-2\\sqrt\\varepsilon$ 有有限极限；这也说明“无界”不等同于“不可积”。",
    "Although the integrand is unbounded, the truncated area $2-2\\sqrt\\varepsilon$ has a finite limit, showing that unbounded does not mean nonintegrable.",
)

add(
    "Q074", 4, "proof", "improper_integral_convergence_tests",
    "用比较法证明对数型发散", "Proving Logarithmic Divergence by Comparison",
    "证明反常积分 $\\displaystyle \\int_1^{+\\infty}\\frac{dx}{x+1}$ 发散。",
    "Prove that $\\displaystyle \\int_1^{+\\infty}\\frac{dx}{x+1}$ diverges.",
    "发散到 $+\\infty$。", "It diverges to $+\\infty$.",
    "在 $x\\ge1$ 时用发散基准函数 $\\frac1x$ 给出下界；非负函数大于一个发散积分的被积函数，因此也发散。",
    "For $x\\ge1$, bound below by a constant multiple of the divergent benchmark $\\frac1x$; a nonnegative integral above a divergent one also diverges.",
    [
        "对 $x\\ge1$，有 $x+1\\le2x$。",
        "两边取正数倒数得到 $\\frac1{x+1}\\ge\\frac1{2x}$。",
        "对任意 $R>1$，$\\int_1^R\\frac{dx}{x+1}\\ge\\frac12\\int_1^R\\frac{dx}{x}=\\frac12\\ln R$。",
        "当 $R\\to+\\infty$ 时，$\\frac12\\ln R\\to+\\infty$。",
        "由比较法，原反常积分发散到 $+\\infty$。",
    ],
    [
        "For $x\\ge1$, $x+1\\le2x$.",
        "Taking reciprocals of positive quantities gives $\\frac1{x+1}\\ge\\frac1{2x}$.",
        "For every $R>1$, $\\int_1^R\\frac{dx}{x+1}\\ge\\frac12\\int_1^R\\frac{dx}{x}=\\frac12\\ln R$.",
        "As $R\\to+\\infty$, $\\frac12\\ln R\\to+\\infty$.",
        "The comparison test therefore proves divergence to $+\\infty$.",
    ],
    "直接计算截断积分为 $\\ln(R+1)-\\ln2$，其极限也为 $+\\infty$，与比较结论一致。",
    "Direct truncation gives $\\ln(R+1)-\\ln2\\to+\\infty$, agreeing with the comparison argument.",
)

add(
    "Q075", 4, "comprehensive", "improper_integral_interior_singularity",
    "主值存在但普通积分发散", "A Principal Value Exists but the Ordinary Integral Diverges",
    "讨论 $\\displaystyle \\int_{-1}^{1}\\frac{dx}{x}$ 的普通反常积分与 Cauchy 主值。",
    "Discuss the ordinary improper integral and the Cauchy principal value of $\\displaystyle \\int_{-1}^{1}\\frac{dx}{x}$.",
    "普通反常积分发散；$\\displaystyle \\operatorname{PV}\\int_{-1}^{1}\\frac{dx}{x}=0$。", "The ordinary improper integral diverges, while $\\displaystyle \\operatorname{PV}\\int_{-1}^{1}\\frac{dx}{x}=0$.",
    "内部瑕点 $0$ 把区间分成左右两个独立反常积分；只有主值才允许采用同一对称截断参数。",
    "The interior singularity at $0$ splits the interval into two independent improper integrals; only the principal value uses one symmetric truncation parameter.",
    [
        "左侧为 $\\lim_{c\\to0^-}\\int_{-1}^{c}\\frac{dx}{x}=\\lim_{c\\to0^-}\\ln|c|=-\\infty$。",
        "右侧为 $\\lim_{d\\to0^+}\\int_d^1\\frac{dx}{x}=\\lim_{d\\to0^+}(-\\ln d)=+\\infty$。",
        "普通反常积分要求左右两侧都收敛到有限值，因此原积分发散；不能把 $-\\infty$ 与 $+\\infty$ 相消。",
        "主值按对称截断定义为 $\\lim_{\\varepsilon\\to0^+}\\left(\\int_{-1}^{-\\varepsilon}\\frac{dx}{x}+\\int_\\varepsilon^1\\frac{dx}{x}\\right)$。",
        "两项对每个 $\\varepsilon$ 都精确相消，所以主值为 $0$。",
    ],
    [
        "The left part is $\\lim_{c\\to0^-}\\int_{-1}^{c}\\frac{dx}{x}=\\lim_{c\\to0^-}\\ln|c|=-\\infty$.",
        "The right part is $\\lim_{d\\to0^+}\\int_d^1\\frac{dx}{x}=\\lim_{d\\to0^+}(-\\ln d)=+\\infty$.",
        "Ordinary convergence requires both sides to have finite limits, so the integral diverges; $-\\infty$ and $+\\infty$ cannot be canceled.",
        "The principal value is $\\lim_{\\varepsilon\\to0^+}\\left(\\int_{-1}^{-\\varepsilon}\\frac{dx}{x}+\\int_\\varepsilon^1\\frac{dx}{x}\\right)$.",
        "The two terms cancel exactly for every $\\varepsilon$, hence the principal value is $0$.",
    ],
    "用不同速率截断，例如左端距离为 $\\varepsilon$、右端距离为 $2\\varepsilon$，和趋于 $-\\ln2$ 而非 $0$，说明普通极限不稳定。",
    "Using unequal cutoffs, such as distances $\\varepsilon$ on the left and $2\\varepsilon$ on the right, makes the sum tend to $-\\ln2$ rather than $0$, showing the lack of an ordinary limit.",
)

add(
    "Q076", 4, "calculation", "improper_integral_singular_endpoint",
    "三次根端点奇性", "A Cube-Root Endpoint Singularity",
    "计算 $\\displaystyle \\int_0^1\\frac{dx}{\\sqrt[3]{x}}$。",
    "Evaluate $\\displaystyle \\int_0^1\\frac{dx}{\\sqrt[3]{x}}$.",
    "$\\frac32$", "$\\frac32$",
    "把被积函数写成 $x^{-\\frac13}$ 并在 $0$ 的右侧截断；原函数指数变为 $\\frac23>0$。",
    "Write the integrand as $x^{-\\frac13}$ and truncate to the right of $0$; the antiderivative has exponent $\\frac23>0$.",
    [
        "定义为 $\\lim_{\\varepsilon\\to0^+}\\int_\\varepsilon^1x^{-\\frac13}\\,dx$。",
        "原函数是 $\\frac32x^{\\frac23}$。",
        "截断积分为 $\\frac32\\left(1-\\varepsilon^{\\frac23}\\right)$。",
        "由于 $\\varepsilon^{\\frac23}\\to0$，极限为 $\\frac32$。",
    ],
    [
        "By definition, use $\\lim_{\\varepsilon\\to0^+}\\int_\\varepsilon^1x^{-\\frac13}\\,dx$.",
        "An antiderivative is $\\frac32x^{\\frac23}$.",
        "The truncated integral is $\\frac32\\left(1-\\varepsilon^{\\frac23}\\right)$.",
        "Since $\\varepsilon^{\\frac23}\\to0$, the limit is $\\frac32$.",
    ],
    "它符合端点幂积分准则：$\\int_0^1x^{-p}dx$ 在 $p<1$ 时收敛；这里 $p=\\frac13$。",
    "It agrees with the endpoint power test: $\\int_0^1x^{-p}dx$ converges for $p<1$, here $p=\\frac13$.",
)

add(
    "Q077", 4, "calculation", "improper_integral_infinite_interval",
    "指数衰减中的参数符号", "The Parameter Sign in Exponential Decay",
    "对实参数 $a$，讨论并计算 $\\displaystyle I(a)=\\int_0^{+\\infty}e^{-ax}\\,dx$。",
    "For real $a$, determine convergence and evaluate $\\displaystyle I(a)=\\int_0^{+\\infty}e^{-ax}\\,dx$.",
    "当且仅当 $a>0$ 时收敛，且 $I(a)=\\frac1a$；$a\\le0$ 时发散。", "It converges exactly for $a>0$, with $I(a)=\\frac1a$; it diverges for $a\\le0$.",
    "参数 $a$ 决定指数是衰减、恒定还是增长，必须在写原函数前分情况。",
    "The parameter $a$ determines whether the exponential decays, stays constant, or grows, so cases must be separated before applying a formula.",
    [
        "若 $a>0$，截断积分为 $\\int_0^Re^{-ax}dx=\\frac{1-e^{-aR}}{a}$。",
        "因 $e^{-aR}\\to0$，得到 $I(a)=\\frac1a$。",
        "若 $a=0$，被积函数恒为 $1$，截断积分等于 $R\\to+\\infty$。",
        "若 $a<0$，写 $a=-c$ 且 $c>0$，被积函数为 $e^{cx}$，截断积分指数增长。",
        "因此只有 $a>0$ 时收敛。",
    ],
    [
        "If $a>0$, the truncated integral is $\\int_0^Re^{-ax}dx=\\frac{1-e^{-aR}}{a}$.",
        "Because $e^{-aR}\\to0$, $I(a)=\\frac1a$.",
        "If $a=0$, the integrand is $1$ and the truncated integral is $R\\to+\\infty$.",
        "If $a<0$, write $a=-c$ with $c>0$; then the integrand is $e^{cx}$ and its truncated integral grows exponentially.",
        "Thus convergence occurs only for $a>0$.",
    ],
    "在收敛区间内令 $u=ax$，可得 $I(a)=\\frac1a\\int_0^{+\\infty}e^{-u}du=\\frac1a$，再次核验尺度因子。",
    "Within the convergence range, $u=ax$ gives $I(a)=\\frac1a\\int_0^{+\\infty}e^{-u}du=\\frac1a$, independently checking the scale factor.",
)

add(
    "Q078", 4, "calculation", "improper_integral_infinite_interval",
    "对数项在无穷远的抵消", "Cancellation of Logarithms at Infinity",
    "计算 $\\displaystyle \\int_1^{+\\infty}\\frac{dx}{x(x+1)}$。",
    "Evaluate $\\displaystyle \\int_1^{+\\infty}\\frac{dx}{x(x+1)}$.",
    "$\\ln2$", "$\\ln2$",
    "先作部分分式 $\\frac1{x(x+1)}=\\frac1x-\\frac1{x+1}$；两个对数必须作为整体取极限。",
    "First decompose $\\frac1{x(x+1)}=\\frac1x-\\frac1{x+1}$; the logarithms must be combined before taking the limit.",
    [
        "对有限 $R>1$，写 $\\int_1^R\\left(\\frac1x-\\frac1{x+1}\\right)dx$。",
        "截断积分为 $\\left.\\ln\\frac{x}{x+1}\\right|_1^R$。",
        "这等于 $\\ln\\frac{R}{R+1}-\\ln\\frac12$。",
        "当 $R\\to+\\infty$ 时，$\\frac{R}{R+1}\\to1$，第一项趋于 $0$。",
        "故积分收敛且值为 $\\ln2$。",
    ],
    [
        "For finite $R>1$, write $\\int_1^R\\left(\\frac1x-\\frac1{x+1}\\right)dx$.",
        "The truncated integral is $\\left.\\ln\\frac{x}{x+1}\\right|_1^R$.",
        "This equals $\\ln\\frac{R}{R+1}-\\ln\\frac12$.",
        "As $R\\to+\\infty$, $\\frac{R}{R+1}\\to1$, so the first term tends to $0$.",
        "Therefore the integral converges to $\\ln2$.",
    ],
    "因 $0<\\frac1{x(x+1)}<\\frac1{x^2}$ 对 $x\\ge1$ 成立，积分应收敛且小于 $1$；$0<\\ln2<1$。",
    "Since $0<\\frac1{x(x+1)}<\\frac1{x^2}$ for $x\\ge1$, the integral must converge and be below $1$; indeed $0<\\ln2<1$.",
)

add(
    "Q079", 4, "proof", "improper_integral_convergence_tests",
    "反常积分的 Cauchy 尾部准则", "The Cauchy Tail Criterion for an Improper Integral",
    "设 $f$ 在每个有限区间 $[a,R]$ 上连续。证明 $\\displaystyle \\int_a^{+\\infty}f(x)\\,dx$ 收敛，当且仅当对任意 $\\varepsilon>0$，存在 $M>a$，使所有 $B>A\\ge M$ 都满足 $\\displaystyle \\left|\\int_A^Bf(x)\\,dx\\right|<\\varepsilon$。",
    "Let $f$ be continuous on every finite interval $[a,R]$. Prove that $\\displaystyle \\int_a^{+\\infty}f(x)\\,dx$ converges if and only if, for every $\\varepsilon>0$, there exists $M>a$ such that all $B>A\\ge M$ satisfy $\\displaystyle \\left|\\int_A^Bf(x)\\,dx\\right|<\\varepsilon$.",
    "证明见解析。", "See the proof.",
    "把截断积分记为 $F(R)=\\int_a^Rf$；题设条件正是实数函数 $F(R)$ 在 $R\\to+\\infty$ 时的 Cauchy 条件。",
    "Let $F(R)=\\int_a^Rf$; the stated tail condition is exactly the Cauchy condition for the real-valued function $F(R)$ as $R\\to+\\infty$.",
    [
        "定义 $F(R)=\\int_a^Rf(x)\\,dx$，则对 $B>A$ 有 $F(B)-F(A)=\\int_A^Bf(x)\\,dx$。",
        "若反常积分收敛到 $L$，取 $M$ 使 $R\\ge M$ 时 $|F(R)-L|<\\frac\\varepsilon2$。",
        "于是 $|F(B)-F(A)|\\le|F(B)-L|+|F(A)-L|<\\varepsilon$，得到尾部条件。",
        "反之，尾部条件说明 $F(R)$ 在 $R\\to+\\infty$ 时满足 Cauchy 条件。",
        "实数完备性保证存在有限极限 $L=\\lim_{R\\to+\\infty}F(R)$。",
        "按反常积分定义，这正说明 $\\int_a^{+\\infty}f(x)\\,dx$ 收敛。",
    ],
    [
        "Define $F(R)=\\int_a^Rf(x)\\,dx$; for $B>A$, $F(B)-F(A)=\\int_A^Bf(x)\\,dx$.",
        "If the improper integral converges to $L$, choose $M$ so that $|F(R)-L|<\\frac\\varepsilon2$ whenever $R\\ge M$.",
        "Then $|F(B)-F(A)|\\le|F(B)-L|+|F(A)-L|<\\varepsilon$, proving the tail condition.",
        "Conversely, the tail condition says that $F(R)$ satisfies the Cauchy condition as $R\\to+\\infty$.",
        "Completeness of the real numbers gives a finite limit $L=\\lim_{R\\to+\\infty}F(R)$.",
        "By definition, this is convergence of $\\int_a^{+\\infty}f(x)\\,dx$.",
    ],
    "对 $f(x)=x^{-2}$，尾积分绝对值为 $\\frac1A-\\frac1B<\\frac1A$；取 $M>\\frac1\\varepsilon$ 即满足准则。",
    "For $f(x)=x^{-2}$, the tail has magnitude $\\frac1A-\\frac1B<\\frac1A$; choosing $M>\\frac1\\varepsilon$ verifies the criterion.",
)

add(
    "Q080", 4, "comprehensive", "improper_integral_infinite_interval",
    "双侧无穷积分的独立拆分", "Independent Splitting of a Two-sided Infinite Integral",
    "按普通反常积分定义计算 $\\displaystyle \\int_{-\\infty}^{+\\infty}\\frac{dx}{1+x^2}$。",
    "Using the ordinary improper-integral definition, evaluate $\\displaystyle \\int_{-\\infty}^{+\\infty}\\frac{dx}{1+x^2}$.",
    "$\\pi$", "$\\pi$",
    "普通双侧积分必须在任意有限分点（取 $0$）拆成两个独立极限；本题两侧都收敛。",
    "An ordinary two-sided integral must be split at a finite point, here $0$, into two independent limits; both pieces converge.",
    [
        "定义为 $\\int_{-\\infty}^0\\frac{dx}{1+x^2}+\\int_0^{+\\infty}\\frac{dx}{1+x^2}$。",
        "左侧是 $\\lim_{A\\to-\\infty}\\left.\\arctan x\\right|_A^0=0-\\left(-\\frac\\pi2\\right)=\\frac\\pi2$。",
        "右侧是 $\\lim_{B\\to+\\infty}\\left.\\arctan x\\right|_0^B=\\frac\\pi2-0=\\frac\\pi2$。",
        "两部分分别有有限极限，因此普通反常积分收敛。",
        "相加得到总值 $\\pi$。",
    ],
    [
        "By definition, split it as $\\int_{-\\infty}^0\\frac{dx}{1+x^2}+\\int_0^{+\\infty}\\frac{dx}{1+x^2}$.",
        "The left part is $\\lim_{A\\to-\\infty}\\left.\\arctan x\\right|_A^0=0-\\left(-\\frac\\pi2\\right)=\\frac\\pi2$.",
        "The right part is $\\lim_{B\\to+\\infty}\\left.\\arctan x\\right|_0^B=\\frac\\pi2-0=\\frac\\pi2$.",
        "Both pieces have finite limits, so the ordinary improper integral converges.",
        "Their sum is $\\pi$.",
    ],
    "被积函数为偶函数，可写成 $2\\int_0^{+\\infty}\\frac{dx}{1+x^2}=2\\cdot\\frac\\pi2=\\pi$；这与独立拆分一致。",
    "The integrand is even, so the value is $2\\int_0^{+\\infty}\\frac{dx}{1+x^2}=2\\cdot\\frac\\pi2=\\pi$, consistent with the independent split.",
)

add(
    "Q081", 4, "error_diagnosis", "improper_integral_infinite_interval",
    "奇函数对称主值的误用", "Misusing Symmetry as Ordinary Convergence",
    "某同学因 $\\frac{x}{1+x^2}$ 是奇函数而断言 $\\displaystyle \\int_{-\\infty}^{+\\infty}\\frac{x}{1+x^2}\\,dx=0$。诊断错误，并说明普通反常积分与对称主值。",
    "A student argues that $\\frac{x}{1+x^2}$ is odd and therefore $\\displaystyle \\int_{-\\infty}^{+\\infty}\\frac{x}{1+x^2}\\,dx=0$. Diagnose the error and determine the ordinary integral and symmetric principal value.",
    "普通反常积分发散；$\\displaystyle \\operatorname{PV}\\int_{-\\infty}^{+\\infty}\\frac{x}{1+x^2}\\,dx=0$。",
    "The ordinary improper integral diverges; $\\displaystyle \\operatorname{PV}\\int_{-\\infty}^{+\\infty}\\frac{x}{1+x^2}\\,dx=0$.",
    "无穷对称区间上的奇性只控制对称截断，不能保证左右无穷尾部分别有有限极限。",
    "Oddness controls symmetric truncations but does not guarantee finite independent limits on the two infinite tails.",
    [
        "右侧截断积分为 $\\int_0^R\\frac{x}{1+x^2}dx=\\frac12\\ln(1+R^2)\\to+\\infty$。",
        "左侧截断积分为 $\\int_{-R}^0\\frac{x}{1+x^2}dx=-\\frac12\\ln(1+R^2)\\to-\\infty$。",
        "普通积分要求两部分分别收敛到有限值，因此它发散。",
        "对称主值是 $\\lim_{R\\to+\\infty}\\int_{-R}^R\\frac{x}{1+x^2}dx$。",
        "每个对称截断积分都因奇性等于 $0$，故主值为 $0$。",
    ],
    [
        "The right truncated integral is $\\int_0^R\\frac{x}{1+x^2}dx=\\frac12\\ln(1+R^2)\\to+\\infty$.",
        "The left truncated integral is $\\int_{-R}^0\\frac{x}{1+x^2}dx=-\\frac12\\ln(1+R^2)\\to-\\infty$.",
        "Ordinary convergence requires both pieces to have finite limits, so the integral diverges.",
        "The symmetric principal value is $\\lim_{R\\to+\\infty}\\int_{-R}^R\\frac{x}{1+x^2}dx$.",
        "Every symmetric truncation is $0$ by oddness, so the principal value is $0$.",
    ],
    "若左右截断分别取 $R$ 与 $2R$，总和趋于 $\\ln2$ 而非 $0$，证明结果依赖截断方式。",
    "If the left and right cutoffs are $R$ and $2R$, the sum tends to $\\ln2$ rather than $0$, proving dependence on the truncation scheme.",
)

add(
    "Q082", 4, "calculation", "improper_integral_singular_endpoint",
    "对数函数的可积奇性", "The Integrable Logarithmic Singularity",
    "计算 $\\displaystyle \\int_0^1\\ln x\\,dx$。",
    "Evaluate $\\displaystyle \\int_0^1\\ln x\\,dx$.",
    "$-1$", "$-1$",
    "$\\ln x$ 在 $0$ 处趋于 $-\\infty$，但其原函数中的乘积 $x\\ln x$ 有有限右极限。",
    "$\\ln x$ tends to $-\\infty$ at $0$, but the product $x\\ln x$ in its antiderivative has a finite right limit.",
    [
        "按定义写成 $\\lim_{\\varepsilon\\to0^+}\\int_\\varepsilon^1\\ln x\\,dx$。",
        "分部积分得到原函数 $x\\ln x-x$。",
        "截断积分为 $-1-\\varepsilon\\ln\\varepsilon+\\varepsilon$。",
        "利用 $\\lim_{\\varepsilon\\to0^+}\\varepsilon\\ln\\varepsilon=0$ 且 $\\varepsilon\\to0$。",
        "所以反常积分收敛，值为 $-1$。",
    ],
    [
        "By definition, write $\\lim_{\\varepsilon\\to0^+}\\int_\\varepsilon^1\\ln x\\,dx$.",
        "Integration by parts gives the antiderivative $x\\ln x-x$.",
        "The truncated integral is $-1-\\varepsilon\\ln\\varepsilon+\\varepsilon$.",
        "Use $\\lim_{\\varepsilon\\to0^+}\\varepsilon\\ln\\varepsilon=0$ and $\\varepsilon\\to0$.",
        "Thus the improper integral converges to $-1$.",
    ],
    "令 $x=e^{-t}$ 可化为 $-\\int_0^{+\\infty}te^{-t}dt=-1$，提供独立换元核验。",
    "The substitution $x=e^{-t}$ gives $-\\int_0^{+\\infty}te^{-t}dt=-1$, providing an independent check.",
)

add(
    "Q083", 4, "calculation", "improper_integral_infinite_interval",
    "同时含零端与无穷端的换元", "A Substitution with Both Zero and Infinite Endpoints",
    "计算 $\\displaystyle \\int_0^{+\\infty}\\frac{dx}{(1+x)\\sqrt{x}}$。",
    "Evaluate $\\displaystyle \\int_0^{+\\infty}\\frac{dx}{(1+x)\\sqrt{x}}$.",
    "$\\pi$", "$\\pi$",
    "该积分在 $0$ 处有可积根式奇性且区间无穷；令 $x=t^2$ 可同时消去根号并保留两个反常端点。",
    "The integral has an integrable square-root singularity at $0$ and an infinite interval; $x=t^2$ removes the radical while preserving both improper endpoints.",
    [
        "对 $0<\\varepsilon<R$ 先考察 $\\int_\\varepsilon^R\\frac{dx}{(1+x)\\sqrt{x}}$。",
        "令 $x=t^2$ 且 $t>0$，则 $dx=2t\\,dt$、$\\sqrt{x}=t$。",
        "截断积分化为 $2\\int_{\\sqrt{\\varepsilon}}^{\\sqrt{R}}\\frac{dt}{1+t^2}$。",
        "其值为 $2\\left(\\arctan\\sqrt{R}-\\arctan\\sqrt{\\varepsilon}\\right)$。",
        "分别令 $R\\to+\\infty$、$\\varepsilon\\to0^+$，得到 $2\\left(\\frac\\pi2-0\\right)=\\pi$。",
    ],
    [
        "For $0<\\varepsilon<R$, first consider $\\int_\\varepsilon^R\\frac{dx}{(1+x)\\sqrt{x}}$.",
        "Set $x=t^2$ with $t>0$, so $dx=2t\\,dt$ and $\\sqrt{x}=t$.",
        "The truncated integral becomes $2\\int_{\\sqrt{\\varepsilon}}^{\\sqrt{R}}\\frac{dt}{1+t^2}$.",
        "Its value is $2\\left(\\arctan\\sqrt{R}-\\arctan\\sqrt{\\varepsilon}\\right)$.",
        "Letting $R\\to+\\infty$ and $\\varepsilon\\to0^+$ gives $2\\left(\\frac\\pi2-0\\right)=\\pi$.",
    ],
    "在 $0$ 附近被积函数与 $x^{-\\frac12}$ 同阶，在无穷远与 $x^{-\\frac32}$ 同阶；两端均满足幂积分收敛条件。",
    "Near $0$ the integrand is comparable to $x^{-\\frac12}$, and at infinity to $x^{-\\frac32}$; both endpoints meet the power-integral convergence conditions.",
)

add(
    "Q084", 4, "proof", "improper_integral_convergence_tests",
    "非负函数比较审敛法", "The Comparison Test for Nonnegative Functions",
    "设 $0\\le f(x)\\le g(x)$ 对所有 $x\\ge a$ 成立，且两函数在有限区间上可积。证明：若 $\\displaystyle \\int_a^{+\\infty}g(x)\\,dx$ 收敛，则 $\\displaystyle \\int_a^{+\\infty}f(x)\\,dx$ 收敛；若 $\\displaystyle \\int_a^{+\\infty}f(x)\\,dx$ 发散，则 $\\displaystyle \\int_a^{+\\infty}g(x)\\,dx$ 发散。",
    "Assume $0\\le f(x)\\le g(x)$ for all $x\\ge a$, with both functions integrable on finite intervals. Prove: if $\\displaystyle \\int_a^{+\\infty}g(x)\\,dx$ converges, then $\\displaystyle \\int_a^{+\\infty}f(x)\\,dx$ converges; if $\\displaystyle \\int_a^{+\\infty}f(x)\\,dx$ diverges, then $\\displaystyle \\int_a^{+\\infty}g(x)\\,dx$ diverges.",
    "证明见解析。", "See the proof.",
    "非负性使截断积分随上限单调增加；上比较给出有界性，而“发散小函数推出大发散”是同一命题的逆否形式。",
    "Nonnegativity makes truncated integrals monotone in the upper limit; the upper comparison supplies boundedness, and the divergence statement is the contrapositive.",
    [
        "定义 $F(R)=\\int_a^Rf(x)\\,dx$、$G(R)=\\int_a^Rg(x)\\,dx$。",
        "由 $0\\le f\\le g$，对每个 $R>a$ 有 $0\\le F(R)\\le G(R)$。",
        "若 $\\int_a^{+\\infty}g$ 收敛，则 $G(R)$ 有有限上界；于是单调递增的 $F(R)$ 也有上界。",
        "单调有界原理给出 $F(R)$ 的有限极限，因此 $\\int_a^{+\\infty}f$ 收敛。",
        "第二个结论取逆否：若 $\\int_a^{+\\infty}g$ 收敛，第一部分迫使 $\\int_a^{+\\infty}f$ 收敛；故 $f$ 发散时 $g$ 不可能收敛。",
    ],
    [
        "Define $F(R)=\\int_a^Rf(x)\\,dx$ and $G(R)=\\int_a^Rg(x)\\,dx$.",
        "From $0\\le f\\le g$, we have $0\\le F(R)\\le G(R)$ for every $R>a$.",
        "If $\\int_a^{+\\infty}g$ converges, then $G(R)$ is bounded; hence the increasing function $F(R)$ is also bounded.",
        "Monotone bounded convergence gives a finite limit for $F(R)$, so $\\int_a^{+\\infty}f$ converges.",
        "The second claim is the contrapositive: convergence of the larger integral would force convergence of the smaller, so divergence of the smaller forces divergence of the larger.",
    ],
    "以 $f(x)=\\frac1{x^2+x}$、$g(x)=\\frac1{x^2}$ 为例，$0<f<g$ 且大积分收敛，故小积分也收敛。",
    "For example, $f(x)=\\frac1{x^2+x}$ and $g(x)=\\frac1{x^2}$ satisfy $0<f<g$, and convergence of the larger integral forces convergence of the smaller.",
)

add(
    "Q085", 4, "comprehensive", "improper_integral_infinite_interval",
    "带参数正二次式的无穷积分", "An Infinite Integral with a Parameterized Positive Quadratic",
    "设 $a>0$。计算 $\\displaystyle I(a)=\\int_0^{+\\infty}\\frac{dx}{x^2+2ax+2a^2}$。",
    "Let $a>0$. Evaluate $\\displaystyle I(a)=\\int_0^{+\\infty}\\frac{dx}{x^2+2ax+2a^2}$.",
    "$I(a)=\\frac{\\pi}{4a}$", "$I(a)=\\frac{\\pi}{4a}$",
    "先配方为 $(x+a)^2+a^2$；$a>0$ 保证尺度换元方向与正的反正切尺度因子。",
    "Complete the square as $(x+a)^2+a^2$; $a>0$ fixes the orientation and the positive arctangent scale factor.",
    [
        "分母配方得 $x^2+2ax+2a^2=(x+a)^2+a^2$。",
        "令 $u=\\frac{x+a}{a}$，则 $dx=a\\,du$。",
        "因 $a>0$，当 $x=0$ 时 $u=1$，当 $x\\to+\\infty$ 时 $u\\to+\\infty$。",
        "积分化为 $\\frac1a\\int_1^{+\\infty}\\frac{du}{1+u^2}$。",
        "所以 $I(a)=\\frac1a\\left(\\frac\\pi2-\\frac\\pi4\\right)=\\frac\\pi{4a}$。",
    ],
    [
        "Complete the square: $x^2+2ax+2a^2=(x+a)^2+a^2$.",
        "Set $u=\\frac{x+a}{a}$, so $dx=a\\,du$.",
        "Because $a>0$, $x=0$ gives $u=1$ and $x\\to+\\infty$ gives $u\\to+\\infty$.",
        "The integral becomes $\\frac1a\\int_1^{+\\infty}\\frac{du}{1+u^2}$.",
        "Thus $I(a)=\\frac1a\\left(\\frac\\pi2-\\frac\\pi4\\right)=\\frac\\pi{4a}$.",
    ],
    "直接令 $x=at$ 可见积分应按 $a^{-1}$ 缩放；闭式 $\\frac\\pi{4a}$ 与该量纲完全一致。",
    "The direct scaling $x=at$ shows that the integral must scale as $a^{-1}$; $\\frac\\pi{4a}$ has exactly this dependence.",
)

add(
    "Q086", 4, "error_diagnosis", "improper_integral_interior_singularity",
    "跨越二阶瑕点套公式的错误", "Applying Newton-Leibniz across a Second-order Singularity",
    "某同学写 $\\displaystyle \\int_0^2\\frac{dx}{(x-1)^2}=\\left.-\\frac1{x-1}\\right|_0^2=-2$。指出全部错误并给出正确结论。",
    "A student writes $\\displaystyle \\int_0^2\\frac{dx}{(x-1)^2}=\\left.-\\frac1{x-1}\\right|_0^2=-2$. Identify all errors and give the correct conclusion.",
    "普通反常积分发散到 $+\\infty$；不能跨越 $x=1$ 直接使用 Newton-Leibniz 公式。", "The ordinary improper integral diverges to $+\\infty$; Newton-Leibniz cannot be applied across $x=1$.",
    "被积函数在内部点 $1$ 无定义且始终非负；负答案已构成警报，必须把区间拆开并取两个单侧极限。",
    "The integrand is undefined at the interior point $1$ and is nonnegative; the negative result is already a warning, and the interval must be split into two one-sided limits.",
    [
        "在 $x=1$ 处分母为零，因此原积分是内部瑕积分。",
        "左侧 $\\int_0^1\\frac{dx}{(x-1)^2}=\\lim_{c\\to1^-}\\left[-\\frac1{x-1}\\right]_0^c$。",
        "其中 $-\\frac1{c-1}\\to+\\infty$，所以左侧发散。",
        "右侧 $\\int_1^2\\frac{dx}{(x-1)^2}=\\lim_{d\\to1^+}\\left[-\\frac1{x-1}\\right]_d^2$，同样趋于 $+\\infty$。",
        "任一侧发散已足够说明普通反常积分发散；两侧都为正无穷，更不能得到负值。",
    ],
    [
        "The denominator vanishes at $x=1$, so this is an improper integral with an interior singularity.",
        "The left part is $\\int_0^1\\frac{dx}{(x-1)^2}=\\lim_{c\\to1^-}\\left[-\\frac1{x-1}\\right]_0^c$.",
        "Here $-\\frac1{c-1}\\to+\\infty$, so the left part diverges.",
        "The right part is $\\int_1^2\\frac{dx}{(x-1)^2}=\\lim_{d\\to1^+}\\left[-\\frac1{x-1}\\right]_d^2$, which also tends to $+\\infty$.",
        "Divergence on either side is enough; both are positive infinite, so a negative value is impossible.",
    ],
    "由于被积函数在其定义域内非负，任何截断积分都非负；原计算得到 $-2$ 已违反最基本的符号检查。",
    "Because the integrand is nonnegative wherever defined, every truncated integral is nonnegative; the value $-2$ fails the most basic sign check.",
)

add(
    "Q087", 4, "calculation", "improper_integral_infinite_interval",
    "代数衰减与换元", "Algebraic Decay and Substitution",
    "计算 $\\displaystyle \\int_0^{+\\infty}\\frac{x}{(1+x^2)^{\\frac32}}\\,dx$。",
    "Evaluate $\\displaystyle \\int_0^{+\\infty}\\frac{x}{(1+x^2)^{\\frac32}}\\,dx$.",
    "$1$", "$1$",
    "令 $u=1+x^2$ 后得到标准尾部幂积分 $u^{-\\frac32}$；指数小于 $-1$，故在无穷远收敛。",
    "With $u=1+x^2$, the problem becomes the standard tail integral $u^{-\\frac32}$; the exponent is below $-1$, so it converges at infinity.",
    [
        "先写成 $\\lim_{R\\to+\\infty}\\int_0^R\\frac{x}{(1+x^2)^{\\frac32}}dx$。",
        "令 $u=1+x^2$，则 $du=2x\\,dx$，端点变为 $1$ 与 $1+R^2$。",
        "截断积分为 $\\frac12\\int_1^{1+R^2}u^{-\\frac32}du$。",
        "其值为 $1-\\frac1{\\sqrt{1+R^2}}$。",
        "令 $R\\to+\\infty$，第二项趋于 $0$，故结果为 $1$。",
    ],
    [
        "First write $\\lim_{R\\to+\\infty}\\int_0^R\\frac{x}{(1+x^2)^{\\frac32}}dx$.",
        "Set $u=1+x^2$, so $du=2x\\,dx$ and the endpoints become $1$ and $1+R^2$.",
        "The truncated integral is $\\frac12\\int_1^{1+R^2}u^{-\\frac32}du$.",
        "Its value is $1-\\frac1{\\sqrt{1+R^2}}$.",
        "As $R\\to+\\infty$, the second term tends to $0$, so the answer is $1$.",
    ],
    "原函数为 $-\\frac1{\\sqrt{1+x^2}}$；从 $0$ 到无穷的端点差为 $0-(-1)=1$。",
    "An antiderivative is $-\\frac1{\\sqrt{1+x^2}}$; its endpoint difference from $0$ to infinity is $0-(-1)=1$.",
)

add(
    "Q088", 4, "proof", "improper_integral_infinite_interval",
    "无穷远与零点的倒数换元", "Reciprocal Substitution between Infinity and Zero",
    "设 $f$ 在 $[1,+\\infty)$ 上连续。证明在任一侧收敛时，$\\displaystyle \\int_1^{+\\infty}f(x)\\,dx=\\int_0^1\\frac{f\\!\\left(\\frac{1}{t}\\right)}{t^2}\\,dt$，并说明两侧同时收敛或同时发散。",
    "Let $f$ be continuous on $[1,+\\infty)$. Prove that whenever either side converges, $\\displaystyle \\int_1^{+\\infty}f(x)\\,dx=\\int_0^1\\frac{f\\!\\left(\\frac{1}{t}\\right)}{t^2}\\,dt$, and show that the two sides converge or diverge together.",
    "证明见解析。", "See the proof.",
    "先在有限截断区间 $[1,R]$ 上作 $x=\\frac{1}{t}$；无穷上限对应新的瑕点 $t=0^+$，再比较完全相同的截断极限。",
    "First substitute $x=\\frac{1}{t}$ on the finite interval $[1,R]$; the infinite endpoint becomes the new singular endpoint $t=0^+$, and the two truncated limits are identical.",
    [
        "对任意 $R>1$，令 $x=\\frac1t$，则 $dx=-\\frac1{t^2}dt$。",
        "当 $x=1$ 时 $t=1$；当 $x=R$ 时 $t=\\frac1R$。",
        "因此 $\\int_1^Rf(x)\\,dx=\\int_{\\frac{1}{R}}^1\\frac{f\\!\\left(\\frac{1}{t}\\right)}{t^2}\\,dt$。",
        "令 $R\\to+\\infty$ 等价于令 $\\varepsilon=\\frac1R\\to0^+$。",
        "左右截断表达式逐项相等，所以一侧有有限极限当且仅当另一侧有有限极限。",
        "在收敛时取极限，即得题设等式。",
    ],
    [
        "For any $R>1$, set $x=\\frac1t$, so $dx=-\\frac1{t^2}dt$.",
        "When $x=1$, $t=1$; when $x=R$, $t=\\frac1R$.",
        "Hence $\\int_1^Rf(x)\\,dx=\\int_{\\frac{1}{R}}^1\\frac{f\\!\\left(\\frac{1}{t}\\right)}{t^2}\\,dt$.",
        "Letting $R\\to+\\infty$ is equivalent to setting $\\varepsilon=\\frac1R\\to0^+$.",
        "The truncated expressions are identical, so one has a finite limit exactly when the other does.",
        "Taking that limit in the convergent case proves the identity.",
    ],
    "取 $f(x)=x^{-p}$，右侧变为 $\\int_0^1t^{p-2}dt$；其条件 $p-2>-1$ 即 $p>1$，与无穷区间幂积分准则一致。",
    "For $f(x)=x^{-p}$, the right side becomes $\\int_0^1t^{p-2}dt$, which requires $p-2>-1$, namely $p>1$, matching the infinite-interval power test.",
)

add(
    "Q089", 5, "calculation", "improper_integral_convergence_tests",
    "零端点的幂积分全参数分类", "Complete Parameter Classification for an Endpoint Power Integral",
    "对实参数 $p$，讨论并计算 $\\displaystyle I(p)=\\int_0^1\\frac{dx}{x^p}$。",
    "For real $p$, determine convergence and evaluate $\\displaystyle I(p)=\\int_0^1\\frac{dx}{x^p}$.",
    "当且仅当 $p<1$ 时收敛，且 $I(p)=\\frac1{1-p}$；$p\\ge1$ 时发散。", "It converges exactly for $p<1$, with $I(p)=\\frac1{1-p}$; it diverges for $p\\ge1$.",
    "端点 $0$ 的幂指数为 $-p$；分别处理 $p=1$ 的对数临界情形和 $p\\ne1$ 的幂原函数。",
    "The power near $0$ is $-p$; treat the logarithmic boundary case $p=1$ separately from the power antiderivative for $p\\ne1$.",
    [
        "按定义考察 $\\lim_{\\varepsilon\\to0^+}\\int_\\varepsilon^1x^{-p}\\,dx$。",
        "若 $p\\ne1$，截断积分为 $\\frac{1-\\varepsilon^{1-p}}{1-p}$。",
        "当 $p<1$ 时 $1-p>0$，故 $\\varepsilon^{1-p}\\to0$，积分收敛到 $\\frac1{1-p}$。",
        "当 $p>1$ 时 $1-p<0$，$\\varepsilon^{1-p}\\to+\\infty$，截断积分发散到 $+\\infty$。",
        "当 $p=1$ 时，截断积分为 $-\\ln\\varepsilon\\to+\\infty$。",
        "因此收敛条件恰为 $p<1$。",
    ],
    [
        "By definition, examine $\\lim_{\\varepsilon\\to0^+}\\int_\\varepsilon^1x^{-p}\\,dx$.",
        "For $p\\ne1$, the truncated integral is $\\frac{1-\\varepsilon^{1-p}}{1-p}$.",
        "If $p<1$, then $1-p>0$ and $\\varepsilon^{1-p}\\to0$, giving $\\frac1{1-p}$.",
        "If $p>1$, then $1-p<0$ and $\\varepsilon^{1-p}\\to+\\infty$, so the integral diverges to $+\\infty$.",
        "For $p=1$, the truncated integral is $-\\ln\\varepsilon\\to+\\infty$.",
        "Thus the convergence condition is exactly $p<1$.",
    ],
    "取 $p=\\frac12$ 得值 $2$，与 Q073 一致；取 $p=1$ 得对数发散，核验临界点。",
    "For $p=\\frac12$ the value is $2$, agreeing with Q073; $p=1$ gives logarithmic divergence, checking the threshold.",
)

add(
    "Q090", 5, "proof", "improper_integral_convergence_tests",
    "极限比较审敛法", "The Limit Comparison Test",
    "设正函数 $f,g$ 在每个有限区间 $[a,R]$ 上可积，且 $\\displaystyle \\lim_{x\\to+\\infty}\\frac{f(x)}{g(x)}=L$，其中 $0<L<+\\infty$。证明 $\\displaystyle \\int_a^{+\\infty}f(x)\\,dx$ 与 $\\displaystyle \\int_a^{+\\infty}g(x)\\,dx$ 同敛散。",
    "Let positive functions $f,g$ be integrable on every finite interval $[a,R]$, and suppose $\\displaystyle \\lim_{x\\to+\\infty}\\frac{f(x)}{g(x)}=L$ with $0<L<+\\infty$. Prove that $\\displaystyle \\int_a^{+\\infty}f(x)\\,dx$ and $\\displaystyle \\int_a^{+\\infty}g(x)\\,dx$ have the same convergence behavior.",
    "证明见解析。", "See the proof.",
    "用极限定义把比值夹在两个正的常数之间，从而在充分大的尾部得到双向比较；有限首段不影响反常积分敛散。",
    "Use the limit definition to trap the ratio between two positive constants, producing two-sided tail comparisons; a finite initial segment does not affect convergence.",
    [
        "取 $\\varepsilon=\\frac L2$。由极限定义，存在 $M\\ge a$，使 $x\\ge M$ 时 $\\left|\\frac{f(x)}{g(x)}-L\\right|<\\frac L2$。",
        "于是 $\\frac L2<\\frac{f(x)}{g(x)}<\\frac{3L}{2}$，即 $\\frac L2g(x)<f(x)<\\frac{3L}{2}g(x)$。",
        "若 $\\int_a^{+\\infty}g$ 收敛，则其尾部收敛，由上界比较知 $\\int_M^{+\\infty}f$ 收敛。",
        "若 $\\int_a^{+\\infty}f$ 收敛，则由 $g(x)<\\frac2L f(x)$ 得 $\\int_M^{+\\infty}g$ 收敛。",
        "两函数在 $[a,M]$ 上的积分都是有限数，不改变尾部敛散性。",
        "故两个反常积分同敛散。",
    ],
    [
        "Take $\\varepsilon=\\frac L2$. The limit definition gives $M\\ge a$ such that $\\left|\\frac{f(x)}{g(x)}-L\\right|<\\frac L2$ for $x\\ge M$.",
        "Hence $\\frac L2<\\frac{f(x)}{g(x)}<\\frac{3L}{2}$, or $\\frac L2g(x)<f(x)<\\frac{3L}{2}g(x)$.",
        "If $\\int_a^{+\\infty}g$ converges, its tail converges, and the upper comparison makes $\\int_M^{+\\infty}f$ converge.",
        "If $\\int_a^{+\\infty}f$ converges, then $g(x)<\\frac2L f(x)$ makes $\\int_M^{+\\infty}g$ converge.",
        "Both integrals over the finite interval $[a,M]$ are finite and do not affect tail convergence.",
        "Therefore the two improper integrals converge or diverge together.",
    ],
    "对 $f(x)=\\frac1{x^2+1}$、$g(x)=\\frac1{x^2}$，比值趋于 $1$；二者确实都在 $[1,+\\infty)$ 上收敛。",
    "For $f(x)=\\frac1{x^2+1}$ and $g(x)=\\frac1{x^2}$, the ratio tends to $1$, and both integrals converge on $[1,+\\infty)$.",
)

add(
    "Q091", 5, "calculation", "improper_integral_convergence_tests",
    "对数修正幂积分", "A Logarithmically Corrected Power Integral",
    "对实参数 $p$，讨论并计算 $\\displaystyle J(p)=\\int_e^{+\\infty}\\frac{dx}{x(\\ln x)^p}$。",
    "For real $p$, determine convergence and evaluate $\\displaystyle J(p)=\\int_e^{+\\infty}\\frac{dx}{x(\\ln x)^p}$.",
    "当且仅当 $p>1$ 时收敛，且 $J(p)=\\frac1{p-1}$；$p\\le1$ 时发散。", "It converges exactly for $p>1$, with $J(p)=\\frac1{p-1}$; it diverges for $p\\le1$.",
    "换元 $u=\\ln x$ 把对数修正积分精确化为无穷区间幂积分，原下限 $e$ 变成 $1$。",
    "The substitution $u=\\ln x$ converts the logarithmically corrected integral exactly into a power integral on an infinite interval, with lower limit $1$.",
    [
        "对有限 $R>e$，令 $u=\\ln x$，则 $du=\\frac{dx}{x}$。",
        "端点变为 $x=e\\Rightarrow u=1$，$x=R\\Rightarrow u=\\ln R$。",
        "所以 $\\int_e^R\\frac{dx}{x(\\ln x)^p}=\\int_1^{\\ln R}u^{-p}\\,du$。",
        "当 $R\\to+\\infty$ 时，$\\ln R\\to+\\infty$。",
        "由无穷区间幂积分准则，恰在 $p>1$ 时收敛，值为 $\\frac1{p-1}$。",
    ],
    [
        "For finite $R>e$, set $u=\\ln x$, so $du=\\frac{dx}{x}$.",
        "The endpoints become $x=e\\Rightarrow u=1$ and $x=R\\Rightarrow u=\\ln R$.",
        "Thus $\\int_e^R\\frac{dx}{x(\\ln x)^p}=\\int_1^{\\ln R}u^{-p}\\,du$.",
        "As $R\\to+\\infty$, $\\ln R\\to+\\infty$.",
        "The infinite-interval power test gives convergence exactly for $p>1$, with value $\\frac1{p-1}$.",
    ],
    "取 $p=2$ 时原函数为 $-\\frac1{\\ln x}$，从 $e$ 到无穷的端点差为 $0-(-1)=1$，与公式一致。",
    "For $p=2$, an antiderivative is $-\\frac1{\\ln x}$, whose endpoint difference from $e$ to infinity is $0-(-1)=1$, agreeing with the formula.",
)

add(
    "Q092", 5, "proof", "improper_integral_convergence_tests",
    "振荡积分的条件收敛", "Conditional Convergence of an Oscillatory Integral",
    "证明 $\\displaystyle \\int_1^{+\\infty}\\frac{\\sin x}{x}\\,dx$ 收敛但不绝对收敛。",
    "Prove that $\\displaystyle \\int_1^{+\\infty}\\frac{\\sin x}{x}\\,dx$ converges but not absolutely.",
    "条件收敛。", "It converges conditionally.",
    "普通收敛用分部积分控制任意尾积分；绝对值积分则在每个正弦远离零的子区间上给出调和级数型下界。",
    "Ordinary convergence follows by controlling arbitrary tails through integration by parts; the absolute integral has a harmonic-type lower bound on intervals where sine stays away from zero.",
    [
        "对 $B>A\\ge1$，分部积分得 $\\int_A^B\\frac{\\sin x}{x}dx=\\left.-\\frac{\\cos x}{x}\\right|_A^B-\\int_A^B\\frac{\\cos x}{x^2}dx$。",
        "因此尾积分绝对值不超过 $\\frac1A+\\frac1B+\\int_A^B\\frac{dx}{x^2}<\\frac3A$。",
        "当 $A\\to+\\infty$ 时该上界趋于 $0$，由 Cauchy 尾部准则，原积分收敛。",
        "对整数 $k\\ge1$，在区间 $[k\\pi+\\frac\\pi6,k\\pi+\\frac{5\\pi}{6}]$ 上有 $|\\sin x|\\ge\\frac12$。",
        "该区间上的绝对值积分至少为 $\\frac12\\cdot\\frac{2\\pi}{3}\\cdot\\frac{1}{(k+1)\\pi}=\\frac1{3(k+1)}$。",
        "这些互不相交区间的下界之和是发散的调和级数尾部，所以 $\\int_1^{+\\infty}\\frac{|\\sin x|}{x}dx$ 发散。",
    ],
    [
        "For $B>A\\ge1$, integration by parts gives $\\int_A^B\\frac{\\sin x}{x}dx=\\left.-\\frac{\\cos x}{x}\\right|_A^B-\\int_A^B\\frac{\\cos x}{x^2}dx$.",
        "Hence the tail magnitude is at most $\\frac1A+\\frac1B+\\int_A^B\\frac{dx}{x^2}<\\frac3A$.",
        "This bound tends to $0$ as $A\\to+\\infty$, so the Cauchy tail criterion proves convergence.",
        "For every integer $k\\ge1$, $|\\sin x|\\ge\\frac12$ on $[k\\pi+\\frac\\pi6,k\\pi+\\frac{5\\pi}{6}]$.",
        "The absolute integral on this interval is at least $\\frac12\\cdot\\frac{2\\pi}{3}\\cdot\\frac{1}{(k+1)\\pi}=\\frac1{3(k+1)}$.",
        "Summing these lower bounds over disjoint intervals gives a divergent harmonic tail, so $\\int_1^{+\\infty}\\frac{|\\sin x|}{x}dx$ diverges.",
    ],
    "尾估计不仅证明收敛，还给出从 $A$ 开始的截断误差至多为 $\\frac3A$；绝对值下界则明确排除绝对收敛。",
    "The tail estimate proves convergence and gives truncation error at most $\\frac3A$ beyond $A$; the absolute-value lower bound explicitly rules out absolute convergence.",
)

add(
    "Q093", 5, "comprehensive", "gamma_function_enrichment",
    "Gamma 积分的收敛参数", "The Convergence Parameter of the Gamma Integral",
    "对实参数 $s$，讨论 $\\displaystyle \\Gamma(s)=\\int_0^{+\\infty}x^{s-1}e^{-x}\\,dx$ 的收敛性。",
    "For real $s$, determine convergence of $\\displaystyle \\Gamma(s)=\\int_0^{+\\infty}x^{s-1}e^{-x}\\,dx$.",
    "当且仅当 $s>0$ 时收敛。", "It converges exactly for $s>0$.",
    "把积分在 $1$ 处分开：零点附近由幂 $x^{s-1}$ 控制，无穷远由指数衰减控制。",
    "Split at $1$: near zero, behavior is controlled by the power $x^{s-1}$; at infinity, exponential decay dominates.",
    [
        "在 $0<x\\le1$ 上，$e^{-1}\\le e^{-x}\\le1$，所以 $x^{s-1}e^{-x}$ 与 $x^{s-1}$ 同敛散。",
        "端点幂积分 $\\int_0^1x^{s-1}dx$ 当且仅当 $s>0$ 时收敛。",
        "因此 $s\\le0$ 时 Gamma 积分已在 $0$ 附近发散。",
        "若 $s>0$，则在无穷远，固定幂 $x^{s-1}$ 的增长弱于 $e^{\\frac{x}{2}}$；存在 $M$ 使 $x\\ge M$ 时 $x^{s-1}\\le e^{\\frac{x}{2}}$。",
        "于是 $0\\le x^{s-1}e^{-x}\\le e^{-\\frac{x}{2}}$，而 $\\int_M^{+\\infty}e^{-\\frac{x}{2}}\\,dx$ 收敛。",
        "有限中段不影响敛散，故恰在 $s>0$ 时收敛。",
    ],
    [
        "On $0<x\\le1$, $e^{-1}\\le e^{-x}\\le1$, so $x^{s-1}e^{-x}$ has the same local convergence as $x^{s-1}$.",
        "The endpoint power integral $\\int_0^1x^{s-1}dx$ converges exactly when $s>0$.",
        "Thus for $s\\le0$, the Gamma integral already diverges near $0$.",
        "If $s>0$, any fixed power $x^{s-1}$ grows more slowly than $e^{\\frac{x}{2}}$; there is $M$ such that $x^{s-1}\\le e^{\\frac{x}{2}}$ for $x\\ge M$.",
        "Hence $0\\le x^{s-1}e^{-x}\\le e^{-\\frac{x}{2}}$, and $\\int_M^{+\\infty}e^{-\\frac{x}{2}}\\,dx$ converges.",
        "A finite middle interval does not affect convergence, so convergence occurs exactly for $s>0$.",
    ],
    "当 $s=1$ 时积分为 $\\int_0^{+\\infty}e^{-x}dx=1$；当临界值 $s=0$ 时零点附近与 $x^{-1}$ 同阶并发散。",
    "For $s=1$, the integral is $\\int_0^{+\\infty}e^{-x}dx=1$; at the boundary $s=0$, it behaves like $x^{-1}$ near zero and diverges.",
)

add(
    "Q094", 5, "proof", "gamma_function_enrichment",
    "Gamma 函数递推公式", "The Gamma Recurrence",
    "设 $s>0$。证明 $\\displaystyle \\Gamma(s+1)=s\\Gamma(s)$，并严格说明分部积分的两个边界极限。",
    "Let $s>0$. Prove $\\displaystyle \\Gamma(s+1)=s\\Gamma(s)$ and justify both boundary limits used in integration by parts.",
    "$\\Gamma(s+1)=s\\Gamma(s)$。", "$\\Gamma(s+1)=s\\Gamma(s)$.",
    "对截断积分使用分部积分，取 $u=x^s$、$dv=e^{-x}dx$；关键是证明 $x^se^{-x}$ 在 $0^+$ 与 $+\\infty$ 都趋于零。",
    "Apply integration by parts to a truncated integral with $u=x^s$ and $dv=e^{-x}dx$; the key is proving $x^se^{-x}$ tends to zero at both endpoints.",
    [
        "对 $0<\\varepsilon<R$，有 $\\int_\\varepsilon^Rx^se^{-x}dx=\\left.-x^se^{-x}\\right|_\\varepsilon^R+s\\int_\\varepsilon^Rx^{s-1}e^{-x}dx$。",
        "因 $s>0$，当 $\\varepsilon\\to0^+$ 时 $\\varepsilon^se^{-\\varepsilon}\\to0$。",
        "当 $R\\to+\\infty$ 时，指数衰减压倒固定幂次，故 $R^se^{-R}\\to0$。",
        "由 Q093，$\\int_0^{+\\infty}x^{s-1}e^{-x}dx$ 在 $s>0$ 时收敛。",
        "令 $\\varepsilon\\to0^+$、$R\\to+\\infty$，边界项消失，得到 $\\Gamma(s+1)=s\\Gamma(s)$。",
    ],
    [
        "For $0<\\varepsilon<R$, $\\int_\\varepsilon^Rx^se^{-x}dx=\\left.-x^se^{-x}\\right|_\\varepsilon^R+s\\int_\\varepsilon^Rx^{s-1}e^{-x}dx$.",
        "Because $s>0$, $\\varepsilon^se^{-\\varepsilon}\\to0$ as $\\varepsilon\\to0^+$.",
        "As $R\\to+\\infty$, exponential decay dominates every fixed power, so $R^se^{-R}\\to0$.",
        "By Q093, $\\int_0^{+\\infty}x^{s-1}e^{-x}dx$ converges for $s>0$.",
        "Letting $\\varepsilon\\to0^+$ and $R\\to+\\infty$ eliminates the boundary term and gives $\\Gamma(s+1)=s\\Gamma(s)$.",
    ],
    "取 $s=1$ 得 $\\Gamma(2)=\\Gamma(1)=1$；直接计算 $\\int_0^{+\\infty}xe^{-x}dx=1$，吻合。",
    "For $s=1$, the recurrence gives $\\Gamma(2)=\\Gamma(1)=1$; direct evaluation of $\\int_0^{+\\infty}xe^{-x}dx$ also gives $1$.",
)

add(
    "Q095", 5, "calculation", "gamma_function_enrichment",
    "Gamma 函数与阶乘", "Gamma Function and Factorials",
    "设 $n$ 为非负整数。由定义与递推公式求 $\\Gamma(n+1)$。",
    "Let $n$ be a nonnegative integer. Use the definition and recurrence to find $\\Gamma(n+1)$.",
    "$\\Gamma(n+1)=n!$", "$\\Gamma(n+1)=n!$",
    "先算基值 $\\Gamma(1)$，再把递推公式依次用于 $s=1,2,\\ldots,n$；空乘积对应 $n=0$。",
    "First compute $\\Gamma(1)$, then apply the recurrence successively for $s=1,2,\\ldots,n$; the empty product covers $n=0$.",
    [
        "$\\Gamma(1)=\\int_0^{+\\infty}e^{-x}dx=1$。",
        "递推公式给出 $\\Gamma(2)=1\\Gamma(1)$、$\\Gamma(3)=2\\Gamma(2)$，依此类推。",
        "连续展开得到 $\\Gamma(n+1)=n(n-1)\\cdots2\\cdot1\\,\\Gamma(1)$。",
        "因 $\\Gamma(1)=1$，故 $\\Gamma(n+1)=n!$。",
        "当 $n=0$ 时结论为 $\\Gamma(1)=0!=1$，同样成立。",
    ],
    [
        "$\\Gamma(1)=\\int_0^{+\\infty}e^{-x}dx=1$.",
        "The recurrence gives $\\Gamma(2)=1\\Gamma(1)$, $\\Gamma(3)=2\\Gamma(2)$, and so on.",
        "Repeated expansion yields $\\Gamma(n+1)=n(n-1)\\cdots2\\cdot1\\,\\Gamma(1)$.",
        "Since $\\Gamma(1)=1$, $\\Gamma(n+1)=n!$.",
        "For $n=0$, the statement is $\\Gamma(1)=0!=1$, so it also holds.",
    ],
    "取 $n=3$，得到 $\\Gamma(4)=3!=6$；两次分部积分可直接验证 $\\int_0^{+\\infty}x^3e^{-x}dx=6$。",
    "For $n=3$, $\\Gamma(4)=3!=6$; repeated integration by parts directly verifies $\\int_0^{+\\infty}x^3e^{-x}dx=6$.",
)

add(
    "Q096", 5, "comprehensive", "gamma_function_enrichment",
    "尺度换元与 Gamma 值", "Scaling Substitution and a Gamma Value",
    "计算 $\\displaystyle \\int_0^{+\\infty}x^3e^{-2x}\\,dx$。",
    "Evaluate $\\displaystyle \\int_0^{+\\infty}x^3e^{-2x}\\,dx$.",
    "$\\frac38$", "$\\frac38$",
    "先用 $u=2x$ 提取全部尺度因子，再识别 $\\Gamma(4)=3!$；$x^3$ 与 $dx$ 合计产生 $2^{-4}$。",
    "First use $u=2x$ to extract all scale factors, then recognize $\\Gamma(4)=3!$; $x^3$ and $dx$ together contribute $2^{-4}$.",
    [
        "令 $u=2x$，则 $x=\\frac u2$、$dx=\\frac12du$。",
        "端点 $0,+\\infty$ 保持为 $0,+\\infty$。",
        "积分化为 $\\frac1{2^4}\\int_0^{+\\infty}u^3e^{-u}du$。",
        "中间积分是 $\\Gamma(4)=3!=6$。",
        "因此结果为 $\\frac{6}{16}=\\frac38$。",
    ],
    [
        "Set $u=2x$, so $x=\\frac u2$ and $dx=\\frac12du$.",
        "The endpoints remain $0,+\\infty$.",
        "The integral becomes $\\frac1{2^4}\\int_0^{+\\infty}u^3e^{-u}du$.",
        "The remaining integral is $\\Gamma(4)=3!=6$.",
        "Therefore the value is $\\frac6{16}=\\frac38$.",
    ],
    "也可连续分部积分得到 $I_3=\\frac32I_2=\\frac32I_1=\\frac34I_0$，而 $I_0=\\frac12$，故 $I_3=\\frac38$。",
    "Repeated integration by parts gives $I_3=\\frac32I_2=\\frac32I_1=\\frac34I_0$ with $I_0=\\frac12$, again yielding $I_3=\\frac38$.",
)

add(
    "Q097", 5, "calculation", "gamma_function_enrichment",
    "半整数 Gamma 值", "A Half-integer Gamma Value",
    "已知 $\\Gamma\\!\\left(\\frac12\\right)=\\sqrt\\pi$。计算 $\\displaystyle \\Gamma\\!\\left(\\frac52\\right)$。",
    "Given $\\Gamma\\!\\left(\\frac12\\right)=\\sqrt\\pi$, evaluate $\\displaystyle \\Gamma\\!\\left(\\frac52\\right)$.",
    "$\\frac{3\\sqrt\\pi}{4}$", "$\\frac{3\\sqrt\\pi}{4}$",
    "递推两次，把参数从 $\\frac52$ 依次降到 $\\frac32$ 与 $\\frac12$；每次乘以前一个参数。",
    "Apply the recurrence twice, reducing the argument from $\\frac52$ to $\\frac32$ and then $\\frac12$, multiplying by the preceding argument each time.",
    [
        "由递推式，$\\Gamma\\!\\left(\\frac52\\right)=\\frac32\\Gamma\\!\\left(\\frac32\\right)$。",
        "再次递推得 $\\Gamma\\!\\left(\\frac32\\right)=\\frac12\\Gamma\\!\\left(\\frac12\\right)$。",
        "代入已知值 $\\Gamma\\!\\left(\\frac12\\right)=\\sqrt\\pi$。",
        "所以 $\\Gamma\\!\\left(\\frac52\\right)=\\frac32\\cdot\\frac12\\sqrt\\pi=\\frac{3\\sqrt\\pi}{4}$。",
    ],
    [
        "The recurrence gives $\\Gamma\\!\\left(\\frac52\\right)=\\frac32\\Gamma\\!\\left(\\frac32\\right)$.",
        "Applying it again, $\\Gamma\\!\\left(\\frac32\\right)=\\frac12\\Gamma\\!\\left(\\frac12\\right)$.",
        "Insert the given value $\\Gamma\\!\\left(\\frac12\\right)=\\sqrt\\pi$.",
        "Thus $\\Gamma\\!\\left(\\frac52\\right)=\\frac32\\cdot\\frac12\\sqrt\\pi=\\frac{3\\sqrt\\pi}{4}$.",
    ],
    "由定义，$\\Gamma\\!\\left(\\frac52\\right)=\\int_0^{+\\infty}x^{\\frac32}e^{-x}dx>0$；闭式为正且约 $1.329$，符号合理。",
    "By definition, $\\Gamma\\!\\left(\\frac52\\right)=\\int_0^{+\\infty}x^{\\frac32}e^{-x}dx>0$; the closed form is positive and approximately $1.329$.",
)

add(
    "Q098", 5, "calculation", "gamma_function_enrichment",
    "指数尺度下的阶乘积分", "A Factorial Integral with Exponential Scaling",
    "设 $a>0$，$m$ 为非负整数。计算 $\\displaystyle I_m(a)=\\int_0^{+\\infty}x^m e^{-ax}\\,dx$。",
    "Let $a>0$ and let $m$ be a nonnegative integer. Evaluate $\\displaystyle I_m(a)=\\int_0^{+\\infty}x^m e^{-ax}\\,dx$.",
    "$I_m(a)=\\frac{m!}{a^{m+1}}$", "$I_m(a)=\\frac{m!}{a^{m+1}}$",
    "$a>0$ 保证指数衰减；尺度换元 $u=ax$ 后，幂因子与微分合计贡献 $a^{-(m+1)}$。",
    "$a>0$ ensures exponential decay; after $u=ax$, the power and differential together contribute $a^{-(m+1)}$.",
    [
        "令 $u=ax$，则 $x=\\frac ua$、$dx=\\frac1a du$。",
        "因 $a>0$，端点 $0,+\\infty$ 仍变为 $0,+\\infty$。",
        "因此 $I_m(a)=\\frac1{a^{m+1}}\\int_0^{+\\infty}u^me^{-u}du$。",
        "中间积分为 $\\Gamma(m+1)=m!$。",
        "故 $I_m(a)=\\frac{m!}{a^{m+1}}$。",
    ],
    [
        "Set $u=ax$, so $x=\\frac ua$ and $dx=\\frac1a du$.",
        "Because $a>0$, the endpoints $0,+\\infty$ remain $0,+\\infty$.",
        "Thus $I_m(a)=\\frac1{a^{m+1}}\\int_0^{+\\infty}u^me^{-u}du$.",
        "The remaining integral is $\\Gamma(m+1)=m!$.",
        "Therefore $I_m(a)=\\frac{m!}{a^{m+1}}$.",
    ],
    "取 $m=0$ 得 $\\int_0^{+\\infty}e^{-ax}dx=\\frac1a$，与 Q077 在 $a>0$ 的结果一致。",
    "For $m=0$, the formula gives $\\int_0^{+\\infty}e^{-ax}dx=\\frac1a$, agreeing with Q077 for $a>0$.",
)

add(
    "Q099", 5, "proof", "improper_integral_convergence_tests",
    "Beta 型积分的两端审敛", "Two-endpoint Convergence of a Beta-type Integral",
    "对实参数 $\\alpha,\\beta$，证明 $\\displaystyle \\int_0^{+\\infty}\\frac{x^{\\alpha-1}}{(1+x)^{\\alpha+\\beta}}\\,dx$ 当且仅当 $\\alpha>0$ 且 $\\beta>0$ 时收敛。",
    "For real $\\alpha,\\beta$, prove that $\\displaystyle \\int_0^{+\\infty}\\frac{x^{\\alpha-1}}{(1+x)^{\\alpha+\\beta}}\\,dx$ converges if and only if $\\alpha>0$ and $\\beta>0$.",
    "收敛当且仅当 $\\alpha>0$ 且 $\\beta>0$。", "It converges exactly when $\\alpha>0$ and $\\beta>0$.",
    "在 $1$ 处分开；零点附近与 $x^{\\alpha-1}$ 极限比较，无穷远与 $x^{-\\beta-1}$ 极限比较，两端条件必须同时满足。",
    "Split at $1$; use limit comparison with $x^{\\alpha-1}$ near zero and with $x^{-\\beta-1}$ at infinity, and require both endpoint conditions.",
    [
        "记被积函数为 $h(x)=\\frac{x^{\\alpha-1}}{(1+x)^{\\alpha+\\beta}}>0$。",
        "当 $x\\to0^+$ 时，$\\frac{h(x)}{x^{\\alpha-1}}=(1+x)^{-(\\alpha+\\beta)}\\to1$。",
        "故零点附近与 $\\int_0^1x^{\\alpha-1}dx$ 同敛散，条件为 $\\alpha>0$。",
        "当 $x\\to+\\infty$ 时，$\\frac{h(x)}{x^{-\\beta-1}}=\\left(\\frac{x}{1+x}\\right)^{\\alpha+\\beta}\\to1$。",
        "故无穷远与 $\\int_1^{+\\infty}x^{-\\beta-1}dx$ 同敛散，条件为 $\\beta>0$。",
        "原积分要求两段都收敛，因此充要条件为 $\\alpha>0$ 且 $\\beta>0$。",
    ],
    [
        "Let $h(x)=\\frac{x^{\\alpha-1}}{(1+x)^{\\alpha+\\beta}}>0$.",
        "As $x\\to0^+$, $\\frac{h(x)}{x^{\\alpha-1}}=(1+x)^{-(\\alpha+\\beta)}\\to1$.",
        "Thus local convergence matches $\\int_0^1x^{\\alpha-1}dx$, requiring $\\alpha>0$.",
        "As $x\\to+\\infty$, $\\frac{h(x)}{x^{-\\beta-1}}=\\left(\\frac{x}{1+x}\\right)^{\\alpha+\\beta}\\to1$.",
        "Thus tail convergence matches $\\int_1^{+\\infty}x^{-\\beta-1}dx$, requiring $\\beta>0$.",
        "Both pieces must converge, so the necessary and sufficient conditions are $\\alpha>0$ and $\\beta>0$.",
    ],
    "取 $\\alpha=\\beta=1$，积分化为 $\\int_0^{+\\infty}\\frac{dx}{(1+x)^2}=1$，确实收敛；任一参数取 $0$ 都出现临界 $x^{-1}$ 行为。",
    "For $\\alpha=\\beta=1$, the integral becomes $\\int_0^{+\\infty}\\frac{dx}{(1+x)^2}=1$; setting either parameter to $0$ creates the critical $x^{-1}$ behavior.",
)

add(
    "Q100", 5, "comprehensive", "gamma_function_enrichment",
    "双参数 Gamma 尺度积分", "A Two-parameter Gamma Scaling Integral",
    "对实参数 $a,b$，完整讨论并计算 $\\displaystyle I(a,b)=\\int_0^{+\\infty}x^{a-1}e^{-bx}\\,dx$。",
    "For real parameters $a,b$, completely classify and evaluate $\\displaystyle I(a,b)=\\int_0^{+\\infty}x^{a-1}e^{-bx}\\,dx$.",
    "当且仅当 $a>0$ 且 $b>0$ 时收敛；此时 $I(a,b)=\\frac{\\Gamma(a)}{b^a}$。", "It converges exactly when $a>0$ and $b>0$; then $I(a,b)=\\frac{\\Gamma(a)}{b^a}$.",
    "参数 $a$ 控制零点幂奇性，参数 $b$ 控制无穷远的指数行为；只有两个独立条件都满足时，尺度换元才合法并产生 Gamma 值。",
    "Parameter $a$ controls the power behavior near zero, while $b$ controls the exponential tail; only when both independent conditions hold does scaling produce a Gamma value.",
    [
        "先看 $0$ 附近：$e^{-bx}\\to1$，所以局部与 $x^{a-1}$ 同阶；必须且只需 $a>0$。",
        "若 $b>0$，指数在无穷远衰减并压倒任意固定幂次，因此尾部收敛。",
        "若 $b=0$，无穷远变成幂积分；其尾部要求 $a<0$，与零点要求 $a>0$ 矛盾，所以不存在收敛参数。",
        "若 $b<0$，写 $b=-c$ 且 $c>0$，则 $e^{-bx}=e^{cx}$ 指数增长，尾部对任意实数 $a$ 都发散。",
        "因此总体收敛充要条件是 $a>0$ 且 $b>0$。",
        "在该范围令 $u=bx$，则 $dx=\\frac1bdu$、$x^{a-1}=b^{1-a}u^{a-1}$。",
        "于是 $I(a,b)=b^{-a}\\int_0^{+\\infty}u^{a-1}e^{-u}du=\\frac{\\Gamma(a)}{b^a}$。",
    ],
    [
        "Near $0$, $e^{-bx}\\to1$, so the integrand is comparable to $x^{a-1}$; this requires exactly $a>0$.",
        "If $b>0$, the exponential decays at infinity and dominates every fixed power, so the tail converges.",
        "If $b=0$, the tail is a power integral requiring $a<0$, which contradicts the near-zero condition $a>0$; no value of $a$ works.",
        "If $b<0$, write $b=-c$ with $c>0$; then $e^{-bx}=e^{cx}$ grows exponentially, so the tail diverges for every real $a$.",
        "Thus the necessary and sufficient conditions are $a>0$ and $b>0$.",
        "In that range, set $u=bx$, so $dx=\\frac1bdu$ and $x^{a-1}=b^{1-a}u^{a-1}$.",
        "Therefore $I(a,b)=b^{-a}\\int_0^{+\\infty}u^{a-1}e^{-u}du=\\frac{\\Gamma(a)}{b^a}$.",
    ],
    "取 $a=1$ 得 $I(1,b)=\\frac1b$，与指数积分一致；取 $a=m+1$ 得 $\\frac{m!}{b^{m+1}}$，与 Q098 一致。",
    "For $a=1$, $I(1,b)=\\frac1b$, matching the exponential integral; for $a=m+1$, it gives $\\frac{m!}{b^{m+1}}$, agreeing with Q098.",
)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(QUESTIONS, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(QUESTIONS)} questions to {OUTPUT}")


if __name__ == "__main__":
    main()
