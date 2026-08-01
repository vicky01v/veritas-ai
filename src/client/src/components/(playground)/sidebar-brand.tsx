"use client";

import { BrainCircuit, ChevronsLeft, ChevronsRight } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import { cn } from "@/lib/utils";
import version from "../../../package.json";
import {
	playgroundTopBarClassName,
	useSidebarLayout,
} from "./sidebar-layout-context";

export default function SidebarBrand() {
	const { isExpanded, toggleSidebar } = useSidebarLayout();

	return (
		<div
			className={playgroundTopBarClassName("relative gap-2 px-3")}
		>
			<Tooltip delayDuration={100}>
				<TooltipTrigger asChild>
					<Button
						variant="outline"
						size="icon"
						onClick={toggleSidebar}
						aria-label={isExpanded ? "Collapse sidebar" : "Expand sidebar"}
						aria-expanded={isExpanded}
						className="absolute -right-3 top-1/2 z-50 size-6 -translate-y-1/2 rounded-full border-stone-300 bg-white p-0 text-stone-600 shadow-sm hover:bg-stone-100 hover:text-stone-950 focus-visible:ring-2 focus-visible:ring-primary dark:border-stone-700 dark:bg-stone-900 dark:text-stone-300 dark:hover:bg-stone-800 dark:hover:text-white"
					>
						{isExpanded ? (
							<ChevronsLeft className="size-3.5" />
						) : (
							<ChevronsRight className="size-3.5" />
						)}
					</Button>
				</TooltipTrigger>
				<TooltipContent side="right" sideOffset={10}>
					{isExpanded ? "Collapse sidebar" : "Expand sidebar"}
				</TooltipContent>
			</Tooltip>
			<div className="size-9 shrink-0 rounded-xl bg-gradient-to-br from-violet-500 via-purple-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-violet-500/25">
				<BrainCircuit className="size-5 text-white" strokeWidth={2} />
			</div>
			<div
				className={cn(
					"flex min-w-0 flex-1 items-center gap-1.5 transition-opacity",
					!isExpanded && "pointer-events-none invisible opacity-0"
				)}
			>
				<p className="truncate text-lg font-bold bg-gradient-to-r from-violet-700 via-purple-600 to-indigo-700 bg-clip-text text-transparent dark:from-violet-400 dark:via-purple-400 dark:to-indigo-400">
					Veritas AI
				</p>
				<p className="shrink-0 text-[10px] text-stone-500 font-medium">v{version.version}</p>
			</div>
		</div>
	);
}
