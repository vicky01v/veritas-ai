#!/usr/bin/env python3
"""Generate demo telemetry data for OpenLIT/Veritas AI dashboard."""
import json, random, uuid
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen

CH_URL = "http://localhost:8123"
CH_USER = "default"
CH_PASS = "OPENLIT"
DB = "openlit"

SERVICES = [
    {"name": "chatbot-api", "env": "production", "app": "Customer Support Bot"},
    {"name": "rag-service", "env": "production", "app": "Knowledge Assistant"},
    {"name": "code-assistant", "env": "staging", "app": "Code Review Copilot"},
    {"name": "content-generator", "env": "production", "app": "Content Studio"},
    {"name": "analytics-agent", "env": "development", "app": "Data Insights Agent"},
]
PROVIDERS = [
    {"name": "openai", "models": ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo", "text-embedding-3-small"]},
    {"name": "anthropic", "models": ["claude-3-5-sonnet", "claude-3-haiku"]},
    {"name": "cohere", "models": ["command-r-plus", "embed-english-v3.0"]},
    {"name": "mistral", "models": ["mistral-large-latest", "mistral-small-latest"]},
    {"name": "google", "models": ["gemini-1.5-pro", "gemini-1.5-flash"]},
]
VECTOR_DBS = [
    {"name": "pinecone", "collection": "docs-index"},
    {"name": "chromadb", "collection": "knowledge-base"},
    {"name": "qdrant", "collection": "product-catalog"},
]
USERS = ["alice@example.com", "bob@example.com", "carol@example.com", "dave@example.com",
         "erin@example.com", "frank@example.com", "grace@example.com", "henry@example.com",
         "isabel@example.com", "jack@example.com", "kate@example.com", "leo@example.com"]
PROMPTS = [
    "What are the benefits of using our platform?",
    "Can you summarize the latest quarterly report?",
    "Write a product description for our new AI tool",
    "Explain the difference between RAG and fine-tuning",
    "Help me debug this Python error",
    "Generate a marketing email for our launch",
    "What's the best way to optimize our LLM costs?",
    "Create a SQL query to find top customers",
    "Translate this document to Spanish",
    "Analyze the sentiment of these customer reviews",
    "Write a unit test for this function",
    "Suggest improvements for our onboarding flow",
    "What are the security best practices for API keys?",
    "Compare the performance of different embedding models",
    "Draft a response to this customer complaint",
]
RESPONSES = [
    "Based on our analysis, the key benefits include improved efficiency, reduced costs, and better user satisfaction.",
    "The quarterly report shows a 32% increase in active users, with token usage growing 45% month-over-month.",
    "Introducing our next-generation AI observability platform - the all-in-one solution for monitoring and optimizing LLM applications.",
    "RAG combines a retrieval system with a language model to ground responses in your own data. Fine-tuning modifies model weights.",
    "The error occurs because you're passing a None value. Add a type check before the operation.",
    "Subject: Exciting Launch! We're thrilled to announce our new AI observability platform.",
    "To optimize LLM costs: 1) Use smaller models, 2) Implement caching, 3) Set token limits, 4) Use batch processing.",
    "SELECT c.name, COUNT(o.id) as order_count FROM customers c JOIN orders o ON c.id = o.customer_id GROUP BY c.name;",
    "Aquí está la traducción al español: El documento describe las mejores prácticas para implementar observabilidad.",
    "The customer reviews show an overall positive sentiment (78% positive, 15% neutral, 7% negative).",
    "```python\ndef test_calculate_total():\n    assert calculate_total([1, 2, 3]) == 6\n```",
    "For onboarding, I recommend: 1) Interactive product tour, 2) Sample data integration, 3) Quick-start templates.",
    "Security best practices: 1) Never commit keys to version control, 2) Use environment variables, 3) Rotate keys regularly.",
    "text-embedding-3-small offers the best cost-performance ratio for most use cases.",
    "Thank you for reaching out. Our team has identified the issue and is working on a fix.",
]
ERRORS = [
    "Rate limit exceeded for model gpt-4o",
    "Connection timeout to api.openai.com",
    "Invalid API key provided",
    "Model not found: gpt-5",
    "Context length exceeded (max 128000 tokens)",
    "Provider returned 503 Service Unavailable",
]

def ch(query):
    req = Request(f"{CH_URL}/?database={DB}", data=query.encode(), method="POST",
                  headers={"Content-Type": "application/x-www-form-urlencoded",
                           "X-ClickHouse-User": CH_USER, "X-ClickHouse-Key": CH_PASS})
    try:
        with urlopen(req) as r:
            return r.read().decode()
    except Exception as e:
        try:
            body = e.read().decode() if hasattr(e, 'read') else str(e)
            print(f"CH error: {body[:500]}")
        except:
            print(f"CH error: {e}")
        return ""

def esc(s):
    return str(s).replace("\\", "\\\\").replace("'", "\\'")

def m2s(attrs):
    if not attrs: return "{}"
    return "{" + ", ".join(f"'{esc(k)}': '{esc(v)}'" for k, v in attrs.items()) + "}"

def tid(): return uuid.uuid4().hex
def sid(): return uuid.uuid4().hex[:16]

def gen_llm(service, provider, model, op, ts, is_err):
    tr, rs, ls = tid(), sid(), sid()
    dur = random.randint(200, 5000)
    it, ot = random.randint(50, 2000), random.randint(20, 1000)
    cost = (it/1000*random.uniform(0.0005, 0.01)) + (ot/1000*random.uniform(0.0015, 0.03))
    user = random.choice(USERS)
    prompt, resp = random.choice(PROMPTS), random.choice(RESPONSES)
    ra = {"service.name": service["name"], "deployment.environment": service["env"],
          "telemetry.sdk.name": "opentelemetry", "telemetry.sdk.language": "python",
          "telemetry.sdk.version": "1.24.0", "gen_ai.application_name": service["app"],
          "gen_ai.environment": service["env"]}
    root_a = {"gen_ai.operation.name": op, "gen_ai.provider.name": provider["name"],
              "gen_ai.request.model": model, "gen_ai.user.name": user, "gen_ai.request.user": user,
              "gen_ai.conversation.id": str(uuid.uuid4())}
    llm_a = {"gen_ai.operation.name": op, "gen_ai.provider.name": provider["name"],
             "gen_ai.request.model": model, "gen_ai.response.model": model,
             "gen_ai.request.temperature": str(round(random.uniform(0.1, 1.0), 2)),
             "gen_ai.request.top_p": str(round(random.uniform(0.8, 1.0), 2)),
             "gen_ai.request.max_tokens": str(random.randint(256, 4096)),
             "gen_ai.request.is_stream": str(random.choice([True, False])).lower(),
             "gen_ai.response.id": f"chatcmpl-{uuid.uuid4().hex[:24]}",
             "gen_ai.response.finish_reasons": '["stop"]',
             "gen_ai.usage.input_tokens": str(it), "gen_ai.usage.output_tokens": str(ot),
             "gen_ai.usage.total_tokens": str(it+ot), "gen_ai.usage.cost": f"{cost:.6f}",
             "gen_ai.user.name": user, "gen_ai.request.user": user,
             "gen_ai.input.messages": json.dumps([{"role": "user", "parts": [{"type": "text", "content": prompt}]}]),
             "gen_ai.output.messages": json.dumps([{"role": "assistant", "parts": [{"type": "text", "content": resp}], "finish_reason": "stop"}]),
             "server.address": f"api.{provider['name']}.com", "server.port": "443"}
    if is_err:
        llm_a["error.type"] = "APIError"
        llm_a["gen_ai.response.finish_reasons"] = '["error"]'
    sc = "ERROR" if is_err else "Ok"
    sm = random.choice(ERRORS) if is_err else ""
    ts_s = ts.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    base = f"INSERT INTO otel_traces (Timestamp, TraceId, SpanId, ParentSpanId, TraceState, SpanName, SpanKind, ServiceName, ResourceAttributes, ScopeName, ScopeVersion, SpanAttributes, Duration, StatusCode, StatusMessage, Events.Timestamp, Events.Name, Events.Attributes, Links.TraceId, Links.SpanId, Links.TraceState, Links.Attributes) VALUES "
    r1 = f"{base}('{ts_s}', '{tr}', '{rs}', '', '', '{op} {model}', 'SERVER', '{esc(service['name'])}', {m2s(ra)}, 'openlit.instrumentation', '1.24.0', {m2s(root_a)}, {dur*1000000}, '{sc}', '{esc(sm)}', [], [], [], [], [], [], [])"
    r2 = f"{base}('{ts_s}', '{tr}', '{ls}', '{rs}', '', '{op} {model}', 'CLIENT', '{esc(service['name'])}', {m2s(ra)}, 'openlit.instrumentation', '1.24.0', {m2s(llm_a)}, {dur*1000000}, '{sc}', '{esc(sm)}', [], [], [], [], [], [], [])"
    return [r1, r2], {"trace_id": tr, "span_id": ls, "service": service["name"], "provider": provider["name"],
                      "model": model, "operation": op, "cost": cost, "input_tokens": it, "output_tokens": ot,
                      "total_tokens": it+ot, "duration_ms": dur, "user": user, "ts": ts, "is_error": is_err}

def gen_emb(service, provider, model, ts):
    tr, rs, ls = tid(), sid(), sid()
    dur = random.randint(50, 800)
    it = random.randint(100, 5000)
    ra = {"service.name": service["name"], "deployment.environment": service["env"],
          "telemetry.sdk.name": "opentelemetry", "telemetry.sdk.language": "python",
          "telemetry.sdk.version": "1.24.0", "gen_ai.application_name": service["app"],
          "gen_ai.environment": service["env"]}
    root_a = {"gen_ai.operation.name": "embeddings", "gen_ai.provider.name": provider["name"], "gen_ai.request.model": model}
    llm_a = {"gen_ai.operation.name": "embeddings", "gen_ai.provider.name": provider["name"],
             "gen_ai.request.model": model, "gen_ai.response.model": model,
             "gen_ai.usage.input_tokens": str(it), "gen_ai.usage.total_tokens": str(it),
             "gen_ai.usage.cost": f"{it/1000*0.00002:.6f}",
             "server.address": f"api.{provider['name']}.com", "server.port": "443"}
    ts_s = ts.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    base = f"INSERT INTO otel_traces (Timestamp, TraceId, SpanId, ParentSpanId, TraceState, SpanName, SpanKind, ServiceName, ResourceAttributes, ScopeName, ScopeVersion, SpanAttributes, Duration, StatusCode, StatusMessage, Events.Timestamp, Events.Name, Events.Attributes, Links.TraceId, Links.SpanId, Links.TraceState, Links.Attributes) VALUES "
    r1 = f"{base}('{ts_s}', '{tr}', '{rs}', '', '', 'embeddings {model}', 'SERVER', '{esc(service['name'])}', {m2s(ra)}, 'openlit.instrumentation', '1.24.0', {m2s(root_a)}, {dur*1000000}, 'OK', '', [], [], [], [], [], [], [])"
    r2 = f"{base}('{ts_s}', '{tr}', '{ls}', '{rs}', '', 'embeddings {model}', 'CLIENT', '{esc(service['name'])}', {m2s(ra)}, 'openlit.instrumentation', '1.24.0', {m2s(llm_a)}, {dur*1000000}, 'OK', '', [], [], [], [], [], [], [])"
    return [r1, r2], {"trace_id": tr, "span_id": ls, "service": service["name"], "provider": provider["name"],
                      "model": model, "operation": "embeddings", "cost": it/1000*0.00002, "input_tokens": it,
                      "output_tokens": 0, "total_tokens": it, "duration_ms": dur, "user": random.choice(USERS),
                      "ts": ts, "is_error": False}

def gen_vdb(service, vdb, ts):
    tr, rs, ds = tid(), sid(), sid()
    dur = random.randint(20, 500)
    ra = {"service.name": service["name"], "deployment.environment": service["env"],
          "telemetry.sdk.name": "opentelemetry", "telemetry.sdk.language": "python",
          "telemetry.sdk.version": "1.24.0", "gen_ai.application_name": service["app"],
          "gen_ai.environment": service["env"]}
    root_a = {"gen_ai.operation.name": "vectordb", "db.system": vdb["name"]}
    db_a = {"gen_ai.operation.name": "vectordb", "db.system": vdb["name"],
            "db.collection.name": vdb["collection"], "db.operation.name": "query",
            "db.query.text": "SELECT * FROM collection WHERE vector_distance < 0.5",
            "db.vector.query.top_k": str(random.randint(5, 20)),
            "server.address": f"{vdb['name']}.example.com", "server.port": "443"}
    ts_s = ts.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    base = f"INSERT INTO otel_traces (Timestamp, TraceId, SpanId, ParentSpanId, TraceState, SpanName, SpanKind, ServiceName, ResourceAttributes, ScopeName, ScopeVersion, SpanAttributes, Duration, StatusCode, StatusMessage, Events.Timestamp, Events.Name, Events.Attributes, Links.TraceId, Links.SpanId, Links.TraceState, Links.Attributes) VALUES "
    r1 = f"{base}('{ts_s}', '{tr}', '{rs}', '', '', 'vectordb query', 'SERVER', '{esc(service['name'])}', {m2s(ra)}, 'openlit.instrumentation', '1.24.0', {m2s(root_a)}, {dur*1000000}, 'OK', '', [], [], [], [], [], [], [])"
    r2 = f"{base}('{ts_s}', '{tr}', '{ds}', '{rs}', '', 'vectordb query', 'CLIENT', '{esc(service['name'])}', {m2s(ra)}, 'openlit.instrumentation', '1.24.0', {m2s(db_a)}, {dur*1000000}, 'OK', '', [], [], [], [], [], [], [])"
    return [r1, r2], {"trace_id": tr, "span_id": ds, "service": service["name"], "provider": vdb["name"],
                      "model": vdb["collection"], "operation": "vectordb", "cost": 0, "input_tokens": 0,
                      "output_tokens": 0, "total_tokens": 0, "duration_ms": dur, "user": random.choice(USERS),
                      "ts": ts, "is_error": False}

def gen_http(service, ts):
    tr, rs, hs = tid(), sid(), sid()
    dur = random.randint(10, 300)
    ep = random.choice(["/api/health", "/api/users", "/api/orders", "/api/products", "/api/search"])
    ra = {"service.name": service["name"], "deployment.environment": service["env"],
          "telemetry.sdk.name": "opentelemetry", "telemetry.sdk.language": "python",
          "telemetry.sdk.version": "1.24.0", "gen_ai.application_name": service["app"],
          "gen_ai.environment": service["env"]}
    root_a = {"http.method": "GET", "http.route": ep}
    h_a = {"http.method": "GET", "http.url": f"https://{service['name']}.example.com{ep}",
           "http.status_code": str(random.choice([200, 200, 200, 200, 201, 404, 500])),
           "http.route": ep, "server.address": f"{service['name']}.example.com", "server.port": "443"}
    ts_s = ts.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    base = f"INSERT INTO otel_traces (Timestamp, TraceId, SpanId, ParentSpanId, TraceState, SpanName, SpanKind, ServiceName, ResourceAttributes, ScopeName, ScopeVersion, SpanAttributes, Duration, StatusCode, StatusMessage, Events.Timestamp, Events.Name, Events.Attributes, Links.TraceId, Links.SpanId, Links.TraceState, Links.Attributes) VALUES "
    r1 = f"{base}('{ts_s}', '{tr}', '{rs}', '', '', 'GET {ep}', 'SERVER', '{esc(service['name'])}', {m2s(ra)}, 'openlit.instrumentation', '1.24.0', {m2s(root_a)}, {dur*1000000}, 'OK', '', [], [], [], [], [], [], [])"
    r2 = f"{base}('{ts_s}', '{tr}', '{hs}', '{rs}', '', 'GET {ep}', 'CLIENT', '{esc(service['name'])}', {m2s(ra)}, 'openlit.instrumentation', '1.24.0', {m2s(h_a)}, {dur*1000000}, 'OK', '', [], [], [], [], [], [], [])"
    return [r1, r2], {"trace_id": tr, "span_id": hs, "service": service["name"], "provider": "http",
                      "model": ep, "operation": "http", "cost": 0, "input_tokens": 0, "output_tokens": 0,
                      "total_tokens": 0, "duration_ms": dur, "user": random.choice(USERS), "ts": ts, "is_error": False}

def gen_metrics(sd, ts):
    m = []
    ra = {"service.name": sd["service"], "deployment.environment": "production",
          "telemetry.sdk.name": "opentelemetry", "telemetry.sdk.language": "python", "telemetry.sdk.version": "1.24.0"}
    base_a = {"telemetry.sdk.name": "opentelemetry", "service.name": sd["service"],
              "deployment.environment": "production", "gen_ai.provider.name": sd["provider"],
              "gen_ai.request.model": sd["model"], "gen_ai.operation.name": sd["operation"]}
    ts_s = ts.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    st = (ts - timedelta(milliseconds=sd["duration_ms"])).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    ins = f"INSERT INTO otel_metrics_sum (ResourceAttributes, ResourceSchemaUrl, ScopeName, ScopeVersion, ScopeAttributes, ScopeDroppedAttrCount, ScopeSchemaUrl, ServiceName, MetricName, MetricDescription, MetricUnit, Attributes, StartTimeUnix, TimeUnix, Value, Flags, Exemplars.FilteredAttributes, Exemplars.TimeUnix, Exemplars.Value, Exemplars.SpanId, Exemplars.TraceId, AggregationTemporality, IsMonotonic) VALUES "
    if sd["total_tokens"] > 0:
        for tt, cnt in [("input", sd["input_tokens"]), ("output", sd["output_tokens"])]:
            a = {**base_a, "gen_ai.token.type": tt}
            m.append(f"{ins}({m2s(ra)}, '', 'openlit.instrumentation', '1.24.0', {{}}, 0, '', '{esc(sd['service'])}', 'gen_ai.client.token.usage', 'Number of tokens used', '{{token}}', {m2s(a)}, '{st}', '{ts_s}', {cnt}, 0, [], [], [], [], [], 2, true)")
    m.append(f"{ins}({m2s(ra)}, '', 'openlit.instrumentation', '1.24.0', {{}}, 0, '', '{esc(sd['service'])}', 'gen_ai.client.operation.duration', 'Duration of the operation', 's', {m2s(base_a)}, '{st}', '{ts_s}', {sd['duration_ms']/1000}, 0, [], [], [], [], [], 2, false)")
    if sd["cost"] > 0:
        m.append(f"{ins}({m2s(ra)}, '', 'openlit.instrumentation', '1.24.0', {{}}, 0, '', '{esc(sd['service'])}', 'gen_ai.usage.cost', 'Cost in USD', 'USD', {m2s(base_a)}, '{st}', '{ts_s}', {sd['cost']}, 0, [], [], [], [], [], 2, false)")
    return m

def gen_logs(sd, ts):
    ra = {"service.name": sd["service"], "deployment.environment": "production",
          "telemetry.sdk.name": "opentelemetry", "telemetry.sdk.language": "python", "telemetry.sdk.version": "1.24.0"}
    la = {"gen_ai.provider.name": sd["provider"], "gen_ai.request.model": sd["model"], "gen_ai.operation.name": sd["operation"]}
    ts_s = ts.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    sev, num = ("ERROR", 17) if sd["is_error"] else ("INFO", 9)
    body = random.choice(ERRORS) if sd["is_error"] else f"Completed {sd['operation']} request to {sd['provider']} in {sd['duration_ms']}ms"
    return [f"INSERT INTO otel_logs (Timestamp, TimestampTime, TraceId, SpanId, TraceFlags, SeverityText, SeverityNumber, ServiceName, Body, ResourceSchemaUrl, ResourceAttributes, ScopeSchemaUrl, ScopeName, ScopeVersion, ScopeAttributes, LogAttributes) VALUES ('{ts_s}', toDateTime('{ts_s}'), '{sd['trace_id']}', '{sd['span_id']}', 1, '{sev}', {num}, '{esc(sd['service'])}', '{esc(body)}', '', {m2s(ra)}, '', 'openlit.instrumentation', '1.24.0', {{}}, {m2s(la)})"]

def main():
    print("=" * 50)
    print("Generating demo telemetry data for Veritas AI")
    print("=" * 50)
    now = datetime.now(timezone.utc)
    traces, metrics, logs = [], [], []
    N = 2000
    print(f"Generating {N} traces...")
    for i in range(N):
        ts = now - timedelta(hours=random.uniform(0, 7*24))
        svc = random.choice(SERVICES)
        t = random.choices(["llm", "emb", "vdb", "http"], [0.70, 0.15, 0.10, 0.05])[0]
        is_err = random.random() < 0.08
        if t == "llm":
            p = random.choice(PROVIDERS)
            sqls, sd = gen_llm(svc, p, random.choice(p["models"]), random.choice(["chat", "text_completion"]), ts, is_err)
        elif t == "emb":
            p = random.choice(PROVIDERS[:2])
            sqls, sd = gen_emb(svc, p, random.choice(p["models"]), ts)
        elif t == "vdb":
            sqls, sd = gen_vdb(svc, random.choice(VECTOR_DBS), ts)
        else:
            sqls, sd = gen_http(svc, ts)
        traces.extend(sqls)
        if t in ["llm", "emb"]:
            metrics.extend(gen_metrics(sd, ts))
        if random.random() < 0.3:
            logs.extend(gen_logs(sd, ts))
        if (i+1) % 500 == 0:
            print(f"  {i+1}/{N}")
    print(f"Generated {len(traces)} spans, {len(metrics)} metrics, {len(logs)} logs")
    print("Inserting into ClickHouse...")
    for name, data in [("traces", traces), ("metrics", metrics), ("logs", logs)]:
        ok = 0
        # Group statements by their INSERT prefix (same table/columns)
        groups = {}
        for stmt in data:
            # Extract the VALUES part - everything after "VALUES "
            idx = stmt.find("VALUES ")
            if idx == -1:
                continue
            prefix = stmt[:idx + 7]
            values = stmt[idx + 7:]
            groups.setdefault(prefix, []).append(values)
        for prefix, values_list in groups.items():
            # Batch 100 values per INSERT
            for j in range(0, len(values_list), 100):
                batch = values_list[j:j+100]
                r = ch(prefix + ", ".join(batch))
                if not r or "Exception" not in r:
                    ok += len(batch)
        print(f"  {name}: {ok}/{len(data)} inserted")
    print("\nVerification:")
    for q, label in [("SELECT count() FROM otel_traces", "Traces"),
                     ("SELECT count() FROM otel_metrics_sum", "Metrics"),
                     ("SELECT count() FROM otel_logs", "Logs")]:
        print(f"  {label}: {ch(q).strip()}")
    print("\nServices:")
    print(ch("SELECT ServiceName, count() FROM otel_traces GROUP BY ServiceName ORDER BY count() DESC"))
    print("\nProviders:")
    print(ch("SELECT SpanAttributes['gen_ai.provider.name'] p, count() FROM otel_traces WHERE SpanAttributes['gen_ai.provider.name'] != '' GROUP BY p ORDER BY count() DESC"))
    print("\nModels:")
    print(ch("SELECT SpanAttributes['gen_ai.request.model'] m, count() FROM otel_traces WHERE SpanAttributes['gen_ai.request.model'] != '' GROUP BY m ORDER BY count() DESC LIMIT 10"))
    print("\n✅ Demo data generation complete!")

if __name__ == "__main__":
    main()