"use client";
import React from "react";
import { SparklesCore } from "../components/ui/sparkles";

export default function SparklesPreview() {
  return (
    <div className="h-[100vh] relative w-full bg-black flex flex-col items-center justify-center overflow-hidden rounded-md">
      <div className="w-full absolute inset-0 h-full">
        <SparklesCore
          id="tsparticlesfullpage"
          background="transparent"
          minSize={0.6}
          maxSize={1.4}
          particleDensity={100}
          className="w-full h-full"
          particleColor="#FFFFFF"
        />
      </div>
      <div className="relative z-20 flex flex-col items-center justify-center h-full">
        <h1 className="md:text-7xl text-3xl lg:text-6xl font-bold text-center text-white tracking-[.5em]">
          DyslexiAid
        </h1>
      </div>
    </div>
  );
}
