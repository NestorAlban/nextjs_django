import {Header} from "./components/Header"
import Layout from "./components/Layout"

export const metadata = {
  title: 'Next.js',
  description: 'Generated by Next.js',
}
 
export default function RootLayout({ children }) {
 return (
    <html lang="en">
      <body>
        <Layout>
          {children}
        </Layout>
        {/* <Header/> */}
      </body>
    </html>
  )
}
