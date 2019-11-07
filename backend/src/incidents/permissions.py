"""User permission constants"""

# manage incident enables assignment of incident in auto assign
CAN_MANAGE_INCIDENT = "CAN_MANAGE_INCIDENT"

# permission to view / list incidents
CAN_REVIEW_INCIDENTS = "CAN_REVIEW_INCIDENTS"
# police users can only do this so they only see incidents linked to them
CAN_REVIEW_OWN_INCIDENTS = "CAN_REVIEW_OWN_INCIDENTS"
# ec users can do this to view every incident in the system
CAN_REVIEW_ALL_INCIDENTS = "CAN_REVIEW_ALL_INCIDENTS"

# granular workflow permissions
CAN_RUN_WORKFLOW = "CAN_RUN_WORKFLOW"
CAN_VERIFY_INCIDENT = "CAN_VERIFY_INCIDENT"
CAN_CLOSE_INCIDENT = "CAN_CLOSE_INCIDENT"
CAN_CHANGE_ASSIGNEE = "CAN_CHANGE_ASSIGNEE"
CAN_ESCALATE_INCIDENT = "CAN_ESCALATE_INCIDENT"
CAN_ESCALATE_EXTERNAL = "CAN_ESCALATE_EXTERNAL"
CAN_INVALIDATE_INCIDENT = "CAN_INVALIDATE_INCIDENT"

# UI workflow
CAN_VIEW_REPORTS = "CAN_VIEW_REPORTS"
