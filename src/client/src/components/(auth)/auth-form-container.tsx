"use client";
import { MoveRightIcon } from "lucide-react";
import { GithubIcon } from "lucide-react";
import { Button } from "../ui/button";
import Link from "next/link";
import Confetti from "../common/confetti";
import getMessage from "@/constants/messages";
import { BrainCircuit, Sparkles } from "lucide-react";

export default function AuthFormContainer({
	children,
}: {
	children: JSX.Element;
}) {
	const m = getMessage();
	return (
		<div className="flex flex-col justify-center p-8 lg:p-16 bg-gradient-to-br from-white via-violet-50/30 to-indigo-50/40 dark:from-stone-900 dark:via-stone-900 dark:to-indigo-950/30 relative overflow-hidden">
			<div className="absolute top-0 right-0 w-96 h-96 bg-gradient-to-br from-violet-200/40 to-transparent rounded-full -translate-y-1/2 translate-x-1/3 blur-3xl dark:from-violet-900/20"></div>
			<div className="absolute bottom-0 left-0 w-80 h-80 bg-gradient-to-tr from-cyan-200/30 to-transparent rounded-full translate-y-1/3 -translate-x-1/4 blur-3xl dark:from-cyan-900/20"></div>

			<Confetti />
			<div className="flex flex-col w-full max-w-md mx-auto gap-10 z-10">
				<div className="lg:hidden flex flex-col items-center gap-3 mb-4">
					<div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-violet-500 via-purple-500 to-indigo-600 flex items-center justify-center shadow-xl shadow-violet-500/30">
						<BrainCircuit className="h-9 w-9 text-white" strokeWidth={2} />
					</div>
					<h2 className="text-2xl font-bold bg-gradient-to-r from-violet-600 to-indigo-600 bg-clip-text text-transparent">Veritas AI</h2>
				</div>

				<div className="text-center space-y-3">
					<div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-gradient-to-r from-violet-100 to-indigo-100 dark:from-violet-900/40 dark:to-indigo-900/40 border border-violet-200/60 dark:border-violet-800/40 mb-2">
						<Sparkles className="w-3.5 h-3.5 text-violet-600 dark:text-violet-400" />
						<span className="text-xs font-semibold text-violet-700 dark:text-violet-300">AI-Powered Observability</span>
					</div>
					<h1 className="text-4xl font-extrabold tracking-tight bg-gradient-to-r from-violet-700 via-purple-600 to-indigo-700 bg-clip-text text-transparent dark:from-violet-400 dark:via-purple-400 dark:to-indigo-400">
						{m.AUTH_WELCOME}
					</h1>
					<p className="text-stone-600 dark:text-stone-400 font-medium">
						{m.AUTH_SUBTITLE}
					</p>
				</div>
				{children}
				<div className="grid grid-cols-2 gap-3 text-center text-sm pt-2">
					<Link
						href={"https://github.com/openlit/openlit"}
						target="_blank"
						className="w-full"
					>
						<Button
							className={`w-full rounded-xl gap-2 font-semibold bg-stone-900 text-stone-50 hover:bg-stone-900/90 dark:bg-gradient-to-r dark:from-stone-800 dark:to-stone-700 dark:text-stone-100 dark:hover:from-stone-700 dark:hover:to-stone-600 shadow-lg shadow-stone-900/10 dark:shadow-none`}
						>
							{m.AUTH_GITHUB}
							<GithubIcon className="ml-2 w-4" />
						</Button>
					</Link>
					<Link
						href="https://docs.openlit.io/latest/overview"
						target="_blank"
					>
						<Button variant={"outline"} className="rounded-xl font-semibold border-violet-200 dark:border-violet-800 text-violet-700 dark:text-violet-300 hover:bg-violet-50 dark:hover:bg-violet-950/30 hover:text-violet-800 dark:hover:text-violet-200">
							<b>{m.AUTH_DOCUMENTATION}</b>
							<MoveRightIcon className="ml-2 h-4 w-4" />
						</Button>
					</Link>
				</div>
			</div>
		</div>
	);
}
