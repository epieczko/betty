# Data Dictionaries
# Business Glossary and Technical Metadata Registry

---

## Document Metadata

**Version:** 2.0.0
**Last Updated:** 2024-01-15
**Owner:** Data Governance Team
**Classification:** Internal
**Catalog Tool:** Collibra Data Intelligence Cloud

**Approvers:**
- Jennifer Liu, Chief Data Officer (2024-01-15)
- Marcus Thompson, Data Governance Lead (2024-01-15)

---

## Purpose

This data dictionary provides comprehensive documentation of all data elements within the Customer Data Platform (CDP), mapping technical metadata to business terminology and establishing ISO 11179 naming conventions and data stewardship assignments.

**Scope:**
- Customer master data (MDM)
- Transaction and order data
- Product catalog
- Marketing and analytics data

**Standards:**
- ISO 11179: Metadata registry standards
- GDPR Article 30: Record of Processing Activities (ROPA)
- ISO 8000: Data quality management

---

## Data Dictionary Structure

### Section 1: Business Glossary Terms

| Term | Definition | Synonyms | Related Terms | Business Steward |
|------|------------|----------|---------------|-----------------|
| **Customer** | Individual or organization that has purchased or expressed intent to purchase products or services | Client, Account, Buyer | Prospect, Lead | Sarah Chen (Customer Success) |
| **Customer Lifetime Value (CLV)** | Predicted net profit attributed to entire future relationship with customer | LTV, Lifetime Value | Customer Value, Revenue Per Customer | Michael Torres (Analytics) |
| **Order** | Formal request by customer to purchase one or more products | Purchase Order, Sales Order | Transaction, Invoice | David Kim (Operations) |
| **Active Customer** | Customer who has made at least one purchase in the last 12 months | Current Customer, Engaged Customer | Churned Customer, Dormant Customer | Maria Rodriguez (Marketing) |

---

## Section 2: Entity/Table Documentation

### Entity: CUSTOMERS

**Business Definition:** Master record for all individuals and organizations who are customers or prospects
**System of Record:** Salesforce CRM (synchronized to CDP nightly)
**Data Steward:** Sarah Chen (Business), Marcus Johnson (Technical)
**Classification:** PII - Confidential
**Retention Period:** 7 years after last activity (per GDPR Art. 17)

| Attribute Name | Business Name | Data Type | Length | Nullable | PII | Definition | Valid Values | Example Values | Constraints |
|----------------|---------------|-----------|--------|----------|-----|------------|--------------|----------------|-------------|
| `customer_id` | Customer Identifier | UUID | 36 | No | No | Unique identifier for customer record (UUID v4 format) | UUID format | `a7f3c912-4e89-4d3b-9f12-6c8d4e9a1b2c` | Primary Key |
| `email_address` | Email Address | VARCHAR | 255 | No | Yes | Primary email for customer communications and login | Valid RFC 5322 email format | `sarah.chen@example.com` | Unique, Must match regex `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` |
| `first_name` | First Name | VARCHAR | 100 | No | Yes | Customer's legal first name or given name | Alpha characters, hyphens, apostrophes | `Sarah`, `Jean-Pierre` | Length 1-100 |
| `last_name` | Last Name | VARCHAR | 100 | No | Yes | Customer's legal last name or family name | Alpha characters, hyphens, apostrophes, spaces | `Chen`, `van der Berg` | Length 1-100 |
| `customer_type` | Customer Type | VARCHAR | 20 | No | No | Classification of customer as individual or business entity | `Individual`, `Business` | `Individual` | CHECK constraint |
| `account_status` | Account Status | VARCHAR | 20 | No | No | Current operational status of customer account | `Active`, `Suspended`, `Closed` | `Active` | CHECK constraint, Default: `Active` |
| `loyalty_tier` | Loyalty Program Tier | VARCHAR | 20 | Yes | No | Current loyalty program tier based on purchase history and CLV | `Bronze`, `Silver`, `Gold`, `Platinum`, NULL | `Gold` | NULL allowed for non-participants |
| `customer_segment` | Customer Segment | VARCHAR | 30 | Yes | No | Marketing segmentation category (derived monthly) | `High Value`, `Medium Value`, `Low Value`, `At Risk`, `Churned` | `High Value` | Updated via batch process |
| `phone_number` | Phone Number | VARCHAR | 20 | Yes | Yes | Primary contact phone number in E.164 format | E.164 international format | `+1-415-555-0123` | Regex: `^\+[1-9]\d{1,14}$` |
| `date_of_birth` | Date of Birth | DATE | - | Yes | Yes | Customer's date of birth (for age verification and birthday campaigns) | Valid past date | `1985-03-15` | Must be >= 18 years ago |
| `created_date` | Account Created Date | TIMESTAMPTZ | - | No | No | Timestamp when customer record was first created in system | ISO 8601 timestamp | `2023-06-15T14:32:18Z` | Auto-populated |
| `last_purchase_date` | Last Purchase Date | DATE | - | Yes | No | Date of most recent completed order | Valid date | `2024-01-10` | Updated by order processing |
| `total_lifetime_value` | Total Lifetime Value | DECIMAL | 12,2 | Yes | No | Cumulative dollar value of all completed orders | Positive decimal | `15234.50` | Calculated field |

### Entity: ORDERS

**Business Definition:** Customer purchase orders from placement through fulfillment
**System of Record:** Order Management System (OMS)
**Data Steward:** David Kim (Business), Lisa Park (Technical)
**Classification:** Confidential
**Retention Period:** 10 years (financial audit requirements)

| Attribute Name | Business Name | Data Type | Length | Nullable | PII | Definition | Valid Values | Example Values | Constraints |
|----------------|---------------|-----------|--------|----------|-----|------------|--------------|----------------|-------------|
| `order_id` | Order Identifier | VARCHAR | 36 | No | No | Unique identifier for order (format: ORD-YYYY-#######) | Pattern: `ORD-\d{4}-\d{9}` | `ORD-2024-000123456` | Primary Key |
| `customer_id` | Customer Identifier | UUID | 36 | No | No | Foreign key reference to customer who placed order | Valid UUID from CUSTOMERS | `a7f3c912-4e89-4d3b-9f12-6c8d4e9a1b2c` | Foreign Key to CUSTOMERS |
| `order_date` | Order Placement Date | TIMESTAMPTZ | - | No | No | Date and time when customer submitted order | ISO 8601 timestamp | `2024-01-15T09:23:45Z` | Indexed |
| `order_status` | Order Status | VARCHAR | 20 | No | No | Current fulfillment status of order | `Pending`, `Confirmed`, `Shipped`, `Delivered`, `Cancelled` | `Shipped` | State machine workflow |
| `subtotal_amount` | Subtotal Amount | DECIMAL | 10,2 | No | No | Sum of all line items before tax and shipping | Positive decimal | `299.98` | Must equal SUM(line_items.line_total) |
| `tax_amount` | Sales Tax Amount | DECIMAL | 10,2 | No | No | Calculated sales tax based on shipping address | Non-negative decimal | `24.00` | Auto-calculated |
| `shipping_amount` | Shipping and Handling | DECIMAL | 10,2 | No | No | Cost of shipping and handling | Non-negative decimal | `15.00` | Based on carrier rates |
| `total_amount` | Order Total Amount | DECIMAL | 10,2 | No | No | Final amount charged to customer (subtotal + tax + shipping) | Positive decimal | `338.98` | Computed column |
| `payment_method` | Payment Method | VARCHAR | 30 | No | No | Type of payment instrument used | `Credit Card`, `Debit Card`, `PayPal`, `Wire Transfer` | `Credit Card` | Lookup table |

---

## Section 3: Reference Data / Valid Values

### Lookup Table: CUSTOMER_SEGMENTS

| Code | Description | Definition | Criteria |
|------|-------------|------------|----------|
| `HIGH_VALUE` | High Value Customer | Customer with CLV > $10,000 and 5+ orders in last 12 months | `total_lifetime_value > 10000 AND orders_last_12_months >= 5` |
| `MEDIUM_VALUE` | Medium Value Customer | Customer with CLV $1,000-$10,000 and 2-4 orders in last 12 months | `total_lifetime_value BETWEEN 1000 AND 10000` |
| `LOW_VALUE` | Low Value Customer | Customer with CLV < $1,000 or only 1 order in last 12 months | `total_lifetime_value < 1000 OR orders_last_12_months = 1` |
| `AT_RISK` | At Risk Customer | Previously active customer with no orders in last 6-12 months | `days_since_last_purchase BETWEEN 180 AND 365` |
| `CHURNED` | Churned Customer | No orders in last 12+ months | `days_since_last_purchase > 365` |

---

## Section 4: Data Classification and Sensitivity

### PII Data Elements (GDPR/CCPA Compliance)

| Entity | Attribute | PII Category | GDPR Article | Retention Policy | Anonymization |
|--------|-----------|--------------|--------------|------------------|---------------|
| CUSTOMERS | `email_address` | Contact Information | Art. 6(1)(b) - Contract | 7 years after last activity | Hash with SHA-256 |
| CUSTOMERS | `first_name` | Personal Identifiers | Art. 6(1)(b) - Contract | 7 years after last activity | Replace with "REDACTED" |
| CUSTOMERS | `last_name` | Personal Identifiers | Art. 6(1)(b) - Contract | 7 years after last activity | Replace with "REDACTED" |
| CUSTOMERS | `phone_number` | Contact Information | Art. 6(1)(b) - Contract | 7 years after last activity | Mask last 7 digits |
| CUSTOMERS | `date_of_birth` | Sensitive Personal Data | Art. 9 - Special Category | 7 years after last activity | Aggregate to age range |
| CUSTOMER_ADDRESSES | `street_address` | Location Data | Art. 6(1)(b) - Contract | 7 years after last activity | Remove house number |

### Data Sensitivity Classification

| Classification Level | Description | Examples | Access Control |
|---------------------|-------------|----------|----------------|
| **Public** | Information freely shareable | Product catalog, public pricing | All employees |
| **Internal** | General business information | Aggregated sales reports, customer counts | Employees and contractors |
| **Confidential** | Sensitive business data | Individual customer records, order details | Authorized personnel only |
| **Restricted** | Highly sensitive regulated data | Payment card data (PCI), health data (HIPAA) | Minimal access, audit logging |

---

## Section 5: Data Quality Rules

### CUSTOMERS Table Quality Rules

| Rule ID | Rule Name | Definition | Validation Query | Severity | Owner |
|---------|-----------|------------|------------------|----------|-------|
| DQ-001 | Email Uniqueness | Each email address must be unique across all customers | `SELECT email_address, COUNT(*) FROM CUSTOMERS GROUP BY email_address HAVING COUNT(*) > 1` | Critical | Data Governance |
| DQ-002 | Email Format Validation | Email must match RFC 5322 format | `SELECT * FROM CUSTOMERS WHERE email_address !~ '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'` | Critical | Data Governance |
| DQ-003 | Name Completeness | First and last name must not be empty strings | `SELECT * FROM CUSTOMERS WHERE TRIM(first_name) = '' OR TRIM(last_name) = ''` | High | Data Governance |
| DQ-004 | Age Verification | Date of birth must indicate customer is 18+ years old | `SELECT * FROM CUSTOMERS WHERE date_of_birth > CURRENT_DATE - INTERVAL '18 years'` | High | Compliance |
| DQ-005 | CLV Non-Negative | Total lifetime value must be >= 0 | `SELECT * FROM CUSTOMERS WHERE total_lifetime_value < 0` | Medium | Analytics |

---

## Section 6: Data Lineage Summary

### CUSTOMERS.total_lifetime_value

**Lineage:**
```
Source: ORDERS.total_amount
Transformation: SUM(ORDERS.total_amount WHERE order_status = 'Delivered' AND customer_id = X)
Update Frequency: Nightly batch (2 AM UTC)
Owner: Analytics Engineering Team
dbt Model: models/marts/customers/customer_lifetime_value.sql
```

### CUSTOMERS.customer_segment

**Lineage:**
```
Source: CUSTOMERS.total_lifetime_value, ORDERS (aggregated)
Transformation: CASE statement based on business rules (see Section 3)
Update Frequency: Weekly (Sunday 3 AM UTC)
Owner: Marketing Analytics Team
dbt Model: models/marts/customers/customer_segmentation.sql
```

---

## Section 7: ISO 11179 Naming Conventions

### Naming Standards

**Entity/Table Names:**
- Use plural nouns: `CUSTOMERS`, `ORDERS`, `PRODUCTS`
- Snake_case for multi-word names: `ORDER_LINE_ITEMS`
- Avoid abbreviations unless industry-standard

**Attribute/Column Names:**
- Use snake_case: `customer_id`, `email_address`, `total_amount`
- Include class word suffixes:
  - `_id` for identifiers
  - `_date` for dates
  - `_amount` for monetary values
  - `_count` for quantities
  - `_flag` or `is_` for booleans
  - `_code` for reference codes

**Example Compliant Names:**
- `customer_birth_date` (Object Class: customer, Property: birth, Representation: date)
- `order_total_amount` (Object Class: order, Property: total, Representation: amount)
- `product_unit_price` (Object Class: product, Property: unit price, Representation: currency)

---

## Section 8: Data Stewardship

### Stewardship Assignments

| Domain | Business Steward | Technical Custodian | Responsibilities |
|--------|-----------------|---------------------|------------------|
| Customer Master Data | Sarah Chen, VP Customer Success | Marcus Johnson, Sr. Data Engineer | Define customer attributes, approve schema changes |
| Order Management | David Kim, Director of Operations | Lisa Park, Data Platform Engineer | Order lifecycle, fulfillment status definitions |
| Product Catalog | Jennifer Liu, Chief Product Officer | Alex Rodriguez, Product Data Analyst | Product taxonomy, pricing rules |
| Marketing Analytics | Maria Rodriguez, CMO | Kevin Wu, Analytics Engineer | Segmentation logic, campaign attribution |

---

## Section 9: Integration with Data Catalog

**Catalog Platform:** Collibra Data Intelligence Cloud
**Sync Frequency:** Real-time via Collibra API
**Metadata Extracted:**
- Table and column definitions from PostgreSQL information_schema
- Business glossary terms from Collibra
- Data lineage from dbt artifacts
- Data quality rules from Great Expectations

**Catalog URL:** https://collibra.company.com/data-dictionary/customer-platform

---

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.0.0 | 2024-01-15 | Data Governance Team | Complete rewrite with ISO 11179 standards, added PII classification, data quality rules, and stewardship assignments |
| 1.5.0 | 2023-10-01 | Previous Team | Added GDPR compliance fields |
| 1.0.0 | 2023-01-15 | Legacy Team | Initial version |

---

## References

- ISO 11179: Metadata Registry Standards
- GDPR Article 30: Record of Processing Activities
- DAMA DMBoK Chapter 12: Metadata Management
- Collibra Data Dictionary: https://collibra.company.com
- dbt Documentation: https://dbt.company.com
