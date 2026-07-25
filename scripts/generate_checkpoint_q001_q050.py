from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.source_lineage import CATEGORY_RELATIONS, METHOD_FAMILY_REFERENCES


OUTPUT = ROOT / "content" / "parts" / "part_a_q001_q050.json"

FAMILY = {
    "riemann_sums_and_definition": {
        "zh_knowledge": ["Riemann 和定义", "分割宽度与取样点", "和式极限与定积分"],
        "en_knowledge": ["definition by Riemann sums", "subinterval widths and sample points", "limits of sums and definite integrals"],
        "zh_pitfalls": ["遗漏宽度因子 $\\Delta x$", "没有同时检查取样点和积分区间"],
        "en_pitfalls": ["omitting the width factor $\\Delta x$", "failing to check both sample points and the integration interval"],
        "zh_takeaway": "识别 Riemann 和时必须同时匹配函数值、取样点、分割宽度和积分区间。",
        "en_takeaway": "A Riemann sum is identified only after matching the function value, sample points, subinterval width, and interval.",
        "zh_extension": "可改用左端点或中点取样；连续函数所得极限相同。",
        "en_extension": "Left endpoints or midpoints may be used instead; continuity gives the same limiting integral.",
    },
    "definite_integral_properties": {
        "zh_knowledge": ["定积分的线性性质", "区间可加性与换限", "单调性、估值与对称性"],
        "en_knowledge": ["linearity of definite integrals", "interval additivity and reversal", "order bounds and symmetry"],
        "zh_pitfalls": ["把定积分直接等同于几何面积", "换上下限时漏掉负号"],
        "en_pitfalls": ["identifying a definite integral with unsigned geometric area", "forgetting the sign change when limits are reversed"],
        "zh_takeaway": "先判断符号、区间方向和对称性，再决定是否需要逐段计算。",
        "en_takeaway": "Check sign, interval orientation, and symmetry before carrying out piecewise computation.",
        "zh_extension": "将被积函数拆成奇部与偶部，常可进一步简化对称区间上的积分。",
        "en_extension": "Splitting an integrand into odd and even parts can further simplify integrals over symmetric intervals.",
    },
    "integral_mean_value_and_average": {
        "zh_knowledge": ["积分平均值", "积分中值定理", "连续函数的取值范围"],
        "en_knowledge": ["average value of a function", "mean value theorem for integrals", "range of a continuous function"],
        "zh_pitfalls": ["忘记除以区间长度", "把平均值点误认为唯一"],
        "en_pitfalls": ["forgetting to divide by the interval length", "assuming the mean-value point is unique"],
        "zh_takeaway": "平均值等于定积分除以区间长度；中值定理只保证至少存在一个对应点。",
        "en_takeaway": "The average value is the integral divided by interval length; the mean value theorem guarantees at least one corresponding point.",
        "zh_extension": "若函数严格单调，则满足中值等式的点至多一个。",
        "en_extension": "If the function is strictly monotone, the point satisfying the mean-value identity is unique.",
    },
    "fundamental_theorem_and_new_functions": {
        "zh_knowledge": ["变上限积分函数", "微积分基本定理", "链式法则"],
        "en_knowledge": ["accumulation functions", "Fundamental Theorem of Calculus", "chain rule"],
        "zh_pitfalls": ["遗漏上限导数", "下限含变量时漏掉负号"],
        "en_pitfalls": ["omitting the derivative of a variable upper limit", "missing the minus sign from a variable lower limit"],
        "zh_takeaway": "先对每个变限端点应用基本定理，再乘端点导数并按上限减下限组合。",
        "en_takeaway": "Apply the theorem at each variable endpoint, multiply by the endpoint derivative, and combine upper minus lower.",
        "zh_extension": "若被积式还显含参数，应先改写或使用乘积法则，不能只看端点。",
        "en_extension": "If the integrand also contains the parameter explicitly, rewrite first or apply the product rule rather than looking only at the endpoints.",
    },
    "newton_leibniz_evaluation": {
        "zh_knowledge": ["Newton-Leibniz 公式", "原函数", "定积分的精确计算"],
        "en_knowledge": ["Newton-Leibniz formula", "antiderivatives", "exact evaluation of definite integrals"],
        "zh_pitfalls": ["只代入上限而忘记减去下限值", "把不定积分常数带入定积分结果"],
        "en_pitfalls": ["substituting only the upper limit", "carrying an arbitrary antiderivative constant into a definite integral"],
        "zh_takeaway": "任选一个原函数后计算上限值减下限值，任意常数会自动消去。",
        "en_takeaway": "Choose any antiderivative and subtract its lower-end value from its upper-end value; arbitrary constants cancel.",
        "zh_extension": "计算后可用符号、数量级或几何解释做独立核验。",
        "en_extension": "After evaluation, use sign, scale, or a geometric interpretation as an independent check.",
    },
    "definite_integral_substitution": {
        "zh_knowledge": ["定积分换元法", "微分匹配", "上下限同步变换"],
        "en_knowledge": ["substitution in definite integrals", "matching differentials", "transforming both limits"],
        "zh_pitfalls": ["换元后仍保留原变量上下限", "漏掉微分中的常数因子"],
        "en_pitfalls": ["keeping the old limits after changing variables", "losing a constant factor from the differential"],
        "zh_takeaway": "变量、微分和上下限必须成套变换；完成后积分中只能出现新变量。",
        "en_takeaway": "The variable, differential, and both limits must be transformed together, leaving only the new variable.",
        "zh_extension": "也可暂不换限，求得原函数后回代原变量；两种路线应给出同一结果。",
        "en_extension": "One may instead keep the old limits, return to the original variable after antidifferentiation, and obtain the same result.",
    },
    "definite_integral_by_parts": {
        "zh_knowledge": ["定积分分部积分", "边界项", "因子选择"],
        "en_knowledge": ["integration by parts for definite integrals", "boundary terms", "choice of factors"],
        "zh_pitfalls": ["漏算边界项", "边界代入后忘记减去剩余积分"],
        "en_pitfalls": ["omitting the boundary term", "forgetting to subtract the remaining integral after evaluating the boundary"],
        "zh_takeaway": "定积分分部积分必须把乘积边界项和剩余积分一起保留。",
        "en_takeaway": "Definite integration by parts requires both the evaluated product term and the remaining integral.",
        "zh_extension": "交换因子选择并比较复杂度，可判断原选择是否高效。",
        "en_extension": "Compare the complexity after swapping the factor choices to assess whether the original selection was efficient.",
    },
}

ORIGINAL_IDS = {
    "Q018", "Q019", "Q020", "Q039", "Q040", "Q041", "Q042",
    "Q043", "Q044", "Q046", "Q048", "Q049", "Q050",
}

TYPE_META = {
    "single_choice": (5, "S"),
    "multiple_choice": (7, "M"),
    "true_false": (6, "M"),
    "fill_blank": (6, "M"),
    "calculation": (12, "L"),
    "proof": (18, "XL"),
    "comprehensive": (20, "XL"),
    "error_diagnosis": (15, "XL"),
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
) -> None:
    number = int(qid[1:])
    if number <= 22:
        tier, difficulty = "foundation", "basic"
    elif number <= 45:
        tier, difficulty = "methods", "standard"
    else:
        tier, difficulty = "methods", "advanced"

    if number <= 10:
        category = "open_text_adaptation"
    elif qid in ORIGINAL_IDS:
        category = "original_synthesis"
    else:
        category = "classic_method_variant"
    refs = sorted(METHOD_FAMILY_REFERENCES[family])
    references = refs if category == "open_text_adaptation" else [refs[0]]

    data = FAMILY[family]
    minutes, space = TYPE_META[qtype]
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
                "zh": [title_zh, data["zh_knowledge"][0]],
                "en": [title_en, data["en_knowledge"][0]],
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
    "Q001", 1, "single_choice", "riemann_sums_and_definition",
    "辨认等分区间的 Riemann 和", "Recognizing a Riemann Sum on Equal Subintervals",
    "将 $[0,2]$ 等分为 $n$ 段并取右端点。下列哪一项是 $\\int_{0}^{2}(1+x^{2})\\,dx$ 的 Riemann 和？",
    "Partition $[0,2]$ into $n$ equal pieces and use right endpoints. Which expression is a Riemann sum for $\\int_{0}^{2}(1+x^{2})\\,dx$?",
    "B", "B",
    "区间长度给出 $\\Delta x=\\frac{2}{n}$，第 $k$ 个右端点为 $x_k=\\frac{2k}{n}$；必须把函数值和宽度相乘。",
    "The interval gives $\\Delta x=\\frac{2}{n}$ and right endpoint $x_k=\\frac{2k}{n}$; the function value must be multiplied by the width.",
    [
        "由等分可得 $\\Delta x=\\frac{2-0}{n}=\\frac{2}{n}$。",
        "第 $k$ 个右端点是 $x_k=0+k\\Delta x=\\frac{2k}{n}$。",
        "函数值为 $1+x_k^{2}=1+\\left(\\frac{2k}{n}\\right)^{2}$。",
        "因此和式是 $\\sum_{k=1}^{n}\\left[1+\\left(\\frac{2k}{n}\\right)^{2}\\right]\\frac{2}{n}$，即 B。",
    ],
    [
        "Equal subdivision gives $\\Delta x=\\frac{2-0}{n}=\\frac{2}{n}$.",
        "The $k$th right endpoint is $x_k=0+k\\Delta x=\\frac{2k}{n}$.",
        "The sampled value is $1+x_k^{2}=1+\\left(\\frac{2k}{n}\\right)^{2}$.",
        "Hence the sum is $\\sum_{k=1}^{n}\\left[1+\\left(\\frac{2k}{n}\\right)^{2}\\right]\\frac{2}{n}$, which is B.",
    ],
    "取常数函数 $1$ 检查宽度：对应部分应为 $n\\cdot\\frac{2}{n}=2$；只有 B 保留了正确宽度。",
    "Checking the constant part $1$ gives $n\\cdot\\frac{2}{n}=2$; only B retains the correct width.",
    choices_zh=[
        "A. $\\sum_{k=1}^{n}\\left[1+\\left(\\frac{k}{n}\\right)^{2}\\right]\\frac{1}{n}$",
        "B. $\\sum_{k=1}^{n}\\left[1+\\left(\\frac{2k}{n}\\right)^{2}\\right]\\frac{2}{n}$",
        "C. $\\sum_{k=1}^{n}\\left[1+\\left(\\frac{2k}{n}\\right)^{2}\\right]$",
        "D. $\\sum_{k=0}^{n}\\left[1+\\left(\\frac{2k}{n}\\right)^{2}\\right]\\frac{2}{n}$",
    ],
    choices_en=[
        "A. $\\sum_{k=1}^{n}\\left[1+\\left(\\frac{k}{n}\\right)^{2}\\right]\\frac{1}{n}$",
        "B. $\\sum_{k=1}^{n}\\left[1+\\left(\\frac{2k}{n}\\right)^{2}\\right]\\frac{2}{n}$",
        "C. $\\sum_{k=1}^{n}\\left[1+\\left(\\frac{2k}{n}\\right)^{2}\\right]$",
        "D. $\\sum_{k=0}^{n}\\left[1+\\left(\\frac{2k}{n}\\right)^{2}\\right]\\frac{2}{n}$",
    ],
)

add(
    "Q002", 1, "single_choice", "definite_integral_properties",
    "区分定积分与几何面积", "Distinguishing an Integral from Geometric Area",
    "若连续函数在 $[a,b]$ 上满足 $f(x)\\le 0$，则下列说法正确的是哪一项？",
    "If a continuous function satisfies $f(x)\\le 0$ on $[a,b]$, which statement is correct?",
    "C", "C",
    "定积分记录带符号面积；曲线位于横轴下方时积分非正，而几何面积要取相反数。",
    "A definite integral records signed area. A graph below the horizontal axis gives a nonpositive integral, while geometric area is its negative.",
    [
        "由 $f(x)\\le 0$ 和积分的保序性，$\\int_a^b f(x)\\,dx\\le 0$。",
        "横轴与曲线之间的几何面积必须非负。",
        "在本题符号条件下，几何面积为 $-\\int_a^b f(x)\\,dx$。",
        "因此只有 C 同时说明了积分符号和面积关系。",
    ],
    [
        "From $f(x)\\le 0$ and order preservation, $\\int_a^b f(x)\\,dx\\le 0$.",
        "Geometric area between the graph and the horizontal axis is nonnegative.",
        "Under the stated sign condition, that area equals $-\\int_a^b f(x)\\,dx$.",
        "Thus only C gives both the correct sign and the correct area relation.",
    ],
    "取 $f(x)=-1$，则积分为 $-(b-a)$，而几何面积为 $b-a$，验证 C。",
    "For $f(x)=-1$, the integral is $-(b-a)$ while the geometric area is $b-a$, confirming C.",
    choices_zh=[
        "A. $\\int_a^b f(x)\\,dx\\ge 0$",
        "B. 几何面积等于 $\\int_a^b f(x)\\,dx$",
        "C. 几何面积等于 $-\\int_a^b f(x)\\,dx$",
        "D. 定积分一定等于 $0$",
    ],
    choices_en=[
        "A. $\\int_a^b f(x)\\,dx\\ge 0$",
        "B. The geometric area equals $\\int_a^b f(x)\\,dx$.",
        "C. The geometric area equals $-\\int_a^b f(x)\\,dx$.",
        "D. The definite integral must equal $0$.",
    ],
)

add(
    "Q003", 1, "single_choice", "definite_integral_properties",
    "交换积分上下限", "Reversing the Limits of Integration",
    "已知 $\\int_{1}^{4} f(x)\\,dx=7$，则 $\\int_{4}^{1} f(x)\\,dx$ 等于多少？",
    "Given $\\int_{1}^{4} f(x)\\,dx=7$, what is $\\int_{4}^{1} f(x)\\,dx$?",
    "A", "A",
    "交换上下限只改变积分方向，因此积分值乘以 $-1$；被积函数与几何区间本身都不改变。",
    "Reversing the limits changes only the orientation, not the integrand or geometric interval, and therefore multiplies the integral by $-1$.",
    [
        "定积分换限公式为 $\\int_b^a f(x)\\,dx=-\\int_a^b f(x)\\,dx$。",
        "令 $a=1$、$b=4$。",
        "代入已知值，$\\int_4^1 f(x)\\,dx=-7$。",
        "因此在四个选项中应选择 A。",
    ],
    [
        "The reversal rule is $\\int_b^a f(x)\\,dx=-\\int_a^b f(x)\\,dx$.",
        "Set $a=1$ and $b=4$.",
        "Using the given value gives $\\int_4^1 f(x)\\,dx=-7$.",
        "Therefore choice A is the unique correct option.",
    ],
    "两个相反方向的积分相加为 $7+(-7)=0$，与 $\\int_1^1 f(x)\\,dx=0$ 一致。",
    "The oppositely oriented integrals add to $7+(-7)=0$, consistent with $\\int_1^1 f(x)\\,dx=0$.",
    choices_zh=["A. $-7$", "B. $0$", "C. $7$", "D. $14$"],
    choices_en=["A. $-7$", "B. $0$", "C. $7$", "D. $14$"],
)

add(
    "Q004", 1, "single_choice", "definite_integral_properties",
    "用上下界估计定积分", "Bounding a Definite Integral",
    "若 $f$ 在 $[1,4]$ 上可积，且 $2\\le f(x)\\le 5$ 对所有 $x\\in[1,4]$ 成立，则下列哪一项必然成立？",
    "If $f$ is integrable on $[1,4]$ and $2\\le f(x)\\le 5$ for every $x\\in[1,4]$, which statement must hold?",
    "D", "D",
    "把点态上下界在长度为 $3$ 的区间上积分，即可得到积分的双边界。",
    "Integrating the pointwise bounds over an interval of length $3$ gives two-sided bounds for the integral.",
    [
        "由保序性，$\\int_1^4 2\\,dx\\le\\int_1^4 f(x)\\,dx\\le\\int_1^4 5\\,dx$。",
        "左端为 $2(4-1)=6$。",
        "右端为 $5(4-1)=15$。",
        "所以 $6\\le\\int_1^4 f(x)\\,dx\\le 15$，即 D。",
    ],
    [
        "Order preservation gives $\\int_1^4 2\\,dx\\le\\int_1^4 f(x)\\,dx\\le\\int_1^4 5\\,dx$.",
        "The lower bound is $2(4-1)=6$.",
        "The upper bound is $5(4-1)=15$.",
        "Therefore $6\\le\\int_1^4 f(x)\\,dx\\le 15$, which is D.",
    ],
    "常数函数 $f(x)=2$ 和 $f(x)=5$ 分别达到两个端点，说明界限不能普遍收紧。",
    "The constant functions $f(x)=2$ and $f(x)=5$ attain the two endpoints, so the bounds cannot be uniformly tightened.",
    choices_zh=[
        "A. $2\\le\\int_1^4 f(x)\\,dx\\le 5$",
        "B. $3\\le\\int_1^4 f(x)\\,dx\\le 12$",
        "C. $5\\le\\int_1^4 f(x)\\,dx\\le 20$",
        "D. $6\\le\\int_1^4 f(x)\\,dx\\le 15$",
    ],
    choices_en=[
        "A. $2\\le\\int_1^4 f(x)\\,dx\\le 5$",
        "B. $3\\le\\int_1^4 f(x)\\,dx\\le 12$",
        "C. $5\\le\\int_1^4 f(x)\\,dx\\le 20$",
        "D. $6\\le\\int_1^4 f(x)\\,dx\\le 15$",
    ],
)

add(
    "Q005", 1, "multiple_choice", "definite_integral_properties",
    "筛选定积分的恒等性质", "Selecting Valid Integral Identities",
    "设有关定积分均存在。下列恒等式中哪些对任意被积函数都成立？",
    "Assume all displayed integrals exist. Which identities hold for every integrand?",
    "A、C、D", "A, C, D",
    "逐项检查线性、换限、区间可加性；不能把乘积的积分拆成积分的乘积。",
    "Check linearity, reversal, and interval additivity one by one. The integral of a product cannot generally be split into a product of integrals.",
    [
        "A 是常数因子可提出的线性性质，成立。",
        "B 一般不成立；例如在 $[0,1]$ 上取 $f(x)=g(x)=x$，两边分别为 $\\frac13$ 与 $\\frac14$。",
        "C 是交换上下限公式，成立。",
        "D 是区间可加性，任意 $c$ 均成立。",
    ],
    [
        "A is scalar linearity and is valid.",
        "B is generally false; on $[0,1]$, taking $f(x)=g(x)=x$ gives $\\frac13$ on the left and $\\frac14$ on the right.",
        "C is the reversal formula and is valid.",
        "D is interval additivity and is valid for every $c$.",
    ],
    "反例中的 $\\int_0^1 x^2\\,dx=\\frac13$，而 $\\left(\\int_0^1x\\,dx\\right)^2=\\frac14$，明确排除 B。",
    "In the counterexample, $\\int_0^1 x^2\\,dx=\\frac13$ whereas $\\left(\\int_0^1x\\,dx\\right)^2=\\frac14$, excluding B.",
    choices_zh=[
        "A. $\\int_a^b \\lambda f(x)\\,dx=\\lambda\\int_a^b f(x)\\,dx$",
        "B. $\\int_a^b f(x)g(x)\\,dx=\\left(\\int_a^b f(x)\\,dx\\right)\\left(\\int_a^b g(x)\\,dx\\right)$",
        "C. $\\int_a^b f(x)\\,dx=-\\int_b^a f(x)\\,dx$",
        "D. $\\int_a^b f(x)\\,dx=\\int_a^c f(x)\\,dx+\\int_c^b f(x)\\,dx$",
    ],
    choices_en=[
        "A. $\\int_a^b \\lambda f(x)\\,dx=\\lambda\\int_a^b f(x)\\,dx$",
        "B. $\\int_a^b f(x)g(x)\\,dx=\\left(\\int_a^b f(x)\\,dx\\right)\\left(\\int_a^b g(x)\\,dx\\right)$",
        "C. $\\int_a^b f(x)\\,dx=-\\int_b^a f(x)\\,dx$",
        "D. $\\int_a^b f(x)\\,dx=\\int_a^c f(x)\\,dx+\\int_c^b f(x)\\,dx$",
    ],
)

add(
    "Q006", 1, "multiple_choice", "definite_integral_properties",
    "识别可积性与保序结论", "Recognizing Integrability and Order Consequences",
    "在闭区间 $[a,b]$ 上，下列哪些说法正确？",
    "On a closed interval $[a,b]$, which statements are correct?",
    "A、B、D", "A, B, D",
    "本题区分常用充分条件、积分保序性与一个错误的逆推。",
    "This problem separates standard sufficient conditions, order preservation, and an invalid converse.",
    [
        "连续函数在闭区间上 Riemann 可积，所以 A 正确。",
        "闭区间上的单调函数有界且仅有可控间断，因此 Riemann 可积，B 正确。",
        "积分相等只比较总体累积量，不能推出函数逐点相等，所以 C 错误。",
        "若 $f(x)\\ge0$，每个 Riemann 和均非负，取极限得积分非负，所以 D 正确。",
    ],
    [
        "A continuous function on a closed interval is Riemann integrable, so A is correct.",
        "A monotone function on a closed interval is bounded with controlled discontinuities and is Riemann integrable, so B is correct.",
        "Equal integrals compare only total accumulation and do not imply pointwise equality, so C is false.",
        "If $f(x)\\ge0$, every Riemann sum is nonnegative, and its limit is nonnegative; hence D is correct.",
    ],
    "对 C 取 $f(x)=x$、$g(x)=1-x$ 于 $[0,1]$，二者积分均为 $\\frac12$，但函数并不恒等。",
    "For C, take $f(x)=x$ and $g(x)=1-x$ on $[0,1]$. Both integrals equal $\\frac12$, but the functions are not identical.",
    choices_zh=[
        "A. 连续函数一定 Riemann 可积",
        "B. 单调函数一定 Riemann 可积",
        "C. 若两个连续函数积分相等，则它们处处相等",
        "D. 若 $f(x)\\ge0$，则 $\\int_a^b f(x)\\,dx\\ge0$",
    ],
    choices_en=[
        "A. Every continuous function is Riemann integrable.",
        "B. Every monotone function is Riemann integrable.",
        "C. Equal integrals of two continuous functions imply pointwise equality.",
        "D. If $f(x)\\ge0$, then $\\int_a^b f(x)\\,dx\\ge0$.",
    ],
)

add(
    "Q007", 1, "true_false", "definite_integral_properties",
    "绝对值积分不等式", "The Absolute-Value Integral Inequality",
    "判断并说明理由：若 $f$ 在 $[a,b]$ 上可积，则 $\\left|\\int_a^b f(x)\\,dx\\right|\\le\\int_a^b |f(x)|\\,dx$。",
    "Determine whether the statement is true and justify: if $f$ is integrable on $[a,b]$, then $\\left|\\int_a^b f(x)\\,dx\\right|\\le\\int_a^b |f(x)|\\,dx$.",
    "正确。", "True.",
    "从逐点不等式 $-|f(x)|\\le f(x)\\le |f(x)|$ 出发，分别积分后夹住原积分。",
    "Start with the pointwise inequality $-|f(x)|\\le f(x)\\le |f(x)|$ and integrate to trap the original integral.",
    [
        "对每个 $x\\in[a,b]$，有 $-|f(x)|\\le f(x)\\le |f(x)|$。",
        "利用积分保序性，$-\\int_a^b|f(x)|\\,dx\\le\\int_a^b f(x)\\,dx\\le\\int_a^b|f(x)|\\,dx$。",
        "中间量被同一个非负数的正负值夹住，等价于 $\\left|\\int_a^b f(x)\\,dx\\right|\\le\\int_a^b|f(x)|\\,dx$。",
        "所以命题正确；等号是否成立取决于积分过程中是否发生正负抵消。",
    ],
    [
        "For every $x\\in[a,b]$, $-|f(x)|\\le f(x)\\le |f(x)|$.",
        "Order preservation gives $-\\int_a^b|f(x)|\\,dx\\le\\int_a^b f(x)\\,dx\\le\\int_a^b|f(x)|\\,dx$.",
        "Being trapped between the negative and positive of the same nonnegative number is equivalent to $\\left|\\int_a^b f(x)\\,dx\\right|\\le\\int_a^b|f(x)|\\,dx$.",
        "Hence the statement is true; equality depends on whether positive and negative contributions cancel.",
    ],
    "若 $f$ 不变号则取等号；若正负部分抵消，则左边会严格小于右边，符合不等式。",
    "Equality holds when $f$ has constant sign; cancellation between positive and negative parts makes the left side smaller, as expected.",
)

add(
    "Q008", 1, "true_false", "definite_integral_properties",
    "由积分相等反推函数相等", "Inferring Equality of Functions from Equal Integrals",
    "判断并说明理由：若连续函数 $f,g$ 满足 $\\int_0^1 f(x)\\,dx=\\int_0^1 g(x)\\,dx$，则 $f(x)=g(x)$ 在 $[0,1]$ 上恒成立。",
    "Determine whether the statement is true and justify: if continuous functions $f,g$ satisfy $\\int_0^1 f(x)\\,dx=\\int_0^1 g(x)\\,dx$, then $f(x)=g(x)$ throughout $[0,1]$.",
    "错误。", "False.",
    "一个积分只给出一个总体约束，不足以确定整个函数；构造具有相同平均值的不同函数即可。",
    "A single integral gives only one aggregate constraint and cannot determine a whole function; two distinct functions with the same average provide a counterexample.",
    [
        "取 $f(x)=x$ 与 $g(x)=1-x$，二者都在 $[0,1]$ 上连续。",
        "计算得 $\\int_0^1x\\,dx=\\frac12$。",
        "同样 $\\int_0^1(1-x)\\,dx=\\frac12$。",
        "但例如在 $x=0$ 处，$f(0)=0\\ne1=g(0)$，故原命题错误。",
    ],
    [
        "Take $f(x)=x$ and $g(x)=1-x$; both are continuous on $[0,1]$.",
        "We have $\\int_0^1x\\,dx=\\frac12$.",
        "Also $\\int_0^1(1-x)\\,dx=\\frac12$.",
        "Yet at $x=0$, $f(0)=0\\ne1=g(0)$, so the statement is false.",
    ],
    "反例同时满足连续性和积分相等，却不满足函数恒等，足以否定全称命题。",
    "The counterexample satisfies continuity and equality of integrals but not equality of functions, which disproves the universal statement.",
)

add(
    "Q009", 1, "true_false", "definite_integral_properties",
    "奇函数的对称积分", "Symmetric Integral of an Odd Function",
    "判断并说明理由：若 $f$ 是 $[-a,a]$ 上的可积奇函数，则 $\\int_{-a}^{a}f(x)\\,dx=0$。",
    "Determine whether the statement is true and justify: if $f$ is an integrable odd function on $[-a,a]$, then $\\int_{-a}^{a}f(x)\\,dx=0$.",
    "正确。", "True.",
    "把积分在 $0$ 处分开，并在负半轴积分中作代换 $x=-u$。",
    "Split the integral at $0$ and substitute $x=-u$ in the negative-half integral.",
    [
        "区间可加性给出 $\\int_{-a}^{a}f(x)\\,dx=\\int_{-a}^{0}f(x)\\,dx+\\int_0^a f(x)\\,dx$。",
        "在第一项令 $x=-u$，则 $dx=-du$，并得到 $\\int_{-a}^{0}f(x)\\,dx=\\int_0^a f(-u)\\,du$。",
        "奇性给出 $f(-u)=-f(u)$，故第一项等于 $-\\int_0^a f(u)\\,du$。",
        "两项相消，所以总积分为 $0$。",
    ],
    [
        "Interval additivity gives $\\int_{-a}^{a}f(x)\\,dx=\\int_{-a}^{0}f(x)\\,dx+\\int_0^a f(x)\\,dx$.",
        "In the first term let $x=-u$; then $dx=-du$ and $\\int_{-a}^{0}f(x)\\,dx=\\int_0^a f(-u)\\,du$.",
        "Oddness gives $f(-u)=-f(u)$, so the first term is $-\\int_0^a f(u)\\,du$.",
        "The two terms cancel, giving total integral $0$.",
    ],
    "取 $f(x)=x^3$，两侧对称部分符号相反且绝对值相同，结果确为 $0$。",
    "For $f(x)=x^3$, the two symmetric parts have opposite signs and equal magnitude, giving $0$.",
)

add(
    "Q010", 1, "fill_blank", "definite_integral_properties",
    "同端点定积分", "A Definite Integral with Equal Limits",
    "对任意可积函数 $f$，$\\int_a^a f(x)\\,dx=\\underline{\\qquad}$。",
    "For every integrable function $f$, $\\int_a^a f(x)\\,dx=\\underline{\\qquad}$.",
    "$0$", "$0$",
    "零长度区间没有累积量；也可把同一积分与它的换限形式比较后用代数恒等式推出。",
    "An interval of zero length has no accumulation; the same result follows immediately from the reversal rule.",
    [
        "换限公式给出 $\\int_a^a f(x)\\,dx=-\\int_a^a f(x)\\,dx$。",
        "两边相加得到 $2\\int_a^a f(x)\\,dx=0$。",
        "因此 $\\int_a^a f(x)\\,dx=0$。",
        "故填入 $0$，并且结论与 $f$ 的具体形式无关。",
    ],
    [
        "The reversal rule gives $\\int_a^a f(x)\\,dx=-\\int_a^a f(x)\\,dx$.",
        "Adding the two sides yields $2\\int_a^a f(x)\\,dx=0$.",
        "Therefore $\\int_a^a f(x)\\,dx=0$.",
        "Thus the blank is $0$, independently of the particular integrable function $f$.",
    ],
    "Riemann 和中的总区间长度为 $a-a=0$，与答案一致。",
    "The total interval length in the Riemann-sum definition is $a-a=0$, consistent with the answer.",
)

add(
    "Q011", 1, "fill_blank", "integral_mean_value_and_average",
    "常数函数的平均值", "Average Value of a Constant Function",
    "函数 $f(x)=7$ 在区间 $[-2,3]$ 上的平均值为 $\\underline{\\qquad}$。",
    "The average value of $f(x)=7$ on $[-2,3]$ is $\\underline{\\qquad}$.",
    "$7$", "$7$",
    "先用平均值公式，再利用常数函数的积分等于常数乘区间长度。",
    "Apply the average-value formula and use that the integral of a constant is the constant times the interval length.",
    [
        "区间长度为 $3-(-2)=5$。",
        "平均值为 $f_{\\mathrm{avg}}=\\frac{1}{5}\\int_{-2}^{3}7\\,dx$。",
        "积分等于 $7\\cdot5=35$，所以 $f_{\\mathrm{avg}}=\\frac{35}{5}=7$。",
        "因此填入 $7$；区间长度在分子与分母中完全约去。",
    ],
    [
        "The interval length is $3-(-2)=5$.",
        "The average value is $f_{\\mathrm{avg}}=\\frac{1}{5}\\int_{-2}^{3}7\\,dx$.",
        "The integral is $7\\cdot5=35$, so $f_{\\mathrm{avg}}=\\frac{35}{5}=7$.",
        "Thus the blank is $7$; the interval length cancels between numerator and denominator.",
    ],
    "常数函数在每一点的值都为 $7$，其平均值不可能改变。",
    "The function equals $7$ at every point, so its average cannot differ from $7$.",
)

add(
    "Q012", 1, "fill_blank", "riemann_sums_and_definition",
    "写出右端点平方和", "Writing a Right-Endpoint Sum for a Square",
    "将 $[0,1]$ 等分为 $n$ 段并取右端点，则 $f(x)=x^2$ 的 Riemann 和为 $\\underline{\\qquad}$。",
    "Partition $[0,1]$ into $n$ equal pieces and use right endpoints. The Riemann sum for $f(x)=x^2$ is $\\underline{\\qquad}$.",
    "$\\frac{1}{n^3}\\sum_{k=1}^{n}k^2$", "$\\frac{1}{n^3}\\sum_{k=1}^{n}k^2$",
    "等分宽度为 $\\frac1n$，右端点为 $\\frac{k}{n}$，代入平方函数后乘宽度。",
    "The width is $\\frac1n$ and the right endpoint is $\\frac{k}{n}$; substitute into the square and multiply by the width.",
    [
        "每段宽度为 $\\Delta x=\\frac1n$。",
        "第 $k$ 个右端点为 $x_k=\\frac{k}{n}$。",
        "函数值为 $f(x_k)=\\left(\\frac{k}{n}\\right)^2$。",
        "故和式为 $\\sum_{k=1}^{n}\\left(\\frac{k}{n}\\right)^2\\frac1n=\\frac{1}{n^3}\\sum_{k=1}^{n}k^2$。",
    ],
    [
        "Each width is $\\Delta x=\\frac1n$.",
        "The $k$th right endpoint is $x_k=\\frac{k}{n}$.",
        "The sampled value is $f(x_k)=\\left(\\frac{k}{n}\\right)^2$.",
        "Thus the sum is $\\sum_{k=1}^{n}\\left(\\frac{k}{n}\\right)^2\\frac1n=\\frac{1}{n^3}\\sum_{k=1}^{n}k^2$.",
    ],
    "利用 $\\sum_{k=1}^{n}k^2=\\frac{n(n+1)(2n+1)}6$，其极限为 $\\frac13$，与 $\\int_0^1x^2\\,dx$ 一致。",
    "Using $\\sum_{k=1}^{n}k^2=\\frac{n(n+1)(2n+1)}6$, the limiting value is $\\frac13$, agreeing with $\\int_0^1x^2\\,dx$.",
)

add(
    "Q013", 1, "calculation", "riemann_sums_and_definition",
    "把极限化为定积分", "Converting a Limit into a Definite Integral",
    "计算 $\\lim_{n\\to\\infty}\\frac{27}{n^3}\\sum_{k=1}^{n}k^2$，要求先把它识别为定积分。",
    "Evaluate $\\lim_{n\\to\\infty}\\frac{27}{n^3}\\sum_{k=1}^{n}k^2$ by first identifying it as a definite integral.",
    "$9$", "$9$",
    "把因子重组为函数值 $\\left(\\frac{3k}{n}\\right)^2$ 与宽度 $\\frac3n$ 的乘积。",
    "Regroup the factors as the sampled value $\\left(\\frac{3k}{n}\\right)^2$ times the width $\\frac3n$.",
    [
        "重写和式：$\\frac{27}{n^3}\\sum_{k=1}^{n}k^2=\\sum_{k=1}^{n}\\left(\\frac{3k}{n}\\right)^2\\frac3n$。",
        "这里 $\\Delta x=\\frac3n$，右端点 $x_k=\\frac{3k}{n}$，区间是 $[0,3]$。",
        "因此极限为 $\\int_0^3x^2\\,dx$。",
        "计算得 $\\left.\\frac{x^3}{3}\\right|_0^3=9$。",
    ],
    [
        "Rewrite the sum as $\\frac{27}{n^3}\\sum_{k=1}^{n}k^2=\\sum_{k=1}^{n}\\left(\\frac{3k}{n}\\right)^2\\frac3n$.",
        "Here $\\Delta x=\\frac3n$, $x_k=\\frac{3k}{n}$, and the interval is $[0,3]$.",
        "Hence the limit is $\\int_0^3x^2\\,dx$.",
        "Evaluation gives $\\left.\\frac{x^3}{3}\\right|_0^3=9$.",
    ],
    "直接代入平方和公式得到 $\\frac{27}{n^3}\\cdot\\frac{n(n+1)(2n+1)}6\\to9$，与积分法一致。",
    "Direct use of the square-sum formula gives $\\frac{27}{n^3}\\cdot\\frac{n(n+1)(2n+1)}6\\to9$, matching the integral method.",
)

add(
    "Q014", 1, "calculation", "definite_integral_properties",
    "分段计算绝对值积分", "Evaluating an Absolute-Value Integral Piecewise",
    "计算 $\\int_0^3|x-1|\\,dx$。",
    "Evaluate $\\int_0^3|x-1|\\,dx$.",
    "$\\frac52$", "$\\frac52$",
    "绝对值在 $x=1$ 处改变表达式，必须先拆分区间再积分。",
    "The formula inside the absolute value changes at $x=1$, so the interval must be split there.",
    [
        "在 $[0,1]$ 上，$|x-1|=1-x$；在 $[1,3]$ 上，$|x-1|=x-1$。",
        "因此 $\\int_0^3|x-1|\\,dx=\\int_0^1(1-x)\\,dx+\\int_1^3(x-1)\\,dx$。",
        "第一项为 $\\left.x-\\frac{x^2}{2}\\right|_0^1=\\frac12$。",
        "第二项为 $\\left.\\frac{(x-1)^2}{2}\\right|_1^3=2$，总和为 $\\frac52$。",
    ],
    [
        "On $[0,1]$, $|x-1|=1-x$; on $[1,3]$, $|x-1|=x-1$.",
        "Thus $\\int_0^3|x-1|\\,dx=\\int_0^1(1-x)\\,dx+\\int_1^3(x-1)\\,dx$.",
        "The first term is $\\left.x-\\frac{x^2}{2}\\right|_0^1=\\frac12$.",
        "The second is $\\left.\\frac{(x-1)^2}{2}\\right|_1^3=2$, for a total of $\\frac52$.",
    ],
    "几何上是底高分别为 $1,1$ 与 $2,2$ 的两个三角形，面积为 $\\frac12+2=\\frac52$。",
    "Geometrically the two triangles have base-height pairs $1,1$ and $2,2$, so their areas total $\\frac12+2=\\frac52$.",
)

add(
    "Q015", 1, "calculation", "definite_integral_properties",
    "组合相邻区间的积分", "Combining Integrals over Adjacent Intervals",
    "已知 $a<b<c$，$\\int_a^b f(x)\\,dx=4$ 且 $\\int_b^c f(x)\\,dx=-1$。求 $\\int_c^a f(x)\\,dx$。",
    "Let $a<b<c$, with $\\int_a^b f(x)\\,dx=4$ and $\\int_b^c f(x)\\,dx=-1$. Find $\\int_c^a f(x)\\,dx$.",
    "$-3$", "$-3$",
    "先按 $a\\to b\\to c$ 的方向用区间可加性求出正向积分，再用换限公式处理题目要求的反向积分。",
    "First use interval additivity in the forward direction, then reverse the limits.",
    [
        "区间可加性给出 $\\int_a^c f(x)\\,dx=\\int_a^b f(x)\\,dx+\\int_b^c f(x)\\,dx$。",
        "代入数值得 $\\int_a^c f(x)\\,dx=4+(-1)=3$。",
        "交换上下限，$\\int_c^a f(x)\\,dx=-\\int_a^c f(x)\\,dx=-3$。",
        "所以所求反向积分为 $-3$。",
    ],
    [
        "Interval additivity gives $\\int_a^c f(x)\\,dx=\\int_a^b f(x)\\,dx+\\int_b^c f(x)\\,dx$.",
        "Substitution of the values yields $\\int_a^c f(x)\\,dx=4+(-1)=3$.",
        "Reversing the limits gives $\\int_c^a f(x)\\,dx=-\\int_a^c f(x)\\,dx=-3$.",
        "Therefore the requested oppositely oriented integral is $-3$.",
    ],
    "把三段按方向首尾相接：$\\int_a^b f+\\int_b^c f+\\int_c^a f=0$，代入得到 $4-1-3=0$。",
    "Following the oriented loop gives $\\int_a^b f+\\int_b^c f+\\int_c^a f=0$; substitution gives $4-1-3=0$.",
)

add(
    "Q016", 1, "calculation", "definite_integral_properties",
    "利用点态界给出最紧保证", "Using Pointwise Bounds to Give the Sharp Guaranteed Range",
    "设 $f$ 在 $[-2,2]$ 上可积，且 $-1\\le f(x)\\le 3$。求仅由此条件能保证的 $\\int_{-2}^{2}f(x)\\,dx$ 的取值范围，并说明界可达到。",
    "Suppose $f$ is integrable on $[-2,2]$ and $-1\\le f(x)\\le 3$. Find the range for $\\int_{-2}^{2}f(x)\\,dx$ guaranteed by this information alone, and show that both bounds are attainable.",
    "$-4\\le\\int_{-2}^{2}f(x)\\,dx\\le12$", "$-4\\le\\int_{-2}^{2}f(x)\\,dx\\le12$",
    "将两个常数界积分，并用常数函数验证得到的界是最紧的普遍保证。",
    "Integrate the two constant bounds and use constant functions to show that the resulting bounds are the sharp universal guarantee.",
    [
        "由保序性，$\\int_{-2}^{2}(-1)\\,dx\\le\\int_{-2}^{2}f(x)\\,dx\\le\\int_{-2}^{2}3\\,dx$。",
        "区间长度为 $4$，所以下界为 $-1\\cdot4=-4$。",
        "上界为 $3\\cdot4=12$。",
        "取 $f(x)=-1$ 或 $f(x)=3$ 可分别达到下界和上界。",
    ],
    [
        "Order preservation gives $\\int_{-2}^{2}(-1)\\,dx\\le\\int_{-2}^{2}f(x)\\,dx\\le\\int_{-2}^{2}3\\,dx$.",
        "The interval length is $4$, so the lower bound is $-1\\cdot4=-4$.",
        "The upper bound is $3\\cdot4=12$.",
        "The choices $f(x)=-1$ and $f(x)=3$ attain the lower and upper bounds respectively.",
    ],
    "两个端点都由满足原假设的函数取得，因此任何更窄的统一范围都会排除合法情形。",
    "Both endpoints occur for functions satisfying the hypothesis, so no narrower universal interval can be guaranteed.",
)

add(
    "Q017", 1, "calculation", "definite_integral_properties",
    "先用奇偶性再计算", "Using Symmetry before Evaluation",
    "计算 $\\int_{-2}^{2}(x^3+2x^2)\\,dx$，并明确指出被消去的部分。",
    "Evaluate $\\int_{-2}^{2}(x^3+2x^2)\\,dx$ and identify the part that vanishes.",
    "$\\frac{32}{3}$", "$\\frac{32}{3}$",
    "在对称区间上，奇函数部分积分为零；偶函数部分可化为两倍半区间积分。",
    "On a symmetric interval the odd part integrates to zero, while the even part becomes twice the half-interval integral.",
    [
        "$x^3$ 是奇函数，故 $\\int_{-2}^{2}x^3\\,dx=0$。",
        "$2x^2$ 是偶函数，故 $\\int_{-2}^{2}2x^2\\,dx=2\\int_0^2 2x^2\\,dx$。",
        "计算半区间积分：$2\\int_0^2 2x^2\\,dx=4\\left.\\frac{x^3}{3}\\right|_0^2=\\frac{32}{3}$。",
        "因此原积分为 $\\frac{32}{3}$，被消去的是 $x^3$ 部分。",
    ],
    [
        "$x^3$ is odd, so $\\int_{-2}^{2}x^3\\,dx=0$.",
        "$2x^2$ is even, so $\\int_{-2}^{2}2x^2\\,dx=2\\int_0^2 2x^2\\,dx$.",
        "Evaluate the half-interval integral: $2\\int_0^2 2x^2\\,dx=4\\left.\\frac{x^3}{3}\\right|_0^2=\\frac{32}{3}$.",
        "Thus the original integral is $\\frac{32}{3}$, and the $x^3$ part is the part that vanishes.",
    ],
    "直接用原函数 $\\frac{x^4}{4}+\\frac{2x^3}{3}$ 在 $-2$ 与 $2$ 处相减，也得到 $\\frac{32}{3}$。",
    "Direct evaluation of the antiderivative $\\frac{x^4}{4}+\\frac{2x^3}{3}$ at $-2$ and $2$ also gives $\\frac{32}{3}$.",
)

add(
    "Q018", 1, "proof", "definite_integral_properties",
    "由 Riemann 和证明区间可加性", "Proving Interval Additivity from Riemann Sums",
    "设 $f$ 在 $[a,b]$ 上连续，且 $a<c<b$。从 Riemann 和的定义证明 $\\int_a^b f(x)\\,dx=\\int_a^c f(x)\\,dx+\\int_c^b f(x)\\,dx$。",
    "Let $f$ be continuous on $[a,b]$, with $a<c<b$. Starting from Riemann sums, prove $\\int_a^b f(x)\\,dx=\\int_a^c f(x)\\,dx+\\int_c^b f(x)\\,dx$.",
    "证明见解析。", "See the proof.",
    "选取同时含分点 $c$ 的分割，使整个区间的和式精确拆成左右两段的和式，再分别取极限。",
    "Choose partitions containing $c$, so every whole-interval sum splits exactly into a left sum and a right sum, and then pass to the limits.",
    [
        "分别在 $[a,c]$ 与 $[c,b]$ 上取分割 $P_1,P_2$，并令网格宽度都趋于 $0$。",
        "合并分点得到 $[a,b]$ 的分割 $P=P_1\\cup P_2$，其中明确包含 $c$。",
        "对相容取样点，Riemann 和满足精确恒等式 $S(f,P)=S(f,P_1)+S(f,P_2)$。",
        "连续性保证三个 Riemann 和极限都存在。令网格宽度趋于 $0$，即得 $\\int_a^b f=\\int_a^c f+\\int_c^b f$。",
    ],
    [
        "Choose partitions $P_1$ of $[a,c]$ and $P_2$ of $[c,b]$, with both mesh sizes tending to $0$.",
        "Combine their points to obtain a partition $P=P_1\\cup P_2$ of $[a,b]$ that explicitly contains $c$.",
        "With compatible sample points, the sums satisfy the exact identity $S(f,P)=S(f,P_1)+S(f,P_2)$.",
        "Continuity guarantees existence of all three Riemann-sum limits. Passing to the limit gives $\\int_a^b f=\\int_a^c f+\\int_c^b f$.",
    ],
    "对常数函数 $f(x)=1$，结论退化为长度恒等式 $b-a=(c-a)+(b-c)$，与证明结构一致。",
    "For $f(x)=1$, the result reduces to the length identity $b-a=(c-a)+(b-c)$, matching the proof structure.",
)

add(
    "Q019", 1, "proof", "definite_integral_properties",
    "证明积分三角不等式", "Proving the Integral Triangle Inequality",
    "设 $f$ 在 $[a,b]$ 上连续。证明 $\\left|\\int_a^b f(x)\\,dx\\right|\\le\\int_a^b|f(x)|\\,dx$，并说明何时必取等号。",
    "Let $f$ be continuous on $[a,b]$. Prove $\\left|\\int_a^b f(x)\\,dx\\right|\\le\\int_a^b|f(x)|\\,dx$, and state a sufficient condition for equality.",
    "不等式成立；若 $f$ 在区间上不变号，则取等号。", "The inequality holds; equality occurs when $f$ has constant sign on the interval.",
    "先由逐点双边界证明不等式；连续函数不变号时，绝对值可在整个区间统一去除。",
    "First prove the inequality from pointwise two-sided bounds. For a continuous function of constant sign, the absolute value can be removed consistently over the whole interval.",
    [
        "逐点有 $-|f(x)|\\le f(x)\\le |f(x)|$。",
        "积分保序性给出 $-A\\le I\\le A$，其中 $I=\\int_a^b f(x)\\,dx$、$A=\\int_a^b|f(x)|\\,dx\\ge0$。",
        "双边不等式等价于 $|I|\\le A$，得到所需结论。",
        "若 $f(x)\\ge0$，则 $|f|=f$；若 $f(x)\\le0$，则 $|f|=-f$。两种情形都给出等号。",
    ],
    [
        "Pointwise, $-|f(x)|\\le f(x)\\le |f(x)|$.",
        "Order preservation gives $-A\\le I\\le A$, where $I=\\int_a^b f(x)\\,dx$ and $A=\\int_a^b|f(x)|\\,dx\\ge0$.",
        "This two-sided inequality is equivalent to $|I|\\le A$.",
        "If $f(x)\\ge0$, then $|f|=f$; if $f(x)\\le0$, then $|f|=-f$. Either condition gives equality.",
    ],
    "取 $f(x)=x$ 于 $[-1,1]$，左边为 $0$、右边为 $1$，说明变号时可能严格小于。",
    "For $f(x)=x$ on $[-1,1]$, the left side is $0$ and the right side is $1$, showing that sign changes can make the inequality strict.",
)

add(
    "Q020", 1, "comprehensive", "riemann_sums_and_definition",
    "从非线性和式到精确积分值", "From a Nonlinear Sum to an Exact Integral",
    "求极限 $L=\\lim_{n\\to\\infty}\\frac1n\\sum_{k=1}^{n}\\sqrt{1+\\left(\\frac{k}{n}\\right)^2}$，写出对应定积分并求精确值。",
    "Find $L=\\lim_{n\\to\\infty}\\frac1n\\sum_{k=1}^{n}\\sqrt{1+\\left(\\frac{k}{n}\\right)^2}$, identify the corresponding definite integral, and evaluate it exactly.",
    "$L=\\frac12\\left(\\sqrt2+\\ln(1+\\sqrt2)\\right)$", "$L=\\frac12\\left(\\sqrt2+\\ln(1+\\sqrt2)\\right)$",
    "和式已呈现右端点 Riemann 和；识别后调用第四章得到的根式原函数。",
    "The expression is already a right-endpoint Riemann sum; after identifying it, use the radical antiderivative established in Chapter 4.",
    [
        "令 $\\Delta x=\\frac1n$、$x_k=\\frac{k}{n}$，则和式为 $\\sum_{k=1}^{n}\\sqrt{1+x_k^2}\\,\\Delta x$。",
        "因此 $L=\\int_0^1\\sqrt{1+x^2}\\,dx$。",
        "一个原函数是 $\\frac12\\left(x\\sqrt{1+x^2}+\\ln\\left(x+\\sqrt{1+x^2}\\right)\\right)$。",
        "代入 $1$ 与 $0$，得到 $L=\\frac12\\left(\\sqrt2+\\ln(1+\\sqrt2)\\right)$。",
    ],
    [
        "Let $\\Delta x=\\frac1n$ and $x_k=\\frac{k}{n}$; the sum is $\\sum_{k=1}^{n}\\sqrt{1+x_k^2}\\,\\Delta x$.",
        "Hence $L=\\int_0^1\\sqrt{1+x^2}\\,dx$.",
        "An antiderivative is $\\frac12\\left(x\\sqrt{1+x^2}+\\ln\\left(x+\\sqrt{1+x^2}\\right)\\right)$.",
        "Evaluation at $1$ and $0$ gives $L=\\frac12\\left(\\sqrt2+\\ln(1+\\sqrt2)\\right)$.",
    ],
    "各项介于 $1$ 与 $\\sqrt2$，所以极限也应在此区间；所得值约为 $1.1478$，范围合理。",
    "Every summand lies between $1$ and $\\sqrt2$, so the limit must also lie there; the exact answer is approximately $1.1478$, which is consistent.",
)

add(
    "Q021", 2, "single_choice", "fundamental_theorem_and_new_functions",
    "直接求变上限积分的导数", "Differentiating a Basic Accumulation Function",
    "设 $F(x)=\\int_0^x(1+t^4)\\,dt$。下列哪一项等于 $F'(x)$？",
    "Let $F(x)=\\int_0^x(1+t^4)\\,dt$. Which expression equals $F'(x)$?",
    "C", "C",
    "被积函数连续且上限就是 $x$，直接应用微积分基本定理第一部分。",
    "The integrand is continuous and the upper limit is exactly $x$, so apply Part I of the Fundamental Theorem directly.",
    [
        "把被积变量 $t$ 看作积分内部的哑变量。",
        "若 $F(x)=\\int_a^x f(t)\\,dt$ 且 $f$ 连续，则 $F'(x)=f(x)$。",
        "这里 $f(t)=1+t^4$，故 $F'(x)=1+x^4$。",
        "因此选择 C；不需要先求出 $F(x)$ 的显式表达式。",
    ],
    [
        "Treat $t$ as a dummy variable internal to the integral.",
        "If $F(x)=\\int_a^x f(t)\\,dt$ with continuous $f$, then $F'(x)=f(x)$.",
        "Here $f(t)=1+t^4$, so $F'(x)=1+x^4$.",
        "Thus C is correct; an explicit formula for $F(x)$ is unnecessary.",
    ],
    "直接积分得 $F(x)=x+\\frac{x^5}{5}$，求导仍为 $1+x^4$。",
    "Direct integration gives $F(x)=x+\\frac{x^5}{5}$, whose derivative is again $1+x^4$.",
    choices_zh=["A. $1+t^4$", "B. $4x^3$", "C. $1+x^4$", "D. $x+x^5$"],
    choices_en=["A. $1+t^4$", "B. $4x^3$", "C. $1+x^4$", "D. $x+x^5$"],
)

add(
    "Q022", 2, "single_choice", "fundamental_theorem_and_new_functions",
    "变下限与复合端点", "A Variable Lower Limit with a Composite Endpoint",
    "设 $H(x)=\\int_{x^2}^{3}e^{t^2}\\,dt$。下列哪一项等于 $H'(x)$？",
    "Let $H(x)=\\int_{x^2}^{3}e^{t^2}\\,dt$. Which expression equals $H'(x)$?",
    "B", "B",
    "变量位于下限，因此先产生负号；端点是 $x^2$，还要乘以其导数 $2x$。",
    "The variable appears in the lower limit, producing a minus sign, and the endpoint $x^2$ contributes its derivative $2x$.",
    [
        "一般公式为 $\\frac{d}{dx}\\int_{u(x)}^{c}f(t)\\,dt=-f(u(x))u'(x)$。",
        "取 $u(x)=x^2$，则 $u'(x)=2x$。",
        "端点处函数值为 $e^{(x^2)^2}=e^{x^4}$。",
        "所以 $H'(x)=-2xe^{x^4}$，选择 B。",
    ],
    [
        "The general rule is $\\frac{d}{dx}\\int_{u(x)}^{c}f(t)\\,dt=-f(u(x))u'(x)$.",
        "Here $u(x)=x^2$, so $u'(x)=2x$.",
        "The endpoint value is $e^{(x^2)^2}=e^{x^4}$.",
        "Hence $H'(x)=-2xe^{x^4}$, so B is correct.",
    ],
    "当 $x>0$ 时下限随 $x$ 增大而右移，被积函数为正，积分应减小；答案确为负。",
    "For $x>0$, the lower limit moves right while the integrand is positive, so the integral should decrease; the answer is indeed negative.",
    choices_zh=["A. $2xe^{x^2}$", "B. $-2xe^{x^4}$", "C. $e^{x^4}$", "D. $-e^{x^2}$"],
    choices_en=["A. $2xe^{x^2}$", "B. $-2xe^{x^4}$", "C. $e^{x^4}$", "D. $-e^{x^2}$"],
)

add(
    "Q023", 2, "single_choice", "newton_leibniz_evaluation",
    "用 Newton-Leibniz 公式计算", "Evaluating with the Newton-Leibniz Formula",
    "定积分 $\\int_0^1 3x^2\\,dx$ 的值是哪一项？",
    "Which value equals $\\int_0^1 3x^2\\,dx$?",
    "A", "A",
    "选择 $3x^2$ 的原函数 $x^3$，再严格按 Newton-Leibniz 公式计算上限值减下限值。",
    "Choose the antiderivative $x^3$ and subtract its lower-end value from its upper-end value.",
    [
        "$3x^2$ 的一个原函数是 $F(x)=x^3$。",
        "Newton-Leibniz 公式给出 $\\int_0^1 3x^2\\,dx=F(1)-F(0)$。",
        "计算得 $1^3-0^3=1$。",
        "所以选择 A。",
    ],
    [
        "An antiderivative of $3x^2$ is $F(x)=x^3$.",
        "The Newton-Leibniz formula gives $\\int_0^1 3x^2\\,dx=F(1)-F(0)$.",
        "This is $1^3-0^3=1$.",
        "Therefore A is correct.",
    ],
    "被积函数在 $[0,1]$ 上非负，结果应非负；对应曲线下面积为 $1$。",
    "The integrand is nonnegative on $[0,1]$, so the result must be nonnegative; the area is $1$.",
    choices_zh=["A. $1$", "B. $\\frac13$", "C. $3$", "D. $0$"],
    choices_en=["A. $1$", "B. $\\frac13$", "C. $3$", "D. $0$"],
)

add(
    "Q024", 2, "single_choice", "newton_leibniz_evaluation",
    "辨认 Newton-Leibniz 公式", "Recognizing the Newton-Leibniz Formula",
    "若 $F'(x)=f(x)$ 且 $f$ 在 $[a,b]$ 上连续，下列哪一项正确？",
    "If $F'(x)=f(x)$ and $f$ is continuous on $[a,b]$, which statement is correct?",
    "D", "D",
    "连续性保证 Newton-Leibniz 公式适用；定积分等于任一原函数在上限与下限处函数值之差。",
    "The definite integral equals the upper-end value minus the lower-end value of any antiderivative.",
    [
        "假设说明 $F$ 是 $f$ 的一个原函数。",
        "Newton-Leibniz 公式为 $\\int_a^b f(x)\\,dx=F(b)-F(a)$。",
        "常数项不会影响差值，因此无需在答案中保留积分常数。",
        "故选择 D。",
    ],
    [
        "The hypothesis says that $F$ is an antiderivative of $f$.",
        "The Newton-Leibniz formula is $\\int_a^b f(x)\\,dx=F(b)-F(a)$.",
        "An arbitrary constant cancels from this difference and is not retained.",
        "Thus D is correct.",
    ],
    "交换 $a,b$ 后右侧变为 $F(a)-F(b)$，恰好与定积分换限变号一致。",
    "After swapping $a,b$, the right side becomes $F(a)-F(b)$, exactly matching the sign change from reversing limits.",
    choices_zh=[
        "A. $\\int_a^b f(x)\\,dx=F(a)-F(b)$",
        "B. $\\int_a^b f(x)\\,dx=F(b)$",
        "C. $\\int_a^b f(x)\\,dx=f(b)-f(a)$",
        "D. $\\int_a^b f(x)\\,dx=F(b)-F(a)$",
    ],
    choices_en=[
        "A. $\\int_a^b f(x)\\,dx=F(a)-F(b)$",
        "B. $\\int_a^b f(x)\\,dx=F(b)$",
        "C. $\\int_a^b f(x)\\,dx=f(b)-f(a)$",
        "D. $\\int_a^b f(x)\\,dx=F(b)-F(a)$",
    ],
)

add(
    "Q025", 2, "multiple_choice", "fundamental_theorem_and_new_functions",
    "积累函数的必然性质", "Necessary Properties of an Accumulation Function",
    "设 $f$ 在 $[a,b]$ 上连续，$F(x)=\\int_a^x f(t)\\,dt$。下列哪些结论必然成立？",
    "Let $f$ be continuous on $[a,b]$ and $F(x)=\\int_a^x f(t)\\,dt$. Which conclusions must hold?",
    "A、B、D", "A, B, D",
    "连续性保证基本定理可用；逐项检查起点值、导数和终点值，二阶可导则没有保证。",
    "Continuity permits the Fundamental Theorem. Check the initial value, derivative, and endpoint value; a second derivative is not guaranteed.",
    [
        "基本定理给出内点上 $F'(x)=f(x)$（端点按单侧导数理解），所以 A 正确。",
        "$F(a)=\\int_a^a f(t)\\,dt=0$，所以 B 正确。",
        "$F''$ 存在需要 $f$ 可导，仅知连续不足以保证，故 C 错误。",
        "$F(b)=\\int_a^b f(t)\\,dt$ 是定义直接给出的，故 D 正确。",
    ],
    [
        "The Fundamental Theorem gives $F'(x)=f(x)$ at interior points (with one-sided derivatives at the endpoints), so A is correct.",
        "$F(a)=\\int_a^a f(t)\\,dt=0$, so B is correct.",
        "Existence of $F''$ would require differentiability of $f$, which continuity alone does not guarantee; C is false.",
        "$F(b)=\\int_a^b f(t)\\,dt$ follows directly from the definition, so D is correct.",
    ],
    "例如在 $[-1,1]$ 上取连续但在 $0$ 处不可导的 $f(x)=|x|$，相应 $F''(0)$ 不存在，验证 C 不能保证。",
    "For example, on $[-1,1]$ take the continuous function $f(x)=|x|$, which is not differentiable at $0$; then $F''(0)$ does not exist, confirming that C is not guaranteed.",
    choices_zh=[
        "A. 对 $x\\in(a,b)$，$F'(x)=f(x)$",
        "B. $F(a)=0$",
        "C. $F''(x)$ 在整个区间内必存在",
        "D. $F(b)=\\int_a^b f(t)\\,dt$",
    ],
    choices_en=[
        "A. For $x\\in(a,b)$, $F'(x)=f(x)$",
        "B. $F(a)=0$",
        "C. $F''(x)$ must exist throughout the interval.",
        "D. $F(b)=\\int_a^b f(t)\\,dt$",
    ],
)

add(
    "Q026", 2, "multiple_choice", "fundamental_theorem_and_new_functions",
    "双变限积分的规则", "Rules for an Integral with Two Variable Limits",
    "设 $f$ 连续，$u,v$ 可导，$H(x)=\\int_{u(x)}^{v(x)}f(t)\\,dt$。下列哪些结论正确？",
    "Let $f$ be continuous, let $u,v$ be differentiable, and define $H(x)=\\int_{u(x)}^{v(x)}f(t)\\,dt$. Which conclusions are correct?",
    "A、B、D", "A, B, D",
    "把积分写成两个同基点积累函数之差，可同时处理上下限。",
    "Write the integral as the difference of two accumulation functions with a common base point to handle both limits.",
    [
        "取固定基点 $c$，则 $H(x)=\\int_c^{v(x)}f(t)\\,dt-\\int_c^{u(x)}f(t)\\,dt$。",
        "逐项求导得到 $H'(x)=f(v(x))v'(x)-f(u(x))u'(x)$，故 A 正确。",
        "若 $u(x)=v(x)$，同端点积分为 $0$，故 B 正确；交换端点会变号，故 C 错误。",
        "令 $u$ 为常数、$v(x)=x$，A 退化为 $H'(x)=f(x)$，故 D 正确。",
    ],
    [
        "For a fixed base point $c$, write $H(x)=\\int_c^{v(x)}f(t)\\,dt-\\int_c^{u(x)}f(t)\\,dt$.",
        "Differentiating gives $H'(x)=f(v(x))v'(x)-f(u(x))u'(x)$, so A is correct.",
        "If $u(x)=v(x)$, the equal-limit integral is $0$, so B is correct; swapping limits changes the sign, so C is false.",
        "With constant $u$ and $v(x)=x$, A reduces to $H'(x)=f(x)$, so D is correct.",
    ],
    "取 $f(t)=1$，则 $H(x)=v(x)-u(x)$，求导为 $v'(x)-u'(x)$，与 A 完全吻合。",
    "For $f(t)=1$, $H(x)=v(x)-u(x)$ and $H'(x)=v'(x)-u'(x)$, exactly matching A.",
    choices_zh=[
        "A. $H'(x)=f(v(x))v'(x)-f(u(x))u'(x)$",
        "B. 若 $u(x)=v(x)$，则 $H(x)=0$",
        "C. 交换 $u,v$ 后 $H$ 不变",
        "D. 若 $u$ 为常数且 $v(x)=x$，则 $H'(x)=f(x)$",
    ],
    choices_en=[
        "A. $H'(x)=f(v(x))v'(x)-f(u(x))u'(x)$",
        "B. If $u(x)=v(x)$, then $H(x)=0$.",
        "C. Interchanging $u,v$ leaves $H$ unchanged.",
        "D. If $u$ is constant and $v(x)=x$, then $H'(x)=f(x)$.",
    ],
)

add(
    "Q027", 2, "true_false", "fundamental_theorem_and_new_functions",
    "基本定理的连续性条件", "The Continuity Hypothesis in the Fundamental Theorem",
    "判断并说明理由：若 $f$ 在 $[a,b]$ 上连续，$F(x)=\\int_a^x f(t)\\,dt$，则对每个 $x\\in(a,b)$ 都有 $F'(x)=f(x)$。",
    "Determine whether the statement is true and justify: if $f$ is continuous on $[a,b]$ and $F(x)=\\int_a^x f(t)\\,dt$, then $F'(x)=f(x)$ for every $x\\in(a,b)$.",
    "正确。", "True.",
    "用差商把导数写成短区间上的函数平均值，再由连续性令该平均值趋向点值。",
    "Write the derivative quotient as the average of the function over a short interval, then use continuity to make that average approach the point value.",
    [
        "$\\frac{F(x+h)-F(x)}{h}=\\frac1h\\int_x^{x+h}f(t)\\,dt$。",
        "积分中值定理给出某个介于 $x$ 与 $x+h$ 的 $\\xi_h$，使差商等于 $f(\\xi_h)$。",
        "当 $h\\to0$ 时，$\\xi_h\\to x$。",
        "由 $f$ 在 $x$ 处连续，$f(\\xi_h)\\to f(x)$，所以 $F'(x)=f(x)$。",
    ],
    [
        "$\\frac{F(x+h)-F(x)}{h}=\\frac1h\\int_x^{x+h}f(t)\\,dt$.",
        "The integral mean value theorem supplies a point $\\xi_h$ between $x$ and $x+h$ for which the quotient equals $f(\\xi_h)$.",
        "As $h\\to0$, $\\xi_h\\to x$.",
        "Continuity at $x$ gives $f(\\xi_h)\\to f(x)$, hence $F'(x)=f(x)$.",
    ],
    "若 $f(t)=t^2$，则 $F(x)=\\frac{x^3-a^3}{3}$，直接求导为 $x^2=f(x)$。",
    "For $f(t)=t^2$, $F(x)=\\frac{x^3-a^3}{3}$, whose derivative is $x^2=f(x)$.",
)

add(
    "Q028", 2, "true_false", "fundamental_theorem_and_new_functions",
    "一个零积累值不能决定端点函数值", "One Zero Accumulation Value Does Not Determine an Endpoint Value",
    "判断并说明理由：若连续函数满足 $\\int_0^{1}f(t)\\,dt=0$，则必有 $f(1)=0$。",
    "Determine whether the statement is true and justify: if a continuous function satisfies $\\int_0^{1}f(t)\\,dt=0$, then necessarily $f(1)=0$.",
    "错误。", "False.",
    "积分为零可能来自正负抵消，而不是端点函数值为零；构造线性函数即可。",
    "A zero integral may result from cancellation rather than a zero endpoint value; a linear counterexample is enough.",
    [
        "取连续函数 $f(t)=2t-1$。",
        "计算 $\\int_0^1(2t-1)\\,dt=\\left.t^2-t\\right|_0^1=0$。",
        "但 $f(1)=2\\cdot1-1=1$。",
        "因此题设条件成立而结论失败，命题错误。",
    ],
    [
        "Take the continuous function $f(t)=2t-1$.",
        "Then $\\int_0^1(2t-1)\\,dt=\\left.t^2-t\\right|_0^1=0$.",
        "However, $f(1)=2\\cdot1-1=1$.",
        "The hypothesis holds while the conclusion fails, so the statement is false.",
    ],
    "该函数在 $\\frac12$ 左右分别为负和正，两部分带符号面积正好抵消。",
    "The function is negative to the left of $\\frac12$ and positive to the right, and the signed areas cancel exactly.",
)

add(
    "Q029", 2, "fill_blank", "newton_leibniz_evaluation",
    "自然对数的标准定积分", "A Standard Integral for the Natural Logarithm",
    "填空：$\\int_1^e\\frac1x\\,dx=\\underline{\\qquad}$。",
    "Fill in the blank: $\\int_1^e\\frac1x\\,dx=\\underline{\\qquad}$.",
    "$1$", "$1$",
    "先确认积分区间位于正半轴，再使用 $\\ln x$ 是 $\\frac1x$ 的原函数，并严格按“上限值减下限值”代入。",
    "On the positive axis, $\\ln x$ is an antiderivative of $\\frac1x$.",
    [
        "取原函数 $F(x)=\\ln x$。",
        "Newton-Leibniz 公式给出 $\\int_1^e\\frac1x\\,dx=\\ln e-\\ln1$。",
        "利用 $\\ln e=1$、$\\ln1=0$，结果为 $1$。",
        "由于 $\\frac1x>0$ 且积分区间长度为 $e-1>0$，所得正值与函数符号一致。",
    ],
    [
        "Choose the antiderivative $F(x)=\\ln x$.",
        "The Newton-Leibniz formula gives $\\int_1^e\\frac1x\\,dx=\\ln e-\\ln1$.",
        "Since $\\ln e=1$ and $\\ln1=0$, the result is $1$.",
        "Because $\\frac1x>0$ and the interval has positive length, the positive result is consistent with the sign of the integrand.",
    ],
    "被积函数在 $[1,e]$ 上为正，答案为正；同时这正是自然对数的积分定义。",
    "The integrand is positive on $[1,e]$, so the positive answer is consistent; this is also the integral definition of the natural logarithm.",
)

add(
    "Q030", 2, "fill_blank", "fundamental_theorem_and_new_functions",
    "三角端点的变限求导", "Differentiation with Trigonometric Endpoints",
    "设 $F(x)=\\int_{\\sin x}^{\\cos x}e^{t^2}\\,dt$，则 $F'(x)=\\underline{\\qquad}$。",
    "Let $F(x)=\\int_{\\sin x}^{\\cos x}e^{t^2}\\,dt$. Then $F'(x)=\\underline{\\qquad}$.",
    "$-\\sin x\\,e^{\\cos^2x}-\\cos x\\,e^{\\sin^2x}$",
    "$-\\sin x\\,e^{\\cos^2x}-\\cos x\\,e^{\\sin^2x}$",
    "分别处理上限与下限：上限项乘 $-\\sin x$，下限项在整体前面还有负号。",
    "Handle the upper and lower limits separately: the upper term is multiplied by $-\\sin x$, and the lower contribution has an additional overall minus sign.",
    [
        "设 $v(x)=\\cos x$、$u(x)=\\sin x$。",
        "双变限公式给出 $F'(x)=e^{v(x)^2}v'(x)-e^{u(x)^2}u'(x)$。",
        "代入 $v'(x)=-\\sin x$ 与 $u'(x)=\\cos x$。",
        "得到 $F'(x)=-\\sin x\\,e^{\\cos^2x}-\\cos x\\,e^{\\sin^2x}$。",
    ],
    [
        "Set $v(x)=\\cos x$ and $u(x)=\\sin x$.",
        "The two-limit formula gives $F'(x)=e^{v(x)^2}v'(x)-e^{u(x)^2}u'(x)$.",
        "Substitute $v'(x)=-\\sin x$ and $u'(x)=\\cos x$.",
        "This yields $F'(x)=-\\sin x\\,e^{\\cos^2x}-\\cos x\\,e^{\\sin^2x}$.",
    ],
    "在 $x=0$ 处，上限的一阶变化为 $0$，下限以速度 $1$ 右移，所以 $F'(0)=-1$；公式也给出 $-1$。",
    "At $x=0$, the upper limit has zero first-order motion while the lower limit moves right with speed $1$, so $F'(0)=-1$; the formula also gives $-1$.",
)

add(
    "Q031", 2, "fill_blank", "fundamental_theorem_and_new_functions",
    "乘积中的积累函数", "An Accumulation Function inside a Product",
    "设 $G(x)=x\\int_0^x t^2\\,dt$，则 $G'(x)=\\underline{\\qquad}$。",
    "Let $G(x)=x\\int_0^x t^2\\,dt$. Then $G'(x)=\\underline{\\qquad}$.",
    "$\\frac43x^3$", "$\\frac43x^3$",
    "外面还有因子 $x$，不能只对积分求导；应使用乘积法则。",
    "There is an additional factor $x$, so differentiating only the integral is insufficient; use the product rule.",
    [
        "令 $A(x)=\\int_0^x t^2\\,dt$，则 $A'(x)=x^2$。",
        "乘积法则给出 $G'(x)=A(x)+xA'(x)$。",
        "又有 $A(x)=\\frac{x^3}{3}$。",
        "故 $G'(x)=\\frac{x^3}{3}+x^3=\\frac43x^3$。",
    ],
    [
        "Let $A(x)=\\int_0^x t^2\\,dt$; then $A'(x)=x^2$.",
        "The product rule gives $G'(x)=A(x)+xA'(x)$.",
        "Also, $A(x)=\\frac{x^3}{3}$.",
        "Therefore $G'(x)=\\frac{x^3}{3}+x^3=\\frac43x^3$.",
    ],
    "先化简 $G(x)=x\\cdot\\frac{x^3}{3}=\\frac{x^4}{3}$，直接求导同样得到 $\\frac43x^3$。",
    "Simplifying first gives $G(x)=x\\cdot\\frac{x^3}{3}=\\frac{x^4}{3}$, whose derivative is again $\\frac43x^3$.",
)

add(
    "Q032", 2, "fill_blank", "newton_leibniz_evaluation",
    "正弦函数的定积分", "A Definite Integral of Sine",
    "填空：$\\int_0^{\\frac{\\pi}{2}}\\sin x\\,dx=\\underline{\\qquad}$。",
    "Fill in the blank: $\\int_0^{\\frac{\\pi}{2}}\\sin x\\,dx=\\underline{\\qquad}$.",
    "$1$", "$1$",
    "先用求导核对 $\\frac{d}{dx}(-\\cos x)=\\sin x$，再分别计算上下端点值，避免漏掉“上限减下限”的第二个负号。",
    "$-\\cos x$ is an antiderivative of $\\sin x$.",
    [
        "取原函数 $F(x)=-\\cos x$。",
        "代入上下限：$\\int_0^{\\frac{\\pi}{2}}\\sin x\\,dx=\\left.-\\cos x\\right|_0^{\\frac{\\pi}{2}}$。",
        "结果为 $-\\cos\\frac{\\pi}{2}-(-\\cos0)=0+1=1$。",
        "又因 $\\sin x\\ge0$ 于该区间，结果 $1>0$ 与积分的符号一致。",
    ],
    [
        "Choose the antiderivative $F(x)=-\\cos x$.",
        "Evaluate the endpoints: $\\int_0^{\\frac{\\pi}{2}}\\sin x\\,dx=\\left.-\\cos x\\right|_0^{\\frac{\\pi}{2}}$.",
        "The result is $-\\cos\\frac{\\pi}{2}-(-\\cos0)=0+1=1$.",
        "Since $\\sin x\ge0$ throughout the interval, the positive value $1$ has the correct sign.",
    ],
    "在第一象限内正弦曲线位于 $0$ 与 $1$ 之间，区间长度为 $\\frac\\pi2$，面积为 $1$ 在合理范围内。",
    "In the first quadrant the sine curve lies between $0$ and $1$ over a length $\\frac\\pi2$; an area of $1$ is plausible.",
)

add(
    "Q033", 2, "fill_blank", "fundamental_theorem_and_new_functions",
    "在指定点求复合变限导数", "Evaluating a Composite-Limit Derivative at a Point",
    "设 $G(x)=\\int_1^{x^2}\\ln t\\,dt$，则 $G'(1)=\\underline{\\qquad}$。",
    "Let $G(x)=\\int_1^{x^2}\\ln t\\,dt$. Then $G'(1)=\\underline{\\qquad}$.",
    "$0$", "$0$",
    "先写一般导数，再代入指定点；不能先把上限 $x^2$ 误当成 $x$。",
    "Find the general derivative first and then substitute the specified point; the upper limit $x^2$ must not be treated as $x$.",
    [
        "上限函数为 $u(x)=x^2$，其导数为 $u'(x)=2x$。",
        "基本定理与链式法则给出 $G'(x)=\\ln(x^2)\\cdot2x$。",
        "代入 $x=1$，得到 $G'(1)=2\\ln1$。",
        "由于 $\\ln1=0$，故 $G'(1)=0$。",
    ],
    [
        "The upper-limit function is $u(x)=x^2$, with $u'(x)=2x$.",
        "The Fundamental Theorem and chain rule give $G'(x)=\\ln(x^2)\\cdot2x$.",
        "At $x=1$, this becomes $G'(1)=2\\ln1$.",
        "Since $\\ln1=0$, $G'(1)=0$.",
    ],
    "在 $x=1$ 附近，被积函数在移动端点 $t=1$ 处为零，因此积累量的一阶变化确为零。",
    "Near $x=1$, the integrand vanishes at the moving endpoint $t=1$, so the first-order change of the accumulation is indeed zero.",
)

add(
    "Q034", 2, "calculation", "newton_leibniz_evaluation",
    "线性函数的定积分", "A Definite Integral of a Linear Function",
    "计算 $\\int_{-1}^{2}(2x+3)\\,dx$。",
    "Evaluate $\\int_{-1}^{2}(2x+3)\\,dx$.",
    "$12$", "$12$",
    "先逐项求出多项式原函数，再严格按“上限函数值减下限函数值”代入；最后可用线性函数的梯形面积作独立验算。",
    "Find a polynomial antiderivative and evaluate it as upper endpoint minus lower endpoint.",
    [
        "$2x+3$ 的一个原函数是 $F(x)=x^2+3x$。",
        "上限值为 $F(2)=4+6=10$。",
        "下限值为 $F(-1)=1-3=-2$。",
        "故积分为 $F(2)-F(-1)=10-(-2)=12$。",
    ],
    [
        "An antiderivative of $2x+3$ is $F(x)=x^2+3x$.",
        "The upper-end value is $F(2)=4+6=10$.",
        "The lower-end value is $F(-1)=1-3=-2$.",
        "Thus the integral is $F(2)-F(-1)=10-(-2)=12$.",
    ],
    "线性函数端点值为 $1$ 与 $7$，平均高度为 $4$、区间长度为 $3$，梯形面积为 $4\\cdot3=12$。",
    "The endpoint values are $1$ and $7$, so the average height is $4$ over length $3$; the trapezoid area is $4\\cdot3=12$.",
)

add(
    "Q035", 2, "calculation", "newton_leibniz_evaluation",
    "反正切原函数的定积分", "A Definite Integral with the Arctangent Antiderivative",
    "计算 $\\int_0^1\\frac{1}{1+x^2}\\,dx$。",
    "Evaluate $\\int_0^1\\frac{1}{1+x^2}\\,dx$.",
    "$\\frac{\\pi}{4}$", "$\\frac{\\pi}{4}$",
    "识别标准原函数 $\\arctan x$，再代入端点。",
    "Recognize the standard antiderivative $\\arctan x$ and evaluate at the endpoints.",
    [
        "$\\frac{d}{dx}\\arctan x=\\frac{1}{1+x^2}$。",
        "因此 $\\int_0^1\\frac{1}{1+x^2}\\,dx=\\left.\\arctan x\\right|_0^1$。",
        "$\\arctan1=\\frac{\\pi}{4}$ 且 $\\arctan0=0$。",
        "所以结果为 $\\frac{\\pi}{4}$。",
    ],
    [
        "$\\frac{d}{dx}\\arctan x=\\frac{1}{1+x^2}$.",
        "Hence $\\int_0^1\\frac{1}{1+x^2}\\,dx=\\left.\\arctan x\\right|_0^1$.",
        "$\\arctan1=\\frac{\\pi}{4}$ and $\\arctan0=0$.",
        "Therefore the value is $\\frac{\\pi}{4}$.",
    ],
    "被积函数在 $[0,1]$ 上介于 $\\frac12$ 与 $1$，积分应介于 $\\frac12$ 与 $1$；$\\frac\\pi4$ 满足。",
    "The integrand lies between $\\frac12$ and $1$ on $[0,1]$, so the integral should lie between those values; $\\frac\\pi4$ does.",
)

add(
    "Q036", 2, "calculation", "newton_leibniz_evaluation",
    "指数函数的有限区间积分", "An Exponential Integral over a Finite Interval",
    "计算 $\\int_0^{\\ln2}e^{2x}\\,dx$。",
    "Evaluate $\\int_0^{\\ln2}e^{2x}\\,dx$.",
    "$\\frac32$", "$\\frac32$",
    "指数的导数带来因子 $2$，所以原函数需要乘 $\\frac12$。",
    "Differentiating the exponential produces a factor $2$, so the antiderivative needs a factor $\\frac12$.",
    [
        "$e^{2x}$ 的一个原函数是 $F(x)=\\frac12e^{2x}$。",
        "应用公式得 $\\int_0^{\\ln2}e^{2x}\\,dx=\\frac12\\left(e^{2\\ln2}-e^0\\right)$。",
        "$e^{2\\ln2}=e^{\\ln4}=4$，且 $e^0=1$。",
        "故结果为 $\\frac12(4-1)=\\frac32$。",
    ],
    [
        "An antiderivative of $e^{2x}$ is $F(x)=\\frac12e^{2x}$.",
        "Thus $\\int_0^{\\ln2}e^{2x}\\,dx=\\frac12\\left(e^{2\\ln2}-e^0\\right)$.",
        "$e^{2\\ln2}=e^{\\ln4}=4$ and $e^0=1$.",
        "Therefore the value is $\\frac12(4-1)=\\frac32$.",
    ],
    "被积函数从 $1$ 增到 $4$，区间长度约为 $0.693$；积分 $1.5$ 与其平均高度、长度的量级相符。",
    "The integrand grows from $1$ to $4$ over a length of about $0.693$; the value $1.5$ has the expected scale.",
)

add(
    "Q037", 2, "calculation", "newton_leibniz_evaluation",
    "余弦平方的整周期对称积分", "Integrating the Square of Cosine over a Half Period",
    "计算 $\\int_0^{\\pi}\\cos^2x\\,dx$。",
    "Evaluate $\\int_0^{\\pi}\\cos^2x\\,dx$.",
    "$\\frac{\\pi}{2}$", "$\\frac{\\pi}{2}$",
    "使用降幂公式把平方转化为常数项与倍角余弦；倍角余弦在一个完整周期上的积分为零，只剩常数项。",
    "Use the power-reduction identity to turn the square into a constant term and a double-angle cosine.",
    [
        "恒等式为 $\\cos^2x=\\frac{1+\\cos2x}{2}$。",
        "因此积分等于 $\\frac12\\int_0^{\\pi}1\\,dx+\\frac12\\int_0^{\\pi}\\cos2x\\,dx$。",
        "第一项为 $\\frac\\pi2$，第二项为 $\\left.\\frac14\\sin2x\\right|_0^{\\pi}=0$。",
        "故结果是 $\\frac\\pi2$。",
    ],
    [
        "Use $\\cos^2x=\\frac{1+\\cos2x}{2}$.",
        "The integral becomes $\\frac12\\int_0^{\\pi}1\\,dx+\\frac12\\int_0^{\\pi}\\cos2x\\,dx$.",
        "The first term is $\\frac\\pi2$, and the second is $\\left.\\frac14\\sin2x\\right|_0^{\\pi}=0$.",
        "Hence the value is $\\frac\\pi2$.",
    ],
    "$\\cos^2x$ 在一个长度为 $\\pi$ 的完整周期上的平均值是 $\\frac12$，所以积分应为 $\\pi\\cdot\\frac12$。",
    "The average of $\\cos^2x$ over its full period of length $\\pi$ is $\\frac12$, so the integral is $\\pi\\cdot\\frac12$.",
)

add(
    "Q038", 2, "calculation", "fundamental_theorem_and_new_functions",
    "两个变量端点的复合求导", "Differentiating Two Composite Variable Endpoints",
    "设 $F(x)=\\int_x^{x^2}\\ln(1+t^2)\\,dt$。求 $F'(x)$。",
    "Let $F(x)=\\int_x^{x^2}\\ln(1+t^2)\\,dt$. Find $F'(x)$.",
    "$F'(x)=2x\\ln(1+x^4)-\\ln(1+x^2)$", "$F'(x)=2x\\ln(1+x^4)-\\ln(1+x^2)$",
    "上限 $x^2$ 与下限 $x$ 都含变量，必须写出两项；上限项还要乘 $2x$。",
    "Both the upper limit $x^2$ and lower limit $x$ vary, so two terms are required; the upper term also carries the factor $2x$.",
    [
        "令 $g(t)=\\ln(1+t^2)$、$v(x)=x^2$、$u(x)=x$。",
        "双变限公式为 $F'(x)=g(v(x))v'(x)-g(u(x))u'(x)$。",
        "上限项为 $\\ln(1+x^4)\\cdot2x$。",
        "下限项为 $\\ln(1+x^2)\\cdot1$，故 $F'(x)=2x\\ln(1+x^4)-\\ln(1+x^2)$。",
    ],
    [
        "Let $g(t)=\\ln(1+t^2)$, $v(x)=x^2$, and $u(x)=x$.",
        "The two-limit rule is $F'(x)=g(v(x))v'(x)-g(u(x))u'(x)$.",
        "The upper contribution is $\\ln(1+x^4)\\cdot2x$.",
        "The lower contribution is $\\ln(1+x^2)\\cdot1$, so $F'(x)=2x\\ln(1+x^4)-\\ln(1+x^2)$.",
    ],
    "在 $x=1$ 处两个端点重合但运动速度不同，公式给出 $F'(1)=\\ln2$；这与短区间的一阶长度变化为 $2-1=1$ 相符。",
    "At $x=1$ the endpoints coincide but move at different speeds; the formula gives $F'(1)=\\ln2$, consistent with first-order interval-length speed $2-1=1$.",
)

add(
    "Q039", 2, "calculation", "fundamental_theorem_and_new_functions",
    "含参数核的积分函数", "An Integral Function with a Parameter-Dependent Kernel",
    "设 $f$ 连续，$G(x)=\\int_0^x(x-t)f(t)\\,dt$。求 $G'(x)$，要求先把 $x$ 从被积式中分离。",
    "Let $f$ be continuous and $G(x)=\\int_0^x(x-t)f(t)\\,dt$. Find $G'(x)$ after first separating the explicit occurrence of $x$ in the integrand.",
    "$G'(x)=\\int_0^x f(t)\\,dt$", "$G'(x)=\\int_0^x f(t)\\,dt$",
    "本题不能把基本定理机械用于整个被积式，因为其中还显含参数 $x$；先利用线性性质重写。",
    "The Fundamental Theorem cannot be applied mechanically to the whole integrand because it also contains the parameter $x$ explicitly; rewrite by linearity first.",
    [
        "展开并分离参数：$G(x)=x\\int_0^x f(t)\\,dt-\\int_0^x t f(t)\\,dt$。",
        "对第一项用乘积法则，导数为 $\\int_0^x f(t)\\,dt+x f(x)$。",
        "对第二项用基本定理，导数为 $x f(x)$。",
        "两项中的 $x f(x)$ 相消，得到 $G'(x)=\\int_0^x f(t)\\,dt$。",
    ],
    [
        "Expand and separate the parameter: $G(x)=x\\int_0^x f(t)\\,dt-\\int_0^x t f(t)\\,dt$.",
        "The derivative of the first term by the product rule is $\\int_0^x f(t)\\,dt+x f(x)$.",
        "The derivative of the second term by the Fundamental Theorem is $x f(x)$.",
        "The two $x f(x)$ terms cancel, leaving $G'(x)=\\int_0^x f(t)\\,dt$.",
    ],
    "取 $f(t)=1$，则 $G(x)=\\int_0^x(x-t)\\,dt=\\frac{x^2}{2}$，其导数为 $x=\\int_0^x1\\,dt$。",
    "For $f(t)=1$, $G(x)=\\int_0^x(x-t)\\,dt=\\frac{x^2}{2}$, whose derivative is $x=\\int_0^x1\\,dt$.",
)

add(
    "Q040", 2, "calculation", "fundamental_theorem_and_new_functions",
    "由积累量恢复被积函数", "Recovering an Integrand from Its Accumulation",
    "连续函数 $f$ 满足 $\\int_0^x f(t)\\,dt=x^2e^x$。求 $f(x)$。",
    "A continuous function $f$ satisfies $\\int_0^x f(t)\\,dt=x^2e^x$. Find $f(x)$.",
    "$f(x)=e^x(x^2+2x)$", "$f(x)=e^x(x^2+2x)$",
    "对恒等式两边关于 $x$ 求导；左侧由基本定理恢复 $f(x)$，右侧使用乘积法则。",
    "Differentiate both sides with respect to $x$. The Fundamental Theorem recovers $f(x)$ on the left, while the product rule handles the right.",
    [
        "由连续性，$\\frac{d}{dx}\\int_0^x f(t)\\,dt=f(x)$。",
        "对右边求导：$\\frac{d}{dx}(x^2e^x)=2xe^x+x^2e^x$。",
        "提取公因子得 $2xe^x+x^2e^x=e^x(x^2+2x)$。",
        "所以 $f(x)=e^x(x^2+2x)$。",
    ],
    [
        "Continuity gives $\\frac{d}{dx}\\int_0^x f(t)\\,dt=f(x)$.",
        "Differentiate the right side: $\\frac{d}{dx}(x^2e^x)=2xe^x+x^2e^x$.",
        "Factoring gives $2xe^x+x^2e^x=e^x(x^2+2x)$.",
        "Therefore $f(x)=e^x(x^2+2x)$.",
    ],
    "将答案积分：$\\int_0^x e^t(t^2+2t)\\,dt=\\left.t^2e^t\\right|_0^x=x^2e^x$，恢复原等式。",
    "Integrating the answer gives $\\int_0^x e^t(t^2+2t)\\,dt=\\left.t^2e^t\\right|_0^x=x^2e^x$, recovering the given identity.",
)

add(
    "Q041", 2, "calculation", "fundamental_theorem_and_new_functions",
    "变上限积分的二阶导数", "A Second Derivative of an Accumulation Function",
    "设 $F(x)=\\int_0^{x^2}\\cos t\\,dt$。求 $F''(x)$。",
    "Let $F(x)=\\int_0^{x^2}\\cos t\\,dt$. Find $F''(x)$.",
    "$F''(x)=2\\cos(x^2)-4x^2\\sin(x^2)$", "$F''(x)=2\\cos(x^2)-4x^2\\sin(x^2)$",
    "先用基本定理和链式法则求一阶导数，再对乘积 $2x\\cos(x^2)$ 求导。",
    "First use the Fundamental Theorem and chain rule for the first derivative, then differentiate the product $2x\\cos(x^2)$.",
    [
        "一阶导数为 $F'(x)=\\cos(x^2)\\cdot2x=2x\\cos(x^2)$。",
        "对 $2x\\cos(x^2)$ 使用乘积法则。",
        "第一部分为 $2\\cos(x^2)$。",
        "第二部分为 $2x\\cdot[-\\sin(x^2)]\\cdot2x=-4x^2\\sin(x^2)$，合并即得答案。",
    ],
    [
        "The first derivative is $F'(x)=\\cos(x^2)\\cdot2x=2x\\cos(x^2)$.",
        "Apply the product rule to $2x\\cos(x^2)$.",
        "The first contribution is $2\\cos(x^2)$.",
        "The second is $2x\\cdot[-\\sin(x^2)]\\cdot2x=-4x^2\\sin(x^2)$, giving the stated result.",
    ],
    "由于 $F(x)=\\sin(x^2)$，直接求两次导数得到同一表达式。",
    "Since $F(x)=\\sin(x^2)$, differentiating this explicit expression twice gives the same result.",
)

add(
    "Q042", 2, "proof", "fundamental_theorem_and_new_functions",
    "用积分中值定理证明基本定理", "Proving the Fundamental Theorem with the Integral Mean Value Theorem",
    "设 $f$ 在 $[a,b]$ 上连续，$F(x)=\\int_a^x f(t)\\,dt$。证明对 $x\\in(a,b)$ 有 $F'(x)=f(x)$。",
    "Let $f$ be continuous on $[a,b]$ and $F(x)=\\int_a^x f(t)\\,dt$. Prove that $F'(x)=f(x)$ for $x\\in(a,b)$.",
    "证明见解析。", "See the proof.",
    "核心是把差商化为缩短区间上的平均值，并利用连续性控制其中值点。",
    "The key is to turn the difference quotient into an average over a shrinking interval and control its mean-value point using continuity.",
    [
        "对充分小的非零 $h$，$F(x+h)-F(x)=\\int_x^{x+h}f(t)\\,dt$。",
        "因此差商为 $\\frac{F(x+h)-F(x)}h=\\frac1h\\int_x^{x+h}f(t)\\,dt$；该式对正负 $h$ 都按有向积分成立。",
        "积分中值定理给出介于 $x$ 与 $x+h$ 的 $\\xi_h$，使差商等于 $f(\\xi_h)$。",
        "当 $h\\to0$ 时 $\\xi_h\\to x$；由连续性 $f(\\xi_h)\\to f(x)$，故差商极限为 $f(x)$。",
    ],
    [
        "For sufficiently small nonzero $h$, $F(x+h)-F(x)=\\int_x^{x+h}f(t)\\,dt$.",
        "Thus $\\frac{F(x+h)-F(x)}h=\\frac1h\\int_x^{x+h}f(t)\\,dt$; oriented integrals make this valid for both signs of $h$.",
        "The integral mean value theorem gives a point $\\xi_h$ between $x$ and $x+h$ such that the quotient equals $f(\\xi_h)$.",
        "As $h\\to0$, $\\xi_h\\to x$; continuity yields $f(\\xi_h)\\to f(x)$, so the difference quotient tends to $f(x)$.",
    ],
    "对任意常数函数，差商恒等于该常数；证明中的平均值点机制与这一极端情形一致。",
    "For a constant function, the quotient is identically that constant, consistent with the mean-value-point mechanism in the proof.",
)

add(
    "Q043", 2, "proof", "fundamental_theorem_and_new_functions",
    "零积累函数推出原函数为零", "A Zero Accumulation Function Forces a Zero Integrand",
    "设 $f$ 在 $[a,b]$ 上连续，并且对每个 $x\\in[a,b]$ 都有 $\\int_a^x f(t)\\,dt=0$。证明 $f(x)=0$ 在 $[a,b]$ 上恒成立。",
    "Let $f$ be continuous on $[a,b]$, and suppose $\\int_a^x f(t)\\,dt=0$ for every $x\\in[a,b]$. Prove that $f(x)=0$ throughout $[a,b]$.",
    "证明见解析。", "See the proof.",
    "这里的关键比 Q028 强：积累函数对每个上限都为零，因此可对恒等式求导。",
    "The hypothesis is stronger than in the earlier counterexample: the accumulation vanishes for every upper limit, so the identity may be differentiated.",
    [
        "定义 $F(x)=\\int_a^x f(t)\\,dt$。",
        "题设说明 $F(x)\\equiv0$，因此在内点有 $F'(x)=0$。",
        "由微积分基本定理和 $f$ 的连续性，$F'(x)=f(x)$。",
        "故内点处 $f(x)=0$；再由连续性取端点极限，得到端点也为 $0$。",
    ],
    [
        "Define $F(x)=\\int_a^x f(t)\\,dt$.",
        "The hypothesis says $F(x)\\equiv0$, so $F'(x)=0$ at every interior point.",
        "By the Fundamental Theorem and continuity of $f$, $F'(x)=f(x)$.",
        "Hence $f(x)=0$ in the interior; continuity then gives zero values at the endpoints as well.",
    ],
    "反向检查：若 $f\\equiv0$，则任意变上限积分都为 $0$，所以结论与条件相互匹配。",
    "Conversely, if $f\\equiv0$, every accumulation integral is $0$, so the conclusion is fully consistent with the hypothesis.",
)

add(
    "Q044", 2, "error_diagnosis", "fundamental_theorem_and_new_functions",
    "诊断双变限求导漏因子", "Diagnosing Missing Factors in Two-Limit Differentiation",
    "学生对 $H(x)=\\int_x^{x^2}f(t)\\,dt$ 写出 $H'(x)=f(x^2)-f(x)$。指出错误，并在 $f$ 连续时给出正确结果。",
    "For $H(x)=\\int_x^{x^2}f(t)\\,dt$, a student writes $H'(x)=f(x^2)-f(x)$. Identify the error and give the correct result when $f$ is continuous.",
    "遗漏了上限 $x^2$ 的导数；$H'(x)=2x f(x^2)-f(x)$。",
    "The derivative of the upper limit $x^2$ was omitted; $H'(x)=2x f(x^2)-f(x)$.",
    "学生记住了上限减下限的符号，却没有对复合端点应用链式法则。",
    "The student remembered upper minus lower but failed to apply the chain rule to the composite endpoint.",
    [
        "设上限 $v(x)=x^2$、下限 $u(x)=x$。",
        "正确公式是 $H'(x)=f(v(x))v'(x)-f(u(x))u'(x)$。",
        "这里 $v'(x)=2x$、$u'(x)=1$。",
        "因此 $H'(x)=2x f(x^2)-f(x)$；学生答案缺少因子 $2x$。",
    ],
    [
        "Set the upper limit $v(x)=x^2$ and lower limit $u(x)=x$.",
        "The correct rule is $H'(x)=f(v(x))v'(x)-f(u(x))u'(x)$.",
        "Here $v'(x)=2x$ and $u'(x)=1$.",
        "Therefore $H'(x)=2x f(x^2)-f(x)$; the student's answer is missing the factor $2x$.",
    ],
    "取 $f(t)=1$，原函数为 $H(x)=x^2-x$，导数是 $2x-1$；学生公式却给出 $0$，立刻暴露错误。",
    "With $f(t)=1$, $H(x)=x^2-x$ and $H'(x)=2x-1$, whereas the student's formula gives $0$, exposing the error immediately.",
)

add(
    "Q045", 3, "calculation", "definite_integral_substitution",
    "对数型定积分换元", "Substitution in a Logarithmic Definite Integral",
    "用换元法计算 $\\int_0^1\\frac{2x}{1+x^2}\\,dx$，并同步变换上下限。",
    "Use substitution to evaluate $\\int_0^1\\frac{2x}{1+x^2}\\,dx$, transforming both limits.",
    "$\\ln2$", "$\\ln2$",
    "分母 $1+x^2$ 的导数正好是分子 $2x$，令其为新变量。",
    "The derivative of the denominator $1+x^2$ is exactly the numerator $2x$, so use it as the new variable.",
    [
        "令 $u=1+x^2$，则 $du=2x\\,dx$。",
        "当 $x=0$ 时 $u=1$；当 $x=1$ 时 $u=2$。",
        "原积分化为 $\\int_1^2\\frac1u\\,du$。",
        "计算得 $\\left.\\ln u\\right|_1^2=\\ln2-\\ln1=\\ln2$。",
    ],
    [
        "Let $u=1+x^2$, so $du=2x\\,dx$.",
        "When $x=0$, $u=1$; when $x=1$, $u=2$.",
        "The integral becomes $\\int_1^2\\frac1u\\,du$.",
        "Thus its value is $\\left.\\ln u\\right|_1^2=\\ln2-\\ln1=\\ln2$.",
    ],
    "原被积函数是 $\\frac{d}{dx}\\ln(1+x^2)$，直接代入端点也得到 $\\ln2$。",
    "The original integrand is $\\frac{d}{dx}\\ln(1+x^2)$, so direct endpoint evaluation also gives $\\ln2$.",
)

add(
    "Q046", 3, "calculation", "definite_integral_substitution",
    "三角幂积分的反向端点", "A Trigonometric Substitution with Reversed New Limits",
    "用换元法计算 $\\int_0^{\\frac{\\pi}{2}}\\sin x\\cos^3x\\,dx$。",
    "Use substitution to evaluate $\\int_0^{\\frac{\\pi}{2}}\\sin x\\cos^3x\\,dx$.",
    "$\\frac14$", "$\\frac14$",
    "令 $u=\\cos x$ 时 $du=-\\sin x\\,dx$，新上下限从 $1$ 变为 $0$；负号与换限共同处理。",
    "With $u=\\cos x$, $du=-\\sin x\\,dx$ and the new limits run from $1$ to $0$; handle the minus sign together with the reversed orientation.",
    [
        "令 $u=\\cos x$，则 $du=-\\sin x\\,dx$。",
        "当 $x=0$ 时 $u=1$；当 $x=\\frac\\pi2$ 时 $u=0$。",
        "积分化为 $-\\int_1^0u^3\\,du=\\int_0^1u^3\\,du$。",
        "计算得 $\\left.\\frac{u^4}{4}\\right|_0^1=\\frac14$。",
    ],
    [
        "Let $u=\\cos x$, so $du=-\\sin x\\,dx$.",
        "When $x=0$, $u=1$; when $x=\\frac\\pi2$, $u=0$.",
        "The integral becomes $-\\int_1^0u^3\\,du=\\int_0^1u^3\\,du$.",
        "Evaluation gives $\\left.\\frac{u^4}{4}\\right|_0^1=\\frac14$.",
    ],
    "原被积函数非负且不超过 $1$，结果应在 $0$ 与 $\\frac\\pi2$ 之间；$\\frac14$ 符号与量级都合理。",
    "The original integrand is nonnegative and at most $1$, so the result must lie between $0$ and $\\frac\\pi2$; $\\frac14$ has the correct sign and scale.",
)

add(
    "Q047", 3, "calculation", "definite_integral_by_parts",
    "多项式与指数函数的分部积分", "Integration by Parts for a Polynomial Times an Exponential",
    "用分部积分法计算 $\\int_0^1xe^x\\,dx$。",
    "Use integration by parts to evaluate $\\int_0^1xe^x\\,dx$.",
    "$1$", "$1$",
    "令多项式因子求导、指数因子积分，可使剩余积分更简单。",
    "Differentiate the polynomial factor and integrate the exponential factor so that the remaining integral is simpler.",
    [
        "取 $u=x$、$dv=e^x\\,dx$，则 $du=dx$、$v=e^x$。",
        "定积分分部公式给出 $\\int_0^1xe^x\\,dx=\\left.xe^x\\right|_0^1-\\int_0^1e^x\\,dx$。",
        "边界项为 $e$，剩余积分为 $e-1$。",
        "因此结果是 $e-(e-1)=1$。",
    ],
    [
        "Choose $u=x$ and $dv=e^x\\,dx$, so $du=dx$ and $v=e^x$.",
        "Definite integration by parts gives $\\int_0^1xe^x\\,dx=\\left.xe^x\\right|_0^1-\\int_0^1e^x\\,dx$.",
        "The boundary term is $e$, and the remaining integral is $e-1$.",
        "Hence the result is $e-(e-1)=1$.",
    ],
    "一个原函数是 $(x-1)e^x$；在 $1$ 与 $0$ 处相减得 $0-(-1)=1$。",
    "An antiderivative is $(x-1)e^x$; evaluation at $1$ and $0$ gives $0-(-1)=1$.",
)

add(
    "Q048", 3, "calculation", "definite_integral_by_parts",
    "带三角因子的分部积分", "Integration by Parts with a Trigonometric Factor",
    "计算 $\\int_0^{\\frac{\\pi}{2}}x\\sin x\\,dx$。",
    "Evaluate $\\int_0^{\\frac{\\pi}{2}}x\\sin x\\,dx$.",
    "$1$", "$1$",
    "令 $x$ 求导、$\\sin x$ 积分；特别注意 $v=-\\cos x$ 带来的符号。",
    "Differentiate $x$ and integrate $\\sin x$, paying close attention to the sign in $v=-\\cos x$.",
    [
        "取 $u=x$、$dv=\\sin x\\,dx$，则 $du=dx$、$v=-\\cos x$。",
        "分部积分得到 $\\int_0^{\\frac\\pi2}x\\sin x\\,dx=\\left.-x\\cos x\\right|_0^{\\frac\\pi2}+\\int_0^{\\frac\\pi2}\\cos x\\,dx$。",
        "边界项在两个端点都为 $0$。",
        "剩余积分为 $\\left.\\sin x\\right|_0^{\\frac\\pi2}=1$。",
    ],
    [
        "Choose $u=x$ and $dv=\\sin x\\,dx$, so $du=dx$ and $v=-\\cos x$.",
        "Integration by parts gives $\\int_0^{\\frac\\pi2}x\\sin x\\,dx=\\left.-x\\cos x\\right|_0^{\\frac\\pi2}+\\int_0^{\\frac\\pi2}\\cos x\\,dx$.",
        "The boundary term is $0$ at both endpoints.",
        "The remaining integral is $\\left.\\sin x\\right|_0^{\\frac\\pi2}=1$.",
    ],
    "被积函数在区间内非负，结果应为正；数值积分也给出约 $1.0000$。",
    "The integrand is nonnegative on the interval, so the answer must be positive; numerical integration also gives approximately $1.0000$.",
)

add(
    "Q049", 3, "proof", "definite_integral_substitution",
    "区间反射换元恒等式", "An Interval-Reflection Substitution Identity",
    "设 $f$ 在 $[0,a]$ 上连续且 $a>0$。证明 $\\int_0^a f(x)\\,dx=\\int_0^a f(a-x)\\,dx$。",
    "Let $f$ be continuous on $[0,a]$ with $a>0$. Prove $\\int_0^a f(x)\\,dx=\\int_0^a f(a-x)\\,dx$.",
    "证明见解析。", "See the proof.",
    "使用反射换元 $u=a-x$；新上下限顺序反转，而微分也产生负号，两者抵消。",
    "Use the reflection substitution $u=a-x$; the new limits reverse while the differential contributes a minus sign, and the two effects cancel.",
    [
        "在右侧积分中令 $u=a-x$，则 $du=-dx$。",
        "当 $x=0$ 时 $u=a$；当 $x=a$ 时 $u=0$。",
        "所以 $\\int_0^a f(a-x)\\,dx=-\\int_a^0f(u)\\,du$。",
        "交换上下限得到 $\\int_0^a f(u)\\,du$；哑变量改名后即为左侧积分。",
    ],
    [
        "In the right-hand integral let $u=a-x$, so $du=-dx$.",
        "When $x=0$, $u=a$; when $x=a$, $u=0$.",
        "Thus $\\int_0^a f(a-x)\\,dx=-\\int_a^0f(u)\\,du$.",
        "Reversing the limits gives $\\int_0^a f(u)\\,du$, which is the left side after renaming the dummy variable.",
    ],
    "取 $f(x)=x$，左侧为 $\\frac{a^2}{2}$，右侧 $\\int_0^a(a-x)\\,dx$ 也为 $\\frac{a^2}{2}$。",
    "For $f(x)=x$, the left side is $\\frac{a^2}{2}$ and the right side $\\int_0^a(a-x)\\,dx$ is also $\\frac{a^2}{2}$.",
)

add(
    "Q050", 3, "proof", "definite_integral_substitution",
    "互补角换元的对称比值积分", "A Symmetric Ratio Integral via Complementary Angles",
    "设 $f$ 在 $[0,1]$ 上连续且恒正。证明 $\\int_0^{\\frac{\\pi}{2}}\\frac{f(\\sin x)}{f(\\sin x)+f(\\cos x)}\\,dx=\\frac{\\pi}{4}$。",
    "Let $f$ be continuous and strictly positive on $[0,1]$. Prove $\\int_0^{\\frac{\\pi}{2}}\\frac{f(\\sin x)}{f(\\sin x)+f(\\cos x)}\\,dx=\\frac{\\pi}{4}$.",
    "证明见解析。", "See the proof.",
    "把积分记为 $I$，作互补角换元后分子中的正弦与余弦交换；将原式与变换后的式子相加。",
    "Call the integral $I$. A complementary-angle substitution swaps sine and cosine in the numerator; add the original and transformed forms.",
    [
        "记 $I=\\int_0^{\\frac\\pi2}\\frac{f(\\sin x)}{f(\\sin x)+f(\\cos x)}\\,dx$。恒正条件保证分母不为零。",
        "令 $u=\\frac\\pi2-x$，利用 $\\sin\\left(\\frac\\pi2-u\\right)=\\cos u$ 与 $\\cos\\left(\\frac\\pi2-u\\right)=\\sin u$。",
        "得到 $I=\\int_0^{\\frac\\pi2}\\frac{f(\\cos u)}{f(\\cos u)+f(\\sin u)}\\,du$。",
        "把两种表示相加：$2I=\\int_0^{\\frac\\pi2}1\\,dx=\\frac\\pi2$，故 $I=\\frac\\pi4$。",
    ],
    [
        "Let $I=\\int_0^{\\frac\\pi2}\\frac{f(\\sin x)}{f(\\sin x)+f(\\cos x)}\\,dx$. Strict positivity ensures the denominator never vanishes.",
        "Set $u=\\frac\\pi2-x$ and use $\\sin\\left(\\frac\\pi2-u\\right)=\\cos u$ and $\\cos\\left(\\frac\\pi2-u\\right)=\\sin u$.",
        "This gives $I=\\int_0^{\\frac\\pi2}\\frac{f(\\cos u)}{f(\\cos u)+f(\\sin u)}\\,du$.",
        "Adding the two representations yields $2I=\\int_0^{\\frac\\pi2}1\\,dx=\\frac\\pi2$, hence $I=\\frac\\pi4$.",
    ],
    "取 $f(s)=1$，被积函数恒为 $\\frac12$，积分立即为 $\\frac12\\cdot\\frac\\pi2=\\frac\\pi4$。",
    "For $f(s)=1$, the integrand is identically $\\frac12$, and the integral is immediately $\\frac12\\cdot\\frac\\pi2=\\frac\\pi4$.",
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
