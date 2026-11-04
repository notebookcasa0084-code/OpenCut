import { Elysia, t } from "elysia";
import { CloudflareAdapter } from "elysia/adapter/cloudflare-worker";

export default new Elysia({ adapter: CloudflareAdapter })
  .get("/", () => ({ status: "ok" }))
  .post("/", (context: { body: any }) => context.body, {
    body: t.Object({
      name: t.String(),
    }),
  })
  .compile();
