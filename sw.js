const CACHE_NAME = 'abigail-portfolio-v11';
const PRECACHE_ASSETS = [
  './',
  './index.html',
  './site.webmanifest',
  './favicon.ico',
  './favicon.png',
  './apple-touch-icon.png',
  './stickers/gilbert_icon_tight.png',
  './stickers/gilbert_sticker.png',
  './stickers/ladybug_cursor_48.png',
  './stickers/canva_cake.png',
  './stickers/canva_gecko.png',
  './stickers/canva_star_left.png',
  './stickers/canva_shoes.png',
  './stickers/canva_hand_eyes.png',
  './stickers/canva_star.png',
  './stickers/canva_camera.png',
  './stickers/canva_match.png',
  './stickers/canva_abi.png',
  './stickers/canva_gilbert_full.png',
  './stickers/canva_polaroid_couch.png',
  './stickers/sb_wizard_cat.png',
  './stickers/sb_miffy_book.png',
  './stickers/sb_clay_star.png',
  './stickers/sb_star_ladybug.png',
  './stickers/sb_pink_butterfly.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  // Network-first for HTML navigation so live updates show up immediately
  if (event.request.mode === 'navigate' || event.request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      fetch(event.request).then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const copy = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
        }
        return networkResponse;
      }).catch(() => caches.match(event.request).then((r) => r || caches.match('./index.html')))
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        fetch(event.request).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, networkResponse.clone());
            });
          }
        }).catch(() => {});
        return cachedResponse;
      }

      return fetch(event.request).then((networkResponse) => {
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
          return networkResponse;
        }

        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseToCache);
        });

        return networkResponse;
      });
    })
  );
});
