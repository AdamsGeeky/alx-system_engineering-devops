# Postmortem (School Registration Management Website Outage)

## Issue Summary

- **Duration:** The outage occurred on July 25, 2023, starting at 1:00 PM and was resolved within 12 hours (UTC).
- **Impact:**
  - The registration website was down for approximately 12 hours.
  - Users experienced difficulty accessing the site, and payment transactions were severely delayed.
  - Approximately 350+ students were affected by the outage.
  - Financial Loss: The outage resulted in a financial loss of $14 million. While efforts were made to recover, only $10.5 million could be restored.

## Timeline:

- **Issue Detection:**
  - The issue was first detected at 1:30 PM on July 25, 2023, through monitoring alerts indicating a spike in server response times.
- **Actions Taken:**
  - Immediate investigation focused on server logs and database performance metrics.
  - Initial assumption: Database overload due to increased registration traffic.
  - Misleading Path: Explored server-side optimizations before realizing the payment API communication issues.
  - Escalation: The incident was escalated to the DevOps and Database teams for collaborative troubleshooting.
  - Resolution: Optimized database queries, increased server resources, and addressed communication glitches with the payment API.

## Root Cause and Resolution:

- **Root Cause:**
  - Unexpected traffic surge during the registration deadline exceeded server capacity.
  - Increased database load and communication issues with the payment API further compounded the problem.
- **Resolution:**
  - Optimized database queries and increased server resources to handle the surge in traffic.
  - Identified and resolved technical glitches causing communication delays with the payment API.

## Financial Impact:

- The outage resulted in a total financial loss of $14 million.
- Efforts to recover funds were partially successful, with $10.5 million restored.

## Corrective and Preventative Measures:

- **Improvements/Fixes:**
  - Implement a robust capacity planning strategy to handle peak traffic.
  - Regularly optimize database queries to ensure efficient performance.
  - Enhance monitoring systems to detect and address communication issues with external services.
- **Tasks:**
  1. Conduct a comprehensive review of server capacity planning to prevent future overloads.
  2. Implement automated alerts for database performance thresholds.
  3. Establish a protocol for real-time communication with payment API services to promptly address issues.
  4. Schedule regular load testing to simulate peak traffic scenarios.
  5. Document and share lessons learned with the development and operations teams.

## Conclusion:

In summary, the outage on July 25, 2023, lasting 12 hours, resulted in a financial loss of $14 million, with only $10.5 million recovered. The root cause was the underestimation of the traffic surge during the registration deadline, leading to server overload and communication glitches with the payment API. The immediate resolution involved optimizing server resources, database queries, and addressing API communication issues. The corrective measures aim to fortify the system against similar incidents and enhance overall reliability.


