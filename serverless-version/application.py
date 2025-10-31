import json, os, uuid, boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

CORS_HEADERS = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type,Authorization",
    "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS",
}

def _resp(code, body):
    return {"statusCode": code, "headers": CORS_HEADERS, "body": json.dumps(body)}

def handler(event, context):
    method = event.get("httpMethod")
    resource = event.get("resource")        # e.g., "/todos" or "/todos/{id}"
    path = event.get("path", "")            # fallback
    body = event.get("body")

    # CORS preflight
    if method == "OPTIONS":
        return _resp(200, {"ok": True})

    # ---- LIST ----
    if method == "GET" and (resource == "/todos" or path.endswith("/todos")):
        items = table.scan().get("Items", [])
        return _resp(200, {"todos": items})

    # ---- CREATE ----
    if method == "POST" and (resource == "/todos" or path.endswith("/todos")):
        try:
            data = json.loads(body or "{}")
        except Exception as e:
            return _resp(400, {"error": "invalid_json", "detail": str(e)})
        task = data.get("task")
        if not task:
            return _resp(400, {"error": "task is required"})
        item = {
            "id": str(uuid.uuid4()),
            "task": task,
            "created_at": datetime.utcnow().isoformat()
        }
        table.put_item(Item=item)
        return _resp(201, item)

    # ---- DELETE ----
    if method == "DELETE" and (resource == "/todos/{id}" or "/todos/" in path):
        todo_id = (event.get("pathParameters") or {}).get("id")
        # Fallback if API didn’t pass pathParameters for some reason
        if not todo_id and path:
            # path looks like ".../dev/todos/<id>"
            parts = path.rstrip("/").split("/")
            if len(parts) >= 1:
                todo_id = parts[-1]
        if not todo_id or todo_id.lower() == "todos":
            return _resp(400, {"error": "id is required"})
        table.delete_item(Key={"id": todo_id})
        return _resp(200, {"deleted": todo_id})

    return _resp(404, {"error": "not found"})

