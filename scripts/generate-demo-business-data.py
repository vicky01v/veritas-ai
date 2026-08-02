#!/usr/bin/env python3
"""Generate synthetic business demo data for live QA/demo walkthroughs.

This data is intentionally app-agnostic JSON so it can be imported into demos,
mock APIs, analytics fixtures, or presentation environments without adding
commerce-specific implementation to the OpenLIT CE app.
"""

import json
import random
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path


random.seed(42)

OUT = Path("demo_business_data.json")

FIRST_NAMES = [
    "Aarav", "Aisha", "Alex", "Amelia", "Arjun", "Carlos", "Chloe",
    "Daniel", "Diya", "Elena", "Fatima", "Grace", "Hiro", "Isha",
    "Jordan", "Kavya", "Liam", "Maya", "Noah", "Priya", "Ravi",
    "Sara", "Sophia", "Theo", "Vikram",
]
LAST_NAMES = [
    "Anderson", "Brown", "Chen", "Davis", "Fernandez", "Garcia",
    "Gupta", "Iyer", "Johnson", "Kapoor", "Kim", "Kumar", "Lee",
    "Martinez", "Mehta", "Nair", "Patel", "Rao", "Shah", "Singh",
]
COMPANIES = [
    "Acme AI", "Northstar Health", "Vertex Retail", "Nimbus Finance",
    "Helio Energy", "Summit Labs", "BluePeak Logistics", "CivicCloud",
    "BrightCart", "QuantumOps",
]
PRODUCTS = [
    ("AI Observability Pro", "subscription", 249.00),
    ("Prompt Hub Team", "subscription", 149.00),
    ("Evaluation Credits", "usage", 0.08),
    ("Trace Retention Add-on", "subscription", 99.00),
    ("Enterprise Support", "service", 899.00),
    ("OpenGround Seats", "seat", 39.00),
    ("Model Cost Analytics", "subscription", 179.00),
    ("Vault Secrets Pack", "subscription", 129.00),
    ("Fleet Hub Nodes", "usage", 19.00),
    ("Custom Dashboard Pack", "service", 499.00),
]
STATUSES = ["active", "trial", "past_due", "cancelled"]
ORDER_STATUSES = ["paid", "pending", "refunded", "failed"]


def iso(days_ago=0, minutes_offset=0):
    value = datetime.now(timezone.utc) - timedelta(days=days_ago, minutes=minutes_offset)
    return value.replace(microsecond=0).isoformat()


def money(value):
    return round(value, 2)


users = []
for index in range(100):
    first = FIRST_NAMES[index % len(FIRST_NAMES)]
    last = LAST_NAMES[(index * 3) % len(LAST_NAMES)]
    role = ["owner", "admin", "developer", "viewer"][index % 4]
    users.append({
        "id": f"user_{index + 1:03d}",
        "name": f"{first} {last}",
        "email": f"{first.lower()}.{last.lower()}{index + 1}@example.com",
        "role": role,
        "organisation": COMPANIES[index % len(COMPANIES)],
        "status": "active" if index < 88 else "invited",
        "lastLoginAt": iso(random.randint(0, 30), random.randint(0, 1440)),
        "mfaEnabled": index % 3 != 0,
    })

customers = []
for index in range(60):
    company = COMPANIES[index % len(COMPANIES)]
    customers.append({
        "id": f"cust_{index + 1:03d}",
        "name": f"{company} Division {index + 1}",
        "industry": ["SaaS", "Healthcare", "Retail", "Finance", "Education"][index % 5],
        "plan": ["Starter", "Growth", "Scale", "Enterprise"][index % 4],
        "status": STATUSES[index % len(STATUSES)],
        "ownerUserId": users[index % len(users)]["id"],
        "monthlyRecurringRevenue": money(random.uniform(500, 18000)),
        "createdAt": iso(random.randint(20, 420)),
    })

products = []
for index, (name, kind, price) in enumerate(PRODUCTS, start=1):
    products.append({
        "id": f"prod_{index:03d}",
        "name": name,
        "category": kind,
        "unitPrice": price,
        "status": "active",
        "sku": f"OPENLIT-{index:03d}",
    })

orders = []
transactions = []
for index in range(180):
    customer = random.choice(customers)
    line_count = random.randint(1, 4)
    selected_products = random.sample(products, line_count)
    line_items = []
    total = 0.0
    for product in selected_products:
        quantity = random.randint(1, 12)
        subtotal = product["unitPrice"] * quantity
        total += subtotal
        line_items.append({
            "productId": product["id"],
            "quantity": quantity,
            "unitPrice": product["unitPrice"],
            "subtotal": money(subtotal),
        })
    status = random.choices(ORDER_STATUSES, weights=[78, 12, 6, 4], k=1)[0]
    order_id = f"ord_{index + 1:04d}"
    orders.append({
        "id": order_id,
        "customerId": customer["id"],
        "status": status,
        "lineItems": line_items,
        "total": money(total),
        "createdAt": iso(random.randint(0, 120), random.randint(0, 1440)),
    })
    transactions.append({
        "id": f"txn_{index + 1:04d}",
        "orderId": order_id,
        "customerId": customer["id"],
        "amount": money(total if status != "refunded" else -total),
        "currency": "USD",
        "status": "succeeded" if status == "paid" else status,
        "paymentMethod": random.choice(["card", "bank_transfer", "invoice"]),
        "processedAt": iso(random.randint(0, 120), random.randint(0, 1440)),
    })

notifications = []
notification_templates = [
    ("Cost anomaly detected", "warning"),
    ("New evaluation failure", "critical"),
    ("Dashboard export completed", "info"),
    ("API key rotated", "info"),
    ("Database connection failed", "critical"),
    ("Weekly report ready", "success"),
]
for index in range(80):
    title, severity = random.choice(notification_templates)
    notifications.append({
        "id": f"notif_{index + 1:03d}",
        "title": title,
        "severity": severity,
        "recipientUserId": users[index % len(users)]["id"],
        "read": index % 4 == 0,
        "createdAt": iso(random.randint(0, 21), random.randint(0, 1440)),
    })

reports = []
for index in range(24):
    reports.append({
        "id": f"report_{index + 1:03d}",
        "name": f"{['Executive', 'Cost', 'Quality', 'Usage'][index % 4]} Report Week {index + 1}",
        "type": ["executive", "cost", "evaluation", "usage"][index % 4],
        "status": ["ready", "ready", "ready", "generating"][index % 4],
        "generatedByUserId": users[index % len(users)]["id"],
        "generatedAt": iso(index * 3),
        "downloadUrl": f"/exports/report_{index + 1:03d}.csv",
    })

daily_revenue = []
daily_activity = []
for days_ago in range(90, -1, -1):
    revenue = sum(t["amount"] for t in transactions if t["processedAt"][:10] == iso(days_ago)[:10])
    daily_revenue.append({
        "date": iso(days_ago)[:10],
        "revenue": money(max(revenue, random.uniform(2000, 16000))),
        "orders": random.randint(8, 45),
        "newCustomers": random.randint(0, 5),
    })
    daily_activity.append({
        "date": iso(days_ago)[:10],
        "requests": random.randint(12000, 180000),
        "errors": random.randint(5, 900),
        "avgLatencyMs": random.randint(240, 2400),
        "tokens": random.randint(600000, 15000000),
    })

dashboard_kpis = {
    "totalUsers": len(users),
    "activeCustomers": sum(1 for customer in customers if customer["status"] == "active"),
    "monthlyRecurringRevenue": money(sum(customer["monthlyRecurringRevenue"] for customer in customers)),
    "ordersLast30Days": sum(1 for order in orders if order["createdAt"] >= iso(30)),
    "revenueLast30Days": money(sum(transaction["amount"] for transaction in transactions if transaction["processedAt"] >= iso(30))),
    "evaluationPassRate": 96.4,
    "p95LatencyMs": 1840,
    "errorRate": 0.38,
}

activity_logs = []
actions = ["login", "create_prompt", "edit_dashboard", "export_report", "rotate_api_key", "delete_rule", "invite_user"]
for index in range(250):
    user = users[index % len(users)]
    activity_logs.append({
        "id": f"act_{index + 1:04d}",
        "actorUserId": user["id"],
        "actorEmail": user["email"],
        "action": random.choice(actions),
        "target": random.choice(["dashboard", "prompt", "rule", "report", "api_key", "organisation"]),
        "ipAddress": f"10.24.{index % 255}.{(index * 7) % 255}",
        "createdAt": iso(random.randint(0, 45), random.randint(0, 1440)),
    })

data = {
    "generatedAt": iso(),
    "users": users,
    "customers": customers,
    "products": products,
    "orders": orders,
    "transactions": transactions,
    "notifications": notifications,
    "reports": reports,
    "analytics": {
        "dailyRevenue": daily_revenue,
        "dailyActivity": daily_activity,
        "charts": {
            "revenueByPlan": [
                {"plan": plan, "revenue": money(sum(c["monthlyRecurringRevenue"] for c in customers if c["plan"] == plan))}
                for plan in ["Starter", "Growth", "Scale", "Enterprise"]
            ],
            "ordersByStatus": [
                {"status": status, "count": sum(1 for order in orders if order["status"] == status)}
                for status in ORDER_STATUSES
            ],
        },
    },
    "dashboardKpis": dashboard_kpis,
    "activityLogs": activity_logs,
}

OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
print(f"Wrote {OUT} with {len(users)} users, {len(orders)} orders, and {len(transactions)} transactions")
