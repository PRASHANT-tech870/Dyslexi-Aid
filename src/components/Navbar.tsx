"use client";
import React, { useState } from "react";
import { HoveredLink, Menu, MenuItem, ProductItem } from "./ui/navbar-menu";
import { cn } from "@/utils/cn";
import Link from "next/link";

export default function NavbarDemo() {
  return (
    <div className="relative w-full flex items-center justify-center">
      <Navbar className="top-2" />
    </div>
  );
}

function Navbar({ className }: { className?: string }) {
  const [active, setActive] = useState<string | null>(null);
  return (
    <div
      className={cn("fixed top-10 inset-x-0 max-w-2xl mx-auto z-50 bg-black dark:bg-black", className)}
    >
      <div className="flex items-center justify-between p-4">
        <HoveredLink href="/" className="text-white">
          Home
        </HoveredLink>
        <Menu setActive={setActive}>
          <MenuItem setActive={setActive} active={active} item="Products">
            <div className="text-sm grid grid-cols-2 gap-10 p-4">
              <ProductItem
                title="ChatBot"
                href="https://ambition-ircd68w2bzd8qexuik92ed.streamlit.app/"
                src="/image1.avif"
                description="Interactive support tool tailored for dyslexic individuals communication needs"
              />
              <ProductItem
                title="Reading Assistance"
                href="https://ambition2-ggwgwgnfpsdaygctpmoc2a.streamlit.app/"
                src="/image2.jpeg"
                description="Enhanced reading aid designed to assist individuals with dyslexia"
              />
            </div>
          </MenuItem>
        </Menu>
        {/* <HoveredLink href="/about" className="text-white">
          About
        </HoveredLink> */}
      </div>
    </div>
  );
}
