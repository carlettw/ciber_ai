<<<<<<< HEAD
import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";
import { useState } from "react";
=======
import { useState } from "react"
>>>>>>> 0e93f95 (update)

const data = [
  { name: "Mon", risk: 2 },
  { name: "Tue", risk: 5 },
  { name: "Wed", risk: 3 },
  { name: "Thu", risk: 6 },
  { name: "Fri", risk: 4 },
];

const scanSite = async () => {
  if (!url) return alert("URL kiriting");

  setLoading(true);
  try {
    const res = await fetch("http://127.0.0.1:8000/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url }),
    });
    const data = await res.json();
    setResult(data);
  } catch (e) {
    alert("Backend bilan aloqa yo‘q");
  }
  setLoading(false);
};

export default function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="min-h-screen flex bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-slate-900 text-white p-6">
        <h1 className="text-2xl font-bold mb-10">Cyber MVP</h1>
        <nav className="space-y-4">
          <p>📊 Dashboard</p>
          <p>🔍 Scans</p>
          <p>📁 Reports</p>
          <p>🤖 AI Analysis</p>
          <p>⚙️ Settings</p>
        </nav>
      </aside>

      {/* Main */}
      <main className="flex-1 p-8">
        <h2 className="text-3xl font-semibold mb-6">Dashboard</h2>

        {/* Stats cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white rounded-xl p-6 shadow">
            <p className="text-gray-500">Total Scans</p>
            <h3 className="text-4xl font-bold">24</h3>
          </div>

          <div className="bg-white rounded-xl p-6 shadow">
            <p className="text-gray-500">High Risk</p>
            <h3 className="text-4xl font-bold text-red-500">5</h3>
          </div>

          <div className="bg-white rounded-xl p-6 shadow">
            <p className="text-gray-500">Safe</p>
            <h3 className="text-4xl font-bold text-green-500">19</h3>
          </div>
        </div>

        {/* Chart — 4-qadam */}
        <div className="mt-10 bg-white p-6 rounded-xl shadow">
          <h3 className="text-xl font-semibold mb-4">Risk Trend</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={data}>
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Line
                  type="monotone"
                  dataKey="risk"
                  stroke="#ef4444"
                  strokeWidth={3}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </main>
    </div>
  );
}
