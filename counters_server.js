import { serve } from "https://deno.land/std/http/mod.ts";

const server = serve({ port: 8888 });
console.log("Counter server is up!");
console.log("Waiting on new request...");
for await (const req of server) {
  await req.respond({
    status: 200,
  });
}
