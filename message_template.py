
main_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/V2tkpQb.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "即時查詢",
              "text": "查詢即時匯率"
            },
            "height": "md",
            "color": "#ff6666",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/nQaCDXh.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "近期趨勢圖",
              "text": "查詢趨勢走向"
            },
            "height": "md",
            "color": "#ff66b3",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/UrSkoW4.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "推薦與否",
              "text": "是否推薦兌幣"
            },
            "height": "md",
            "color": "#b366ff",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/lFq9NTg.jpg",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "介紹與說明",
              "text": "功能介紹與說明"
            },
            "height": "md",
            "color": "#66b3ff",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

cancel_menu = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "已結束本次操作",
        "weight": "bold",
        "size": "xl",
        "margin": "lg",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

plot_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "趨勢圖區間選擇",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "最近三個月",
              "text": "最近三個月趨勢"
            },
            "height": "md",
            "color": "#00ff80",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "最近兩週",
              "text": "最近兩週趨勢"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "結束本次操作",
              "text": "結束本次操作"
            },
            "height": "md",
            "color": "#00994d",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

plot = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
        "aspectMode": "fit",
        "size": "full"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "查詢其他趨勢",
              "text": "查詢趨勢走向"
            },
            "height": "md",
            "color": "#5cd65c",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "結束本次操作",
              "text": "結束本次操作"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

now_table = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "即時匯率",
        "weight": "bold",
        "size": "xl",
        "margin": "md"
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "現金買入",
                "size": "md",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$0.99",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "現金賣出",
                "size": "md",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$3.33",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "匯率買入",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "匯率賣出",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$0.69",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}

recommend_message = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "推薦程度",
        "weight": "bold",
        "size": "xl",
        "margin": "md"
      },
      {
        "type": "text",
        "text": "(台幣換成日幣)"
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "最近三個月前五點",
                "size": "md",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "否",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "最近兩週前三低點",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "否",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "推薦程度",
                "size": "md",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "低",
                "size": "md",
                "color": "#111111",
                "align": "end"
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "返回主選單",
          "text": "主選單"
        }
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}