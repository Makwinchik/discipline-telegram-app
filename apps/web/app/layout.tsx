import './globals.css';
import { Sidebar } from '@/components/sidebar';
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body><Sidebar /><main className="min-h-screen p-4 lg:pl-80">{children}</main></body></html>; }
