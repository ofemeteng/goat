import { type Chain, PluginBase, ToolBase } from "@goat-sdk/core";
import { mode } from "viem/chains";
import type { EVMWalletClient } from "@goat-sdk/wallet-evm";
import { KimService } from "./kim.service";

const SUPPORTED_CHAINS = [mode];
export class KimPlugin extends PluginBase<EVMWalletClient> {
    constructor() {
        super("kim", [new KimService()]);
    }

    supportsChain = (chain: Chain) =>
        chain.type === "evm" && SUPPORTED_CHAINS.some((c) => c.id === chain.id);
}

export const kim = () => new KimPlugin();
