# Use Case Models
<!-- See also: artifact_descriptions/use-case-models.md for complete guidance -->

## Document Information

**Project**: [Project Name]
**Version**: 1.0.0
**Created**: YYYY-MM-DD
**Last Modified**: YYYY-MM-DD
**Status**: Draft | Review | Approved
**Author**: [Author Name]
**Document Owner**: [Owner Role/Team]
**Classification**: Internal

### Approvers

| Name | Role | Date | Status |
|------|------|------|--------|
| [Approver Name] | [Approver Role] | YYYY-MM-DD | Pending |

---

## Purpose

This document provides detailed textual specifications for use cases following Alistair Cockburn's fully-dressed template format. Each use case documents the step-by-step interaction between actors and the system, including preconditions, main success scenarios, extensions (alternative flows), exception handling, postconditions, business rules, and non-functional requirements.

Use cases serve as the foundation for requirements elicitation, system design, test case development, and user acceptance criteria.

---

## Use Case Catalog

### UC-001: Process Customer Order

**Goal in Context**: Customer successfully places an order for products through the e-commerce platform

**Scope**: E-Commerce Web Application

**Level**: User-goal level (blue/sea level)

**Primary Actor**: Customer

**Stakeholders and Interests**:
- **Customer**: Wants efficient, error-free ordering process with confirmation
- **Sales Department**: Wants accurate order capture, payment verification, inventory allocation
- **Fulfillment Center**: Needs clear order specifications for picking and shipping
- **Finance**: Requires payment validation and fraud detection

**Preconditions**:
- Customer has registered account with valid email and payment method on file
- Customer is authenticated (logged in with session active)
- Product catalog is accessible and synchronized with inventory system
- Payment gateway (Stripe) is operational

**Minimal Guarantees** (even if use case fails):
- System logs all order attempts for auditing
- No duplicate charges are made to customer payment method
- Inventory is not allocated without confirmed payment
- Customer is notified of failure reason

**Success Guarantees** (Postconditions):
- Order record is created in database with unique order ID
- Inventory is decremented for ordered items
- Payment authorization is obtained from payment gateway
- Order confirmation email is sent to customer
- Order appears in "My Orders" section of customer account
- Fulfillment system receives order for processing
- Sales metrics are updated (revenue, order count)

---

## Main Success Scenario (Happy Path)

1. Customer browses product catalog and adds items to shopping cart
2. System updates cart total, applying any active promotions or discounts
3. Customer clicks "Proceed to Checkout"
4. System validates cart contents:
   - Verifies all items still in stock
   - Checks price changes since items added to cart
   - Validates quantity limits
5. System displays checkout page with shipping address (pre-filled from customer profile)
6. Customer reviews shipping address, selects shipping method (Standard, Express, Overnight)
7. System calculates shipping cost based on destination, weight, and shipping method
8. System displays payment methods on file (credit cards, PayPal)
9. Customer selects payment method
10. Customer reviews order summary (items, quantities, prices, subtotal, tax, shipping, total)
11. Customer clicks "Place Order"
12. System performs final validations:
    - Re-verifies inventory availability (prevent race conditions)
    - Checks customer credit limit (if applicable)
    - Validates payment method is not expired
13. System sends payment authorization request to payment gateway (Stripe API)
14. Payment gateway returns authorization approval
15. System creates order record in database with status "Payment Authorized"
16. System allocates inventory (reserves items, decrements available stock)
17. System generates order confirmation number (ORD-YYYY-MM-DD-XXXXX)
18. System sends order details to fulfillment system (warehouse management system)
19. System sends order confirmation email to customer (includes order number, items, total, estimated delivery date)
20. System displays order confirmation page with order number
21. System redirects customer to order status page after 5 seconds

**Duration**: 2-5 minutes (typical customer interaction time)

**Frequency**: 10,000+ per day (peak traffic)

---

## Extensions (Alternative Flows)

### 4a. Item in cart is out of stock
4a1. System identifies out-of-stock item during validation
4a2. System removes out-of-stock item from cart
4a3. System displays notification: "Item [Product Name] is no longer available and has been removed"
4a4. System suggests alternative products (similar items in stock)
4a5. Customer reviews updated cart
4a6. Use case continues at step 5

### 4b. Price has increased since item added to cart
4b1. System detects price increase
4b2. System displays notification: "Price for [Product Name] has changed from $X to $Y"
4b3. Customer confirms acceptance of new price OR removes item
4b4. Use case continues at step 5

### 6a. Customer wants to ship to different address
6a1. Customer clicks "Ship to different address"
6a2. System displays address entry form
6a3. Customer enters new shipping address
6a4. System validates address via address verification service (USPS API)
6a5. If address invalid, system suggests corrections
6a6. Customer confirms address
6a7. Use case continues at step 7

### 6b. Shipping not available to customer's location
6b1. System checks shipping availability for destination
6b2. System determines location is outside delivery zone (e.g., international, restricted area)
6b3. System displays error: "We're sorry, we cannot ship to this location"
6b4. System provides alternative: "Contact customer service for assistance"
6b5. Customer cancels checkout OR contacts customer service
6b6. Use case ends

### 9a. Customer wants to use new payment method
9a1. Customer clicks "Add new payment method"
9a2. System displays payment method entry form (credit card, PayPal)
9a3. Customer enters payment details
9a4. System validates payment information (Luhn algorithm for credit card, PayPal OAuth)
9a5. System sends tokenization request to payment gateway (PCI compliance - never store PAN)
9a6. Payment gateway returns token
9a7. System stores token and displays masked payment method
9a8. Use case continues at step 10

### 14a. Payment authorization declined
14a1. Payment gateway returns decline code (insufficient funds, card expired, fraud detection)
14a2. System logs decline reason (not shown to customer for security)
14a3. System displays generic error: "Payment could not be processed. Please verify payment details or try a different payment method"
14a4. System returns to payment selection (step 9)
14a5. Customer selects different payment method OR updates payment details
14a6. Use case continues at step 10
**OR**
14a7. Customer cancels order
14a8. System returns items to cart
14a9. Use case ends

### 14b. Payment gateway timeout/unavailable
14b1. System sends payment request, waits 10 seconds
14b2. No response received from gateway
14b3. System displays error: "Payment processing is temporarily unavailable. Please try again in a few minutes."
14b4. System logs incident for operations team
14b5. System sends alert to on-call engineer (critical service failure)
14b6. Customer can retry immediately OR cancel
14b7. Use case continues at step 11 (retry) OR ends (cancel)

### 16a. Inventory allocation fails (concurrent order depleted last item)
16a1. System attempts to allocate inventory (database transaction)
16a2. Database returns constraint violation (insufficient stock)
16a3. System rolls back payment authorization (void transaction via payment gateway)
16a4. System displays error: "We're sorry, an item in your order just sold out. Your card has not been charged."
16a5. System removes out-of-stock item from cart
16a6. System offers: "Continue with remaining items OR cancel entire order"
16a7. If customer continues, use case restarts at step 3
16a8. If customer cancels, use case ends

### 19a. Email sending fails
19a1. System sends order confirmation email via email service (SendGrid)
19a2. Email service returns error (invalid email, service unavailable)
19a3. System logs email failure
19a4. System queues email for retry (exponential backoff: 1 min, 5 min, 15 min)
19a5. System still displays order confirmation page (email failure doesn't block order completion)
19a6. System displays notice: "Order confirmation email will be sent shortly"
19a7. Use case continues at step 20

---

## Special Requirements (Non-Functional)

- **Performance**:
  - Checkout process (steps 3-20) must complete in < 5 seconds (p95)
  - Payment authorization (step 13-14) timeout: 10 seconds max
  - Inventory check (step 12) must use database row-level locking to prevent overselling

- **Usability**:
  - All forms must validate fields in real-time with inline error messages
  - Progress indicator must show checkout steps (Cart → Shipping → Payment → Review → Confirmation)
  - Autosave cart every 30 seconds (prevent data loss on session timeout)

- **Security**:
  - Payment card data must never be stored (PCI DSS Level 1 - tokenization required)
  - All checkout pages must use HTTPS (TLS 1.2+)
  - Customer session must be re-verified before payment (CSRF protection)
  - Rate limiting: Max 3 order attempts per minute per customer (fraud prevention)

- **Reliability**:
  - Order placement must use database transactions (ACID guarantees)
  - Idempotency: Duplicate "Place Order" clicks within 5 seconds must be ignored (prevent double charging)
  - Payment authorization failure must auto-retry once before prompting customer

- **Availability**:
  - Checkout system must maintain 99.95% uptime (21.6 min downtime/month max)
  - Graceful degradation: If recommendation engine fails, checkout continues without suggestions

---

## Technology and Data Variations

**4a. Mobile App Variation**:
- Step 3: Customer taps "Checkout" button
- Step 6: System uses GPS to suggest nearest shipping address
- Step 9: System offers Apple Pay, Google Pay in addition to saved cards
- Biometric authentication (Face ID/Touch ID) for payment confirmation

**4b. Guest Checkout Variation** (no account):
- Precondition: Customer is not authenticated
- Step 4: System displays "Checkout as Guest" option
- Step 5: Customer enters email, shipping address, and payment details in single form
- Step 19: System sends order tracking link via email (no account created)
- Postcondition: Customer can optionally create account post-purchase

---

## Frequency of Occurrence

- **Average**: 10,000 orders per day
- **Peak**: 50,000 orders per day (Black Friday, Cyber Monday)
- **Concurrent Users**: 5,000 simultaneous checkouts during peak

---

## Business Rules

**BR-001**: Customers cannot place orders exceeding $10,000 without phone verification (fraud prevention)

**BR-002**: Tax calculation must use customer's shipping address jurisdiction (Avalara Tax API)

**BR-003**: Free shipping applies to orders > $50 (excluding Alaska, Hawaii)

**BR-004**: Maximum 10 units per SKU per order (prevent inventory hoarding)

**BR-005**: Promotional codes cannot be combined (single promotion per order)

**BR-006**: Digital products (eBooks, software licenses) skip shipping address collection

**BR-007**: Order cancellation allowed within 1 hour of placement (before fulfillment processing begins)

**BR-008**: Payment authorization expires after 7 days; orders not fulfilled within 7 days require re-authorization

---

## Open Issues

| Issue ID | Description | Decision Needed | Owner | Target Resolution |
|----------|-------------|-----------------|-------|-------------------|
| ISS-001 | Should system allow backorders for out-of-stock items? | Product decision | Product Manager | Sprint 5 |
| ISS-002 | Currency support for international customers (USD only currently) | Technical feasibility + business case | Architecture + Product | Q2 2025 |
| ISS-003 | Buy Now Pay Later (BNPL) integration (Affirm, Klarna) | Payment gateway selection | Payments Team | Sprint 8 |

---

## UI Mockups

- Wireframe: `designs/checkout-flow-wireframe.pdf`
- High-fidelity mockup: `designs/checkout-ui-mockup.figma`
- Mobile prototype: `designs/mobile-checkout-prototype.invision`

---

## Related Artifacts

- **Requirements**: `requirements/functional-requirements-spec.md` (REQ-CHECKOUT-001 through REQ-CHECKOUT-025)
- **Architecture**: `architecture/checkout-service-design.md`
- **Test Cases**: `tests/checkout-test-cases.xlsx` (TC-CHECKOUT-001 through TC-CHECKOUT-087)
- **API Documentation**: `api-docs/checkout-api.yaml` (OpenAPI 3.0)
- **User Stories**: `jira/ECOM-245` (Epic: Checkout Experience Enhancement)

---

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2024-01-15 | Jane Smith | Initial use case specification |
| 1.1.0 | 2024-03-20 | Jane Smith | Added guest checkout variation, mobile app flows |
| 1.2.0 | 2024-06-10 | John Doe | Updated payment gateway flows for Stripe integration |
| 1.3.0 | 2024-10-25 | Jane Smith | Added SCA (3D Secure 2.0) extension for EU compliance |

---

### UC-002: Process Refund Request

**Goal in Context**: Customer receives refund for returned merchandise

**Scope**: E-Commerce Order Management System

**Level**: User-goal level

**Primary Actor**: Customer Service Representative

**Stakeholders and Interests**:
- **Customer**: Wants prompt refund processing
- **Finance**: Needs accurate refund accounting, fraud prevention
- **Inventory**: Needs returned merchandise restocking

**Preconditions**:
- Original order exists in system with payment record
- Return merchandise authorization (RMA) has been issued
- Product has been received at returns warehouse

**Success Guarantees**:
- Refund is issued to original payment method
- Order status is updated to "Refunded"
- Inventory is incremented for returned items
- Customer is notified of refund completion
- Accounting records are updated

---

## Main Success Scenario

1. Customer Service Representative (CSR) opens customer order in system
2. CSR verifies return eligibility:
   - Order placed within 30 days
   - Item is returnable (not final sale)
   - Item condition is acceptable (not damaged by customer)
3. CSR creates refund request in system
4. System calculates refund amount:
   - Full item price (original purchase price)
   - Prorated shipping (if applicable per return policy)
   - Restocking fee (if applicable - 15% for opened electronics)
5. CSR reviews refund amount, enters reason code (Customer Remorse, Defective Product, Wrong Item Shipped)
6. CSR submits refund request
7. System validates refund against business rules
8. System sends refund transaction to payment gateway
9. Payment gateway processes refund to original payment method
10. System updates order status to "Refunded"
11. System increments inventory for returned SKU
12. System sends refund confirmation email to customer
13. System generates accounting journal entry (debit: Sales Returns, credit: Customer Refunds Payable)
14. CSR closes refund ticket, system displays confirmation

**Duration**: 5-10 minutes

---

## Extensions

### 2a. Return window expired (> 30 days)
2a1. System displays warning: "Return window expired"
2a2. CSR can request manager override for exceptional circumstances
2a3. Manager reviews customer history, order details
2a4. Manager approves OR denies exception
2a5. If approved, use case continues at step 3
2a6. If denied, CSR explains policy to customer, use case ends

### 2b. Item is not returnable (final sale)
2b1. System displays: "Item marked as Final Sale - not eligible for return"
2b2. CSR explains policy to customer
2b3. CSR can escalate to manager for store credit (discretionary)
2b4. Use case ends (no refund issued)

### 9a. Payment gateway rejects refund (card expired, account closed)
9a1. Payment gateway returns error
9a2. System prompts CSR: "Original payment method unavailable"
9a3. CSR requests alternative refund method from customer (different card, check, store credit)
9a4. Customer provides alternative
9a5. System processes refund to alternative method
9a6. Use case continues at step 10

---

## Special Requirements

- **Performance**: Refund must appear in customer's account within 5-7 business days
- **Audit Trail**: All refunds must be logged with CSR ID, timestamp, reason code
- **Approval**: Refunds > $500 require manager approval
- **Fraud Detection**: Flag customers with > 5 refunds in 30 days for review

---

## Business Rules

**BR-010**: Refunds processed within 24 hours for defective products
**BR-011**: Shipping charges refunded only if error was merchant's fault
**BR-012**: Digital products (non-returnable) require separate approval workflow

---

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2024-02-01 | Jane Smith | Initial refund use case specification |

---

## Notes on Use Case Template Format

This template follows **Alistair Cockburn's fully-dressed use case format**, which includes:

- **Numbered steps** in main scenario for precise referencing
- **Extensions** numbered with step prefix (4a, 4b, 14a, etc.)
- **Actor-system dialogue** format (Actor action → System response)
- **Goal-level scoping** (user-goal level = one user session, typically 2-20 minutes)
- **Preconditions** (testable system state before use case starts)
- **Success Guarantees** (postconditions - testable system state after successful completion)
- **Minimal Guarantees** (what system ensures even if use case fails)
- **Stakeholders and Interests** (who cares about this use case and why)

For simpler use cases, use **brief format** (paragraph description) or **casual format** (numbered steps only, no extensions). Reserve fully-dressed format for complex, high-risk, or contractually significant use cases.

---

**IEEE 29148 Traceability**: Each use case should trace to business requirements (BR-xxx), functional requirements (REQ-xxx), test cases (TC-xxx), and design elements (DESIGN-xxx) in the Requirements Traceability Matrix.

**Test Derivation**: Each numbered step and extension can generate test cases:
- Main scenario → Happy path tests
- Extensions → Alternative flow tests
- Business rules → Validation tests
- Special requirements → Non-functional tests
