# Restrict Pricelist Users

Odoo addon that restricts access to **Product Pricelists** using a Many2many field (`allowed_users`) and **Record Rules**.

## What it does
- Adds an **Allowed Users** field (`allowed_users`) on `product.pricelist`.
- Displays the field on the Pricelist form (right after `company_id`) as tags.
- Defines two security groups:
  - **Own Pricelists**: can only *see* pricelists where:
    - the current user is in `allowed_users`, **or**
    - `allowed_users` is empty (treated as unrestricted)
  - **All Pricelists**: can see all pricelists (empty domain) and implies **Own Pricelists**.

## Installation
1. Copy the addon to your addons path.
2. Restart Odoo.
3. Apps → Update Apps List.
4. Install **Restrict Pricelist Users**.

## Configuration
### 1) Assign groups to users
- Settings → Users & Companies → Users
- On the user:
  - for restricted access: enable **Own Pricelists**
  - for full access: enable **All Pricelists**

### 2) Configure each Pricelist
- Sales → Products → Pricelists (or your equivalent menu)
- Set **Allowed Users**:
  - if empty: visible to users in **Own Pricelists** (acts like “public” within that group)
  - if set: only those users (within **Own Pricelists**) will see it

## How it works (technical)
- View: `views/product_pricelist_views.xml`
  - inserts `allowed_users` into the `product.pricelist` form view
- Model: `models/product_pricelist.py`
  - adds `allowed_users = fields.Many2many('res.users', ...)`
- Security: `security/pricelist_rules.xml`
  - Rule “Own pricelists” domain:
    - `['|', ('allowed_users', 'in', user.id), ('allowed_users', '=', False)]`
  - Rule “All pricelists” domain:
    - `[]` (sees everything)

## Notes / limitations
- The record rules are defined for **read** access. Write/create/delete permissions are governed by ACLs and any other security rules in your database.
- If a user has **All Pricelists**, the unrestricted domain will override the restricted visibility (by design).
- This addon is placed under an `odoo-16` folder; the manifest version is set to `16.0.1.0.0` accordingly.

## Quick test
1. Create two users: U1 and U2 (both in **Own Pricelists**).
2. Create two pricelists:
   - PL1: Allowed Users = U1
   - PL2: Allowed Users = (empty)
3. Login as U1: you should see PL1 and PL2.
4. Login as U2: you should only see PL2.


## Live Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/2kjrHfIb4Dc?si=xg19Ed1XfYv1KyDd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>