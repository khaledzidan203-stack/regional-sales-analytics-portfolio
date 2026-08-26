import { cp, mkdir } from 'node:fs/promises';
await mkdir('app', { recursive: true });
await cp('src/index.html', 'app/index.html');
await cp('data', 'app/data', { recursive: true });
console.log('Prepared portfolio dashboard for desktop packaging.');
