# Consent Models
<!-- See also: artifact_descriptions/consent-models.md for complete guidance -->

## Purpose

Consent Models define **GDPR-compliant consent collection, management, and withdrawal mechanisms** for personal data processing. This artifact documents consent purposes, legal bases, granular consent options, and user rights implementation.

**GDPR Requirements** (Articles 6, 7, 13, 14):
- **Freely given**: No coercion, genuine choice
- **Specific**: Separate consent for different purposes
- **Informed**: Clear explanation of data use
- **Unambiguous**: Affirmative action required (no pre-ticked boxes)
- **Withdrawable**: Easy to withdraw consent as to give

---

## Consent Purposes & Legal Bases

### Purpose 1: Marketing Communications

**Data Collected**: Email address, name, communication preferences

**Legal Basis**: Consent (GDPR Article 6(1)(a))

**Purpose Description**: 
"We would like to send you information about our products, special offers, and company news via email. You can unsubscribe at any time."

**Consent Collection Method**:
- **Opt-in checkbox** (unchecked by default)
- **Separate from Terms of Service acceptance**
- **Granular options**: Product updates, Promotional offers, Newsletter

**Consent Text**:
```
☐ I agree to receive marketing emails from [Company Name]
  - ☐ Product updates and new features
  - ☐ Promotional offers and discounts  
  - ☐ Monthly newsletter

You can unsubscribe at any time by clicking the link in our emails 
or managing preferences in your account settings.
```

**Withdrawal Method**: 
- Unsubscribe link in every email
- Account settings page
- Email to privacy@company.com

**Data Retention**: 
- If consent given: Until withdrawn
- If consent withdrawn: Email removed from marketing list within 48 hours

---

### Purpose 2: Analytics & Performance Tracking

**Data Collected**: Cookies, IP address, device info, usage patterns

**Legal Basis**: Consent (GDPR Article 6(1)(a)) for non-essential cookies

**Purpose Description**:
"We use cookies to understand how you use our website and improve your experience. This includes analytics (Google Analytics), performance monitoring, and personalization."

**Consent Collection Method**:
- **Cookie banner** (shown on first visit)
- **Granular cookie categories**: Essential, Analytics, Marketing, Preferences
- **Pre-consent state**: Only essential cookies loaded

**Consent Text**:
```
We use cookies to improve your experience. 
Essential cookies are required for the site to function.

☑ Essential (always active)
☐ Analytics (Google Analytics, Mixpanel)
☐ Marketing (Facebook Pixel, Google Ads)
☐ Preferences (Remember your settings)

[Accept All] [Reject Non-Essential] [Manage Preferences]
```

**Withdrawal Method**:
- Cookie settings page (footer link)
- Browser cookie deletion

**Data Retention**:
- Analytics data: 26 months (Google Analytics default)
- Cookie consent record: 12 months, then re-prompt

---

### Purpose 3: Third-Party Data Sharing (Partners)

**Data Collected**: Email, name, purchase history

**Legal Basis**: Consent (GDPR Article 6(1)(a))

**Purpose Description**:
"We partner with [Partner Name] to provide complementary services. With your consent, we may share your contact information with our trusted partners."

**Consent Collection Method**:
- **Separate opt-in checkbox** (unchecked by default)
- **List of partners** provided with links to their privacy policies

**Consent Text**:
```
☐ I agree to share my information with [Company Name]'s partners:
  - Partner A (loyalty program) - Privacy Policy
  - Partner B (insurance services) - Privacy Policy
  
You can withdraw consent at any time in your account settings.
```

**Withdrawal Method**:
- Account settings → Privacy → Data sharing preferences
- Email to privacy@company.com

---

## Consent Record (Proof of Consent)

For each consent, system must record:

| Field | Example Value | Requirement |
|-------|---------------|-------------|
| User ID | user_12345 | Unique identifier |
| Consent Purpose | marketing_emails | Specific purpose |
| Consent Given | true | Boolean |
| Consent Date | 2024-10-26T14:23:45Z | ISO 8601 timestamp |
| Consent Method | web_form_checkout | How consent was collected |
| Consent Text Shown | "I agree to receive..." | Exact wording shown to user |
| IP Address | 192.0.2.1 | For fraud detection |
| User Agent | Mozilla/5.0... | Browser/device info |
| Version | v1.2 | Privacy policy version |

**Storage**: 
- Database table: `user_consents`
- Immutable records (no updates, only inserts for changes)
- Retention: Life of account + 7 years (compliance)

---

## Consent Withdrawal Process

**User-Initiated Withdrawal**:
1. User clicks "Manage Privacy Preferences" in account settings
2. User unchecks consent checkbox
3. System records withdrawal with timestamp
4. System stops processing for that purpose within 48 hours
5. Confirmation email sent: "Your preferences have been updated"

**Data Subject Access Request (DSAR)**:
- User can request full consent history: `GET /api/privacy/consents`
- Response includes all consents given, withdrawn, and current status

**Right to be Forgotten**:
- User can request account deletion
- All personal data deleted within 30 days
- Consent records retained for 7 years (legal obligation)

---

## Consent Lifecycle States

```
[No Consent] 
    → [Consent Requested] (banner/form shown)
        → [Consent Given] (user clicks "I agree")
            → [Consent Active] (processing permitted)
                → [Consent Withdrawn] (user opts out)
                    → [Consent Expired] (data deleted per retention policy)
```

---

## Cookie Consent Banner Example

**Required Elements**:
- Clear statement of cookie usage
- Link to full Cookie Policy
- Granular consent options
- "Accept All" and "Reject Non-Essential" buttons
- No pre-ticked boxes

**Example Implementation**:
```html
<div id="cookie-banner">
  <p>We use cookies to improve your experience. 
  <a href="/cookie-policy">Learn more</a></p>
  
  <button id="accept-all">Accept All</button>
  <button id="reject-non-essential">Reject Non-Essential</button>
  <button id="manage-preferences">Manage Preferences</button>
</div>
```

---

## GDPR Rights Implementation

| Right | Implementation | Response Time |
|-------|----------------|---------------|
| Right to Access (Article 15) | User can download consent history and all personal data | 30 days |
| Right to Rectification (Article 16) | User can update profile information | Immediate |
| Right to Erasure (Article 17) | User can delete account and all data | 30 days |
| Right to Data Portability (Article 20) | User can export data in JSON format | 30 days |
| Right to Object (Article 21) | User can opt out of marketing, profiling | 48 hours |
| Right to Withdraw Consent (Article 7) | User can withdraw consent anytime | 48 hours |

---

## Consent Audit Log

All consent changes must be logged immutably:

```sql
CREATE TABLE consent_audit_log (
  id UUID PRIMARY KEY,
  user_id VARCHAR,
  consent_purpose VARCHAR,
  action VARCHAR, -- 'given', 'withdrawn', 'updated'
  timestamp TIMESTAMP,
  ip_address VARCHAR,
  user_agent TEXT,
  previous_value BOOLEAN,
  new_value BOOLEAN,
  consent_text TEXT -- Exact text shown to user
);
```

**Retention**: Permanent (audit trail for regulatory compliance)

---

## Privacy Policy Integration

Consent models must reference current Privacy Policy version:

- **Privacy Policy URL**: https://company.com/privacy
- **Current Version**: v3.0 (effective 2024-10-01)
- **Change Log**: Link to privacy policy changelog

**When Privacy Policy Changes**:
1. Increment version number
2. Notify users via email (if material changes)
3. Re-prompt for consent if processing purposes changed
4. Archive previous policy versions

---

## Related Artifacts

- **Privacy Policy**: `compliance/privacy-policy.yaml`
- **Cookie Policy**: `compliance/cookie-policy.yaml`
- **DSAR Playbooks**: `compliance/dsar-playbooks.md`
- **Data Processing Addendum**: `compliance/data-processing-addendum.md`

---

**Note**: Consent models must be reviewed by legal counsel before implementation. GDPR fines for non-compliant consent can reach €20M or 4% of global revenue.
