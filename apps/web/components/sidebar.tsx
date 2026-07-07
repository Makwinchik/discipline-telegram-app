import Link from 'next/link';
const items = ['Dashboard', 'Videos', 'Generated Clips', 'Editor', 'Exports', 'Billing', 'Settings'];
const href: Record<string, string> = { Dashboard: '/dashboard', Videos: '/videos', 'Generated Clips': '/clips', Editor: '/editor', Exports: '/exports', Billing: '/billing', Settings: '/settings' };
export function Sidebar() {
  return <aside className="glass fixed inset-y-4 left-4 hidden w-64 rounded-3xl p-4 lg:block"><div className="mb-8 text-xl font-bold">ClipForge AI</div><nav className="space-y-2">{items.map((item) => <Link key={item} href={href[item]} className="block rounded-2xl px-4 py-3 text-sm text-white/70 transition hover:bg-white/10 hover:text-white">{item}</Link>)}</nav></aside>;
}
