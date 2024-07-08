import dynamic from 'next/dynamic';

const WobbleCardDemo = dynamic(() => import('./_ui/WobbleCardDemo'), { ssr: false });

const AboutPage = () => {
  return <WobbleCardDemo />;
};

export default AboutPage;
