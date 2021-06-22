import { serve } from "https://deno.land/std/http/mod.ts";

const server = serve({ port: 8888 });
console.log("Counter server is up!");
console.log("Waiting on new request...");
console.log("");

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

for await (const req of server) {

  console.log("Received a thing (sleep)")
  await sleep(10000);
  await req.respond({
    status: 200,
  });
  console.log("done")
  // console.log(Deno.readAll(req.body))
}
