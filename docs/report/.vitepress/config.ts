export default {
    base: "/EvenToNight/",
    title: "Report Progetto",
    head: [
        ["link", { rel: "icon", type: "image/png", href: "./logo.png" }]
    ],
    themeConfig: {
        nav: [
        { text: "Introduzione", link: "/" },
        { text: "Intervista 1", link: "/intervista1" },
        { text: "Intervista 2", link: "/intervista2" },
        { text: "Intervista 3", link: "/intervista3" }
        ],
        sidebar: [
        {
            text: "Report",
            items: [
                { text: "Introduzione", link: "/" },
                { text: "Requisiti", link: "/requisiti" },
                { text: "Architettura", link: "/architettura" },
                { text: "Conclusioni", link: "/conclusioni" }
              ]
        }
        ]
    }
}