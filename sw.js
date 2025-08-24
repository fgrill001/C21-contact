
const CACHE_NAME="c21-card-cache-final";
const URLS=["./","./index.html","./manifest.webmanifest",
"./icon-192.png","./icon-512.png","./icon-apple.png",
"./fredrik-grill.vcf","./fredrik-card.pdf"];
self.addEventListener("install",e=>e.waitUntil(caches.open(CACHE_NAME).then(c=>c.addAll(URLS))));
self.addEventListener("activate",e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE_NAME).map(k=>caches.delete(k))))));
self.addEventListener("fetch",e=>e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request))));
