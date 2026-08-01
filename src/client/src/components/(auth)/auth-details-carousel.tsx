import Image from "next/image";
import getMessage from "@/constants/messages";
import {
	BarChart3,
	BrainCircuit,
	FlaskConical,
	GitCompare,
	Lock,
	MessageSquareText,
	Search,
	Shield,
	Sparkles,
	Zap,
} from "lucide-react";

const featureIcons = [Search, BarChart3, Shield, BrainCircuit, GitCompare, MessageSquareText, FlaskConical, Lock, Zap, Sparkles];

const featureKeys: Array<{ title: keyof ReturnType<typeof getMessage>; desc: keyof ReturnType<typeof getMessage> }> = [
	{ title: "AUTH_FEATURE_TRACING", desc: "AUTH_FEATURE_TRACING_DESC" },
	{ title: "AUTH_FEATURE_ANALYTICS", desc: "AUTH_FEATURE_ANALYTICS_DESC" },
	{ title: "AUTH_FEATURE_EVALS", desc: "AUTH_FEATURE_EVALS_DESC" },
	{ title: "AUTH_FEATURE_JUDGE", desc: "AUTH_FEATURE_JUDGE_DESC" },
	{ title: "AUTH_FEATURE_OPENGROUND", desc: "AUTH_FEATURE_OPENGROUND_DESC" },
	{ title: "AUTH_FEATURE_PROMPT_HUB", desc: "AUTH_FEATURE_PROMPT_HUB_DESC" },
	{ title: "AUTH_FEATURE_RULE_ENGINE", desc: "AUTH_FEATURE_RULE_ENGINE_DESC" },
	{ title: "AUTH_FEATURE_VAULT", desc: "AUTH_FEATURE_VAULT_DESC" },
	{ title: "AUTH_FEATURE_AGENTS", desc: "AUTH_FEATURE_AGENTS_DESC" },
	{ title: "AUTH_FEATURE_OTEL", desc: "AUTH_FEATURE_OTEL_DESC" },
];

export default function AuthDetailsCarousel() {
	const messages = getMessage();
	return (
		<div className="relative hidden lg:flex flex-col justify-between overflow-hidden p-10 bg-gradient-to-br from-violet-600 via-purple-600 to-indigo-700">
			<div className="absolute inset-0 opacity-20">
				<div className="absolute top-10 left-10 w-72 h-72 bg-fuchsia-400 rounded-full mix-blend-multiply filter blur-3xl animate-pulse"></div>
				<div className="absolute top-1/2 -right-20 w-96 h-96 bg-cyan-400 rounded-full mix-blend-multiply filter blur-3xl animate-pulse" style={{ animationDelay: "1s" }}></div>
				<div className="absolute -bottom-20 left-1/3 w-80 h-80 bg-pink-400 rounded-full mix-blend-multiply filter blur-3xl animate-pulse" style={{ animationDelay: "2s" }}></div>
			</div>

			<div className="relative z-10 flex items-center gap-3">
				<div className="w-12 h-12 rounded-xl bg-white/15 backdrop-blur-sm flex items-center justify-center border border-white/20">
					<BrainCircuit className="h-7 w-7 text-white" />
				</div>
				<div className="flex flex-col">
					<span className="text-xl font-bold text-white tracking-tight">
						Veritas AI
					</span>
					<span className="text-xs text-white/70">
						AI Insights Platform
					</span>
				</div>
			</div>

			<div className="relative z-10 flex-1 flex items-center justify-center py-8">
				<div className="grid grid-cols-2 gap-3 max-w-lg w-full">
					{featureKeys.map((feature, i) => {
						const Icon = featureIcons[i];
						return (
							<div
								key={feature.title}
								className="flex items-start gap-3 p-4 rounded-2xl bg-white/10 backdrop-blur-md border border-white/15 hover:bg-white/15 transition-all duration-300 hover:scale-[1.02] hover:-translate-y-0.5"
							>
								<div className="shrink-0 mt-0.5 p-2 rounded-xl bg-white/20">
									<Icon className="h-4 w-4 text-white" strokeWidth={2.25} />
								</div>
								<div className="min-w-0">
									<p className="text-sm font-semibold text-white leading-tight">
										{messages[feature.title] as string}
									</p>
									<p className="text-xs text-white/70 mt-1 leading-snug">
										{messages[feature.desc] as string}
									</p>
								</div>
							</div>
						);
					})}
				</div>
			</div>

			<div className="relative z-10">
				<div className="flex items-center justify-center gap-4 mb-4">
					<div className="flex -space-x-2">
						{[0, 1, 2, 3].map((i) => (
							<div key={i} className="w-8 h-8 rounded-full bg-white/20 border-2 border-white/30 flex items-center justify-center">
								<span className="text-[10px] font-semibold text-white">{["AI", "ML", "DX", "OP"][i]}</span>
							</div>
						))}
					</div>
					<span className="text-xs text-white/80">Trusted by AI teams worldwide</span>
				</div>
				<p className="text-xs text-white/60 text-center">
					{messages.AUTH_FOOTER}
				</p>
			</div>
		</div>
	);
}
