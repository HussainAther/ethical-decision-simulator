{
  "scenario_id": "medical_ethics_case_01",
  "title": "Medical Dilemma: Informed Consent",
  "description": "You are a doctor with a patient who needs a risky surgery. Should you fully disclose the risks?",
  "branches": [
    {
      "choice": "Disclose all risks",
      "outcome": "Patient is overwhelmed, but they trust your honesty.",
      "next_branch": "patient_reassurance"
    },
    {
      "choice": "Disclose limited risks",
      "outcome": "Patient agrees, but may be surprised by complications.",
      "next_branch": "complication_response"
    }
  ]
}

