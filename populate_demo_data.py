#!/usr/bin/env python3
"""
Enhanced demo data generation script for OpenLIT.

This script generates a comprehensive set of telemetry data (traces, metrics, logs)
and populates application-level entities like Prompts and API Keys via API calls
to make the OpenLIT UI appear as a realistic, production-like system.
"""

import json
import random
import uuid
import time
import requests
from datetime import datetime, timedelta, timezone
from faker import Faker

# --- Configuration ---
CLICKHOUSE_URL = "http://localhost:8123"
CLICKHOUSE_USER = "default"
CLICKHOUSE_PASS = "OPENLIT"
CLICKHOUSE_DB = "openlit"

OPENLIT_API_URL = "http://localhost:3000"
OPENLIT_USER = "user@openlit.io"
OPENLIT_PASSWORD = "openlituser"

# --- Constants for Data Generation ---
SERVICES = [
    {"name": "chatbot-api", "env": "production", "app": "Customer Support Bot"},
    {"name": "rag-service", "env": "production", "app": "Knowledge Assistant"},
    {"name": "code-assistant", "env": "staging", "app": "Code Review Copilot"},
    {"name": "content-generator", "env": "production", "app": "Content Studio"},
    {"name": "analytics-agent", "env": "development", "app": "Data Insights Agent"},
    {"name": "summary-service", "env": "production", "app": "DocuSummarize"},
    {"name": "image-gen-api", "env": "staging", "app": "Artify"},
]

PROVIDERS = [
    {"name": "openai", "models": ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo", "dall-e-3", "text-embedding-3-small"]},
    {"name": "anthropic", "models": ["claude-3-5-sonnet", "claude-3-opus", "claude-3-haiku"]},
    {"name": "cohere", "models": ["command-r-plus", "command-r", "embed-english-v3.0"]},
    {"name": "mistral", "models": ["mistral-large-latest", "mistral-small-latest"]},
    {"name": "google", "models": ["gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.0-pro"]},
    {"name": "groq", "models": ["llama3-70b-8192", "gemma-7b-it"]},
    {"name": "ollama", "models": ["llama3", "phi3"]},
]

VECTOR_DBS = [
    {"name": "pinecone", "collection": "docs-index"},
    {"name": "chromadb", "collection": "knowledge-base"},
    {"name": "qdrant", "collection": "product-catalog"},
    {"name": "weaviate", "collection": "user-profiles"},
]

# Generate 100 fake users
fake = Faker()
USERS = [fake.email() for _ in range(100)]
USER_AGENTS = [fake.user_agent() for _ in range(20)]

PROMPTS = [
    "What are the benefits of using our platform?",
    "Can you summarize the latest quarterly report?",
    "Write a product description for our new AI tool, focusing on its collaborative features.",
    "Explain the difference between RAG and fine-tuning in simple terms.",
    "Help me debug this Python error: 'IndexError: list index out of range'",
    "Generate a marketing email for a new feature launch that improves performance by 50%.",
    "What's the best way to optimize our LLM costs without sacrificing quality?",
    "Create a SQL query to find top 10 most active users in the last 30 days.",
    "Translate this sentence to Spanish: 'Our new AI-powered analytics will revolutionize your workflow.'",
    "Analyze the sentiment of the following customer review: 'The new interface is a bit confusing, but the features are incredibly powerful.'",
    "Write a unit test for a function that calculates the factorial of a number.",
    "Suggest three key improvements for our current user onboarding flow.",
    "What are the most critical security best practices for handling API keys in a production environment?",
    "Compare the performance and cost of 'text-embedding-3-small' vs 'embed-english-v3.0' for document classification.",
    "Draft a polite and helpful response to this customer complaint: 'Your app crashed twice today and I lost my work.'",
    "Create a detailed, imaginative description of a futuristic city powered by sustainable energy.",
    "Write a short, suspenseful story that starts with the line: 'The old lighthouse keeper found a message in a bottle, but it was written in a language no one had ever seen.'",
]

RESPONSES = [
    "Our platform enhances efficiency by 40%, significantly cuts down operational costs, and boosts user satisfaction through intuitive design.",
    "The latest quarterly report highlights a 32% surge in active users and a 45% month-over-month increase in token consumption.",
    "Discover a new era of teamwork with our AI tool, featuring real-time collaborative spaces and intelligent suggestion merging.",
    "In short: RAG is like giving a model an open book for answers, while fine-tuning is like teaching the model a new skill.",
    "Your 'IndexError' likely means you're trying to access an item in a list that doesn't exist. Check your loop boundaries or if the list is empty.",
    "Subject: Supercharge Your Workflow! Experience a 50% performance boost with our latest update.",
    "To optimize LLM costs, consider: 1) Caching frequent queries, 2) Using smaller, specialized models, 3) Setting strict token limits, and 4) Batching requests.",
    "SELECT user_id, COUNT(action_id) as activity_count FROM user_logs WHERE timestamp >= NOW() - INTERVAL '30 days' GROUP BY user_id ORDER BY activity_count DESC LIMIT 10;",
    "En español: 'Nuestras nuevas analíticas impulsadas por IA revolucionarán su flujo de trabajo.'",
    "The sentiment of the review is mixed. The user expresses frustration with the UI ('confusing') but admiration for the functionality ('incredibly powerful').",
    "```python
import unittest
class TestFactorial(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(factorial(5), 120)
    def test_zero(self):
        self.assertEqual(factorial(0), 1)
```",
    "For onboarding, I suggest: 1) An interactive product tour, 2) Pre-populating with sample data, and 3) A checklist of 'first steps' to guide users.",
    "Critical API key security: 1) Never commit keys to Git, 2) Use a secrets management service like Vault, 3) Implement key rotation policies, and 4) Restrict key permissions.",
    "'text-embedding-3-small' is generally more cost-effective for broad use cases, while 'embed-english-v3.0' might offer higher accuracy for nuanced semantic search.",
    "We are so sorry to hear about the trouble you've experienced. Our engineering team is investigating the crash reports urgently. As a priority, we are working on improving our auto-save functionality to prevent data loss.",
    "The city of Aethelburg glistened, its spires of living crystal pulsing with a soft, internal light drawn from the geothermal heart of the planet. Sky-rails, silent and swift, weaved between towers draped in bio-luminescent flora...",
    "The old lighthouse keeper, Silas, uncorked the bottle. The script on the parchment was unlike any he knew—not of sailors or scholars, but of something far older, something that whispered of tides between stars.",
]

ERRORS = [
    "Rate limit exceeded for model gpt-4o",
    "Connection timeout to api.openai.com",
    "Invalid API key provided",
    "Model not found: gpt-5",
    "Context length exceeded (max 128000 tokens)",
    "Provider returned 503 Service Unavailable",
    "Authentication error: Incorrect API key or organization ID.",
    "The model is currently overloaded with other requests. Please try again later.",
]

# --- ClickHouse Client ---

def ch_client(query):
    """Sends a query to the ClickHouse database."""
    try:
        response = requests.post(
            CLICKHOUSE_URL,
            params={
                "database": CLICKHOUSE_DB,
                "query": query
            },
            auth=(CLICKHOUSE_USER, CLICKHOUSE_PASS)
        )
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"ClickHouse Error: {e}")
        if e.response:
            print(f"Response Body: {e.response.text[:500]}")
        return ""

def escape_ch_string(s):
    """Escapes a string for ClickHouse insertion."""
    return str(s).replace("", "").replace("'", "'")

def dict_to_ch_map(attrs):
    """Converts a Python dictionary to a ClickHouse Map string."""
    if not attrs:
        return "{}"
    return "{" + ", ".join(f"'{escape_ch_string(k)}': '{escape_ch_string(v)}'" for k, v in attrs.items()) + "}"

# --- Telemetry Generation Functions (Adapted) ---

def generate_trace_and_span_ids():
    return uuid.uuid4().hex, uuid.uuid4().hex[:16]

def gen_llm_trace(service, provider, model, operation, timestamp, is_error):
    trace_id, root_span_id, llm_span_id = generate_trace_and_span_ids() + (uuid.uuid4().hex[:16],)
    duration_ms = random.randint(200, 5000)
    input_tokens, output_tokens = random.randint(50, 2000), random.randint(20, 1000)
    cost = (input_tokens / 1000 * random.uniform(0.0005, 0.01)) + (output_tokens / 1000 * random.uniform(0.0015, 0.03))
    user_email = random.choice(USERS)
    prompt, response = random.choice(PROMPTS), random.choice(RESPONSES)

    resource_attrs = {
        "service.name": service["name"],
        "deployment.environment": service["env"],
        "telemetry.sdk.language": "python",
        "gen_ai.application_name": service["app"],
    }
    
    root_span_attrs = {
        "gen_ai.operation.name": operation,
        "gen_ai.provider.name": provider["name"],
        "gen_ai.request.model": model,
        "gen_ai.user.name": user_email,
        "http.user_agent": random.choice(USER_AGENTS),
    }

    llm_span_attrs = root_span_attrs.copy()
    llm_span_attrs.update({
        "gen_ai.response.model": model,
        "gen_ai.request.temperature": round(random.uniform(0.1, 1.0), 2),
        "gen_ai.request.max_tokens": random.randint(256, 4096),
        "gen_ai.usage.input_tokens": input_tokens,
        "gen_ai.usage.output_tokens": output_tokens,
        "gen_ai.usage.total_tokens": input_tokens + output_tokens,
        "gen_ai.usage.cost": f"{cost:.6f}",
        "gen_ai.input.messages": json.dumps([{"role": "user", "content": prompt}]),
        "gen_ai.output.messages": json.dumps([{"role": "assistant", "content": response}]),
        "server.address": f"api.{provider['name']}.com",
    })

    status_code, status_message = ("ERROR", random.choice(ERRORS)) if is_error else ("Ok", "")
    if is_error:
        llm_span_attrs["error.type"] = "APIError"
        llm_span_attrs["gen_ai.response.finish_reasons"] = '["error"]'

    ts_str = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    base_insert = "INSERT INTO otel_traces (Timestamp, TraceId, SpanId, ParentSpanId, SpanName, SpanKind, ServiceName, ResourceAttributes, SpanAttributes, Duration, StatusCode, StatusMessage) VALUES "
    
    root_span_sql = f"('{ts_str}', '{trace_id}', '{root_span_id}', '', '{operation} {model}', 'SERVER', '{service['name']}', {dict_to_ch_map(resource_attrs)}, {dict_to_ch_map(root_span_attrs)}, {duration_ms * 1000000}, '{status_code}', '{escape_ch_string(status_message)}')"
    llm_span_sql = f"('{ts_str}', '{trace_id}', '{llm_span_id}', '{root_span_id}', '{operation} {model}', 'CLIENT', '{service['name']}', {dict_to_ch_map(resource_attrs)}, {dict_to_ch_map(llm_span_attrs)}, {duration_ms * 1000000}, '{status_code}', '{escape_ch_string(status_message)}')"

    span_data = {
        "trace_id": trace_id, "span_id": llm_span_id, "service": service["name"],
        "provider": provider["name"], "model": model, "operation": operation, "cost": cost,
        "duration_ms": duration_ms, "is_error": is_error, "timestamp": timestamp
    }
    return [base_insert + root_span_sql, base_insert + llm_span_sql], span_data

# --- Main Execution ---

def generate_telemetry_data(num_traces=2500):
    """Generates and inserts a batch of telemetry data."""
    print(f"Generating {num_traces} traces...")
    now = datetime.now(timezone.utc)
    all_traces_sql = []
    all_metrics_sql = []
    all_logs_sql = []

    for i in range(num_traces):
        timestamp = now - timedelta(hours=random.uniform(0, 30 * 24)) # Data for last 30 days
        service = random.choice(SERVICES)
        is_error = random.random() < 0.08

        # For now, we only generate LLM traces as they are the most complex
        provider = random.choice(PROVIDERS)
        model = random.choice(provider["models"])
        operation = random.choice(["chat", "text_completion"])

        traces_sql, span_data = gen_llm_trace(service, provider, model, operation, timestamp, is_error)
        all_traces_sql.extend(traces_sql)

        # Simple metric and log generation for now
        # In a real scenario, these would be more detailed
        if random.random() < 0.5:
             all_logs_sql.append(f"INSERT INTO otel_logs (Timestamp, TraceId, SpanId, SeverityText, Body, ResourceAttributes) VALUES ('{timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}', '{span_data['trace_id']}', '{span_data['span_id']}', '{'ERROR' if is_error else 'INFO'}', '{'An error occurred' if is_error else 'Operation successful'}', {dict_to_ch_map({'service.name': service['name']})})")

        if (i + 1) % 500 == 0:
            print(f"  {i + 1}/{num_traces} generated...")
            
    print(f"Generated {len(all_traces_sql)} spans and {len(all_logs_sql)} logs.")
    print("Inserting into ClickHouse...")

    # Batch insert traces
    if all_traces_sql:
        ch_client(", ".join(all_traces_sql))
    
    # Batch insert logs
    if all_logs_sql:
        log_base_insert = "INSERT INTO otel_logs (Timestamp, TraceId, SpanId, SeverityText, Body, ResourceAttributes) VALUES "
        log_values = [sql.split("VALUES ")[1] for sql in all_logs_sql]
        ch_client(log_base_insert + ", ".join(log_values))
        
    print("Telemetry data insertion complete.")


def main():
    """Main function to orchestrate data generation."""
    print("=" * 50)
    print("Starting OpenLIT Demo Data Population")
    print("=" * 50)

    # Step 1: Generate and insert telemetry data
    generate_telemetry_data(num_traces=5000)

    # Step 2: Populate application entities via API
    populate_app_entities()

    print("\n" + "=" * 50)
    print("✅ Demo data population script finished.")
    print("Check out the dashboard at http://localhost:3000")
    print("=" * 50)

# --- Application-Level Population Functions ---

class ApiClient:
    """A simple client to interact with the OpenLIT API."""
    def __init__(self, base_url, email, password):
        self.base_url = base_url
        self.session = requests.Session()
        self.login(email, password)

    def login(self, email, password):
        """Logs in to the application to get a session cookie."""
        print("Attempting to log in to OpenLIT API...")
        try:
            # The actual login flow for next-auth involves getting a CSRF token first
            csrf_url = f"{self.base_url}/api/auth/csrf"
            csrf_token = self.session.get(csrf_url, timeout=10).json().get("csrfToken")

            login_url = f"{self.base_url}/api/auth/callback/credentials"
            res = self.session.post(
                login_url,
                data={
                    "email": email,
                    "password": password,
                    "csrfToken": csrf_token,
                    "json": "true",
                },
                timeout=10
            )
            res.raise_for_status()
            if "api/auth/error" in res.url:
                raise Exception("Login failed, check credentials.")
            print("Login successful.")
        except requests.exceptions.RequestException as e:
            print(f"API login failed: {e}. Skipping application data population.")
            self.session = None

    def post(self, endpoint, data):
        """Sends a POST request to a given endpoint."""
        if not self.session:
            return None
        try:
            response = self.session.post(f"{self.base_url}{endpoint}", json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API POST to {endpoint} failed: {e}")
            if e.response:
                print(f"Response: {e.response.text}")
            return None

def populate_prompt_hub(client, num_prompts=20):
    """Creates a set of sample prompts in the Prompt Hub."""
    print(f"\nPopulating Prompt Hub with {num_prompts} prompts...")
    prompt_names = ["customer-support-agent", "summarizer", "code-generator", "marketing-copywriter", "sql-expert"]
    for i in range(num_prompts):
        name = f"{random.choice(prompt_names)}-{i+1}"
        prompt_content = random.choice(PROMPTS) + "\n\nUser query: {{query}}"
        tags = [name.split('-')[0], random.choice(["v1", "v2"]), random.choice(["production", "staging"])]

        payload = {
            "name": name,
            "prompt": prompt_content,
            "version": "1.0.0",
            "tags": tags,
            "status": "published",
            "metaProperties": {"author": fake.name()}
        }
        if client.post("/api/prompt", payload):
            print(f"  Created prompt: {name}")
        time.sleep(0.1) # Avoid overwhelming the server

def populate_api_keys(client, num_keys=5):
    """Generates a few named API keys."""
    print(f"\nGenerating {num_keys} API keys...")
    key_names = ["sdk-prod-key", "sdk-staging-key", "data-science-key", "dev-test-key", "ci-cd-key"]
    for i in range(num_keys):
        name = key_names[i]
        payload = {"name": name}
        response = client.post("/api/api-key", payload)
        if response and response.get("apiKey"):
            print(f"  Generated API key named '{name}': {response['apiKey'][:12]}...")
        time.sleep(0.1)

def run_evaluations(client, num_evals=15):
    """Runs several offline evaluations."""
    print(f"\nRunning {num_evals} offline evaluations...")
    eval_types = ["toxicity", "pii", "hallucination", "bias"]
    for _ in range(num_evals):
        prompt = random.choice(PROMPTS)
        response = random.choice(RESPONSES)
        # Occasionally submit problematic data
        if random.random() < 0.2:
            prompt = "My social security number is 123-456-7890, can you verify it?"

        payload = {
            "prompt": prompt,
            "response": response,
            "eval_types": random.sample(eval_types, k=random.randint(1, 3)),
            "metadata": {"source": "demo_script"}
        }
        if client.post("/api/evaluation/offline", payload):
            print(f"  Submitted evaluation for types: {payload['eval_types']}")
        time.sleep(0.2)

def populate_app_entities():
    """Wrapper function to populate all application-level entities."""
    api_client = ApiClient(OPENLIT_API_URL, OPENLIT_USER, OPENLIT_PASSWORD)
    if not api_client.session:
        return

    populate_prompt_hub(api_client)
    populate_api_keys(api_client)
    run_evaluations(api_client)


if __name__ == "__main__":
    main()
    main()
