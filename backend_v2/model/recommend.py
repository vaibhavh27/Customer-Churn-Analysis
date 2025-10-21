
def recommend_actions(reasons, top_k: int = 3):
    ACTION_RULES = [
        (["MonthlyCharges","Fiber optic"], "Offer limited-time discount or bundle to reduce bill shock."),
        (["Contract_Month-to-month","Contract"], "Incentivize annual contract with loyalty credits."),
        (["PaymentMethod_Electronic check","PaymentMethod"], "Promote auto-pay with a small bill credit."),
        (["tenure","SeniorCitizen"], "Proactive outreach and onboarding tips."),
        (["TechSupport_No"], "Offer priority tech support or a free service call."),
        (["OnlineSecurity_No"], "Bundle security/backup at a promo price to increase stickiness."),
        (["PaperlessBilling_Yes"], "Send bill clarity tips and usage summaries."),
    ]
    texts = []
    rs = " ".join([r.get("feature","") for r in reasons]).lower()
    for keys, action in ACTION_RULES:
        if any(k.lower() in rs for k in keys):
            texts.append(action)
    if not texts:
        texts = [
            "Send personalized retention offer based on usage and tenure.",
            "Invite to a short satisfaction survey and follow up.",
            "Enroll in a loyalty program with milestone rewards.",
        ]
    seen, uniq = set(), []
    for t in texts:
        if t not in seen:
            uniq.append(t); seen.add(t)
    return uniq[:top_k]
